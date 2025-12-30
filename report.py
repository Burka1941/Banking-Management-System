#W4
import csv
from datetime import datetime

def view_transaction_history(user, limit=10):
    history = user.get("transactions", [])
    return history[-limit:]

def generate_summary_report(users):
    total_balance = sum(u['balance'] for u in users.values())
    user_count = len(users)
    return {
        "total_assets": total_balance,
        "total_users": user_count,
        "avg_balance": total_balance / user_count if user_count > 0 else 0
    }