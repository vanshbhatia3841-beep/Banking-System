# 🏦 Bank Management System

A command-line banking management system built in Python, backed by a MySQL database. Supports new account creation and existing user sign-in with basic balance, deposit, and withdrawal operations.

## Features

- 🆕 **New Account Creation** — Collects user details and auto-generates a username and account number
- 🔐 **Secure Sign-In** — Password-protected login for existing users
- 💰 **Balance Inquiry** — Check your current balance anytime
- 💵 **Deposit Funds** — Add money to your account
- 💸 **Withdraw Funds** — Withdraw money with insufficient-funds protection
- 🎨 **Colored CLI Output** — Clear, color-coded terminal feedback via `termcolor`
- 🔒 **Environment-based Config** — Database credentials managed securely via `.env`

## Project Structure

```
├── bank.py         # Entry point — welcome screen & routing
├── newacc.py       # New account creation logic
├── existing.py     # Existing user login, balance, deposit & withdrawal
├── db_config.py    # MySQL connection setup (env-based)
└── .env            # Database credentials (not committed)
```

## Requirements

- Python 3.10+
- MySQL Server
- Python packages:
  ```
  mysql-connector-python
  python-dotenv
  termcolor
  ```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vanshbhatia3841-beep/Banking-System.git
   cd Banking-System
   ```

2. **Install dependencies**
   ```bash
   pip install mysql-connector-python python-dotenv termcolor
   ```

3. **Configure the database**

   Create a `BANK` table in your MySQL database with the following columns:
   ```
   Name, Phone, Address, City, State, `email id`, Aadhar,
   `Account No.`, Username, PAN, Password, Balance
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database_name
   ```

5. **Run the application**
   ```bash
   python bank.py
   ```

## Usage

On launch, you'll be prompted to:

1. **Open Account** — Enter your details to register and receive a generated username and account number
2. **Sign In** — Log in with your username and password to access:
   - Show Balance
   - Deposit
   - Withdraw
   - Log Out

## 🚧 Coming Soon

- 🔢 **TPIN Support** — An additional transaction PIN layer for verifying deposits and withdrawals
- 🔁 **Account Transfer** — Transfer funds directly between two accounts within the system

## Disclaimer

This project is for educational purposes only and is not intended for use with real financial data. Passwords are currently stored as plain text — this is on the roadmap to be improved with proper hashing.

## License

MIT
