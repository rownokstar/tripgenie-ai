from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_engine import get_travel_plan
import json

app = FastAPI()

class TripRequest(BaseModel):
    city: str
    days: int
    prefs: str

@app.post("/plan_trip")
async def plan_trip(request: TripRequest):
    try:
        plan = get_travel_plan(request.city, request.days, request.prefs)
        return {"success": True, "data": plan}
    except Exception as e:
        return {"success": False, "error": str(e)}
