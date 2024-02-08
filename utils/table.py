class Seat:
    def __init__(self, free = True, occupant = ""):
        self._free = free
        self._occupant = occupant
        
    
    def __str__(self):
        if self._free != True:
            return self._occupant
        else:
            return "Empty"
    
    def set_occupant(self, name):
        self._occupant = name
        self._free = False
        return name
    """    
    def remove_occupant(self, position):
        self._position = position
        if self._position in Table():
            self._free = True
            oldoccupant = self._occupant
            self._occupant = ""
            return oldoccupant
        """

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
        self._occupant = ""
    
class Table(Seat):
    def __init__(self, capacity, seats):
        self._capacity = capacity
        self._seats = seats
    
    def __str__(self):
        return str([str(seat) for seat in self._seats])
    
    def has_free_spot(self):
        if self._capacity == len(self._seats):
            return False
        else:
            return True
        
    def assign_seat(self, name):
        if self.has_free_spot() == True:
            self._seats.append(name)
        else:
            return False
            
    def left_capacity(self):
        return self._capacity - len(self._seats)
    
    
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self):
        self._capacity = 4
    @property
    def seats(self):
        return self._seats
    @seats.setter
    def seats(self):
        self._seats = []