from flask import Blueprint, render_template, jsonify, request
from login.forms import RegistrationForm, LoginForm
from login.user_authentication import register_user
from config.config import conn

login_routes = Blueprint('login', __name__)


user_id = 2

@login_routes.route("/login")
def login():
  return "This is the login page"

@login_routes.route("/register", methods=['GET','POST'])
def register():
    global user_id
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            register_user(user_id, username, password, email)
            user_id += 1
            return jsonify({'message': 'User registered successfully'}), 200
        else:
            errors = {field: error for field, error in form.errors.items()}
            return jsonify({'message': 'Validation failed', 'errors': errors}), 400
    elif request.method == 'GET':
        return render_template("register.html", form=form)
    else:
        return jsonify({'message': 'Method not allowed'}), 405