class Bus:
    def __init__(self, city, route, passengers, fare):
        self.city_name = city
        self.route_number = route
        self.pass_capacity = passengers
        self.bus_fare = fare

    def display_details(self):
        print(f"City: {self.city_name}, Route: {self.route_number}, Passenger Capacity: {self.pass_capacity}, Fare: ${self.bus_fare}")

def add_route(city, route, passengers, fare):
        buses[route] = Bus(city, route, passengers, fare)

def display_all():
     print("\nBus routes: ")
     for bus in buses.values():
        bus.display_details()

buses = {}

while True:
    choice = input("Add route, display all routes, or quit?\n >> ").lower()
    if choice == "quit":
        break
    try:
        if choice == "add route" or choice == "add":
            city = input("City name: ")
            route = input("Route number: ")
            passengers = input("Passenger capacity: ")
            fare = input("Bus fare: ")
            add_route(city, route, passengers, fare)
    
        elif choice == "display" or choice == "display all routes":
            display_all()
    
    except Exception as e:
        print(f"Error {e}.")



