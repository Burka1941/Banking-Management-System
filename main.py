#W4
import user as user_mod
import bank_operations as bank
import file_manager as fm
import report

USERS_FILE = "data/users.json"

def main():
    users = fm.load_data(USERS_FILE, "")
    current_user = None
    while True:
        if not current_user:
            print("\n--- WELCOME TO YU-BANK ---")
            print("1. Register\n2. Login\n3. Exit")
            choice = input("Choice: ")

            if choice == "1":
                uname = input("Username: ")
                pwd = input("Password: ")
                name = input("Full Name: ")
                dep = input("Initial Deposit: ")
                success, msg = user_mod.register_user(users, uname, pwd, name, dep)
                print(msg)
                fm.save_data(USERS_FILE, users)

            elif choice == "2":
                uname = input("Username: ")
                pwd = input("Password: ")
                if uname == "admin" and pwd == "admin123":
                    admin_dashboard(users)
                    continue

                res = user_mod.login_user(users, uname, pwd)
                if res == "LOCKED":
                    print("!!! Account is LOCKED. Contact admin. !!!")
                elif res:
                    current_user = res
                    print(f"Login Successful! Welcome {current_user['full_name']}")
                    current_user['failed_attempts'] = 0
                    fm.save_data(USERS_FILE, users)
                else:
                    print("Invalid credentials!")
                    if uname in users:
                        users[uname]['failed_attempts'] = users[uname].get('failed_attempts', 0) + 1
                        if users[uname]['failed_attempts'] >= 3:
                            users[uname]['status'] = 'locked'
                            print("Too many attempts. Account LOCKED!")
                        fm.save_data(USERS_FILE, users)

            elif choice == "3":  # Bu satır 'elif choice == "2"' ile aynı hizada olmalı
                break

        else:
            print(f"\n--- Welcome, {current_user['full_name']} ---")
            print(f"Current Balance: ${current_user['balance']:.2f}")
            print("1. Deposit\n2. Withdraw\n3. View History\n4. Logout")
            u_choice = input("Choice: ")

            if u_choice == "1":
                amt = float(input("Amount to Deposit: "))
                bank.deposit_money(current_user, amt)
                fm.save_data(USERS_FILE, users)
                print(f"Success! New Balance: ${current_user['balance']:.2f}")

            elif u_choice == "2":
                amt = float(input("Amount to Withdraw: "))
                res, msg = bank.withdraw_money(current_user, amt)
                if res:
                    fm.save_data(USERS_FILE, users)
                    print(f"Success! Remaining Balance: ${current_user['balance']:.2f}")
                else:
                    print(f"Error: {msg}")

            elif u_choice == "3":
                history = report.view_transaction_history(current_user)
                print("\n--- Transaction History ---")
                for t in history:
                    print(t)

            elif u_choice == "4":
                current_user = None
def admin_dashboard(users):
    stats = report.generate_summary_report(users)
    print("\n--- ADMIN DASHBOARD ---")
    print(f"Total Users: {stats['total_users']}")
    print(f"Total Bank Balance: {stats['total_assets']}$")
    input("\nPress Enter to return...")


if __name__ == "__main__":
    main()