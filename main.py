import sqlite3
from tkinter import *

# Create the database and table
connection = sqlite3.connect("HospitalDB.db")
crsr = connection.cursor()

sql_command = """
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INTEGER,
    gender TEXT,
    diagnosis TEXT,
    admission_date DATE
);
"""

crsr.execute(sql_command)
connection.commit()
connection.close()


def submit_record():
    try:
        connection = sqlite3.connect("HospitalDB.db")
        crsr = connection.cursor()

        crsr.execute(
            "INSERT INTO patients VALUES (NULL, ?, ?, ?, ?, ?, ?)",
            (
                first_name.get(),
                last_name.get(),
                int(age.get()),
                gender.get(),
                diagnosis.get(),
                admission_date.get(),
            ),
        )

        connection.commit()
        connection.close()

        # Clear the input fields
        for entry in data_entries:
            entry.delete(0, END)

    except ValueError:
        # Handle invalid input
        result_label.config(text="Invalid input")


def query_database():
    connection = sqlite3.connect("HospitalDB.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM patients")
    records = crsr.fetchall()

    # Display records in a label
    result_text = ""
    for record in records:
        result_text += f"ID: {record[0]}, Name: {record[1]} {record[2]}, Age: {record[3]}, Gender: {record[4]}, Diagnosis: {record[5]}, Admission Date: {record[6]}\n"

    result_label.config(text=result_text)
    connection.close()


# Create the main window
root = Tk()
root.title("Hospital Database")
root.geometry("600x400")

# Input fields
labels = ["First Name", "Last Name", "Age", "Gender", "Diagnosis", "Admission Date"]
data_entries = []

for i, label_text in enumerate(labels):
    label = Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=10)

    entry = Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=10)
    data_entries.append(entry)

# Submit button
submit_button = Button(root, text="Submit Record", command=submit_record)
submit_button.grid(row=len(labels), columnspan=2, pady=10)

# Query button
query_button = Button(root, text="Query Database", command=query_database)
query_button.grid(row=len(labels) + 1, columnspan=2, pady=10)

# Result label
result_label = Label(root, text="", font=("Arial", 12))
result_label.grid(row=len(labels) + 2, columnspan=2, pady=10)

root.mainloop()
