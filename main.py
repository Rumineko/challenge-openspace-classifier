from utils.openspace import Openspace
import csv

table_capacity = 4
table_list = []
number_of_tables = 6


file = "./new_colleagues.csv"
list = ['Afaf', 'Alexander', 'Alfiya', 'Alice', 'Andrea', 'Ariana', 'Caroline', 'Danil', 'Daryoush', 'Em', 'Fabienne', 'Geraldine', 'Gerrit', 'Ivan ', 'Jens', 'Karel', 'Mahsa', 'Miguel', 'Nasrin', 'Nathalie', 'Niels', 'Sweta', 'Viktor', 'Yanina']
tables = []
openspace = Openspace(number_of_tables)
"""
with open(file, 'r') as colleagues:
    reader = csv.reader(colleagues, delimiter="\n")
    for i in reader:
        list.append(str(i).replace("[","").replace("]","").replace("'",""))
"""
endresult = openspace.organize(list)



"""
seat.set_occupant(list[0])
table.assign_seat(seat)
seat.set_occupant(list[1])
table.assign_seat(seat)
seat.set_occupant(list[2])
table.assign_seat(seat)
seat.set_occupant(list[3])
table.assign_seat(seat)
if table.assign_seat(list[4]) == "Table is Full":
    print("Table Full Successful")
"""

#seat.remove_occupant()
