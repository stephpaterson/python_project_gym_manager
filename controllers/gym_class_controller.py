from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
from models.booking import Booking
import repositories.booking_repository as booking_repo
import repositories.gym_class_repository as gym_class_repo

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repo.select_all()
    spaces = []
    for gym_class in gym_classes:
        members = gym_class_repo.members(gym_class)
        space = gym_class.capacity_check_space_available(members)
        spaces.append(space)  
    return render_template("gym_class/index.html", gym_classes=gym_classes, spaces=spaces)

@gym_classes_blueprint.route("/gym_classes/new", methods = ['GET'])
def gym_class_new():
    return render_template("gym_class/new.html")

@gym_classes_blueprint.route("/gym_classes", methods=['POST'])
def create_gym_class():
    name = request.form['name']
    instructor = request.form['instructor']
    location = request.form['location']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    gym_class = GymClass(name, instructor, location, date, time, capacity)
    gym_class_repo.save(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>", methods = ['GET'])
def show_gym_class(id):
    gym_class = gym_class_repo.select_id(id)
    bookings = booking_repo.booking_by_gym_class(gym_class)
    booking = bookings[0]
    availability = booking.spaces_available(bookings, gym_class)
    return render_template('gym_class/show.html', gym_class=gym_class, availability=availability, bookings=bookings)

@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods=['GET'])
def edit_class(id):
    gym_class = gym_class_repo.select_id(id)
    return render_template('/gym_class/edit.html', gym_class=gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update_class(id):
    name = request.form['name']
    instructor = request.form['instructor']
    location = request.form['location']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    gym_class = GymClass(name, instructor, location, date, time, capacity, id)
    gym_class_repo.update(gym_class)
    return redirect('/gym_classes')
