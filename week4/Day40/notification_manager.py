import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))
        self.email = os.getenv("SMTPLIB_EMAIL")
        self.password = os.getenv("SMTPLIB_PASS")

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("TWILIO_VIRTUAL_NUMBER")
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv("TWILIO_WHATSAPP_NUMBER")}',
            body=message_body,
            to=f'whatsapp:{os.getenv("TWILIO_VERIFIED_NUMBER")}'
        )
        print(message.sid)

    def send_email(self, message_body, recipients):
        for recipient in recipients:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=recipient["email"],
                    msg=message_body.encode('utf-8')
                )
