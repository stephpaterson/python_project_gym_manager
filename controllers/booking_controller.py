from flask import Flask, render_template, Blueprint, redirect, request

from models.booking import Booking

import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.gym_class_repository as gym_class_repo

booking_blueprint = Blueprint("bookings", __name__)



@booking_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repo.select_by_id(id)
    return render_template('/booking/show.html', booking=booking)

@booking_blueprint.route('/bookings/new')
def new_booking():
    gym_classes = gym_class_repo.select_all()
    members = member_repo.select_all()
    return render_template('/booking/new.html', gym_classes=gym_classes, members=members)

@booking_blueprint.route('/bookings', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repo.select_by_id(member_id)
    gym_class = gym_class_repo.select_id(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repo.save(booking)
    return redirect('/')