# 🏗️ Architecture Overview

This document describes the system architecture of **TripGenie**, an AI-powered travel planning assistant.

## 🌐 System Diagram

```mermaid
graph TD
    A[User] --> B{Voiceflow / Vapi}
    B --> C[FastAPI Backend]
    C --> D[ChromaDB (RAG)]
    D --> C
    C --> E[Generate Itinerary (GPT-4o-mini)]
    E --> F[n8n Automation]
    F --> G[Generate PDF]
    F --> H[Log to Google Sheets]
    F --> I[Send via Email/WhatsApp]
    F --> J[Feedback Collection]
    J --> K{👍 or 👎?}
    K -- 👎 --> L[Alert Admin (Slack/Email)]
