import tkinter as tk
from tkinter import messagebox
from atm_db import ATMDatabase
from dashboard_ui import DashboardUI

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("400x300")

        self.db = ATMDatabase()

        self.label = tk.Label(root, text="ATM Simulator", font=("Arial", 18))
        self.label.pack(pady=10)

        self.account_label = tk.Label(root, text="Account Number:")
        self.account_label.pack()
        self.account_entry = tk.Entry(root)
        self.account_entry.pack()

        self.pin_label = tk.Label(root, text="PIN:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(root, show="*")
        self.pin_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()

        if not account_number or not pin:
            messagebox.showerror("Error", "Please enter account number and PIN")
            return

        if self.db.validate_login(account_number, pin):
            self.open_dashboard(account_number)
        else:
            messagebox.showerror("Error", "Invalid account number or PIN")

    def open_dashboard(self, account_number):
        self.root.destroy()
        dashboard = tk.Tk()
        dashboard.title("ATM Dashboard")

        DashboardUI(dashboard, account_number)
        dashboard.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardUI(root)
    root.mainloop()