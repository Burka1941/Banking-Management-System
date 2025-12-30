\# Yeditepe Banking Management System - Term Project

This is a terminal-based banking application for managing user accounts and transactions that I(Burka) developed for CSE 101.



\## How to Run(Setup)
1\. Open your terminal in the project folder.
Run the command: python main.py

2\. Register a new account or login with 'admin' credentials.



\## Features

Persistent storage using JSON.

Secure password hashing (SHA-256).

Automatic rolling backups in `backups/` folder.

Admin dashboard with total bank assets reporting.


#Project Structure
main.py: Main menu and program loop.

user.py: Registration and authentication logic.

bank_operations.py: Deposit, withdrawal, and transfer functions.

file_manager.py: Loading and saving data to JSON.

report.py: Analytics and transaction summaries.
