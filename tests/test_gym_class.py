import unittest
from models.gym_class import GymClass
from models.member import Member

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.gym_class = GymClass("Spin", "Graeme", "Studio 1", "10/02/2021", "10:00", 5, id = None)
        self.member_1 = Member('Jack', 'Jones', '012345', 'jack@email.com')
        self.member_2 = Member('Jill', 'Jones', '067891', 'jill@email.com')
        self.member_list = [self.member_1, self.member_2]
        self.member_list_2 = [self.member_1, self.member_2, self.member_1, self.member_2, self.member_1, self.member_2 ]

    def test_capacity_check_spaces(self):
        result = self.gym_class.capacity_check_space_available(self.member_list)
        self.assertEqual(True, result)

    
    def test_capacity_check_full(self):
        result = self.gym_class.capacity_check_space_available(self.member_list_2)
        self.assertEqual(False, result)

