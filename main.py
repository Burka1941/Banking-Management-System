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

                current_user = user_mod.login_user(users, uname, pwd)
                if not current_user: print("Invalid credentials!")

            elif choice == "3":
                break

        else:
            print(f"\n--- Welcome, {current_user['full_name']} ---")
            print("1. Deposit\n2. Withdraw\n3. View History\n4. Logout")
            u_choice = input("Choice: ")

            if u_choice == "1":
                amt = input("Amount: ")
                bank.deposit_money(current_user, amt)
                fm.save_data(USERS_FILE, users)
            elif u_choice == "2":
                amt = input("Amount: ")
                res, msg = bank.withdraw_money(current_user, amt)
                print(msg)
                fm.save_data(USERS_FILE, users)
            elif u_choice == "3":
                history = report.view_transaction_history(current_user)
                for t in history: print(t)
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