# ClickFox Take Home Assignment
This project is a take home assignment from ClickFox. The project is a Flask REST service with two endpoints.
The service has an endpoint to accept JSON data, which holds information on a single phone call record. 

# Setup
Clone this repository:
`git clone https://github....`

# Dependencies
  1. Install [MongoDB](https://docs.mongodb.com/manual/installation/)
  2. Start MongoDB on port 27017 with `sudo service mongod start`.
  3. Create a MongoDB database called `clickfox_app` with `use clickfox_app`.
  4. Create a collection in the `clickfox_app` database called `calls`.

# Running the code
  1. After cloning the repository, activate the virtualenv `. venv/bin/activate` 
  2. Install the libraries needed with `pip install -r requirements.txt`
  3. Set the environment variables with `export FLASK_APP=app; export FLASK_ENV=development`
  4. At the top level directory, run the flask app with `flask run`
  
# Endpoints
  1. `/calls/ Methods = ('POST', 'GET')`
  2. `POST /calls/upload/ Methods = ('POST')`
  3. `/calls/mean/<> Methods = ('GET')`
  
# Examples
## `GET /calls/`
  1. `curl http://127.0.0.1:5000/calls/` returns one sample
## `POST /calls/`
  1. `curl -d '{"uuid":"1"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calls/` inserts a single sample
## `POST /calls/upload/`
  1. `curl -F "file=@JDS_Sample-phone_20140401_small.json" http://127.0.0.1:5000/calls/upload` bulk inserts json from file
## `GET /calls/mean/<>`

