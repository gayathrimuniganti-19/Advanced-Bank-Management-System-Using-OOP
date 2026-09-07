#ADVANCED BANK MANAGEMENT SYSTEM USING OOP
#--->Member1
import random
from datetime import date,datetime
import os
from datetime import datetime
class Account:
    last_acc_no = 1000#class attribute to auto generate acc no
    def __init__(self,name,pin,initial_balance,account_type):
        Account.last_acc_no += 1
        self.acc_no = Account.last_acc_no
        self.name = name
        self.__pin= pin #private encapsulation
        self.__balance = initial_balance
        self.account_type = account_type
        self.creation_date = date.today()
    def get_balance(self,entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            return None
    def validate_pin(self,entered_pin):
        return entered_pin == self.__pin
    def _add_balance(self,amount):
        self.__balance += amount
    def show_details(self):
        print(f"Acc no : {self.acc_no} | Name: {self.name} | Type: {self.account_type} | Balance: {self.__balance}")
class SavingAccount(Account): #inheritance
    def __init__(self,name,pin,initial_balance):
        super().__init__(name,pin,initial_balance,"SAVING")
        self.interest_rate = 4.0
    def calculate_interest(self):
        return self._Account__balance * self.interest_rate / 100
class CurrentAccount(Account):
    def __init__(self,name,pin,initial_balance):
        super().__init__(name,pin,initial_balance,"CURRENT")
        self.overdraft_limit = 50000
    def calculate_intrest(self):
        return 0

#--->Member2   
class BankingOperations:
    #Deposit
    def deposit(self, account, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0")
            account._add_balance(amount)
            print(f"{amount} deposited successfully")
            print(f"Current Balance: {account.get_balance(account._Account__pin)}")
        except ValueError as e:
            print("Error:", e)
    #Withdraw
    def withdraw(self, account, pin, amount):
        try:
            if amount <= 0:
                raise valueError("Withdrawl amount must be greater than 0")
            balance = account.get_balance(pin)
            if balance is None:
                raise ValueError("Invalid Account Number")
            if amount > balance:
                raise ValueError("Insufficient balance")
            account._Account__balance -= amount
            print(f"{amount}withdraw successfully")
            print(f"Current Balance: {account.get_balance(pin)}")
        except ValueError as e:
                print("Error:", e)
    #Check Balance
    def check_balance(self, account, pin):
        try:
            balance = account.get_balance(pin)
            if balance is None:
                raise valueError("Invalid PIN")
            print(f"Account Number: {account.acc_no}")
            print(f"Account Holder: {account.name}")
            print(f"Current balance:{balance}")
        except ValueError as e:
            print("Error:", e)
    #Transfer Money
    def transfer_money(self, sender, receiver, sender_pin, amount):
        try:
            if amount <= 0:
                raise valueError("Transfer amount must be greater than 0")
            sender_balance = sender.get_balance(sender_pin)
            if sender_balance is None:
                raise ValueError("Invalid sender PIN")
            if amount > sender_balance:
                raise ValueError("Insufficient balance for transfer")
            sender._Account__balance -= amount
            receiver._add_balance(amount)
            print(f"{amount} transferred successfully")
            print(f"Sender Balance: {sender.get_balance(sender_pin)}")
        except ValueError as e:
                print("Error:", e)
    #Calculate Interest
    def calculate_interest(self, account):
        try:
            interest = account.calculate_interest()
            print(f"Interest: {interest}")
        except Exception as e:
            print("Error:", e)

#--->Member3
class TransactionManager:
    def __init__(self, folder="bank_records"):
        self.folder = folder
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        self.history = {} #account_no--> list of transaction strings(collections)
    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def _ensure(self, acc_no):
        if acc_no not in self.history:
            self.history[acc_no] = []
#--------Deposit History--------
    def record_deposit(self,account,amount):
        self._ensure(account.acc_no)
        balance = account.get_balance(account._Account__pin)
        self.history[account.acc_no].append(f"[{self._timestamp()}] DEPOSIT+{amount}(Balance:{balance})")
#--------Withdrawal History-------
    def record_withdrawal(self,account,amount):
        self._ensure(account.acc_no)
        balance = account.get_balance(account._Account__pin)
        self.history[account.acc_no].append(f"[{self._timestamp()}]WITHDRAW-{amount} (Balance:{balance})")
#----------Transfer History--------
    def record_transfer(self,sender,recevier,amount):
        self._ensure(sender.acc_no)
        self._ensure(recevier.acc_no)
        self.history[sender.acc_no].append(f"[{self._timestamp()}] TRANSFER -{amount} -> Acc {recevier.acc_no}")
        self.history[recevier.acc_no].append(f"[{self._timestamp()}] TRANSFER +{amount} <- Acc {sender.acc_no}")
#----------Intrest History---------
    def record_interest(self,account,interest):
        self._ensure(account.acc_no)
        self.history[account.acc_no].append(f"[{self._timestamp()}] INTEREST +{interest}")
#----------Save account information(File Handling)--------
    def save_account_info(self,account):
        filename = os.path.join(self.folder, f"account_{account.acc_no}.txt")
        balance = account.get_balance(account._Account__pin)
        with open(filename, "w") as f:
            f.write(f"Account Number : {account.acc_no}\n")
            f.write(f"Name           : {account.name}\n")
            f.write(f"Type           : {account.account_type}\n")
            f.write(f"Opened On      : {account.creation_date}\n")
            f.write(f"Balance        : {balance}\n")
            f.write("Transaction History:\n")
            for line in self.history.get(account.acc_no, []):
                f.write(line + "\n")
        print(f"Account info saved to {filename}")
        return filename
#--------Read account information-------
    def read_account_info(self,acc_no):
        filename = os.path.join(self.folder, f"account_{acc_no}.txt")
        if not os.path.exists(filename):
            print("No saved record found for this account")
            return None
        with open(filename, "r") as f:
            content = f.read()
            print(content)
            return content
#---------Generate mini statement-------
    def generate_mini_statement(self,acc_no,last_n=5):
        records = self.history.get(acc_no, [])
        recent = records[-last_n:]
        if not recent:
            print("No transactions yet.")
            return
        print(f"----Mini Statement (Account {acc_no}-----")
        for line in recent:
            print(line)
#function calling
acc1 = SavingAccount("Anjum",1703,10000)
acc2 = SavingAccount("Manasa",2908,20000)
acc3 = SavingAccount("Gayathri",1202,30000)
acc4 = SavingAccount("Asma",2806,15000)
acc5 = SavingAccount("Uzma",1604,25000)
acc6 = SavingAccount("Vaishnavi",1608,35000)
acc7 = SavingAccount("Ashu",2507,40000)
acc8 = SavingAccount("Srivan",2401,45000)
acc9 = CurrentAccount("Manvitha",1712,50000)
acc10 = CurrentAccount("Pandu",2110,55000)
acc11 = CurrentAccount("Hemalatha",1710,60000)
acc12 = CurrentAccount("Vikram",1812,65000)
acc13 = CurrentAccount("Asif",1312,70000)
acc14 = CurrentAccount("Zeba",3101,75000)
acc15 = CurrentAccount("Nandhu",2406,80000)

bank = BankingOperations()
transaction = TransactionManager()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Show Account Details")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. check Balance")
    print("6. calculate Interest")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        for i in range(1,16):
            account = globals()[f'acc{i}']
            account.show_details()

    elif choice == 2:
        account_no = int(input("Enter Account.no to deposit: "))
        amount = float(input("Enter deposit_amount: "))
        if 1 <= account_no <=15:
            account = globals()[f'acc{account_no}']
            bank.deposit(account,amount)
        else:
            print("Invalid account number")
        
    elif choice == 3:
        account_no = int(input("Enter account.no for withdrawal: "))
        pin = int(input("Enter PIN: "))
        amount = float(input("Enter withdrawal amount: "))
        if 1 <= account_no <= 15:
            account = globals()[f'acc{account_no}']
            bank.withdraw(account,pin,amount)
        else:
            print("Invalid account number")
    
    elif choice == 4:
        sender_no = int(input("Enter Sender Account.no: "))
        receiver_no = int(input("Enter Receiver Account.no: "))
        pin = int(input("Enter Sender PIN: "))
        amount = float(input("Enter amount: "))
        if 1 <= sender_no <= 15 and 1 <= receiver_no <= 15:
            sender_account = globals()[f"acc{sender_no}"]
            receiver_account = globals()[f"acc{receiver_no}"]
            bank.transfer_money(sender_account, receiver_account, pin, amount)
            transaction.record_transfer(sender_account, receiver_account, amount)
        else:
            print("Invalid account number")
    elif choice == 5:
        account_no = int(input("Enter Account.no to check balance: "))
        pin = int(input("Enter PIN: "))
        if 1 <= account_no <= 15:
            account = globals()[f"acc{account_no}"]
            bank.check_balance(account, pin)
        else:
            print("Invalid account number")
    elif choice == 6:
        account_no = int(input("Enter Account.no to calculate interest: "))
        if 1 <= account_no <= 15:
            account = globals()[f"acc{account_no}"]
            bank.calculate_interest(account)
        else:
            print("Invalid account number")
    elif choice == 7:
        print("Thank you for using Bank Management System ")
        break
    else:
        print("Invalid choice")









            
