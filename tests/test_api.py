# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


def test_plan_trip_valid_request():
    """Test API returns 200 and valid data for a proper request."""
    response = client.post(
        "/plan_trip",
        json={
            "city": "Paris",
            "days": 3,
            "prefs": "romantic, museums"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "data" in data
    assert data["data"]["city"] == "Paris"
    assert len(data["data"]["itinerary"]) > 0

    print("✅ API: Successfully generated trip plan")


def test_plan_trip_missing_required_fields():
    """Test API rejects request with missing fields."""
    response = client.post(
        "/plan_trip",
        json={"city": "Paris"}  # Missing 'days' and 'prefs'
    )

    assert response.status_code == 422  # Unprocessable Entity
    print("✅ API: Correctly rejects incomplete input")


def test_plan_trip_unknown_city():
    """Test API handles unknown city gracefully."""
    response = client.post(
        "/plan_trip",
        json={
            "city": "Atlantis",
            "days": 2,
            "prefs": "underwater exploration"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["city"] == "Atlantis"

    print("✅ API: Handles unknown city with fallback response")
