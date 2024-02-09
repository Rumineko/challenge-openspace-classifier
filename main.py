from json import load
from utils.openspace import Openspace
from csv import reader
from random import shuffle
from utils.table import Seat, Table

# First we load up our CSV file.
def read_names(filename):
    # We create an empty list, called names. This is where we are going to store all of our names.
    names = []
    # We assign it to a variable to process it
    with open(filename, 'r') as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            # We append the first column to the list of names we created
            names.append(row[0])
    # We return the list
    return names

# Now we create a config loader
def load_config():
    # Assign it to a variable
    with open("./utils/config.json", "r") as config_file:
        config = load(config_file)
    # And return the config
    return config

# Now onto our main function
def main():
    # We start by loading up our config
    config = load_config()

    # Assign our variables to specific parts of the config file
    number_of_tables = config["number_of_tables"]
    file_path = config["file_path"]
    table_capacity = config["table_capacity"]
    
    # This one is probably confusing, but we are essentially creating a List of Tables, where each element is an instance of the Table class we created.
    table = [Table(table_capacity, []) for _ in range(number_of_tables)]

    # and we launch our Openspace class, using some of our variables
    openspace = Openspace(number_of_tables, table)
    # as well as using our read_names function to get our name_list from it
    name_list = read_names(file_path)

    # This is WIP
    seat = Seat()

    # Shuffle the names
    shuffle(name_list)

    # Get the result and remaining names
    endresult, remaining_names = openspace.organize(name_list)

    # Display the information
    openspace.display(endresult)

    # If there are any remaining names we get after organizing, we will print them out.
    if remaining_names:
        print("Unable to seat the following people:")
        print(remaining_names)
    
    # We also Display our Remaining Seats or Missing Seats, if there are any.
    openspace.display_remaining_seats(endresult, remaining_names)

    # Store the information in an Excel file
    openspace.store("output.xlsx", endresult, remaining_names)

"""
    # Work in Progress: Interactive step (WIP)
    changes_requested = input("Do you want to make changes? (yes/no): ").lower()

    while changes_requested == 'yes':
        action = input("Do you want to add or remove an occupant? (add/remove): ").lower()

        if action == 'add':
            name_to_add = input("Enter the name to add: ")
            success = openspace.add_occupant(name_to_add)

            if success:
                print(f"Successfully added {name_to_add} to a random seat.")
            else:
                print("No available seats to add an occupant.")

        elif action == 'remove':
            old_occupant = openspace.remove_occupant()

            if old_occupant:
                print(f"Successfully removed {old_occupant} from a random seat.")
            else:
                print("No occupants to remove.")

        else:
            print("Invalid action. Please enter 'add' or 'remove'.")

        changes_requested = input("Do you want to make more changes? (yes/no): ").lower()

    # Store the information in an Excel file after changes
    openspace.store("output.xlsx", endresult, remaining_names)
"""

# The typical thing, just for common practice
if __name__ == "__main__":
    main()