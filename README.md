# 🏦 Bank Management System (Python CLI)

## 📌 Overview

This is a simple **Bank Management System** built using Python. It runs in the command line and allows users to perform basic banking operations such as creating accounts, depositing money, withdrawing money, and viewing account details.

The project is designed to demonstrate **Object-Oriented Programming (OOP)** concepts and basic real-world logic.

---

## 🚀 Features

* 📄 View all accounts and balances
* ➕ Create a new account
* 💰 Deposit money into an account
* 💸 Withdraw money from an account
* 🔁 Continuous menu-driven interface

---

## 🧠 Concepts Used

* Classes and Objects
* Dictionaries for data storage
* Conditional statements
* Loops (while loop for menu system)
* Basic input/output handling

---

## 🗂️ Project Structure

```
script2.py   # Main Python file containing the banking system
```

---

## ⚙️ How It Works

1. The program starts with a menu:

   ```
   1. View all accounts
   2. Create account
   3. Deposit money
   4. Withdraw money
   5. Exit
   ```

2. Users select an option by entering a number.

3. Based on the choice:

   * Accounts can be created
   * Money can be deposited or withdrawn
   * All account details can be displayed

4. Data is stored in a dictionary:

   ```python
   self.account = {}
   ```

---

## ▶️ How to Run

### Prerequisites

* Python 3.x installed

### Steps

1. Clone the repository:

   ```
   git clone https://github.com/your-username/bank-management-system.git
   ```

2. Navigate to the project folder:

   ```
   cd bank-management-system
   ```

3. Run the script:

   ```
   python script2.py
   ```

---

## ⚠️ Limitations

* No data persistence (data is lost when program exits)
* No validation for negative balance withdrawals
* No authentication system
* CLI-based (no GUI)

---

## 💡 Future Improvements

* Add file/database storage (SQLite or JSON)
* Implement user authentication (PIN/password)
* Add transaction history
* Build a GUI using Tkinter or a web interface
* Add validation for insufficient balance

---

👨‍💻 Author

Jay Vikram

---

📄 License

This project is open-source and available under the MIT License.
