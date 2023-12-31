import sqlite3
from tkinter import *
from tkinter import messagebox

f1 = ('Comic Sans MS', 30, "bold")
f2 = ('Comic Sans MS', 18, "bold")
f3 = ('Comic Sans MS', 20, "bold")
f4 = ('Comic Sans MS', 10, "bold")
f5 = ('Comic Sans MS', 8, "bold")


class Atm:
    def __init__(self, root):
        self.con = sqlite3.connect('atm_db.db')
        self.login = False
        self.root = root
        self.ac = None  # Added to store current account number
        self.top_label = Label(self.root, text="Shriyansh Bank", font=f1)
        self.top_label.pack()
        self.frame = Frame(self.root, width=600, height=600, bg="Light Blue")
        self.frame.pack()
        self.account_label = Label(self.frame, text="Account Number", font=f2)
        self.pin_label = Label(self.frame, text="Pin", font=f2)
        self.account_entry = Entry(self.frame)
        self.pin_entry = Entry(self.frame, show='*')
        self.login_btn = Button(self.frame, text="Login", font=f3, command=self.validate, activeforeground='blue',
                                activebackground='white')
        self.quit_btn = Button(self.frame, text="Quit", font=f3, command=self.root.destroy, activeforeground='blue',
                               activebackground='white')
        self.account_label.place(x=45, y=100, width=220, height=30)
        self.account_entry.place(x=325, y=97, width=200, height=25)
        self.pin_label.place(x=45, y=180, width=220, height=30)
        self.pin_entry.place(x=325, y=180, width=200, height=25)
        self.login_btn.place(x=240, y=260, width=100, height=40)
        self.quit_btn.place(x=400, y=260, width=100, height=40)

    def fetch(self):
        self.list = []
        self.details = self.con.execute("""SELECT * FROM atm_table WHERE account_no = ?""", (self.ac,))
        for i in self.details:
            self.list.append(f'Name: {i[0]}')
            self.list.append(f'Account No: {i[2]}')
            self.ac = i[2]
            self.list.append(f'Type: {i[3]}')
            self.list.append(f'Balance: {i[4]}')

    def validate(self):
        ac = False
        self.details = self.con.execute('''SELECT * FROM atm_table WHERE account_no = ?''', (self.account_entry.get(),))
        for i in self.details:
            self.ac = i[2]
            if self.ac == self.account_entry.get():
                ac = True

            elif i[1] == self.pin_entry.get():
                ac = True
                self.fetch()
                messagebox._show('Login Info', f'{i[0]}, Welcome to the bank!')
                self.frame.destroy()
                self.menu()
            else:
                messagebox._show('Login info', "Wrong Password")
        if not ac:
            messagebox._show('Login Info', 'Wrong account number')

    def menu(self):
        self.frame = Frame(self.root, width=600, height=500)
        self.user_info = Button(self.frame, text="Account Info", command=self.account_details)
        self.balance_inquiry = Button(self.frame, text="Check Balance", command=self.check_balance)
        self.deposit = Button(self.frame, text="Deposit", command=self.deposit)
        self.withdraw = Button(self.frame, text="Withdraw", command=self.withdraw)
        self.last_transaction = Button(self.frame, text="Last Transaction", command=self.history)
        self.change_pin = Button(self.frame, text="Change Pin", command=self.change_pin)
        self.transaction_history = Button(self.frame, text="Transaction History", command=self.transaction_history)
        self.quit = Button(self.frame, text="Quit", command=self.root.destroy)
        self.user_info.place(x=0, y=0, width=200, height=50)
        self.balance_inquiry.place(x=0, y=450, width=200, height=50)
        self.deposit.place(x=450, y=0, width=200, height=50)
        self.withdraw.place(x=450, y=450, width=200, height=50)
        self.last_transaction.place(x=0, y=240, width=200, height=50)
        self.change_pin.place(x=530, y=240, width=200, height=50)
        self.transaction_history.place(x=270, y=400, width=200, height=50)
        self.quit.place(x=270, y=470, width=200, height=50)

    def account_details(self):
        self.fetch()
        display = "\n".join(self.list)
        self.label = Label(self.frame, text=display, font=f5)
        self.label.place(x=180, y=180, width=300, height=100)

    def check_balance(self):
        self.fetch()
        balance_text = f'Balance: {self.list[3]}'
        self.label = Label(self.frame, text=balance_text, font=f5)
        self.label.place(x=180, y=180, width=300, height=100)

    def deposit(self):
        self.label_deposit = Label(self.frame, text="How much would you like to deposit?", font=f3)
        self.entry_deposit = Entry(self.frame)
        self.button_deposit = Button(self.frame, text="Deposit", command=self.deposit_transaction, font=f3)
        self.label_deposit.place(x=180, y=180, width=300, height=50)
        self.entry_deposit.place(x=230, y=250, width=160, height=20)
        self.button_deposit.place(x=400, y=250, width=100, height=20)

    def deposit_transaction(self):
        if not self.entry_deposit.get().isdigit():
            messagebox._show('Transaction Error', 'Enter a valid amount!')
        else:
            self.label_deposit = Label(self.frame, text="Transaction successful", font=f4)
            self.label_deposit.place(x=180, y=180, width=300, height=50)
            self.con.execute("""UPDATE atm_table SET balance = balance + ? WHERE account_no = ?""",
                             (int(self.entry_deposit.get()), self.ac))
            self.con.commit()
            self.write_deposit()

    def write_deposit(self):
        deposit_text = f"An amount of {self.entry_deposit.get()} is deposited in {self.list[1]}"
        with open('last.txt', 'w') as f:
            f.write(deposit_text)

    def withdraw(self):
        self.label_withdraw = Label(self.frame, text="How much would you like to withdraw?", font=f3)
        self.entry_withdraw = Entry(self.frame)
        self.button_withdraw = Button(self.frame, text="Withdraw", command=self.withdraw_transaction, font=f3)
        self.label_withdraw.place(x=180, y=180, width=300, height=50)
        self.entry_withdraw.place(x=230, y=250, width=160, height=20)
        self.button_withdraw.place(x=400, y=250, width=100, height=20)

    def withdraw_transaction(self):
        if not self.entry_withdraw.get().isdigit():
            messagebox._show('Transaction Error', 'Enter a valid amount!')
        else:
            self.label_withdraw = Label(self.frame, text="Transaction successful", font=f4)
            self.label_withdraw.place(x=180, y=180, width=300, height=50)
            self.con.execute("""UPDATE atm_table SET balance = balance - ? WHERE account_no = ?""",
                             (int(self.entry_withdraw.get()), self.ac))
            self.con.commit()
            self.last_withdraw()

    def last_withdraw(self):
        withdraw_text = f"An amount of {self.entry_withdraw.get()} is withdrawn from {self.list[1]}"
        with open('last.txt', 'w') as f:
            f.write(withdraw_text)

    def change_pin(self):
        self.label_change = Label(self.frame, text="Change Pin", font=f3)
        self.old_entry = Entry(self.frame)
        self.new_entry = Entry(self.frame)
        self.confirm_entry = Entry(self.frame)
        self.button_change = Button(self.frame, text="Change Pin", command=self.change_request, font=f3)

        self.old_entry.insert(0, 'Old password')
        self.new_entry.insert(0, 'New password')
        self.confirm_entry.insert(0, 'Confirm password')

        self.label_change.place(x=180, y=180, width=300, height=50)
        self.old_entry.place(x=230, y=250, width=160, height=20)
        self.new_entry.place(x=230, y=280, width=160, height=20)
        self.confirm_entry.place(x=230, y=310, width=160, height=20)
        self.button_change.place(x=230, y=340, width=160, height=20)

    def change_request(self):
        old_password = self.old_entry.get()
        new_password = self.new_entry.get()
        confirm_password = self.confirm_entry.get()

        if old_password == 'Old password' or new_password == 'New password' or confirm_password == 'Confirm password':
            messagebox._show('Failed', 'Kindly fill details correctly')
        else:
            self.fetch()
            self.details = self.con.execute("""SELECT * FROM atm_table WHERE account_no = ?""", (self.ac,))
            for i in self.details:
                password = i[1]
                if old_password == password:
                    if new_password == confirm_password:
                        self.label = Label(self.frame, text="Pin Updated", font=f4)
                        self.label.place(x=180, y=180, width=300, height=50)
                        self.con.execute("""UPDATE atm_table SET password = ? WHERE account_no = ?""",
                                         (confirm_password, self.ac))
                        self.con.commit()
                        self.remove_change_pin()
                        messagebox._show('Restart', 'Login Again')
                        root.destroy()
                    else:
                        self.label = Label(self.frame, text="New Password and Confirm Password do not match", font=f4)
                        self.label.place(x=180, y=180, width=300, height=50)
                else:
                    self.label = Label(self.frame, text="Old password do not match", font=f4)
                    self.label.place(x=180, y=180, width=300, height=50)

    def history(self):
        with open('last.txt', 'r') as f:
            transaction_history = f.read()
        self.history_label = Label(self.frame, text=transaction_history, font=f5)
        self.history_label.place(x=180, y=180, width=300, height=100)

    def transaction_history(self):
        self.details = self.con.execute("""SELECT * FROM atm_table WHERE account_no = ?""", (self.ac,))
        for i in self.details:
            transaction_history = f"Account Number: {i[2]}\nLast Transaction: {i[6]}\nBalance: {i[4]}"
        self.history_label = Label(self.frame, text=transaction_history, font=f5)
        self.history_label.place(x=180, y=180, width=300, height=100)

    def entries(self):
        pass

    def remove_change_pin(self):
        try:
            self.old_entry.place_forget()
            self.new_entry.place_forget()
            self.confirm_entry.place_forget()
            self.button_change.place_forget()
        except:
            pass


root = Tk()
root.title("ATM")
root.geometry("800x800")
root.configure(bg="Light Blue")

connection = sqlite3.connect('atm_db.db')

cursor = connection.cursor()
# sql_command = """CREATE TABLE IF NOT EXISTS atm_table (
# name text,
# password text,
# account_no INTEGER PRIMARY KEY,
# type text,
# balance INTEGER);"""
# cursor.execute(sql_command)
# sql_command = """INSERT INTO atm_table VALUES ('Shriyansh', '123', '12345', 'savings', '9999999999999')"""
# cursor.execute(sql_command)
connection.commit()
connection.close()
a1 = Atm(root)

root.mainloop()
