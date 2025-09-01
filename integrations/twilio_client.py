# integrations/twilio_client.py
from twilio.rest import Client
import os

# এনভায়রনমেন্ট ভেরিয়েবল থেকে লোড
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")  # e.g., +14155238886

def send_whatsapp(to_number: str, message: str, media_url: str = None):
    """
    WhatsApp মেসেজ পাঠান
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    try:
        msg_data = {
            "from_": f"whatsapp:{TWILIO_WHATSAPP_FROM}",
            "to": f"whatsapp:{to_number}",
            "body": message
        }
        if media_url:
            msg_data["media_url"] = [media_url]

        message = client.messages.create(**msg_data)
        print(f"✅ WhatsApp sent! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"❌ WhatsApp send failed: {e}")
        return False

def send_sms(to_number: str, message: str):
    """
    SMS পাঠান
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_FROM,  # বা আলাদা ফোন নম্বর
            to=to_number
        )
        print(f"✅ SMS sent! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"❌ SMS send failed: {e}")
        return False

# টেস্ট
if __name__ == "__main__":
    send_whatsapp("+8801XXXXXXXXX", "Your travel plan is ready!", "https://example.com/itinerary.pdf")
