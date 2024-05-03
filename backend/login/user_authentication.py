from flask import Flask, render_template
from config.config import conn
from .password_hashing import password_hashing

def get_max_user_id():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(user_id) FROM LoginSchema.Users")
    max_user_id = cursor.fetchone()[0]
    cursor.close()
    return max_user_id if max_user_id else 0

def get_max_login_id():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(login_id) FROM LoginSchema.UserLogin")
    max_login_id = cursor.fetchone()[0]
    cursor.close()
    return max_login_id if max_login_id else 0

user_id = get_max_user_id() + 1
login_id = get_max_login_id() + 1

def login_user(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT hashed_password, password_salt, login_name FROM LoginSchema.UserLogin WHERE login_name = ?", (username))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        stored_salt = result[1]
        entered_password_hashed, _ = password_hashing(password, stored_salt)
        if stored_password == entered_password_hashed and username == result[2]:
            return True
    return False

def register_user(user_id, username, first_name, last_name, password, email):
    cursor=conn.cursor()
    hashed_password, password_salt = password_hashing(password)
    cursor.execute("INSERT INTO LoginSchema.Users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)", (user_id, first_name, last_name, email))
    cursor.execute("INSERT INTO LoginSchema.UserLogin (login_id, user_id, login_name, hashed_password, password_salt) VALUES (?, ?, ?, ?, ?)", (login_id, user_id, username, hashed_password, password_salt))
    conn.commit()
    cursor.close()
    return "User registered successfully, next user_id is {user_id}"
def update_username(new_username, confirm_username, password, email):
    cursor=conn.cursor()
    """
    Use email to get user_id
    Use user_id to get login_id
    Check if username provided matches username on file for that login_id
    If True, continue
    Use login_id to get password hash and salt
    hash the password param and compare
    if True, check new_username == confirm_username
    if True, update username in the UserLogin table

    """
    return 
def update_user_password(username, email, new_password, confirm_password):
    """
    Use username to get login_id
    Use login_id to get user_id
    Check if email provided matches email on file for that user_id
    If True, continue
    check if new_password == confirm_password
    If True, hash new_password
    IUpdate password hashing values in the UserLogin table

    """
    return
def delete_user(username, password, email, delete_form):
    """
    Use username to get login_id
    Use login_id to get user_id
    Check if email provided matches email on file for that user_id
    If True, continue
    Use login_id to get password hash and salt
    hash the password param and compare
    if True, continue
    Check that delete_form from user input == "delete", case sensitive
    If True, delete user from DB using user_id and login_id
    """
    return