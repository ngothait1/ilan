############# FUNCTIONS #############


# CHECK INPUTS
def isInputID(input):
    if  not input.isdigit():
        print(f"Error: ID must be a number. {input} is not a number")
        return False
        
    return True

def isInputAge(input):
    if not input.isdigit():
        print(f"Error: Age must be a number. {input} is not a number")
        return False
    
    elif int(input) > 120 and int(input) < 0:
        print(f"Error: Age must be a number between 0 to 120")
        return False
    
    return True

def isInputMenu(input):
    if not input.isdigit():
        print("Error: you must enter a number between 1 to 8")
        return False
        
    elif input.isdigit() and (int(input) < 1 or int(input) > 8):
        print(f"Error: Option [{input}] does not exist. Please try again")
        return False
        
    return True

# OPTION 1
def saveNewEntry(data: dict, count):
    id = input("ID: ")
    if not isInputID(id):
        return
    
    id = int(id)
    if id in data:
        print(f"Error: ID already exists: {data[id]}")
        return

    name = input("Name: ")
    age = input("Age: ")
    if not isInputAge(age):
        return
    
    age = int(age)
    data[id] = {"name": name, "age": age}

    if id in data:
        print(f"ID [{id}] saved successfully")
        count["ages_sum"] += age
        count["id_count"] += 1

    else:
        print("Error: failed to save new entry")

# OPTION 2
def searchById(data: dict):
    id = input("Please enter the ID you want to look for: ")
    if not isInputID(id):
        return
    
    id = int(id)

    if id in data:
        print(f"ID: {id}")
        print(f"Name: {data[id]['name']}")
        print(f"Age: {data[id]['age']}")

    else:
        print(f"Error: ID {id} is not saved")

# OPTION 3
def printAgesAverage(count):
    if count["id_count"] > 0:
        average_age = count["ages_sum"] / count["id_count"]
        print(f"Average age is: {average_age}")
    
    else:
        print("Error: Can't divide by 0")
    
# OPTION 4
def printAllNames(data: dict):
    for i, entry in enumerate(data.values()):
        print(f"{i}. {entry['name']}")

# OPTION 5
def printAllIds(data: dict):
    for i, entry in enumerate(data.keys()):
        print(f"{i}. {entry}")

# OPTION 6
def printAllEntries(data: dict):
    for i, (id, entry) in enumerate(data.items()):
        print(f"{i}.ID: {id}\n  Name: {entry['name']}\n  Age: {entry['age']}")

# OPTION 7
def printEntryByIndex(data: dict):
    user_input = input("Please enter the index you want to print: ")
    if not user_input.isdigit():
        print(f"Error: index must by a number. {user_input} is not a number")
        return
    
    index = int(user_input)
    data_list = list(data.items())

    if index < len(data_list):
        id, values = data_list[index]
        printEntry(id, values['name'], values['age'])

    else:
        print(f"Error: Index out of range. The maxium index allowd is {len(data_list)-1}")


# OPTION 8
def exitProgram():
    while True:
        user_input = input("Are you sure? (y/n) ")
        if user_input == "y":
            print("Goodbye!")
            exit()

        elif user_input == "n":
            return

# ETC
def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")

def printEntry(id, name, age):
    print(f"ID: {id}\n  Name: {name}\n  Age: {age}")


############# MAIN #############

demo_entries = {101: {"name": "Dave", "age": 24}, 102: {"name": "Nate", "age": 31}, 103: {"name": "Bob", "age": 42}}
entries = {}
counter = {"ages_sum": 0, "id_count": 0}

while True:
    printMenu()
    user_choice = input("Please enter your choice: ")
    if not isInputMenu(user_choice):
        continue  

    if user_choice == "1":
        saveNewEntry(entries, counter)

    elif user_choice == "2":
        searchById(entries)

    elif user_choice == "3":
        printAgesAverage(counter)

    elif user_choice == "4":
        printAllNames(entries)

    elif user_choice == "5":
        printAllIds(entries)

    elif user_choice == "6":
        printAllEntries(entries)

    elif user_choice == "7":
        printEntryByIndex(entries)

    elif user_choice == "8":
        exitProgram()
        continue
    
    input("Press to continue")
        