from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repo

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repo.select_all()
    return render_template("gym_class/index.html", gym_classes=gym_classes)

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
    gym_class = GymClass(name, instructor, location, date, time)
    gym_class_repo.save(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>", methods = ['GET'])
def show_gym_class(id):
    gym_class = gym_class_repo.select_id(id)
    return render_template('gym_class/show.html', gym_class=gym_class)
