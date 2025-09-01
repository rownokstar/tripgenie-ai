# integrations/gmail_client.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

GMAIL_USER = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def send_email(to: str, subject: str, body: str, attachments=None):
    """
    Gmail দিয়ে ইমেইল পাঠান
    """
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # অ্যাটাচমেন্ট যোগ করুন
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(file_path)}'
                )
                msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        text = msg.as_string()
        server.sendmail(GMAIL_USER, to, text)
        server.quit()
        print("✅ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# টেস্ট
if __name__ == "__main__":
    send_email(
        to="test@example.com",
        subject="Your Trip Plan",
        body="Hi! Here's your travel itinerary.",
        attachments=["output/itinerary_Paris.pdf"]
    )
