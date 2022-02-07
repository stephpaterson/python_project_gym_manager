import unittest
from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.gym_class = GymClass("Spin", "Graeme", "Studio 1", "10/02/2021", "10:00", 5, 1)
        self.member_1 = Member('Jack', 'Jones', '012345', 'jack@email.com')
        self.member_2 = Member('Jill', 'Jones', '067891', 'jill@email.com')
        self.booking = Booking(self.member_1, self.gym_class)
        self.booking_2 = Booking(self.member_2, self.gym_class)
        self.bookings = [self.booking, self.booking_2]
