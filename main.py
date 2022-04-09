import data_manager
import flight_search
import flight_data
import notification_manager

manager = data_manager.DataManager()
flight_info = flight_search.FlightSearch()
notification = notification_manager.NotificationManager()

my_data = manager.read_sheet()

for row in my_data['flights']:

    # If IATA code is not in spreadsheet, look up code, update sheet
    if row['airport'] == '':
        iata = flight_info.get_airport_info(row['city'])['locations'][0]
        row['airport'] = iata['code']
        manager.update_airport(row)

    # Find cheapest round trip flight over next 6 months
    flight = flight_info.get_flight_info(row['airport'])
    structured_flight = flight_data.FlightData(flight)

    # If flight is cheaper than threshold price, send text
    threshold_price = row['price']
    if structured_flight.flight_data['price'] <= threshold_price:
        notification.send_sms(structured_flight)
