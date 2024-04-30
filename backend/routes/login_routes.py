from flask import Blueprint
from config.config import conn

login_routes = Blueprint('login', __name__)

@login_routes.route("/login")
def login():
  return "This is the login page"

@login_routes.route("/registration")
def registration():
    return "This is the registration page"