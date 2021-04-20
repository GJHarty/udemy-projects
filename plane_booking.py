# Prompt:
# Create a reservation system which books airline seats or hotel rooms. 
# It charges various rates for particular sections of the plane or hotel. 
# Example, first class is going to cost more than coach. 
# Hotel rooms have penthouse suites which cost more. 
# Keep track of when rooms will be available and can be scheduled.

import re
# Define an airplane class. Need a list of seats, need a price of seats, and should have tiers of prices (dict)

tiers = ('Economy', 'Business', 'First')
tier_prices = {'Economy': 100, 'Business': 200, 'First': 500}

# Only works with easy numbers, need to figure out an algo for different numbers for added complexity
econ_ratio = 0.7
bus_ratio = 0.2
first_ratio = 0.1

#assign variables for plane sizes for testing purposes. Will try to implement user input in future.
# Currently only works with multiples of 10. Will try to implement a more complex system for any int

space_large = 240
space_medium = 120
space_small = 30
space_bush = 10


class Airplane:
    
    def __init__(self, number_of_seats):
        self.available_seats = []
        self.booked_seats = []
        self.number_of_seats = number_of_seats
        self.econ_seat_count = num_of_seat_tier(self.number_of_seats, econ_ratio)
        self.bus_seat_count = num_of_seat_tier(self.number_of_seats, bus_ratio)
        self.bus_and_econ_seat_count = self.econ_seat_count + self.bus_seat_count
        self.first_seat_count = num_of_seat_tier(self.number_of_seats, first_ratio)
        
        for tier in tiers:
            if tier == 'Economy':
                for i in range(0, self.econ_seat_count):
                    self.available_seats.append([f"Seat {i+1}",Seat(tier)])
            elif tier == 'Business':
                for i in range(self.econ_seat_count, (self.bus_seat_count + self.econ_seat_count)):
                    self.available_seats.append([f"Seat {i+1}",Seat(tier)])
            else: # tier == 'First'
                for i in range(self.bus_and_econ_seat_count, (self.first_seat_count + self.bus_and_econ_seat_count)):
                    self.available_seats.append([f"Seat {i+1}",Seat(tier)])
    
    def __repr__(self):
        return f'Airplane({self.number_of_seats!r})'
    
    def __str__(self):
        return "This airplane has {} seats.".format(len(self.available_seats))          
    
    def book_seat(self):
        seat_to_book = input("Please select a seat to book. (ex. 'Seat 1')")
        for seat in self.available_seats:
            if len(self.booked_seats) > 0 and seat_to_book in self.booked_seats[0]:
                print("Sorry, this seat is already booked.")
                break
                
            elif seat_to_book == seat[0]:
                self.booked_seats.append(seat)
                self.available_seats.remove(seat)
                Seat.seat_booked(seat[1])
                break               
    
class Seat:
    
    def __init__(self, tier, booked=False):
        self.tier = tier
        self.booked = booked
    
    def __repr__(self):
        return f'Seat({self.tier!r},{self.booked!r})'
    
    def __str__(self):
        if not self.booked:
            return f"This seat is tier {self.tier} and is available"
        else:
            return f"This seat is tier {self.tier} and is already booked"
    
    def seat_value(self):
        self.value = tier_prices[self.tier]
        
        if not self.booked:
            return f"This seat costs ${self.value}.00 and is available"
        else:
            return f"This seat costs ${self.value}.00 and is already booked"
  
    def seat_booked(self):
        self.booked = True

# This is a helper function for calculating the number of seats by ratio. hopefully can edit to allow situations for more
# complex seat amounts
    
def num_of_seat_tier(seats, ratio):
        return int(seats * ratio)

def main():
    bushplane = Airplane(space_bush)
    large = Airplane(space_large)
    med = Airplane(space_medium)
    bushplane.book_seat()
    
if __name__ == "__main__":
    main()
    print(bushplane.booked_seats)

