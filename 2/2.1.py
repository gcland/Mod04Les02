from building_manager import Building
import os

buildings = {}

def save_buildings():
     with open("2/Buildings.txt", 'w') as file:
          for building in buildings.values():
               file.write(f"{building.name}, {building.floors}, {building.location}\n")

def load_bulidings():
    if os.path.exists('2/Buildings.txt'):
         with open("2/Buildings.txt", 'r') as file:
              for line in file:
                   name, floors, location = line.strip().split(',')
                   building = Building(name, floors, location)
                   buildings[name] = building
load_bulidings()

def add_building(name, floors, location):
        buildings[name] = Building(name, floors, location)

def update(name, new_floors, new_location):
     if name in buildings:
          buildings[name].update_details(new_floors, new_location)
          print(f"Updated building:'{name}' to have {new_floors} number of floors!")
          print(f"Updated building:'{name}' location to '{new_location}'!")

def display_all():
     print("\nBuildings Details: ")
     for building in buildings.values():
        building.display_details()

while True:
    choice = input("Add building, update building details, display all buildings details, save, or quit?\n >> ").lower()
    if choice == "quit":
        break
    try:
        if choice == "add route" or choice == "add":
            name = input("Building name: ")
            floors = input("Building number of floors: ")
            location = input("Building location: ")
            add_building(name, floors, location)
        elif choice == "update" or choice == "update building details":
            name = input("Enter building name: ")
            new_floors = input("Enter new number of floors: ")
            new_location = input("Enter new building location: ")
            update(name, new_floors, new_location)
        elif choice == "display" or choice == "display all buildings details":
            display_all()
        elif choice == "save":
             save_buildings()
    except Exception as e:
        print(f"Error; {e}.")        
    