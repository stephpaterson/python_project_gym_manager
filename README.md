# python_project_gym_manager

#### Project Overview

This project was set by CodeClan as part of the Professional Software Development bootcamp. The breif was to create a gym manangement tool that helped a local gym to manage gym classes and memberships. The MVP was to do the folowing:

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

The project went on to complete a few extensions:
- The ability to manage class capacities and display availability to the user.
- Update the status of classes to account for cancelled classes and those that took place in the past.
- The ability to search by member names.

#### Tech Stack

This is a fully functioning CRUD app created with the following:

- Python
- Flask
- Postgresql & psycopg2
- HTML and CSS (no javascript or frameworks allowed)


https://user-images.githubusercontent.com/96059379/154314570-a37f361d-f122-478a-beb5-0ce912077fee.mov

#### How to Run

You will need Python3, Flask, postgres and psycopg2 installed.

Clone the repo and create a database via the terminal: 

```createdb <databse name>```

You'll then need to run the SQL file with psql in the terminal:

```psql -d <data base name> -f gym_manager.sql```

Finally, run the command following command in the terminal from the project root directory:

```flask run```
