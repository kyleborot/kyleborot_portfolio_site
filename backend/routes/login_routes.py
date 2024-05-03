from flask import Blueprint, render_template, jsonify, request
from login.forms import RegistrationForm, LoginForm, UpdateUserForm, UpdatePasswordForm, DeleteForm
from login.user_authentication import login_user, register_user, update_username, update_user_password, delete_user, get_max_user_id, get_max_login_id
from login.password_hashing import password_hashing
from config.config import conn

login_routes = Blueprint('login', __name__)

user_id = get_max_user_id() + 1
login_id = get_max_login_id() + 1

@login_routes.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            if login_user(username, password):
                return jsonify({'message': 'User login successful.'}), 200
            else:
                return jsonify({'message': 'User login failed.'}), 200
        else:
            errors = {field: error for field, error in form.errors.items()}
            return jsonify({'message': 'Validation failed', 'errors': errors}), 400
    elif request.method == 'GET':
        return render_template("login.html", form=form)
    else:
        return jsonify({'message': 'Method not allowed'}), 405
@login_routes.route("/register", methods=['GET','POST'])
def register():
    global user_id
    global login_id
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data
            email = form.email.data
            register_user(user_id, username, first_name, last_name, password, email)
            user_id += 1
            login_id += 1
            return jsonify({'message': 'User registered successfully.', 'user_id': user_id}), 200
        else:
            errors = {field: error for field, error in form.errors.items()}
            return jsonify({'message': 'Validation failed', 'errors': errors}), 400
    elif request.method == 'GET':
        return render_template("register.html", form=form)
    else:
        return jsonify({'message': 'Method not allowed'}), 405
@login_routes.route("/delete", methods=['GET', 'POST'])
def delete():
    global user_id
    global login_id
    """
    Match the Delete Form
    get all data from form fields
    Use in delete_user() from user_authentication
    return same jsonify's
    """
    return

@login_routes.route("/update/user", methods=['GET', 'POST'])
def update_username():
    global user_id
    global login_id
    form = UpdateUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_username = form.new_username.data
            confirm_username = form.confirm_username.data
            password = form.password.data
            email = form.email.data
            update_username(new_username, confirm_username, password, email)
            return jsonify({'message': 'User updated successfully.', 'username': new_username}), 200
        else:
            errors = {field: error for field, error in form.errors.items()}
            return jsonify({'message': 'Update failed', 'errors': errors}), 400
    elif request.method == 'GET':
        return render_template("updateUser.html", form=form)
    else:
        return jsonify({'message': 'Method not allowed'}), 405

@login_routes.route("/update/password", methods=['GET', 'POST'])
def update_password():
    global user_id
    global login_id
    """
    Match the update Password form
    get all data from form fields
    Use data in update_user_password() in user_authentication
    return same jsonify's
    """
    return