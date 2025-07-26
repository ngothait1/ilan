import os
import json
import pandas as pd

############# FUNCTIONS #############


# CHECK INPUTS
def isNumber(input, type: str):
    if not input.isdigit():
        print(f"Error: {type} must be a number. {input} is not a number")
        return False
    
    return True

def isValidAge(input):
    if not isNumber(input, "age"):
        return False
    
    elif int(input) > 120 or int(input) < 0:
        print(f"Error: Age must be a number between 0 to 120")
        return False
    
    return True

def isValidMenuChoice(input):
    if not input.isdigit():
        print("Error: you must enter a number between 1 to 9")
        return False
        
    elif input.isdigit() and (int(input) < 1 or int(input) > 9):
        print(f"Error: Option [{input}] does not exist. Please try again")
        return False
        
    return True

# OPTION 1
def saveNewEntry(data: dict, count: dict, ids: list):
    id = input("ID: ")
    if not isNumber(id, "id"):
        return
    
    id = int(id)
    if id in data:
        print(f"Error: ID already exists: {data[id]}")
        return

    name = input("Name: ")
    age = input("Age: ")
    if not isValidAge(age):
        return
    
    age = int(age)
    data[id] = {"name": name, "age": age}

    # if id in data:
    print(f"ID [{id}] saved successfully")
    count["ages_sum"] += age
    count["id_count"] += 1
    ids.append(id)

    # else:
    #     print("Error: failed to save new entry")

# OPTION 2
def searchById(data: dict):
    id = input("Please enter the ID you want to look for: ")
    if not isNumber(id, "id"):
        return
    
    id = int(id)

    if id in data:
        printEntry(id, data[id]['name'], data[id]['age'])

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
        print(f"{i}.", end=" ")
        printEntry(id, entry['name'], entry['age'])

# OPTION 7
def printEntryByIndex(data: dict, ids: list):
    user_input = input("Please enter the index you want to print: ")
    if not isNumber(user_input, "index"):
        return
    
    index = int(user_input)
    # data_list = list(data.items())

    if index < len(ids):
        id = ids[index]
        values = data[id]
        printEntry(id, values['name'], values['age'])

    else:
        print(f"Error: Index out of range. The maxium index allowd is {len(ids)-1}")

# OPTION 8
def saveToCSV(data: dict):
    if not os.path.exists("./config.json"):
        print(f"Error: Config file conf.json is missing in path {os.getcwd()}")
        return

    output_file_name = input("What is your output file name? ") + ".csv"

    with open("config.json") as config_json:
        loaded_config = json.load(config_json)

        data_table = {
            loaded_config["id"]: list(data.keys()),
            loaded_config["name"]: [],
            loaded_config["age"]: []
        }

        for value in data.values():
            data_table[loaded_config["name"]].append(value['name'])
            data_table[loaded_config["age"]].append(value['age'])

        df = pd.DataFrame(data_table)
        df.to_csv(output_file_name, index=False)

# OPTION 9
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
    print("8. Save all data")
    print("9. Exit")

def printEntry(id, name, age):
    print(f"ID: {id}\n  Name: {name}\n  Age: {age}")


############# MAIN #############

demo_data = {101: {"name": "Dave", "age": 24}, 102: {"name": "Nate", "age": 31}, 103: {"name": "Bob", "age": 42}}
counter = {"ages_sum": 0, "id_count": 0}
data = {}
id_list = []

while True:
    printMenu()
    user_choice = input("Please enter your choice: ")
    if not isValidMenuChoice(user_choice):
        continue  

    if user_choice == "1":
        saveNewEntry(data, counter, id_list)

    elif user_choice == "2":
        searchById(data)

    elif user_choice == "3":
        printAgesAverage(counter)

    elif user_choice == "4":
        printAllNames(data)

    elif user_choice == "5":
        printAllIds(data)

    elif user_choice == "6":
        printAllEntries(data)

    elif user_choice == "7":
        printEntryByIndex(data, id_list)

    elif user_choice == "8":
        saveToCSV(demo_data)

    elif user_choice == "9":
        exitProgram()
        continue
    
    input("Press Enter to continue")
        