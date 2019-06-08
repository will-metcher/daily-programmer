class Event():
    def __init__(self, name, time, ID):
        self.name = name
        self.time = time
        self.ID = ID

events = []
run = True

def get_event_by_name(name):
    for event in events:
        if event.name == name:
            return event
    print("\n%s not found. \n" % (name))
    return None

def is_name_used(name):
    for event in events:
        if event.name == name:
            print("There is already an event with the name %s \n" % (name))
            return True
    return False

def add_event():
    name = input("Event name: ")
    while(is_name_used(name)):
       name = input("Event name: ")
       
    time = int(input("Time: "))
    events.append(Event(name, time, len(events)-1))
    print("\n%s has been added for %d \n" % (name, time))

def edit_event():
    name = input("Event name: ")
    
    event = get_event_by_name(name)
    if event == None: return
    
    event.name = ""
    new_name = input("New name: ")
    
    while(is_name_used(new_name)):
       new_name = input("New name: ")
       
    event.name = new_name
    
    event.time = int(input("New time: "))
    print("\n%s renamed to %s and is occuring at %d \n" % (name, event.name, event.time))

def delete_event():
    name = input("Event name: ")
    event = get_event_by_name(name)
    
    if event == None: return
    
    del events[event.ID]
    print("\n%s has been deleted. \n" % (name))

def print_events():
    print("")
    events.sort(key=lambda x: x.time)
    for e in range(len(events)):
        print("%s. %s at %s." % (e+1, events[e].name, events[e].time))
    print("")
        

while run:
    print("a. Add new event")
    print("b. Edit event")
    print("c. Delete event")
    print("p. Print events")
    print("x. Exit")

    cmd = input("Please choose from the options above: ").lower()

    if cmd == "a":
        add_event()
    elif cmd == "b":
        edit_event()
    elif cmd == "c":
        delete_event()
    elif cmd == "p":
        print_events()
    elif cmd == "x":
        run = False
    else:
        print("Unkown command."+"\n")
        
