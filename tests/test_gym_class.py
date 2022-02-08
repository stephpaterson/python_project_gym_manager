import unittest
from models.gym_class import GymClass
from models.member import Member
import pdb

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.gym_class = GymClass("Spin", "Graeme", "Studio 1", "2022-02-07", "10:00", 5, "active", id = None)
        self.member_1 = Member('Jack', 'Jones', '012345', 'jack@email.com')
        self.member_2 = Member('Jill', 'Jones', '067891', 'jill@email.com')
        self.member_list = [self.member_1, self.member_2]
        self.member_list_2 = [self.member_1, self.member_2, self.member_1, self.member_2, self.member_1, self.member_2 ]

    @unittest.skip
    def test_capacity_check_spaces(self):
        result = self.gym_class.capacity_check_space_available(self.member_list)
        self.assertEqual(True, result)

    @unittest.skip
    def test_capacity_check_full(self):
        result = self.gym_class.capacity_check_space_available(self.member_list_2)
        self.assertEqual(False, result)

    def test_change_to_inactive(self):
        # pdb.set_trace()
        self.gym_class.change_status_inactive()
        result = self.gym_class.status
        self.assertEqual('inactive', result)

