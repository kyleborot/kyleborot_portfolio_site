from flask import Flask, render_template
from config.config import conn

user_id = 1

def login_user():
    
    return

def register_user(user_id, username, password, email):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO LoginSchema.Users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)", (user_id, username, password, email))
    conn.commit()
    cursor.close()
    return "User registered successfully, next user_id is {user_id}"
def update_user_password():

    return
def delete_user():

    return
