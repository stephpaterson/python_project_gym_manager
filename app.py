from flask import Flask, render_template

from controllers.gym_classes_controller import gym_classes_blueprint
from controllers.members_controller import members_blueprint
from controllers.bookings_controller import booking_blueprint

app = Flask(__name__)

app.register_blueprint(gym_classes_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(booking_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

