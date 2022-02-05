from models.gym_class import GymClass
from db.run_sql import run_sql

# CREATE

def save(gym_class):

    sql = """
    INSERT INTO gym_classes (name, instructor, location, date, time)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id
    """
    values = [gym_class.name, gym_class.instructor, gym_class.location, gym_class.date, gym_class.time]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

# READ
# Select all

def select_all():

    gym_classes = []
    
    sql = """
    SELECT * FROM gym_classes
    """
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(
            row['name'], 
            row['instructor'],
            row['location'],
            row['date'],
            row['time'],
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
            result['id'])

    return gym_class    


# UPDATE

def update(gym_class):
    sql = """
    UPDATE gym_classes 
    SET (name, instructor, location, date, time) = (%s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [gym_class.name, gym_class.instructor, gym_class.location, gym_class.date, gym_class.time, gym_class.id]
    run_sql(sql, values)


# DELETE

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)
