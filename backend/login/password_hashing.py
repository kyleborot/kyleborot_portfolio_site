import bcrypt


def password_hashing(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    stored_password = hashed_password.decode('utf-8')
    stored_salt = salt.decode('utf-8')
    return stored_password, stored_salt