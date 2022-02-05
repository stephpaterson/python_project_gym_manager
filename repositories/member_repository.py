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
        member = Member(row['first_name'], row['last_name'], row['phone_number'], row['email'])
        members.append(member)

    return members

# UPDATE
# DELETE