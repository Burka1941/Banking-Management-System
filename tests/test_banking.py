import bank_operations as bank

def test_system():
    # 1. Test: Successful Deposit
    user = {"balance": 100, "transactions": []}
    bank.deposit_money(user, 50)
    assert user["balance"] == 150

    # 2. Test: Overdraft Prevention
    res = bank.withdraw_money(user, 200)
    assert user["balance"] == 150

    # 3. Test: Negative Amount Check
    res_neg = bank.deposit_money(user, -10)
    assert res_neg is False or user["balance"] == 150
    print("All 3 tests passed successfully!")

if __name__ == "__main__":
    test_system()