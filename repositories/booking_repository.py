from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member

import repositories.member_repository as member_repo
import repositories.gym_class_repository as gym_class_repo

from db.run_sql import run_sql

# CREATE

def save(booking):

    sql = """
    INSERT INTO bookings (member_id, gym_class_id) VALUES (%s, %s)
    RETURNING id
    """
    values =[booking.member.id, booking.gym_class.id]
    result = run_sql(sql, values)
    booking.id = result[0]['id']
    return booking
# READ

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select_by_id(row['member_id'])
        gym_class = gym_class_repo.select_id(row['gym_class_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)

    return bookings

def select_by_id(id):

    booking = None

    sql ="SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repo.select_by_id(result['member_id'])
        gym_class = gym_class_repo.select_id(result['gym_class_id'])
        booking = Booking(member, gym_class, id)

    return booking

# UPDATE
# DELETE

def delete_by_id(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def booking_by_gym_class(gym_class):

    bookings = []

    sql= """
    SELECT bookings.* FROM bookings
    WHERE gym_class_id = %s
    """
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = member_repo.select_by_id(row['member_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings

def booking_by_member(member):
    bookings = []

    sql = """
    SELECT bookings.* FROM bookings
    WHERE member_id =%s
    """
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = gym_class_repo.select_id(row['gym_class_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings