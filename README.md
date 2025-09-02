# tripgenie-ai# 🧳 TripGenie – AI-Powered Travel Guide Assistant

TripGenie is an intelligent travel assistant that generates personalized itineraries using AI, RAG, and automation. It supports chat, voice, PDF delivery, and feedback monitoring.

## 🌟 Features

- ✈️ Natural language trip planning (text or voice)
- 🧠 Grounded responses using curated travel data (RAG)
- 📄 Instant PDF delivery via email or WhatsApp
- 🤖 Multi-channel support: Voiceflow, Vapi, n8n
- 🔄 Feedback loop for continuous improvement

## 🧰 Tech Stack

- **AI**: GPT-4o-mini + LangChain + ChromaDB
- **Backend**: FastAPI (Python)
- **Frontend**: Voiceflow (chat), Vapi (voice)
- **Automation**: n8n (PDF, WhatsApp, logging)
- **Delivery**: Twilio (WhatsApp), Gmail (SMTP), FPDF
- **Storage**: Google Sheets, ChromaDB

## 🚀 Quick Start

```bash
git clone https://github.com/yourname/tripgenie-ai.git
cd tripgenie-ai

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your keys

# Create vector DB
python create_vector_db.py

# Run API server
python run_api.py
