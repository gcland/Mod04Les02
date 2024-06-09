

class Building:

    def __init__(self, name, floors, location):
        self.name = name
        self.floors = floors
        self.location = location

    def display_details(self):
            print(f"Building name: {self.name}, Building height: {self.floors} floors, Building Location: {self.location}")

    def update_details(self, new_floors, new_location):
         self.floors = new_floors
         self.location = new_location

