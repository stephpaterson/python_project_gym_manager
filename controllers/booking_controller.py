from flask import Flask, render_template, Blueprint, redirect, request

import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.gym_class_repository as gym_class_repo

booking_blueprint = Blueprint("bookings", __name__)

@booking_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repo.select_by_id(id)
    return render_template('/booking/show.html', booking=booking)