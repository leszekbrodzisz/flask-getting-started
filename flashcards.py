from datetime import datetime
from flask import Flask

visit_counter = 0

app = Flask(__name__)

@app.route("/")

def welcome():
    return "Welcome to my Flask3"

@app.route("/date")
def date():

    return "This Page was served at " + str(datetime.now())

@app.route("/count_views")
def count_views():
    global visit_counter
    visit_counter += 1
    return "This is " + str(visit_counter) + " visit"

