# automation/scripts/generate_pdf.py
from fpdf import FPDF
import json
import sys
import os

def generate_pdf(itinerary_data, output_path=None):
    if not output_path:
        output_path = f"output/itinerary_{itinerary_data['city']}.pdf"
    
    # Create output directory
    os.makedirs("output", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"✈️ Trip to {itinerary_data['city']}", ln=True, align='C')
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Duration: {itinerary_data['days']} days | Interests: {itinerary_data['preferences']}", ln=True)
    pdf.ln(10)

    for day_plan in itinerary_data.get("itinerary", []):
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"📅 Day {day_plan['day']}", ln=True)
        pdf.set_font("Arial", "", 12)
        for act in day_plan["schedule"]:
            pdf.cell(0, 8, f"⏰ {act['time']}: {act['activity']}", ln=True)
            pdf.cell(0, 8, f"📍 {act['location']}", ln=True)
            if act.get("notes"):
                pdf.cell(0, 8, f"💡 {act['notes']}", ln=True)
            pdf.ln(2)
        pdf.ln(5)

    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Safe travels! Bon voyage! 🌍", ln=True, align='C')
    pdf.output(output_path)
    print(f"✅ PDF generated: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_pdf.py <json_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        data = json.load(f)
    
    # If response has {"success": true, "data": {...}}
    if "data" in data:
        data = data["data"]
    
    generate_pdf(data)
