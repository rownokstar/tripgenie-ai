from pydantic import BaseModel
from typing import List, Optional

# Nested Models
class ScheduleItem(BaseModel):
    time: str
    activity: str
    location: str
    notes: Optional[str] = None

class DayPlan(BaseModel):
    day: int
    schedule: List[ScheduleItem]

# Main Response Model
class ItineraryResponse(BaseModel):
    city: str
    days: int
    preferences: str
    itinerary: List[DayPlan]
    recommendations: List[str]
    tips: List[str]

# Request Model
class TripRequest(BaseModel):
    city: str
    days: int
    prefs: str  # User preferences (e.g., "romantic, food, museums")

# Response Wrapper
class TripPlanResponse(BaseModel):
    success: bool
    data: Optional[ItineraryResponse] = None
    error: Optional[str] = None
