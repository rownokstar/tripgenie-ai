# frontend/vapi/webhook_handler.py
from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# তোমার নিজের FastAPI ব্যাকএন্ড
BACKEND_URL = "http://127.0.0.1:8000/plan_trip"

@app.post("/vapi/webhook")
async def vapi_webhook(request: Request):
    data = await request.json()

    if data.get("message") == "function-call":
        func = data["functionCall"]["name"]
        params = data["functionCall"]["parameters"]

        if func == "get_travel_plan":
            # ব্যাকএন্ড API কল করো
            response = requests.post(BACKEND_URL, json={
                "city": params["city"],
                "days": params["days"],
                "prefs": params["preferences"]
            })

            if response.status_code == 200:
                result = response.json()["data"]
                return {
                    "result": result
                }
            else:
                return {
                    "error": "Failed to generate plan"
                }

    return {"status": "received"}
