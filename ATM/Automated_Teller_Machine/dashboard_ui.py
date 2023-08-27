import tkinter as tk
from tkinter import messagebox, simpledialog
from atm_db import ATMDatabase

class DashboardUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("ATM Dashboard")
        self.db = ATMDatabase()

        self.login_label = tk.Label(root, text="Enter Account Number:")
        self.login_label.pack(pady=10)

        self.account_entry = tk.Entry(root)
        self.account_entry.pack()

        self.pin_label = tk.Label(root, text="Enter PIN:")
        self.pin_label.pack(pady=10)

        self.pin_entry = tk.Entry(root, show='*')
        self.pin_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=10)

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()

        if self.db.validate_login(account_number, pin):
            self.account_number = account_number
            self.account_entry.config(state=tk.DISABLED)
            self.pin_entry.config(state=tk.DISABLED)
            self.login_button.config(state=tk.DISABLED)
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Account Number or PIN")

    def show_dashboard(self):
        self.balance_label = tk.Label(self.root, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.change_pin_button = tk.Button(self.root, text="Change PIN", command=self.change_pin)
        self.change_pin_button.pack(pady=10)

        self.transaction_history_button = tk.Button(self.root, text="Transaction History", command=self.transaction_history)
        self.transaction_history_button.pack(pady=10)

        self.quit_button.pack(pady=10)

    def check_balance(self):
        balance = self.db.get_balance(self.account_number)
        self.balance_label.config(text=f"Balance: ${balance:.2f}")

    def deposit(self):
        amount = float(tk.simpledialog.askstring("Deposit", "Enter amount to deposit:"))
        if amount:
            self.db.update_balance(self.account_number, amount)
            self.db.add_transaction(self.account_number, "Deposit", amount)
            self.check_balance()

    def withdraw(self):
        amount = float(tk.simpledialog.askstring("Withdraw", "Enter amount to withdraw:"))
        if amount:
            balance = self.db.get_balance(self.account_number)
            if amount > balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.db.update_balance(self.account_number, -amount)
                self.db.add_transaction(self.account_number, "Withdraw", amount)
                self.check_balance()

    def change_pin(self):
        new_pin = tk.simpledialog.askstring("Change PIN", "Enter new PIN:")
        if new_pin:
            self.db.update_pin(self.account_number, new_pin)
            messagebox.showinfo("Success", "PIN changed successfully")

    def transaction_history(self):
        history = self.db.get_transaction_history(self.account_number)
        if history:
            history_text = "\n".join([f"{row[2]}: ${row[3]:.2f}" for row in history])
            messagebox.showinfo("Transaction History", history_text)
        else:
            messagebox.showinfo("Transaction History", "No transaction history")

# ... (rest of the code)