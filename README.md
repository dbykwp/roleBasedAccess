# roleBasedAccess
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bina/activate

# intall dependencies

pip install requirments.txt

#-------------------------

To run the app
---
# getting migration file
python manage.py makemigrations role_base_access
# to do migration
python manage.py migrate
# runing app
python manage.py runserver

api end points:
To Create user
    POST request
    http://localhost:8000/rba/user
        json body
            {
                "first_name": "UserName",
            }

To get list of all users:
    http://localhost:8000/rba/user (GET)

Role apis
---
To get all existing roles
GET request http://localhost:8000/rba/role

To Add Role
POST request http://localhost:8000/rba/role
    request body
    {
        "name": "Admin123"
    }

To Assign role to user
---
POST: http://localhost:8000/rba/user_role
request body
    {
        "role": "Admin", (name of user role)
        "user_id": 11 (user id of user one can get this one from http://localhost:8000/rba/user(GET))
    }

To Remove role assigned to user
---
DELETE: http://localhost:8000/rba/user_role
request body
    {
        "role": "Admin", (name of user role)
        "user_id": 11 (user id of user one can get this one from http://localhost:8000/rba/user(GET))
    }

# To add Role resouce action

POST: http://localhost:8000/rba/role_resource_action

body:
    {
        "action": "W", (optrion W, R, D [Write, Read, Delete])
        "role_resource": 3, # get http://localhost:8000/rba/resource (GET)
        "resource_role": 2 # get http://localhost:8000/rba/role (GET)
    }
