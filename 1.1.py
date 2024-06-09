

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print()
        print(f"Registration: {self.reg_num}, Type: {self.type}, Owner: {self.owner}")

vehicles = {}

def register(reg_num, type, owner):
    if reg_num in vehicles:
        print(f"{reg_num} already exists!")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle {reg_num} registered!")

def update(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated {reg_num} owner to {new_owner}!")
    else:
        print("Vehicle not found.")

def display_all():
    for vehicle in vehicles.values():
        vehicle.display_details()

while True:
    choice = input("Register, update, display, or quit?\n >> ").lower()
    if choice == "quit":
        break
    try:
        if choice == "register":
            reg_num = input("Enter registration number for the vehicle: ")
            type = input("Enter the vehicle type: ")
            owner = input("Enter name of owner: ")
            register(reg_num, type, owner)
        elif choice == "update":
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter name of new owner: ")
            update(reg_num, new_owner)
        elif choice == "display":
            display_all()
    except Exception:
        print("Error.")
    