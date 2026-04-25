# 🏦 Bank Management System

A Python-based command-line banking application that allows users to open a new bank account or sign in to an existing one — with features like balance check, deposit, and withdrawal — powered by a MySQL database.

---

## 📋 Features

- 🆕 **Open a new account** — collects personal details (name, phone, address, Aadhar, PAN, etc.) and auto-generates a username and account number
- 🔐 **Secure login** — existing users can sign in with their username and password
- 💰 **Check Balance** — view current account balance
- ➕ **Deposit** — add funds to your account
- ➖ **Withdraw** — withdraw funds with insufficient balance protection
- 🎨 Colored terminal output using `termcolor`

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`, `termcolor`

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sbi-bank-management.git
cd sbi-bank-management
```

### 2. Install dependencies

```bash
pip install mysql-connector-python termcolor python-dotenv
```

### 3. Configure the database connection

Create a `.env` file in the project folder:

```
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
```

### 4. Set up the MySQL database

Make sure your MySQL database has a table named `bank` with the following columns:

| Column | Type |
|---|---|
| id | INT AUTO_INCREMENT PRIMARY KEY |
| Name | VARCHAR |
| Phone | LONG |
| Address | VARCHAR |
| City | VARCHAR |
| State | VARCHAR |
| email id | VARCHAR |
| Aadhar | LONG |
| Account No. | BIGINT |
| Username | VARCHAR |
| PAN | VARCHAR |
| Password | BLOB |
| Balance | FLOAT |

---

## 🚀 Usage

Run the script from your terminal:

```bash
python bank.py
```

You will be greeted and prompted to choose an operation:

```
Hi! Welcome to ____ bank.
What do you like to do?
      1) Open Account
      2) Existing user? Sign in
```

### Opening an Account
Enter your personal details. A unique username is auto-generated from your name, phone, and PAN number.

### Signing In
Enter your username and password to access your account dashboard:

```
1. Show Balance        2. Deposit
3. Withdraw            4. Exit
```

---

## 📸 Sample Output

```
Hi! Welcome to SBI bank.
What do you like to do?
      1) Open Account
      2) Existing user? Sign in
2
Enter your username: Johns989AB12
Enter your password: ********
Login Successful!

1. Show Balance          2. Deposit
3. Withdraw              4. Exit

Enter your choice(1-4): 1
5000.0
```

---


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Vansh** — [GitHub Profile](https://github.com/vanshbhatia3841-beep)
