import datetime


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

    def change_status_inactive(self):
        # Need to convert date to a string
        gym_class_date_str =str(self.date)
        # convert this string to datetime object
        gym_class_date = datetime.date.fromisoformat(gym_class_date_str)
        # get today's date
        today = datetime.date.today()
        # if status is active
        if self.status == "active":
        # compare the class date to the time now
            if gym_class_date < today:
        # if date in past set to inactive
                self.status = "inactive"
        
        
