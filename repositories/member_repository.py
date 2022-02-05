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