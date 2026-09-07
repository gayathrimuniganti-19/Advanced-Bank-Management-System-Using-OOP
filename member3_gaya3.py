import os
from datetime import datetime

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
        self.history[account_no].append(f"[{self._timestamp()}] DEPOSIT+{amount}(Balance:{balance})")
#--------Withdrawal History-------
    def record_withdrawal(self,acccount,amount):
        self._ensure(account.acc_no)
        balance = account.get_balance(account._Account__pin)
        self.history[account.acc_no].append(f"[{self._timestamp()}]WITHDRAW-{amount} (Balance:{balance})")
#----------Transfer History--------
    def record_transfer(self,sender,recevier,amount):
        self._ensure(sender.acc_no)
        self._ensure(receiver.acc_no)
        self.history[sender.acc_no].append(f"[{self._timestamp}] TRANSFER -{amount} -> Acc {receiver.acc_no}")
        self.history[receiver.acc_no].append(f"[{self._timestamp}] TRANSFER +{amount} <- Acc {sender.acc_no}")
#----------Intrest History---------
    def record_interest(self,account,interest):
        self._ensure(account.acc_no)
        self.history[account.acc_no].append(f"[{self._timestamp()}] INTEREST +{interest}")
#----------Save account information(File Handling)--------
    def save_account_info(self,account):
        filename = os.path.join(self.folder, f"account_{account.acc_not}.txt")
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
            return cotent
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

                     

        
        
