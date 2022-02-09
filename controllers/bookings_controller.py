from flask import Flask, render_template, Blueprint, redirect, request, url_for

from models.booking import Booking

import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.gym_class_repository as gym_class_repo

booking_blueprint = Blueprint("bookings", __name__)

@booking_blueprint.route('/bookings')
def show_all_bookings():
    bookings = booking_repo.select_all()
    return render_template('/booking/index.html', bookings=bookings)

@booking_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repo.select_by_id(id)
    return render_template('/booking/show.html', booking=booking)

@booking_blueprint.route('/bookings/new')
def new_booking():
    gym_classes = gym_class_repo.select_all()
    members = member_repo.select_all()
    return render_template('/booking/new.html', gym_classes=gym_classes, members=members)

@booking_blueprint.route('/bookings/', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repo.select_by_id(member_id)
    gym_class = gym_class_repo.select_id(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repo.save(booking)
    return redirect('/bookings/')

# Booking from gym_class

@booking_blueprint.route('/gym_classes/<id>/bookings/new')
def new_booking_gym_class(id):
    gym_class = gym_class_repo.select_id(id)
    members = member_repo.select_all()
    return render_template('/booking/new_gym.html', gym_class=gym_class, members=members)

@booking_blueprint.route('/bookings/gym_class', methods=['POST'])
def create_booking_by_gym_class():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repo.select_by_id(member_id)
    gym_class = gym_class_repo.select_id(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repo.save(booking)
    return redirect(f'/gym_classes/{gym_class_id}')

# Booking from member

@booking_blueprint.route('/members/<id>/bookings/new')
def new_booking_member(id):
    gym_classes_future_active = gym_class_repo.select_active_future()
    gym_classes = []
    for gym_class in gym_classes_future_active:
        count = gym_class_repo.count_members(gym_class)
        gym_class.set_availability(count)
        gym_classes.append(gym_class)
    member = member_repo.select_by_id(id)
    return render_template('/booking/new_member.html', gym_classes=gym_classes, member=member)

@booking_blueprint.route('/bookings/member', methods=['POST'])
def create_booking_by_member():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repo.select_by_id(member_id)
    gym_class = gym_class_repo.select_id(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repo.save(booking)
    return redirect(f'/members/{member_id}')

@booking_blueprint.route('/bookings/<id>/delete', methods=['POST'])
def delete_booking(id):
    booking_repo.delete_by_id(id)
    return redirect('/bookings')

@booking_blueprint.route('/members/<m_id>/bookings/<id>/delete', methods=['POST'])
def delete_member_booking(m_id, id):
    booking_repo.delete_by_id(id)
    return redirect(f'/members/{m_id}')

@booking_blueprint.route('/gym_classes/<g_id>/bookings/<id>/delete', methods=['POST'])
def delete_class_booking(g_id, id):
    booking_repo.delete_by_id(id)
    return redirect(f'/gym_classes/{g_id}')