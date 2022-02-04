from flask import Flask, render_template
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repo

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repo.select_all()
    return render_template("gym_class/index.html", gym_classes=gym_classes)