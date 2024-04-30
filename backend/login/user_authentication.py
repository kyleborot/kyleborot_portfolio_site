from flask import Flask, render_template
from config.config import conn
from .password_hashing import password_hashing

user_id = 1
login_id = 1

def login_user():
    
    return

def register_user(user_id, username, first_name, last_name, password, email):
    cursor=conn.cursor()
    hashed_password, password_salt = password_hashing(password)
    cursor.execute("INSERT INTO LoginSchema.Users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)", (user_id, first_name, last_name, email))
    cursor.execute("INSERT INTO LoginSchema.UserLogin (login_id, user_id, login_name, hashed_password, password_salt) VALUES (?, ?, ?, ?, ?)", (login_id, user_id, username, hashed_password, password_salt))
    conn.commit()
    cursor.close()
    return "User registered successfully, next user_id is {user_id}"
def update_user_password():

    return
def delete_user():

    return
