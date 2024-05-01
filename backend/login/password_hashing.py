import bcrypt


def password_hashing(password, salt=None):
    if salt is None:
        salt = bcrypt.gensalt()
    else:
        salt = salt.encode('utf-8')
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, salt)
    stored_password = hashed_password.decode('utf-8')
    stored_salt = salt.decode('utf-8')
    return stored_password, stored_salt