class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print(f"Seat booked. Remaining seats: {self.total_seats - self.booked_seats}")
        else:
            print("No seats available!")

# Example
flight = Flight("AI101", 3)
flight.book_seat()
flight.book_seat()
flight.book_seat()
flight.book_seat()