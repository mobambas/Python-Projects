import csv
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("Customer Relationship Manager")
root.geometry("450x600")
mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = 'shyluck09',
    database = 'shriyanshcrm'
)
my_cursor = mydb.cursor()
# my_cursor.execute('CREATE DATABASE shriyanshCRM')
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
#     print(db)

#
# my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
# first_name VARCHAR(255),
# last_name VARCHAR(255),
# adress_1 VARCHAR(255),
# adress_2 VARCHAR(255),
# city VARCHAR(50),
# state VARCHAR(50),
# zipcode INT(10),
# country VARCHAR(255),
# phone INT(25),
# email VARCHAR(255),
# payment_method VARCHAR(50),
# discount_code VARCHAR(50),
# price_paid DECIMAL(10,2),
# user_id INT AUTO_INCREMENT PRIMARY KEY)
# """)

def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    adress_1_box.delete(0, END)
    adress_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)



def add_customer():
    sql_command  = """INSERT INTO customers (first_name, last_name, adress_1, adress_2, city, state, zipcode, country, phone, email, payment_method, discount_code, price_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (first_name_box.get(), last_name_box.get(), adress_1_box.get(), adress_2_box.get(), city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(), email_box.get(), payment_method_box.get(), discount_code_box.get(), price_paid_box.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear_fields()

def wrong_info():
    index = 0
    if zipcode_box.get()[index] != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        messagebox.showerror('Error', 'Please enter correct zipcode!')
        index += 1


def write_to_csv(result):
    with open('Customers.csv', 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for i in result:
            w.writerow(i)

def search_customer():
    root2 = Tk()
    root2.title("Search Customers")
    def update():
        sql_command = """UPDATE customers SET first_name = %s, last_name = %s, adress_1 = %s, adress_2 = %s, city = %s, state = %s, zipcode = %s, country = %s , phone = %s, email = %s, payment_method = %s, discount_code = %s, price_paid = %s WHERE user_id = %s"""
        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        adress_1 = adress_1_box2.get()
        adress_2 = adress_2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        email = email_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()
        price_paid = price_paid_box2.get()

        inputs = (first_name, last_name, adress_1, adress_2, city, state, country, phone, email,  payment_method, discount_code, price_paid)
        my_cursor.execute(sql_command, inputs)
        mydb.commit()


    def edit(id, index):
        sql_command = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id)
        result2 = my_cursor.execute(sql_command, name2)
        result2 = my_cursor.fetchall()
        index += 1

        first_name_label = Label(root2, text = 'First Name', font=("Comic Sans MS", 14)).grid(row = index + 1, column = 0, sticky = W, padx = 10, pady = 10)
        last_name_label = Label(root2, text='Last Name').grid(row=index + 2, column=0, sticky = W, padx = 10)
        adress_1_label = Label(root2, text='Adress 1').grid(row=index + 3, column=0, sticky = W, padx = 10)
        adress_2_label = Label(root2, text='Adress 2').grid(row=index + 4, column=0, sticky = W, padx = 10)
        city_label = Label(root2, text='City').grid(row=index + 5, column=0, sticky = W, padx = 10)
        state_label = Label(root2, text='State').grid(row=index + 6, column=0, sticky = W, padx = 10)
        zipcode_label = Label(root2, text='Zipcode').grid(row=index + 7, column=0, sticky = W, padx = 10)
        country_label = Label(root2, text='Country').grid(row=index + 8, column=0, sticky = W, padx = 10)
        phone_label = Label(root2, text='Phone').grid(row=index + 9, column=0, sticky = W, padx = 10)
        email_label = Label(root2, text='Email').grid(row=index + 10, column=0, sticky = W, padx = 10)
        payment_method_label = Label(root2, text='Payment Method').grid(row=index + 11, column=0, sticky = W, padx = 10)
        discount_code_label = Label(root2, text='Discount Code').grid(row=index + 12, column=0, sticky = W, padx = 10)
        price_paid_label = Label(root2, text='Price Paid').grid(row=index + 13, column=0, sticky = W, padx = 10)
        id_label = Label(root2, text='User ID').grid(row=index + 14, column=0, sticky = W, padx = 10)

        global first_name_box2, last_name_box2, adress_1_box2, adress_2_box2, city_box2, state_box2, zipcode_box2, country_box2, phone_box2, email_box2, payment_method_box2, discount_code_box2, price_paid_box2, user_id_box2
        first_name_box2 = Entry(root2)
        first_name_box2.grid(row = index + 1, column = 1, pady = 10)
        first_name_box2.insert(0, result2[0][0])


        last_name_box2 = Entry(root2)
        last_name_box2.grid(row= index + 2, column=1, pady = 5)
        last_name_box2.insert(0, result2[0][1])

        adress_1_box2 = Entry(root2)
        adress_1_box2.grid(row=index + 3, column=1, pady = 5)
        adress_1_box2.insert(0, result2[0][2])

        adress_2_box2 = Entry(root2)
        adress_2_box2.grid(row=index + 4, column=1, pady = 5)
        adress_2_box2.insert(0, result2[0][3])

        city_box2 = Entry(root2)
        city_box2.grid(row=index + 5, column=1, pady = 5)
        city_box2.insert(0, result2[0][4])

        state_box2 = Entry(root2)
        state_box2.grid(row=index + 6, column=1, pady = 5)
        state_box2.insert(0, result2[0][5])

        zipcode_box2 = Entry(root2)
        zipcode_box2.grid(row=index + 7, column=1, pady = 5)
        zipcode_box2.insert(0, result2[0][6])

        country_box2 = Entry(root2)
        country_box2.grid(row=index + 8, column=1, pady = 5)
        country_box2.insert(0, result2[0][7])

        phone_box2 = Entry(root2)
        phone_box2.grid(row=index + 9, column=1, pady = 5)
        phone_box2.insert(0, result2[0][8])

        email_box2= Entry(root2)
        email_box2.grid(row=index + 10, column=1, pady = 5)
        email_box2.insert(0, result2[0][9])

        payment_method_box2 = Entry(root2)
        payment_method_box2.grid(row=index + 11, column=1, pady = 5)
        payment_method_box2.insert(0, result2[0][10])

        discount_code_box2 = Entry(root2)
        discount_code_box2.grid(row=index + 12, column=1, pady = 5)
        discount_code_box2.insert(0, result2[0][11])

        price_paid_box2 = Entry(root2)
        price_paid_box2.grid(row=index + 13, column=1, pady = 5)
        price_paid_box2.insert(0, result2[0][12])

        user_id_box2 = Entry(root2)
        user_id_box2.grid(row=index + 14, column=1, pady = 5)
        user_id_box2.insert(0, result2[0][13])

        save_btn = Button(root2, text = "Update", command = update)
        save_btn.grid(row = index + 15, column = 0)
        quit_btn = Button(root2, text= "Quit", command = root2.destroy)
        quit_btn.grid(row = index + 15, column = 1)


    def search_now():
        selected = drop.get()
        sql_command3 = ''
        if selected == 'Search by':
            test = Label(root2, text = "You forgot to pick a dropdown. Try again.")
            test.grid(row = 2, column = 0)

        if selected == 'Email':
            sql_command3 = """SELECT * FROM customers WHERE email = %s"""

        if selected == 'Last Name':
            sql_command3 = """SELECT * FROM customers WHERE last_name = %s"""
        searched = search_box.get()
        name = (searched,)
        result = my_cursor.execute(sql_command3,name)
        result = my_cursor.fetchall()

        if not result:
            search_label = Label(root2, text = 'Result not found')
            search_label.grid(row = 2, column = 0)
        else:
            for index, item in enumerate(result):
                num = 0
                index += 1
                id_ref = str(item[0])
                edit_btn = Button(root2, text="Edit", command = lambda id_ref = id_ref:edit(id_ref, index))
                edit_btn.grid(row = index, column = num)
                for x in item:
                    search_label = Label(root2, text=x)
                    search_label.grid(row = index, column = num + 1)
                    num += 1


    search_box = Entry(root2)
    search_box.grid(row = 0, column = 1, padx = 10, pady = 10)

    search_box_label = Label(root2, text = 'Search Customers')
    search_box_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    search_box_btn = Button(root2, text = "Search Customers", command = search_now)
    search_box_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

    drop = ttk.Combobox(root2, value = ['Search by', 'Last Name', 'Email'])
    drop.current(0)
    drop.grid(row = 0, column = 2)

def list_customers():
    root3 = Tk()
    root.title("List all cumstomers")
    my_cursor.execute("""SELECT * FROM customers""")
    result = my_cursor.fetchall()
    for index, item in enumerate(result):
        num = 0
        for i in item:
            label = Label(root3, text=i)
            label.grid(row = index, column = num)
            num += 1
    csv_btn = Button(root3, text="Save to excel", command = lambda:write_to_csv(result))
    csv_btn.grid(row = index+1, column = 0)


title_label = Label(root, text = 'Customer Database', font= ('Helvetica', 25))
title_label.grid(row = 0, column = 0, pady = 10)




first_name_label = Label(root, text = "First Name", font=("Times New Roman", 14), bg='red').grid(row = 1, column = 0, sticky = W, padx = 10)
last_name_label = Label(root, text = "Last Name").grid(row = 2, column = 0, sticky = W, padx = 10)
adress_1_label = Label(root, text = "Address 1").grid(row = 3, column = 0, sticky = W, padx = 10)
adress_2_label = Label(root, text = "Address 2").grid(row = 4, column = 0, sticky = W, padx = 10)
city_label = Label(root, text = "City").grid(row = 5, column = 0, sticky = W, padx = 10)
state_label = Label(root, text = "State").grid(row = 6, column = 0, sticky = W, padx = 10)
zipcode_label = Label(root, text = "ZipCode").grid(row = 7, column = 0, sticky = W, padx = 10)
country_label = Label(root, text = "Country").grid(row = 8, column = 0, sticky = W, padx = 10)
phone_label = Label(root, text = "Phone").grid(row = 9, column = 0, sticky = W, padx = 10)
email_label = Label(root, text = "Email").grid(row = 10, column = 0, sticky = W, padx = 10)
payment_method_label = Label(root, text = "Payment Method").grid(row = 11, column = 0, sticky = W, padx = 10)
discount_code_label = Label(root, text = "Discount Code").grid(row = 12, column = 0, sticky = W, padx = 10)
price_paid_label = Label(root, text = "Price Paid").grid(row = 13, column = 0, sticky = W, padx = 10)

first_name_box = Entry(root)
first_name_box.grid(row = 1, column = 1, pady = 5)
last_name_box = Entry(root)
last_name_box.grid(row = 2, column = 1, pady = 5)
adress_1_box = Entry(root)
adress_1_box.grid(row = 3, column = 1, pady = 5)
adress_2_box = Entry(root)
adress_2_box.grid(row = 4, column = 1, pady = 5)
city_box = Entry(root)
city_box.grid(row = 5, column = 1, pady = 5)
state_box = Entry(root)
state_box.grid(row = 6, column = 1, pady = 5)
zipcode_box = Entry(root)
zipcode_box.grid(row = 7, column = 1, pady = 5)
country_box = Entry(root)
country_box.grid(row = 8, column = 1, pady = 5)
phone_box = Entry(root)
phone_box.grid(row = 9, column = 1, pady = 5)
email_box = Entry(root)
email_box.grid(row = 10, column = 1, pady = 5)
payment_method_box = Entry(root)
payment_method_box.grid(row = 11, column = 1, pady = 5)
discount_code_box = Entry(root)
discount_code_box.grid(row = 12, column = 1, pady = 5)
price_paid_box = Entry(root)
price_paid_box.grid(row = 13, column = 1, pady = 5)

add_customer_btn = Button(root, text = "Add Customer", command= add_customer)
add_customer_btn.grid(row = 14, column = 0, padx = 10, pady = 10)

clear_fields_btn = Button(root, text = "Clear Fields", command = clear_fields)
clear_fields_btn.grid(row = 14, column = 1, padx = 10, pady = 10)

list_customer_btn = Button(root, text = "List Customer", command = list_customers)
list_customer_btn.grid(row = 15, column = 0, padx = 10, pady = 10)

search_customer_btn = Button(root, text = "Search Customer", command = search_customer)
search_customer_btn.grid(row = 15, column = 1, padx = 10, pady = 10)


root.mainloop()
