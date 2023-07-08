import sqlite3
from tkinter import *

connection = sqlite3.connect("EmpInfo.db")

crsr = connection.cursor()

sql_command = """CREATE TABLE yes(
staff_id INTEGER PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(20),
role_appointed VARCHAR(20),
gender text);"""

crsr.execute(sql_command)

sql_command = """INSERT INTO yes VALUES(1, "Lakshmi", "Singh", "CEO", "female")"""

crsr.execute(sql_command)

sql_command = """INSERT INTO yes VALUES(2, "Shyam", "Singh", "CEO", "male")"""

crsr.execute(sql_command)

connection.commit()

connection.close()


def Submit():
    # connecting to the database
    connection = sqlite3.connect("EmpInfo.db")
    # cursor
    crsr = connection.cursor()
    # Insert Into Table
    crsr.execute("INSERT INTO yes VALUES (:Staffno,  :f_name , :l_name , :role , :Gender)",
                 {
                     'Staffno': Staffno.get(),
                     'f_name': f_name.get(),
                     'l_name': l_name.get(),
                     'role': role.get(),
                     'Gender': Gender.get()

                 }
                 )
    connection.commit()  # Commit all the changes to the database
    connection.close()
    # Clear the Text Boxes
    Staffno.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    role.delete(0, END)
    Gender.delete(0, END)


def Query():
    # connecting to the database
    connection = sqlite3.connect("EmpInfo.db")
    # cursor
    crsr = connection.cursor()
    # Insert Into Table
    crsr.execute("SELECT *,oid FROM yes")
    # store all the fetched data in the ans variable
    ans = crsr.fetchall()
    # Since we have already selected all the data entries
    # using the "SELECT *" SQL command and stored them in
    # the ans variable, all we need to do now is to print
    # out the ans variable
    # As we want to display the dataframe in our GUI we can use label widget
    # ans is a list and for example we want to find the names of all the
    # People in datatable we can use the following command
    records = ""
    for record in ans:
        records += record[0] + " " + record[1] + " " + record[2] + " " + record[3] + '\n'
    Label(root, text=records).grid(row=7, column=0, columnspan=2)


def Delete():
    connection = sqlite3.connect("EmpInfo.db")

    crsr = connection.cursor()

    connection.execute("DELETE from yes where staff_id=" + deli.get())
    deli.delete(0, END)

    connection.commit()


def Update():
    up = Tk()

    connection = sqlite3.connect("EmpInfo.db")

    crsr = connection.cursor()


    file_id = deli.get()

    crsr.execute("SELECT * FROM yes where oid = " +
                 file_id)

    file = crsr.fetchall()

    # Create Text Boxes

    global Staffno_edit
    Staffno_edit = Entry(up, width=30)
    Staffno.grid(row=0, column=1, padx=20)

    global f_name_edit
    f_name_edit = Entry(up, width=30)
    f_name.grid(row=1, column=1, padx=20)

    global l_name_edit
    l_name_edit = Entry(up, width=30)
    l_name.grid(row=2, column=1, padx=20)

    global role_edit
    role_edit = Entry(up, width=30)
    role.grid(row=3, column=1, padx=20)

    global Gender_edit
    Gender_edit = Entry(up, width=30)
    Gender.grid(row=4, column=1, padx=20)

    # Create text box labels
    Studentno_label = Label(up, text="Staff Number")
    Studentno_label.grid(row=0, column=0)

    f_name_label = Label(up, text="First Name")
    f_name_label.grid(row=1, column=0)

    l_name_label = Label(up, text="Last Name")
    l_name_label.grid(row=2, column=0)

    role_label = Label(up, text="Role Appointed")
    role_label.grid(row=3, column=0)

    Gender_label = Label(up, text="Gender")
    Gender_label.grid(row=4, column=0)

    for file in files:
        Staffno_edit.insert(0, record[0])
        f_name_edit.insert(0, record[1])
        l_name_edit.insert(0, record[2])
        role_edit.insert(0, record[3])
        Gender_edit.insert(0, record[4])

    Button(up, text="Submit Changes", command=
    edit).grid(row=4, column=1, pady=10, padx=10)

    Button(up, text="Delete", command=
    up.destroy).grid(row=5, column=1, pady=10, padx=10)

    connection.commit()
    connection.close()


root = Tk()

# Create Text Boxes
Studentno = Entry(root, width=30)
Studentno.grid(row=0, column=1, padx=20)

f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=2, column=1, padx=20)

Gender = Entry(root, width=30)
Gender.grid(row=3, column=1, padx=20)

# Create text box labels
Studentno_label = Label(root, text="Staff Number")
Studentno_label.grid(row=0, column=0)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=0)

role_label = Label(root, text="Role Appointed")
role_label.grid(row=3, column=0)

Gender_label = Label(root, text="Gender")
Gender_label.grid(row=3, column=0)

deli_label = Label(root, text="Enter ID of the person to be deleted")
deli_label.grid(row=8, column=0)

deli = Entry(root, width=30)
deli.grid(row=8, column=1, padx=20)

# Create a submit button
Button(root, text="Add record to data base", command=Submit).grid(row=5, columnspan=2, pady=10, padx=20, ipadx=100)
Button(root, text="Query the database", command=Query).grid(row=6, columnspan=2, pady=10, padx=20, ipadx=100)
Button(root, text="Delete the entered ID", command=Delete).grid(row=9, columnspan=2, pady=10, padx=20, ipadx=100)
Button(root, text="Select the entered ID", command=Update).grid(row=10, columnspan=2, pady=10, padx=20, ipadx=100)
