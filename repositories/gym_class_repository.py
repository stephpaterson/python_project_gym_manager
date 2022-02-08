from models.gym_class import GymClass
from db.run_sql import run_sql
from models.member import Member

# CREATE

def save(gym_class):

    sql = """
    INSERT INTO gym_classes (name, instructor, location, date, time, capacity, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING id
    """
    values = [gym_class.name, gym_class.instructor, gym_class.location, gym_class.date, gym_class.time, gym_class.capacity, gym_class.status]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

# READ
# Select all

def select_all():

    gym_classes = []
    
    sql = """
    SELECT * FROM gym_classes
    ORDER BY date, time
    """
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(
            row['name'], 
            row['instructor'],
            row['location'],
            row['date'],
            row['time'],
            row['capacity'],
            row['status'],
            row['id']
            )
        gym_classes.append(gym_class)

    return gym_classes
    

# Select by id

def select_id(id):
    gym_class = None

    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = GymClass(
            result['name'], 
            result['instructor'], 
            result['location'],
            result['date'],
            result['time'],
            result['capacity'],
            result['status'],
            result['id'])

    return gym_class    

# Select only active courses

def select_active():
    gym_classes = []
    
    sql = """
    SELECT * FROM gym_classes
    WHERE status = %s
    ORDER BY date, time
    """
    values = ['active']
    results = run_sql(sql, values)

    for row in results:
        gym_class = GymClass(
            row['name'], 
            row['instructor'],
            row['location'],
            row['date'],
            row['time'],
            row['capacity'],
            row['status'],
            row['id']
            )
        gym_classes.append(gym_class)

    return gym_classes


# UPDATE

def update(gym_class):
    sql = """
    UPDATE gym_classes 
    SET (name, instructor, location, date, time, capacity, status) = (%s, %s, %s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [gym_class.name, gym_class.instructor, gym_class.location, gym_class.date, gym_class.time, gym_class.capacity, gym_class.status, gym_class.id]
    run_sql(sql, values)


# DELETE

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def members(gym_class):

    members = []

    sql = """
    SELECT members.* FROM members
    INNER JOIN bookings
    ON bookings.member_id = members.id
    WHERE gym_class_id = %s
    """
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['phone_number'], row['email'], row['id'])
        members.append(member)
    return members

# Count the number of members (bookings) on gym_class
def count_members(gym_class):
    count = None

    sql = """
    SELECT COUNT(*)
    FROM members
    INNER JOIN bookings
    ON bookings.member_id = members.id
    WHERE gym_class_id = %s
    """
    values = [gym_class.id]
    result = run_sql(sql, values)[0]
    count = result['count']
    return count