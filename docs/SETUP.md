Here is the complete, ready-to-use **`SETUP.md`** file in **English only**, properly formatted and optimized for your `docs/` folder.

You can copy and save this directly as:  
`docs/SETUP.md`

---

### 📄 `docs/SETUP.md`

```markdown
# ⚙️ Setup Guide

Follow this step-by-step guide to install, configure, and run the **TripGenie AI Travel Assistant** on your local machine.

---

## 🧰 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.10 or higher**  
  Download: https://www.python.org/downloads/
- **Git** (optional, for cloning)  
  Download: https://git-scm.com/
- **OpenAI API Key**  
  Get one at: https://platform.openai.com/account/api-keys
- **ngrok** (for webhook testing)  
  Download & install: https://ngrok.com/download
- **Docker** (only if using n8n automation)  
  Download: https://www.docker.com/products/docker-desktop/

---

## 📦 Step 1: Clone the Project

Open your terminal and run:

```bash
git clone https://github.com/yourname/tripgenie-ai.git
cd tripgenie-ai
```

> Replace `yourname` with your actual GitHub username if you've uploaded it.

---

## 🐍 Step 2: Set Up Virtual Environment

Create and activate a virtual environment to isolate dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

You should now see `(venv)` in your terminal prompt.

---

## 📦 Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r backend/requirements.txt
```

This installs FastAPI, LangChain, ChromaDB, FPDF2, and other dependencies.

---

## 🔐 Step 4: Configure Environment Variables

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Now, edit `.env` with your credentials:

```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here

# Twilio (WhatsApp)
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=+14155238886  # Your Twilio number

# Gmail (Email delivery)
GMAIL_ADDRESS=your.email@gmail.com
GMAIL_APP_PASSWORD=your_app_password  # Use App Password, not regular password

# Google Sheets
GOOGLE_SHEETS_CREDENTIALS_PATH=secrets/gsheets-creds.json  # Service account JSON

# Optional: OpenWeatherMap
OPENWEATHER_API_KEY=your_openweather_api_key
```

> 🔐 **Never commit `.env` to GitHub.** It's already git-ignored.

---

## 🧠 Step 5: Build the Vector Database

Run this script to load travel data into ChromaDB:

```bash
python create_vector_db.py
```

This:
- Reads `data/cities.json`
- Generates embeddings using OpenAI
- Saves them to `./vector_db/`

> ✅ Output: `✅ Vector DB created and saved at ./vector_db/`

---

## ▶️ Step 6: Run the FastAPI Backend

Start the API server:

```bash
python run_api.py
```

Visit the live docs at:  
👉 **http://127.0.0.1:8000/docs**

You should see the Swagger UI with the `/plan_trip` endpoint.

---

## 🧪 Step 7: Test the API

Use `curl` to test a sample request:

```bash
curl -X POST http://127.0.0.1:8000/plan_trip \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Paris",
    "days": 3,
    "prefs": "romantic, food, museums"
  }'
```

You should receive a structured JSON itinerary in response.

---

## 🔗 Step 8: Connect to Voiceflow (Frontend)

1. Go to [Voiceflow](https://studio.voiceflow.com/) and create a new project.
2. Add an **Intent** block: "Plan a trip"
3. Extract slots:
   - `{city}` (text)
   - `{days}` (number)
   - `{preferences}` (text)
4. Add an **Integration** → **Webhook**
   - Method: `POST`
   - URL: `https://your-ngrok-url.ngrok.io/plan_trip`
   - Body:
     ```json
     {
       "city": "{city}",
       "days": {days},
       "prefs": "{preferences}"
     }
     ```
5. Save the response to a variable: `itinerary`
6. Use a **Speak/Text** block to display the plan.

> 💡 To get a public URL, run:
> ```bash
> ngrok http 8000
> ```
> Use the `https://...ngrok.io` URL in Voiceflow.

---

## 🔁 Step 9: Set Up Automation (n8n – Optional)

Start n8n with Docker:

```bash
docker-compose -f automation/n8n-docker-compose.yml up -d
```

Access the dashboard:  
👉 **http://localhost:5678**

Then:
1. Import `automation/workflows/trip-delivery-workflow.json`
2. Configure nodes:
   - Google Sheets (connect your sheet)
   - Gmail / Twilio (add credentials)
3. Set webhook trigger to receive data from FastAPI

---

## ✅ Final Checklist

| Task | Status |
|------|--------|
| ✅ Python & pip installed |  |
| ✅ Virtual environment activated |  |
| ✅ `.env` configured with API keys |  |
| ✅ `create_vector_db.py` run successfully |  |
| ✅ `run_api.py` running on port 8000 |  |
| ✅ Tested API with `curl` |  |
| ✅ Connected to Voiceflow via ngrok |  |
| ✅ (Optional) n8n workflow imported |  |

---

## 🚨 Troubleshooting

| Issue | Solution |
|------|----------|
| `ModuleNotFoundError` | Make sure `venv` is activated and dependencies are installed |
| `422 Unprocessable Entity` | Check if `days` is a number, not a string |
| `OpenAI API error` | Verify your API key and billing setup |
| `ngrok connection failed` | Restart ngrok and update URL in Voiceflow |
| `PDF not generated` | Ensure `output/` folder exists or create it manually |

---

You're all set! 🎉  
TripGenie is now running locally and ready for customization or deployment.
```

---

✅ This `SETUP.md` is:
- Fully in **English**
- Step-by-step and beginner-friendly
- Includes commands, code, and troubleshooting
- Ready for GitHub or internal documentation

---

Just save this file as:  
`tripgenie-ai/docs/SETUP.md`

And you're good to go!

Let me know when you're ready for the **full ZIP** — I’ll prepare it for you. 🚀
