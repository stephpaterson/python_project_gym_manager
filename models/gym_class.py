from tabnanny import check


class GymClass:

    def __init__(self, name, instructor, location, date, time, capacity, status, id = None, availability = None ):
        self.name = name
        self.instructor = instructor
        self.location = location
        self.date = date
        self.time = time
        self.capacity = capacity
        self.status = status
        self.id = id
        self.availability = availability

    def check_space_available(self, member_count):
        if member_count >= self.capacity:
            return False
        elif member_count < self.capacity:
            return True
    
    def set_availability(self, member_count):
        availability = self.check_space_available(member_count)
        self.availability = availability
