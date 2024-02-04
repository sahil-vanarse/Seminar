from flask import *
from flask_mail import Mail

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"