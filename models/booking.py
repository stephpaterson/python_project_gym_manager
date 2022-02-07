class Booking:

    def __init__(self, member, gym_class, id = None):
        self.member = member
        self.gym_class = gym_class
        self.id = id

    def spaces_available(self, bookings, gym_class):
        # Need pass in all bookings and the gym_class
        # Get the length of the list of bookings
        number_bookings = len(bookings)
        # Get the capacity from the gym_class
        capacity = gym_class.capacity
        # Compare the length of the list and the capacity of the gym_class
         # Return True is length of list is less than capacity
        if number_bookings < capacity:
            return True
         # Return False if length of list is equal to or more than capacity       
        elif number_bookings >= capacity:
            return False
       
