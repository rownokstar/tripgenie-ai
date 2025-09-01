import json
import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-openai-key-here")

def load_data():
    with open("../data/cities.json", "r", encoding="utf-8") as f:
        return json.load(f)

def create_vector_db():
    data = load_data()
    docs = []
    for city_data in data:
        city = city_data["city"]
        for attr in city_data["attractions"]:
            docs.append(Document(
                page_content=f"{attr['name']} in {city}: {attr['description']} Duration: {attr['duration']}, Fee: {attr['entry_fee']}",
                metadata={"type": "attraction", "city": city}
            ))
        for rest in city_data["restaurants"]:
            docs.append(Document(
                page_content=f"{rest['name']} in {city}: {rest['cuisine']} cuisine, price: {rest['price']}, must try: {rest['must_try']}",
                metadata={"type": "restaurant", "city": city}
            ))
        for tip in city_data["tips"]:
            docs.append(Document(
                page_content=f"Travel tip for {city}: {tip}",
                metadata={"type": "tip", "city": city}
            ))
        for days, plan in city_data["itineraries"].items():
            docs.append(Document(
                page_content=f"{city} {days} itinerary: " + "; ".join(plan),
                metadata={"type": "itinerary", "city": city, "days": days}
            ))

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    db = Chroma.from_documents(docs, embeddings, persist_directory="../vector_db")
    print("✅ Vector DB created and saved.")
    return db

def get_travel_plan(city: str, days: int, prefs: str):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    db = Chroma(persist_directory="../vector_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"filter": {"city": city}, "k": 5})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    template = """
    You are a travel planner. Create a personalized {days}-day itinerary for {city}.
    User preferences: {prefs}.
    Use only the provided context. Be specific with times, locations, and include tips.
    Return in strict JSON format:
    {{
      "city": "{city}",
      "days": {days},
      "preferences": "{prefs}",
      "itinerary": [
        {{
          "day": 1,
          "schedule": [
            {{"time": "9:00", "activity": "...", "location": "...", "notes": "..."}}
          ]
        }}
      ],
      "recommendations": ["..."],
      "tips": ["..."]
    }}
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True
    )

    result = qa.invoke({"query": f"Plan a {days}-day trip to {city} for {prefs}"})
    try:
        return json.loads(result["result"])
    except:
        return {
            "city": city, "days": days, "preferences": prefs,
            "itinerary": [{"day": 1, "schedule": [{"time": "Error", "activity": "Parse failed", "location": "", "notes": ""}]}],
            "recommendations": [], "tips": ["Check logs."]
        }
