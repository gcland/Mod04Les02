

class Event:
    def __init__(self, name, date, count):
        self.name = name
        self.date = date
        self.count = count

    def display_details(self):
        print(f"#{self.count}. {self.name}, Event date: {self.date}, ")

participants = {}

def add_participant(name, date, count):
    if name in participants:
        print(f"{name} is already a participant!")
        return
    else:
        participants[name] = Event(name, date, count)
        print(f"{name} registered as a participant!")

def display_all():
     print("\nParticipants: ")
     for participant in participants.values():
        participant.display_details()

def get_participant_count(count):
    print(f"\nParticipant count: {count}")



count = 0
while True:
    choice = input("Add participant, display participants, get participant count, or quit?\n >> ").lower()
    if choice == "quit":
        break
    try:
        if choice == "add" or choice == "add participant":
            name = input("Enter name of participant:\n >> ")
            date = input("Enter event date: ")
            count += 1
            add_participant(name, date, count)
        elif choice == "display" or choice == "display participants":
            display_all()
        elif choice == "count" or choice == "get" or choice == "get count" or choice == "get participant count":
            get_participant_count(count)
    except:
        pass