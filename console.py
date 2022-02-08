import pdb
from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking

import repositories.gym_class_repository as gym_class_repo
import repositories.member_repository as member_repo
import repositories.booking_repository as booking_repo

gym_class_repo.delete_all()

gym_class_1 = GymClass('Spin', 'Beth', 'Studio 1', '2022-02-01', '10:00', 5, 'active')
gym_class_repo.save(gym_class_1)

gym_class_2 = GymClass('Spin', 'Beth', 'Studio 1', '2022-02-20', '10:00', 5, 'active')
gym_class_repo.save(gym_class_2)

member_1 = Member('David', 'Henderson', '019876', 'david@email.com')
member_repo.save(member_1)

booking_1 = Booking(member_1, gym_class_1)
booking_repo.save(booking_1)
booking_2 = Booking(member_1, gym_class_1)
booking_repo.save(booking_2)

member_count = gym_class_repo.count_members(gym_class_1)
print(gym_class_repo.select_all())
print(gym_class_repo.select_future() )

pdb.set_trace()