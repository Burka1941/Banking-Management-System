#W
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(users, username, password, full_name, initial_deposit):
    if username in users:
        return False, "User already exists"

    users[username] = {
        "username": username,
        "hashed_password": hash_password(password),
        "full_name": full_name,
        "balance": float(initial_deposit),
        "transactions": [],
        "status": "active"
    }
    return True, "Registration successful"


def login_user(users, uname, pwd):
    if uname in users:
        user_data = users[uname]

        stored_password = user_data.get('password')

        if stored_password and stored_password == hash_password(pwd):
            if user_data.get('is_locked', False):
                return "LOCKED"

            return user_data

    return None