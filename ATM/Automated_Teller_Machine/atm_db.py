import sqlite3
from tkinter import messagebox

class ATMDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('atm_db.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                pin TEXT,
                balance REAL
            )
        ''')

        self.cursor.execute('''
            INSERT OR IGNORE INTO accounts (account_number, pin, balance)
            VALUES ('12345', '1234', 1000.00)
        ''')

        self.connection.commit()

    def validate_login(self, account_number, pin):
        self.cursor.execute('SELECT * FROM accounts WHERE account_number = ? AND pin = ?', (account_number, pin))
        return self.cursor.fetchone() is not None

    def get_balance(self, account_number):
        self.cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
        return self.cursor.fetchone()[0]

    def update_balance(self, account_number, amount):
        self.cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_number = ?', (amount, account_number))
        self.connection.commit()

    def update_pin(self, account_number, new_pin):
        self.cursor.execute('UPDATE accounts SET pin = ? WHERE account_number = ?', (new_pin, account_number))
        self.connection.commit()

    def add_transaction(self, account_number, transaction_type, amount):
        self.cursor.execute('INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)',
                            (account_number, transaction_type, amount))
        self.connection.commit()

    def get_transaction_history(self, account_number):
        self.cursor.execute('SELECT * FROM transactions WHERE account_number = ?', (account_number,))
        return self.cursor.fetchall()


class ATMTransaction:
    def __init__(self):
        self.connection = sqlite3.connect('atm_db.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                account_number TEXT,
                transaction_type TEXT,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        self.connection.commit()

    def make_deposit(self, account_number, amount):
        try:
            self.cursor.execute('INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)',
                                (account_number, 'Deposit', amount))
            self.connection.commit()
            return True
        except Exception as e:
            messagebox._show('Transaction Error', f'Error during deposit: {str(e)}')
            return False

    def make_withdrawal(self, account_number, amount):
        try:
            self.cursor.execute('INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)',
                                (account_number, 'Withdrawal', amount))
            self.connection.commit()
            return True
        except Exception as e:
            messagebox._show('Transaction Error', f'Error during withdrawal: {str(e)}')
            return False
