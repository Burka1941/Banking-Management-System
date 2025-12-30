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

def login_user(users, username, password):
    if username in users and users[username]["hashed_password"] == hash_password(password):
        return users[username]
    return None