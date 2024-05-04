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
    cursor.execute("SELECT user_id FROM LoginSchema.Users WHERE email = ?", (email))
    user_id = cursor.fetchone()
    if user_id:
        cursor.execute("SELECT hashed_password, password_salt, login_id FROM LoginSchema.UserLogin WHERE login_id = ?", (user_id))
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            stored_salt = result[1]
            entered_password_hashed, _ = password_hashing(password, stored_salt)
            if stored_password == entered_password_hashed and user_id[0] == result[2]:
                if new_username == confirm_username:
                    cursor.execute("UPDATE LoginSchema.UserLogin SET login_name = ? WHERE user_id = ?", (new_username, user_id[0]))
                    conn.commit()
                    cursor.close()
                    return "User updated successfully"
            else:
                return "Either your username confirmation did not match, or the password you have entered is incorrect."
    return "There has been a problem, please try again later."
def update_user_password(username, email, new_password, confirm_password):
    cursor = conn.cursor()
    cursor.execute("SELECT login_id, user_id FROM LoginSchema.UserLogin WHERE login_name = ?",(username,))
    id = cursor.fetchone()
    cursor.execute("SELECT email FROM LoginSchema.Users WHERE user_id = ?", (id[0],))
    validate_email = cursor.fetchone()
    if email == validate_email[0] and new_password == confirm_password:
        password, salt = password_hashing(new_password)
        cursor.execute("UPDATE LoginSchema.UserLogin SET hashed_password = ?, password_salt = ? WHERE login_id = ?", (password, salt, id[0]))
        conn.commit()
        cursor.close()
        return "Password successfully reset"
    return "There has been a problem, please try again later"
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
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, email FROM LoginSchema.UserLogin WHERE login_name = ?", (username,))
    result_1 = cursor.fetchone()
    if result_1 and result_1[1] == email:
        cursor.execute("SELECT hashed_password, password_salt, login_id FROM LoginSchema.UserLogin WHERE login_id = ?", (user_id))
        pw_result = cursor.fetchone()
        if pw_result:
            stored_password = pw_result[0]
            stored_salt = pw_result[1]
            entered_password_hashed, _ = password_hashing(password, stored_salt)
            if stored_password == entered_password_hashed and result_1[0] == pw_result[2] and delete_form == "delete":
                cursor.execute("DELETE FROM LoginSchema.UserLogin WHERE user_id = ?", (result_1[0],))
                cursor.execute("DELETE FROM LoginSchema.Users WHERE user_id = ?", (result_1[0],))
                conn.commit()
                cursor.close()
                return "user successfully deleted"
    return "user could not be deleted"