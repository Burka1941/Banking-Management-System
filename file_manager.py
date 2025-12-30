import json
import os
import shutil
from datetime import datetime

def load_data(users_path, transactions_path):
    if not os.path.exists(users_path):
        return {}, []
    with open(users_path, 'r') as f:
        users = json.load(f)
    return users

def save_data(users_path, users):
    with open(users_path, 'w') as f:
        json.dump(users, f, indent=4)
    backup_data(users_path)

def backup_data(source_path):
    if not os.path.exists('backups'):
        os.makedirs('backups')
    time = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"backups/{time}_users.json"
    shutil.copy(source_path, backup_name)