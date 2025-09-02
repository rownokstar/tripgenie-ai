

---

## 📄 `README.md` – Full Practical Guide

```markdown
# 🧳 TripGenie – AI-Powered Travel Guide Assistant

**TripGenie** is an intelligent travel assistant that generates **personalized travel itineraries** using **AI (RAG + GPT-4o-mini)**, and delivers them via **chat, voice, email, or WhatsApp**. Built for developers, travelers, and AI hackers.

---

## 🌟 Features

- ✈️ Plan trips with **natural language**
- 🧠 Uses **RAG (Retrieval-Augmented Generation)** to avoid hallucinations
- 📄 Generates and sends **PDF itineraries**
- 🤖 Multi-channel support: **Voiceflow (chat)**, **Vapi (voice)**, **n8n (automation)**
- 🔄 Feedback loop for continuous improvement
- 📧 WhatsApp/email delivery (via Twilio/Gmail)
- 📊 Logs to Google Sheets for analytics

---

## 🧰 Tech Stack

| Layer | Tech |
|------|------|
| **AI Engine** | GPT-4o-mini + LangChain + ChromaDB |
| **Backend** | FastAPI (Python) |
| **Frontend** | Voiceflow (chat), Vapi (voice) |
| **Automation** | n8n |
| **PDF Generation** | FPDF2 |
| **Messaging** | Twilio (WhatsApp), Gmail |
| **Storage** | Google Sheets, ChromaDB |
| **Deployment** | Docker (optional) |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-github-username/tripgenie-ai.git
cd tripgenie-ai
```

---

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
# OR
venv\Scripts\activate        # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

### 4. Configure API Keys

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your keys:

```env
OPENAI_API_KEY=sk-your-openai-key-here
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_WHATSAPP_FROM=+1234567890
GMAIL_ADDRESS=you@gmail.com
GMAIL_APP_PASSWORD=your-app-password
GOOGLE_SHEETS_CREDENTIALS_PATH=secrets/gsheets-creds.json
```

> 🔐 Never commit `.env` to GitHub.

---

### 5. Build Vector Database

```bash
python create_vector_db.py
```

✅ This will load `data/cities.json` into `./vector_db/`.

---

### 6. Run the Backend API

```bash
python run_api.py
```

Visit:  
👉 **http://127.0.0.1:8000/docs**  
for interactive API docs.

---

### 7. Test the API

```bash
curl -X POST http://127.0.0.1:8000/plan_trip \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Paris",
    "days": 3,
    "prefs": "romantic, food"
  }'
```

You should get a JSON itinerary.

---

## 🧪 Generate a PDF

Save the JSON response to a file (e.g., `trip.json`), then:

```bash
python pdf_generator/pdf_generator.py trip.json
```

👉 PDF will be saved in `output/itinerary_Paris.pdf`

---

## 🧑‍💻 Connect to Voiceflow (Chat UI)

1. Go to [Voiceflow](https://studio.voiceflow.com/)
2. Create a new project
3. Add an **Intent**: "Plan a trip"
4. Add an **Integration Node**:
   - Method: `POST`
   - URL: `http://localhost:8000/plan_trip`
   - Body:
     ```json
     {
       "city": "{city}",
       "days": {days},
       "prefs": "{preferences}"
     }
     ```
5. Save response to variable: `itinerary`
6. Use a **Speak** block to show the itinerary

> 💡 To make it public:
```bash
ngrok http 8000
```
Use the `https://xxxx.ngrok.io` URL in Voiceflow.

---

## 🔄 Automate Delivery with n8n (Optional)

Start n8n with Docker:

```bash
docker-compose -f automation/n8n-docker-compose.yml up -d
```

Go to:  
👉 **http://localhost:5678**

Import workflow:
- File: `automation/workflows/trip-delivery-workflow.json`
- Configure:
  - Google Sheets
  - Twilio (WhatsApp)
  - Gmail

---

## 📁 Project Structure

```
tripgenie-ai/
├── backend/              # FastAPI + RAG logic
├── data/                 # Travel data (cities.json)
├── vector_db/            # ChromaDB persistence
├── frontend/             # Voiceflow + Vapi assets
├── automation/           # n8n workflows + scripts
├── pdf_generator/        # PDF templates + logic
├── integrations/         # Gmail, Twilio, Sheets
├── tests/                # Unit + integration tests
├── docs/                 # Documentation
├── README.md
├── .env.example
├── docker-compose.yml
├── LICENSE
└── CODE_OF_CONDUCT.md
```

---

## 🧪 Run Tests

```bash
pytest tests/ -v
```

---

## 📚 Documentation

| File | Description |
|------|-------------|
| [SETUP.md](docs/SETUP.md) | Full setup instructions |
| [API.md](docs/API.md) | API endpoints |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design |
| [FEEDBACK_LOOP.md](docs/FEEDBACK_LOOP.md) | Monitoring and improvement |

---

## 🛠️ Future Enhancements

- Add weather data (OpenWeatherMap)
- Support for calendar export (.ics)
- Multilingual support
- Fine-tune travel model on curated data
- Deploy to cloud (Render, Railway, Vercel)

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

---

## 🤝 Contributing

We welcome contributions! Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) first.

---

🌍 Built with ❤️ for travel lovers & AI hackers.
```

---

✅ This `README.md` is:
- Fully in **English**
- Beginner and developer-friendly
- Includes commands, structure, and examples
- Ready to be dropped into your GitHub repo

---

### ✅ How to Use

1. Create a file: `README.md` in your project root
2. Paste the content above
3. Commit and push to GitHub

---

## 🎁 Want the Full Project ZIP?

👉 Type:  
**"Yes, I want the full project ZIP file"**

I’ll generate a downloadable `.zip` of the **entire TripGenie project** — including all folders, files, and instructions — ready to run on your local machine.

You're just one step away from a complete, deployable AI product! 🚀🌍

Let me know when you're ready!
