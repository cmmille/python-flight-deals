# Python Flight Deal Finder
Use [Google Sheets](https://www.google.com/sheets/about/), [Sheety API](https://sheety.co/), [Kiwi Tequila API](https://tequila.kiwi.com/), and [Twilio API](https://www.twilio.com/) to get SMS alerts for flight deals.

# Description
The app looks up the cheapest round trip flight (1 passenger, direct flights only) for all of the cities in your Google sheet. If the flight is cheaper than your maximum price, a SMS message is sent to your phone with the flight details.

# Instructions
* Create a Google sheet with the following parameters
  * Sheet name: 'flights'
  * Columns:
    * 'City': Where you might want to fly
    * 'Airport': IATA code for the city. If unknown, leave blank and Kiwi will automatically fill.
    * 'Price': Maximum amount you would be willing to pay for the flights
* Link the Google sheet to Sheety
* Create ".env" in the same directory "main.py" was unzipped with the following parameters:
  * 'SHEETY_API': Sheety API key
  * 'SHEETY_TOKEN': 'Bearer [TOKEN]'
  * 'KIWI_API': Kiwi API key
  * 'TWILIO_ACCOUNT_SID': Twilio SID
  * 'TWILIO_AUTH_TOKEN': Twilio Token
  * 'PHONE_FROM': Twilio phone number to send texts from
  * 'PHONE_TO': Phone number you would like alerts sent to

# 100 Days of Code: Day 39
Created as part of the python 100 days of code challenge (https://www.udemy.com/course/100-days-of-code/)
