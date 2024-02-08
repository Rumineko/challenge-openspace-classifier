from utils.table import Table
from utils.table import Seat
#from utils.openspace import Openspace
import csv

table_capacity = 20
table_list = []


file = "./new_colleagues.csv"
list = []
tables = []
table = Table(table_capacity, table_list)
seat = Seat()

with open(file, 'r') as colleagues:
    reader = csv.reader(colleagues, delimiter="\n")
    for i in reader:
        list.append(str(i).replace("[","").replace("]","").replace("'",""))


print(table.has_free_spot())
if table.has_free_spot() == True:
    print("There're free spots")
else:
    print("Something went wrong")
i = 0
for i in range(len(list)):
    seat = Seat()
    seat.set_occupant(list[i])
    table.assign_seat(seat)
    i += 1

#openspace = Openspace()
    
print(list)

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
print(table)
