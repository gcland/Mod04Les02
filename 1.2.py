

class Event:
    def __init__(self, event_name, date, participants):
        self.event_name = event_name
        self.date = date
        self.participants  = participants

    def display_details(self):
        print(f"#{self.count}. {self.name}, Event date: {self.date}, ")
            
    def display_all(self):
        j = 1
        print(f"\nEvent: '{self.event_name}' - Participants: ")
        for participant in self.participants:
            print(f'{j}. {participant}')
            j+=1

    def get_participant_count(self):
        print(f'Event "{event_name}" participant count: {len(self.participants)}')

    def add_participants(self):
        while True:
            participant_add = input(f"\nEnter participant name to add to {self.event_name} attendee list ('end' to finish):\n>>  ")
            if participant_add.lower() == "end":
                break
            else:
                self.participants.append(participant_add)

events = {}

def add_event(event_name, date):
    participants = []
    events[event_name] = Event(event_name, date, participants)
    events[event_name].add_participants()
    print(f'Event "{event_name}" and participants logged.')
    events[event_name].display_all()

while True:
    choice = input("\n1. Add event\n2. Add participants to existing event\n3. Display participants of an event\n4. Get participant count of an event\n5. View events\n6. Quit\n>> ").lower()
    try:
        if choice == '1' or choice == 'add event':
            event_name = input('Enter name of event:\n>> ')
            if event_name in events:
                print(f"{event_name} is already exists!")
            else:
                date = input("Enter event date: ")
                add_event(event_name,date)

        elif choice == '2' or choice == "add participants" or choice == 'add participants to existing event':
            try:
                event_name = input('Enter name of event:\n>> ')
                events[event_name].display_all()
                events[event_name].add_participants()
            except Exception as e:
                print(f"Error: {e}.")

        elif choice == '3' or choice == "display" or choice == "display participants" or choice == 'display participants of an event':
            try:
                event_name = input('Enter name of event:\n>> ')
                events[event_name].display_all()
            except Exception as e:
                print(f"Error: {e}.")

        elif choice == '4' or choice == "count" or choice == "get" or choice == "get count" or choice == "get participant count of an event":
            try:
                event_name = input('Enter name of event:\n>> ')
                events[event_name].get_participant_count()
            except Exception as e:
                print(f"Error: {e}.")
        elif choice == '5' or choice == "view" or choice == 'view events':
            for event in events:
                print(event)
        elif choice == '6' or choice == "quit":
            break
    except Exception as e:
        print(f"Error: {e}.")