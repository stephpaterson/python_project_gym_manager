from models.gym_class import GymClass
from models.member import Member
from db.run_sql import run_sql

# CREATE

def save(member):

    sql = """
    INSERT INTO members (first_name, last_name, phone_number, email) VALUES (%s, %s, %s, %s)
    RETURNING id
    """
    values = [member.first_name, member.last_name, member.phone_number, member.email]
    result = run_sql(sql, values)
    member.id = result[0]['id']
    return member

# READ

def select_all():

    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['phone_number'], row['email'], row['id'])
        members.append(member)

    return members

def select_by_id(id):

    member = None

    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['phone_number'], result['email'], result['id'])
    
    return member

    
# UPDATE
def update(member):

    sql = """
    UPDATE members SET (first_name, last_name, phone_number, email) = (%s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [member.first_name, member.last_name, member.phone_number, member.email, member.id]
    run_sql(sql, values)
# DELETE

def delete(id):

    sql = "DELETE FROM members WHERE id = %s"
    values =[id]
    run_sql(sql, values)

def gym_classes(member):

    gym_classes = []

    sql = """
    SELECT gym_classes.* FROM gym_classes
    INNER JOIN bookings
    ON bookings.gym_class_id = gym_classes.id
    WHERE member_id = %s
    """
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = GymClass(row['name'], row['instructor'], row['location'], row['date'], row['time'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def search_by_name(name):

    search_results = []

    sql = """
    SELECT * FROM members
    WHERE first_name LIKE %s OR last_name LIKE %s
    """
    values = [ '%'+name+'%' , '%'+name+'%' ]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['phone_number'], row['email'], row['id'])
        search_results.append(member)
    return search_results