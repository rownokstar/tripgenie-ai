# tests/test_rag.py
import pytest
import os
from backend.rag_engine import get_travel_plan, create_vector_db


@pytest.fixture(scope="module", autouse=True)
def setup_vector_db():
    """Ensure vector database is created before running RAG tests."""
    if not os.path.exists("../vector_db/collection_metadata.json"):
        print("📁 Vector DB not found. Creating...")
        create_vector_db()
    else:
        print("📁 Using existing Vector DB")


def test_get_travel_plan_returns_valid_structure():
    """Test that a valid itinerary is generated with correct structure."""
    city = "Paris"
    days = 3
    preferences = "romantic, food, museums"

    plan = get_travel_plan(city, days, preferences)

    assert "city" in plan
    assert plan["city"] == "Paris"
    assert "days" in plan
    assert plan["days"] == 3
    assert "itinerary" in plan
    assert isinstance(plan["itinerary"], list)
    assert len(plan["itinerary"]) > 0

    first_day = plan["itinerary"][0]
    assert "day" in first_day
    assert "schedule" in first_day
    assert isinstance(first_day["schedule"], list)

    first_activity = first_day["schedule"][0]
    assert "time" in first_activity
    assert "activity" in first_activity
    assert "location" in first_activity

    assert "tips" in plan
    assert isinstance(plan["tips"], list)

    print("✅ RAG: Valid itinerary structure generated for Paris")


def test_get_travel_plan_handles_unknown_city():
    """Test graceful handling of unknown cities."""
    plan = get_travel_plan("Mars", 5, "adventure")

    assert "city" in plan
    assert plan["city"] == "Mars"
    assert "itinerary" in plan
    assert len(plan["itinerary"]) > 0

    first_activity = plan["itinerary"][0]["schedule"][0]
    assert "Error" in first_activity["activity"] or "fallback" in str(plan).lower()

    print("✅ RAG: Gracefully handles unknown city")


def test_get_travel_plan_one_day_request():
    """Test 1-day itinerary generation."""
    plan = get_travel_plan("Tokyo", 1, "food and culture")

    assert plan["city"] == "Tokyo"
    assert plan["days"] == 1
    assert len(plan["itinerary"]) == 1
    assert "schedule" in plan["itinerary"][0]
    assert len(plan["itinerary"][0]["schedule"]) > 0

    print("✅ RAG: Successfully generated 1-day itinerary for Tokyo")
