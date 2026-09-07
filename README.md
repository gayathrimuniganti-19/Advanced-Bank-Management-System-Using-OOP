# Advanced Bank Management System using OOP

A Python-based banking application built to demonstrate the major object-oriented programming concepts commonly discussed in Python interviews — implemented through a realistic, end-to-end banking system.

---

## 📌 Problem Statement

Develop a banking application specifically designed to demonstrate the major object-oriented programming concepts that are commonly discussed in Python interviews.

---

## 🚀 Features / Modules

- Customer Class
- Account Base Class
- Savings Account
- Current Account
- Deposit
- Withdrawal
- Fund Transfer
- Interest Calculation
- Account Statement
- Custom Banking Exceptions

---

## 🧠 Concepts Used from the Course

- Classes and Objects
- Constructors
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
- Method Overriding
- Custom Exceptions
- Basic Modules
- TXT File Handling

---

## 🎯 Expected Outcome

Students gain a strong interview-level understanding of Python OOP by implementing the major OOP concepts in a single, easy-to-explain project.

---

## 👥 Team & Module Division

| Member | Module | Core OOP Concepts Applied |
|---|---|---|
| Anjum (Member 1) | Account Management | Classes, Objects, Encapsulation, Inheritance |
| Manasa (Member 2) | Banking Operations | Methods, Polymorphism, Exception Handling |
| **Gayathri (Member 3)** | **Transaction & Database** | **File Handling, Collections, Integration** |

---

## 🔧 Module Breakdown

### 1. Account Management (Anjum)
- Create account
- Store customer details
- Savings account
- Current account
- Check account details
- PIN / Password

### 2. Banking Operations (Manasa)
- Deposit
- Withdraw
- Check balance
- Transfer money
- Calculate interest
- Validate transaction
- Handle insufficient balance

### 3. Transaction & Database (Gayathri) — *My Contribution*
- Transaction history
- Deposit history
- Withdrawal history
- Transfer history
- Save account information
- Read account information
- Generate mini statement

---

## 🛠️ My Contribution (Gayathri — Transaction & Database)

I was responsible for the **Transaction & Database module**, which forms the persistence and reporting backbone of the application. This involved:

- **Transaction Logging** — Recording every deposit, withdrawal, and transfer as a timestamped transaction entry.
- **History Tracking** — Maintaining separate, queryable histories for deposits, withdrawals, and transfers per account.
- **Data Persistence** — Reading and writing account information to `.txt` files so account data survives between program runs.
- **Mini Statement Generation** — Compiling recent transaction history into a readable account statement on demand.
- **Module Integration** — Connecting the Account Management and Banking Operations modules to a shared data layer so all three components work together as a single cohesive application.

**Concepts applied:** File Handling, Collections (lists/dicts for history tracking), and Integration of multi-member modules into one system.

---

## 🗂️ Tech Stack

- **Language:** Python
- **Storage:** TXT File Handling (file-based persistence)
- **Paradigm:** Object-Oriented Programming (OOP)

---

## ▶️ How to Run

```bash
git clone <repo-url>
cd advanced-bank-management-system
python main.py
