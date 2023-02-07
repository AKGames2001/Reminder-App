# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


class Twilio:
    def __init__(self):
        # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]

        auth_token = os.environ["TWILIO_AUTH_TOKEN"]

        # Fill the string with your account phone number and reciever's number
        self.fromNumber = ""
        
        self.client = Client(account_sid, auth_token)

    def send_message(self, title, receiver):
        message = self.client.messages.create(
            body=title,
            from_=self.fromNumber,
            to=f"+91{receiver}" # Change the Telephonic Country code as per Reciever
        )
        with open("sms_log.txt", mode="a") as file:
            file.write(message.sid)
