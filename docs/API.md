
---

### 📄 `docs/API.md`

```markdown
# 📡 API Reference

This document describes the REST API provided by **TripGenie**, an AI-powered travel planning assistant. The API generates personalized, RAG-enhanced travel itineraries based on user input.

---

## 🔗 Base URL

All endpoints are served from your local server when running:

```
http://127.0.0.1:8000
```

When exposed via ngrok (e.g., for Voiceflow), the base URL becomes:
```
https://your-ngrok-subdomain.ngrok.io
```

---

## 🚀 Endpoint: `POST /plan_trip`

Generates a personalized travel itinerary using RAG (Retrieval-Augmented Generation) and GPT-4o-mini.

### 🔎 Purpose

This endpoint:
- Accepts travel preferences
- Retrieves relevant context from the knowledge base (`cities.json`)
- Uses LLM to generate a structured, realistic itinerary
- Returns JSON suitable for frontend display or automation

---

### 📥 Request

#### URL
```
POST /plan_trip
```

#### Headers
```http
Content-Type: application/json
```

#### Body (JSON)

| Field | Type | Description |
|------|------|-------------|
| `city` | string | Destination city (e.g., `"Paris"`, `"Tokyo"`) |
| `days` | integer | Number of travel days (e.g., `3`) |
| `prefs` | string | User interests (e.g., `"romantic, food, museums"`) |

#### Example Request

```bash
curl -X POST http://127.0.0.1:8000/plan_trip \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Paris",
    "days": 3,
    "prefs": "romantic, fine dining, art"
  }'
```

---

### 📤 Response

#### Success (200 OK)

```json
{
  "success": true,
  "data": {
    "city": "Paris",
    "days": 3,
    "preferences": "romantic, fine dining, art",
    "itinerary": [
      {
        "day": 1,
        "schedule": [
          {
            "time": "9:00",
            "activity": "Visit Eiffel Tower",
            "location": "Champ de Mars",
            "notes": "Buy tickets online to skip the line"
          },
          {
            "time": "12:30",
            "activity": "Lunch at Le Marais",
            "location": "Le Marais",
            "notes": "Try duck confit"
          },
          {
            "time": "15:00",
            "activity": "Seine River Cruise",
            "location": "Bateaux Mouches",
            "notes": "Beautiful views of Notre-Dame"
          }
        ]
      },
      {
        "day": 2,
        "schedule": [
          {
            "time": "10:00",
            "activity": "Louvre Museum",
            "location": "Louvre",
            "notes": "See Mona Lisa early to avoid crowds"
          }
        ]
      }
    ],
    "recommendations": [
      "L’As du Fallafel for street food",
      "Café de Flore for ambiance"
    ],
    "tips": [
      "Buy a Paris Museum Pass",
      "Use the Metro for fast travel",
      "Visit Eiffel Tower at night for light show"
    ]
  }
}
```

#### Error (422 Unprocessable Entity or 500)

Returned when input is invalid or server fails.

```json
{
  "success": false,
  "error": "Invalid request: 'days' must be a positive number"
}
```

---

## 🧪 Interactive Documentation

After starting the server with `python run_api.py`, visit:

👉 **http://127.0.0.1:8000/docs**

This opens **Swagger UI**, an interactive API playground where you can:
- View all endpoints
- Test requests directly
- See response examples
- Copy cURL commands

---

## 🧩 Integration Examples

### 1. Python (requests)

```python
import requests

url = "http://127.0.0.1:8000/plan_trip"
data = {
    "city": "Tokyo",
    "days": 2,
    "prefs": "food and culture"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    plan = response.json()["data"]
    print(plan["itinerary"])
```

### 2. JavaScript (fetch)

```javascript
fetch('http://127.0.0.1:8000/plan_trip', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    city: 'Paris',
    days: 3,
    prefs: 'romantic, food'
  })
})
.then(res => res.json())
.then(data => console.log(data.data.itinerary));
```

---

## ⚠️ Notes

- The API uses **RAG** to avoid hallucinations — responses are grounded in curated data.
- It does **not require authentication** (for demo purposes). In production, add API key checks.
- Response time depends on OpenAI API speed (~1–3 seconds).
- All responses are in **valid JSON** format for easy parsing in automation tools (e.g., n8n, Voiceflow).

---

## 📚 Related Docs

- [Architecture](ARCHITECTURE.md) – System design
- [Setup Guide](SETUP.md) – How to run locally
- [Feedback Loop](FEEDBACK_LOOP.md) – Monitoring and improvement
```

---

✅ This `API.md` is:
- Fully in **English**
- Professional and detailed
- Includes cURL, Python, JS examples
- Ready for GitHub or team documentation

---

### ✅ How to Save

1. Create the folder: `docs/` (if not exists)
2. Create file: `docs/API.md`
3. Paste the content above
4. Commit to your project

---

You now have a complete, professional API documentation file.

Let me know when you're ready for:
- ✅ `FEEDBACK_LOOP.md`
- ✅ Or the **full project ZIP**

I’ll deliver it instantly! 🚀
