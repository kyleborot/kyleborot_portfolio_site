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

"""
cursor.execute("SELECT x FROM Schema.Table1")
cursor.execute("SELECT y FROM Schema.Table2")
results = cursor.fetchall()
x, y = results
"""