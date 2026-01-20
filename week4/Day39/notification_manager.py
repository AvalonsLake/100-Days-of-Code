import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("MY_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv("TWILIO_WHATSAPP_NUMBER")}',
            body=message_body,
            to=f'whatsapp:{os.getenv("TWILIO_VERIFIED_NUMBER")}'
        )
        print(message.sid)