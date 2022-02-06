
class GymClass:

    def __init__(self, name, instructor, location, date, time, capacity, id = None ):
        self.name = name
        self.instructor = instructor
        self.location = location
        self.date = date
        self.time = time
        self.capacity = capacity
        self.id = id

    def capacity_check_space_available(self, member_list):
        number_bookings = len(member_list)
        if number_bookings >= self.capacity:
            return False
        elif number_bookings < self.capacity:
            return True