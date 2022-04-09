class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.flight_data = {
            'origin': flight['cityFrom'],
            'destination': flight['cityTo'],
            'price': flight['price'],
            'flights': [
                {'depart_date': flight['route'][0]['local_departure'].split('T')[0],
                 'depart_time': flight['route'][0]['local_departure'].split('T')[1].split('.')[0],
                 'arrive_date': flight['route'][0]['local_arrival'].split('T')[0],
                 'arrive_time': flight['route'][0]['local_arrival'].split('T')[1].split('.')[0]
                 },
                {'depart_date': flight['route'][1]['local_departure'].split('T')[0],
                 'depart_time': flight['route'][1]['local_departure'].split('T')[1].split('.')[0],
                 'arrive_date': flight['route'][1]['local_arrival'].split('T')[0],
                 'arrive_time': flight['route'][1]['local_arrival'].split('T')[1].split('.')[0]
                 }
            ]
        }

    def print_flight(self):
        return f"{self.flight_data['origin']} to {self.flight_data['destination']}\n" \
               f"${self.flight_data['price']}\n" \
               f"Depart: {self.flight_data['flights'][0]['depart_date']} {self.flight_data['flights'][0]['depart_time']}\n" \
               f"Return: {self.flight_data['flights'][1]['depart_date']} {self.flight_data['flights'][1]['depart_time']}"
