#W3
from datetime import datetime

def deposit_money(user, amount, channel="ATM"):
    amount = float(amount)
    user["balance"] += amount
    transaction = {
        "type": "deposit",
        "amount": amount,
        "balance_after": user["balance"],
        "timestamp": datetime.now().isoformat(),
        "channel": channel
    }
    user["transactions"].append(transaction)
    return user

def withdraw_money(user, amount, channel="ATM"):
    amount = float(amount)
    if amount > user["balance"]:
        return None, "Insufficient funds"

    user["balance"] -= amount
    transaction = {
        "type": "withdrawal",
        "amount": amount,
        "balance_after": user["balance"],
        "timestamp": datetime.now().isoformat(),
        "channel": channel
    }
    user["transactions"].append(transaction)
    return user, "Success"