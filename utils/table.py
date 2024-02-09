# Our class, Seat.
class Seat:
    # Initializes two variables, free, a boolean, and occupant, a string
    def __init__(self, free = True, occupant = ""):
        self._free = free
        self._occupant = occupant
    # When called on, it will either return the Occupant string or Empty, in case it is currently Empty
    def __str__(self):
        if self._free:
            return "Empty"
        else:
            return str(self._occupant)
    
    def set_occupant(self, name):
        """
        Function that will add an occupant to an existing seat.

        :param name: Name of the person that will occupy the seat
        :return: Either True or False, depending on whether or not the seat is currently Empty.
        """
        if self._free:
            self._occupant = name
            self._free = False
            return True
        else:
            return False
    
    def remove_occupant(self):
        """
        WIP Function that will remove a random person from a seat that is currently occupied

        :return: A string with either the name of the previous Occupant, or, if there are no seats being occupied, will mention it.
        """
        if not self._free:
            old_occupant = self._occupant
            self._occupant = ""
            self._free = True
            return old_occupant
        else:
            return "No occupants to remove"
    
    # Some of our properties, probably didn't make as much good use of them as I had hoped
    @property
    def free(self):
        return self._free

    @free.setter
    def free(self):
        if self._occupant == "":
            self._free = True
        else:
            self._free = False
  
    @property
    def occupant(self):
        return self._occupant
    
    @occupant.setter
    def occupant(self):
        if self._free:
            return ""
        else:
            return self._occupant
    
# Our table Class
class Table(Seat):
    # We initialize two variables, the maximum amount of seats we can have per table, and seats, a list, where we will store the name of people sitting 
    # at the tables.
    def __init__(self, capacity, seats):
        self._capacity = capacity
        self._seats = seats
    
    # Our string will return the occupants of said table.
    def __str__(self):
        return str([str(seat) for seat in self._seats])
    
    def has_free_spot(self):
        """
        Function that will check whether or not there are free spots in the current table.

        :return: Either False, if the table is at its capacity, or True, if there are still seats available.
        """
        if self._capacity == len(self._seats):
            return False
        else:
            return True
        
    def assign_seat(self, name):
        """
        Function that will assign a seat to someone. It is reliant on has_free_spot, therefore will assign a seat if there is one available, and not, if not.

        :param name: Name of the person taking a seat at said table
        :return: True, if there is a free spot. False, if not.
        """
        if self.has_free_spot():
            self._seats.append(name)
            return True
        else:
            return False
            
    def left_capacity(self):
        """
        Function that will check the amount of seats we have remaining at the table.

        :return: Amount of seats we still have free.
        """
        return self._capacity - len(self._seats)
    
    # Some properties, mainly capacity and seats
    @property
    def capacity(self):
        return self._capacity

    @property
    def seats(self):
        return self._seats