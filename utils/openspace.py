from .table import Table
from .table import Seat
from random import randint

table_capacity = 4
seats_table = []
table = Table(table_capacity, seats_table)
tables = []

class Openspace:
    def __init__(self, number_of_tables):
        self._number_of_tables = number_of_tables
        
    def __str__(self):
        for table in tables:
            for seat in table:
                return f"{table[seat]} sitting in table {table}"  
    
    def organize(self, names):
        self._names = names
        while self._number_of_tables > len(tables):
            for person in names:
                seat = Seat()
                seat.set_occupant(person)
                if table.assign_seat(seat) == False:
                    tables.append(seats_table)
                    print(seats_table)
                    seats_table.clear()
                    table.assign_seat(person)
                else:
                    table.assign_seat(person)
        
        
    def display(self):
        return str([str(tables) for table in tables])
        
    def store(self, filename):
        pass

    @property
    def number_of_tables(self):
        return self._number_of_tables
    
    @number_of_tables.setter
    def number_of_tables(self):
        self._number_of_tables = 6