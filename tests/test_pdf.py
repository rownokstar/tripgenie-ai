# tests/test_pdf.py
import pytest
import os
from pdf_generator.pdf_generator import generate_pdf


# Sample itinerary data for testing
SAMPLE_ITINERARY = {
    "city": "Paris",
    "days": 3,
    "preferences": "romantic, food",
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
                    "notes": "Go early to avoid crowds"
                }
            ]
        }
    ],
    "recommendations": ["L’As du Fallafel", "Café de Flore"],
    "tips": ["Use Metro for transport", "Visit Eiffel Tower at night"]
}


def test_generate_pdf_creates_output_file():
    """Test that PDF file is created and not empty."""
    output_dir = "test_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "test_paris_itinerary.pdf")

    result_path = generate_pdf(SAMPLE_ITINERARY, output_path)

    assert os.path.exists(result_path)
    assert os.path.getsize(result_path) > 0

    print(f"✅ PDF: Generated successfully at {result_path}")


def test_generate_pdf_with_missing_logo():
    """Test PDF generation works even if logo.png is missing."""
    # Temporarily rename logo to simulate missing file
    logo_path = "pdf_generator/static/logo.png"
    backup_path = "pdf_generator/static/logo.png.bak"

    was_renamed = False
    if os.path.exists(logo_path):
        os.rename(logo_path, backup_path)
        was_renamed = True

    try:
        output_path = "test_output/no_logo_test.pdf"
        result_path = generate_pdf(SAMPLE_ITINERARY, output_path)

        assert os.path.exists(result_path)
        print("✅ PDF: Successfully generated even without logo")

    finally:
        # Restore logo
        if was_renamed and os.path.exists(backup_path):
            os.rename(backup_path, logo_path)


def test_generate_pdf_with_incomplete_data():
    """Test that PDF generator handles incomplete itinerary data."""
    incomplete_data = {
        "city": "Test City",
        "days": 1,
        "preferences": "unknown",
        "itinerary": [],
        "recommendations": [],
        "tips": []
    }

    output_path = "test_output/incomplete.pdf"
    try:
        generate_pdf(incomplete_data, output_path)
        assert os.path.exists(output_path)
        print("✅ PDF: Tolerates incomplete data without crashing")
    except Exception as e:
        pytest.fail(f"PDF generation failed with incomplete data:  {e}")
