from twilio.rest import Client
import dotenv, os
import flight_data


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        dotenv.load_dotenv()
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.client = Client(account_sid, auth_token)
        self.number_to = os.getenv('PHONE_TO')
        self.number_from = os.getenv('PHONE_FROM')

    def send_sms(self, structured_flight: flight_data):
        message = self.client.messages \
            .create(
            body=f"✈️FOUND FLIGHT! ✈️\n"
                 f"{structured_flight.print_flight()}",
            from_=self.number_from,
            to=self.number_to
        )
        print(message.sid)
