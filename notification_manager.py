import smtplib
from twilio.rest import Client

TWILIO_SID = "AC81a9f9bd48da96fc89e289dd61bd35b0"
TWILIO_AUTH_TOKEN = '28e43dbbd5a47b2cb9199196a7482901'
TWILIO_VIRTUAL_NUMBER = '+14782421829'
TWILIO_VERIFIED_NUMBER = '+2348107723143'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "ikumez8@gmail.com"
MY_PASSWORD = "Umuogo_1234"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

