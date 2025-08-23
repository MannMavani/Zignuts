from getpass import getpass
from mysql.connector import connect, Error

try:
    conn = connect(
        host="localhost",
        user="root",
        password="blackpanther@1105",
        database="Bank_Management_Sytem",
    )
    cursor = conn.cursor()
    print("Connected to database.")
except Error as e:
    print(e)
    raise SystemExit(1)


class BankAccount:

    def __init__(self, account_id=None, name=None):
        self.account_id = account_id
        self.name = name
        self.balance = 0.0
        if account_id:
            self.load_account()

    def create_account(self, name, balance=0.0):
        cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, balance))
        conn.commit()
        print(f"✅ Account created for {name} with balance {balance}")

    def load_account(self):
        cursor.execute("SELECT name, balance FROM accounts WHERE account_id=%s", (self.account_id,))
        row = cursor.fetchone()
        if row:
            self.name, self.balance = row
        else:
            print("❌ Account not found")

    def deposit(self, amount):
        self.balance = float(self.balance)+float(amount) 
        cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (self.balance, self.account_id))
        conn.commit()
        print(f"✅ Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds")
        else:
            self.balance = float(self.balance)-float(amount) 
            cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (self.balance, self.account_id))
            conn.commit()
            print(f"✅ Withdrawn {amount}. Balance: {self.balance}")

    def check_balance(self):
        self.load_account()
        print(f"💰 Balance for {self.name}: {self.balance}")

    def delete_account(self):
        cursor.execute("DELETE FROM accounts WHERE account_id=%s", (self.account_id,))
        conn.commit()
        print("🗑️ Account deleted.")


while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Delete Account\n6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        bal = float(input("Enter initial balance: "))
        BankAccount().create_account(name, bal)

    elif choice in ["2", "3", "4", "5"]:

        name = input("Enter Account Holder Name: ")

        cursor.execute("SELECT account_id, name, balance FROM accounts WHERE name=%s", (name,))
        results = cursor.fetchall()

        if not results:
            print("❌ No account found with this name.")
            continue
        elif len(results) == 1:
            acc_id = results[0][0]   # unique account_id
        else:
            print("⚠️ Multiple accounts found with this name:")
            for acc_row in results:
                print(f"ID: {acc_row[0]} | Name: {acc_row[1]} | Balance: {acc_row[2]}")
            acc_id = int(input("Enter Account ID from above list: "))

    acc = BankAccount(account_id=acc_id)

    if choice == "2":
        amt = float(input("Enter deposit amount: "))
        acc.deposit(amt)
    elif choice == "3":
        amt = float(input("Enter withdrawal amount: "))
        acc.withdraw(amt)
    elif choice == "4":
        acc.check_balance()
    elif choice == "5":
        acc.delete_account()


    elif choice == "6":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice.")