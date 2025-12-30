import unittest
import user as user_mod
import bank_operations as bank


class TestBank(unittest.TestCase):
    def test_operations(self):
        u = {"username": "t", "balance": 500.0, "transactions": []}

        # 1 Deposit Test
        bank.deposit_money(u, 200.0)
        self.assertEqual(u['balance'], 700.0)

        # 2 Withdraw Test
        res, msg = bank.withdraw_money(u, 100.0)
        self.assertTrue(res)
        self.assertEqual(u['balance'], 600.0)

        # 3 Error Management Test, Negative numbers
        res, msg = bank.withdraw_money(u, 1000.0)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()