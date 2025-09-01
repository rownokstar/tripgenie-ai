# automation/scripts/send_notifications.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import json
import os

# Load credentials
TWILIO_WHATSAPP_URL = "https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
GMAIL_USER = os.getenv("GMAIL_ADDRESS")
GMAIL_PASS = os.getenv("GMAIL_APP_PASSWORD")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")

def send_email(to, subject, body, pdf_path):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if pdf_path:
        with open(pdf_path, "rb") as f:
            mime = MIMEBase('application', 'octet-stream')
            mime.set_payload(f.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_path)}')
        msg.attach(mime)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASS)
    text = msg.as_string()
    server.sendmail(GMAIL_USER, to, text)
    server.quit()
    print("✅ Email sent!")

def send_whatsapp(to_number, message, media_url=None):
    data = {
        'From': f'whatsapp:{WHATSAPP_FROM}',
        'To': f'whatsapp:{to_number}',
        'Body': message
    }
    if media_url:
        data['MediaUrl'] = media_url

    response = requests.post(
        TWILIO_WHATSAPP_URL.format(account_sid=TWILIO_SID),
        data=data,
        auth=(TWILIO_SID, TWILIO_TOKEN)
    )
    if response.status_code == 201:
        print("✅ WhatsApp message sent!")
    else:
        print("❌ Failed to send WhatsApp:", response.text)

if __name__ == "__main__":
    # Test
    send_email(
        to="test@example.com",
        subject="Your Trip Plan",
        body="Here is your travel itinerary.",
        pdf_path="output/itinerary_Paris.pdf"
    )
    send_whatsapp(
        to_number="+8801XXXXXXXXX",
        message="Your travel plan is ready! Check your email.",
        media_url="https://example.com/itinerary_Paris.pdf"
    )
