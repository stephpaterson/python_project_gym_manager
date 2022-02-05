import pdb
from models.gym_class import GymClass

import repositories.gym_class_repository as gym_class_repo

gym_class_repo.delete_all()

gym_class_1 = GymClass('Spin', 'Beth', 'Studio 1', '1st Feb', '10am')
gym_class_repo.save(gym_class_1)

print(gym_class_repo.select_all())


pdb.set_trace()