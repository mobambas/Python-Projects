from tkinter import *
import random
from PIL import ImageTk, Image
from random import randint

def math_random():
    global num1, num2, add_image_1, add_image_2
    num1 = randint(1,10)
    num2 = randint(1,10)
    card_1 = 'flashcard/' + str(num1) + '.jpg'
    card_2 = 'flashcard/' + str(num2) + '.jpg'

    add_image_1 = ImageTk.PhotoImage(Image.open(card_1))
    add_image_2 = ImageTk.PhotoImage(Image.open(card_2))

    add_1.config(image = add_image_1)
    add_2.config(image = add_image_2)


def answer_add():
    answer = num1 + num2
    if int(add_answer.get()) == answer:
        response = 'Correct!'
    else:
        response = 'Incorrect! The answer was ' + str(answer)
    answer_message.config(text=response)
    add_answer.delete(0, 'end')
    math_random()


def add():
    hide_all_frame()
    add_frame.pack()
    add_label = Label(add_frame, text='Addition Flashcard', font=('Comic Sans MS', 20, 'bold'))
    add_label.pack(pady=15)
    pic_frame = Frame(add_frame, width=600,height=600)
    pic_frame.pack()

    global num1, num2, add_1, add_2, add_image_1, add_image_2, add_answer, answer_message

    num1 = randint(1,10)
    num2 = randint(1,10)

    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sign = Label(pic_frame, text = '+', font=('Comic Sans MS', 30, 'italic'))

    add_1.grid(row = 0, column = 0)
    math_sign.grid(row = 0, column = 1)
    add_2.grid(row = 0, column = 2)
    card_1 = 'flashcard/' + str(num1) + '.jpg'
    card_2 = 'flashcard/' + str(num2) + '.jpg'

    add_image_1 = ImageTk.PhotoImage(Image.open(card_1))
    add_image_2 = ImageTk.PhotoImage(Image.open(card_2))

    add_1.config(image = add_image_1)
    add_2.config(image=add_image_2)

    add_answer = Entry(add_frame, font=('Comic Sans MS', 20, 'bold', 'italic'))
    add_answer.pack(pady=50)

    add_answer_btn = Button(add_frame, text='Answer', font=('Comic Sans MS', 20, 'bold', 'italic'), command = answer_add)
    add_answer_btn.pack()

    answer_message  = Label(add_frame, text= '', font=('Comic Sans MS', 20, 'bold', 'italic'))
    answer_message.pack(pady=40)
def random_country():

    global our_countries, rando, country_image
    our_countries = open("filenames.txt").read().splitlines()

    rando = randint(0, len(our_countries) - 1)
    country = 'flags/' + our_countries[rando]
    print(country)
    country_image = ImageTk.PhotoImage(Image.open(country))
    show_country.config(image=country_image)



def country_answer():
    answer = answer_input.get().title()
    answer = 'Flag of ' + answer + '.gif'
    print(answer)
    if answer == our_countries[rando]:
        response = "Correct!"
    else:
        response = "Incorrect, the answer was " + our_countries[rando].split()[-1].split('.')[0]

    answer_label.config(text=response)
    answer_input.delete(0, END)
    random_country()

def countries():
    hide_all_frame()
    country_frame.pack()
    global show_country, answer_input, answer_label
    show_country = Label(country_frame)
    show_country.pack(pady=15)
    random_country()
    answer_input = Entry(country_frame, font=('Comic Sans MS',20,'bold'), bd =2)
    answer_input.pack(pady=15)
    rando_btn = Button(country_frame, text = 'Pass', command = countries)
    rando_btn.pack(pady=10)
    answer_btn = Button(country_frame, text="Answer", command=country_answer)
    answer_btn.pack(pady=5)
    answer_label = Label(country_frame, text='', font=('Comic Sans MS',20,'bold'))
    answer_label.pack(pady=15)



def country_capital_answer():
    if capital_radio.get() == our_countries_capital[answer]:
        response = "Correct"
    else:
        response = "Not correct.The answer was " + our_countries_capital[answer]
    answer_label_capital.config(text = response)
def country_capital():
    hide_all_frame()
    country_capital_frame.pack()
    global show_country, our_countries, our_countries_capital, capital_radio, answer, country_image, answer_label_capital
    show_country = Label(country_capital_frame)
    show_country.pack(pady = 15)
    our_countries = open("Capitals.txt").read().splitlines()
    our_country_capitals = {}
    for i in our_countries:
        a = i.split("-")
        our_country_capitals[a[0].strip()] = a[1].strip()
    answer_list = []
    count = 1
    while count < 4:
        rando = randint(0, len(our_countries) - 1)
        if count == 1:
            answer = our_countries[rando].split('-')[0].strip()
            country = 'flags/' + 'Flag of ' + answer + '.gif'
            country_image = ImageTk.PhotoImage(Image.open(country))
            show_country.config(image = country_image)

            answer_list.append(our_countries[rando])
            our_countries.remove(our_countries[rando])
            random.shuffle(our_countries)
            count += 1

    for i in range (0,4):
        answer_list[i] = answer_list[i].split("-")[0].strip()

    random.shuffle(answer_list)

    print(answer_list)






    capital_radio = StringVar()
    capital_radio_btn_1 = Radiobutton(country_capital_frame, text = our_country_capitals[answer_list[0]].title(), variable = capital_radio, value = our_country_capitals[answer_list[0]])
    capital_radio_btn_1.pack()
    capital_radio_btn_2 = Radiobutton(country_capital_frame, text = our_country_capitals[answer_list[1]].title(), variable = capital_radio, value = our_country_capitals[answer_list[1]])
    capital_radio_btn_2.pack()
    capital_radio_btn_3 = Radiobutton(country_capital_frame, text = our_country_capitals[answer_list[2]].title(), variable = capital_radio, value = our_country_capitals[answer_list[2]])
    capital_radio_btn_3.pack()

    pass_btn = Button(country_capital_frame, text='Pass', command=country_capital)
    pass_btn.pack(pady=15)

    answer_btn = Button(country_capital_frame, text="Answer", command=country_capital_answer)
    answer_btn.pack(pady=15)

    answer_label_capitals = Label(country_capital_frame, text="", font = ('Arial', 20, 'bold'))
    answer_label_capitals.pack(pady=15)



def hide_all_frame():
    for i in country_frame.winfo_children():
        i.destroy()
    for i in country_capital_frame.winfo_children():
        i.destroy()
    for i in add_frame.winfo_children():
        i.destroy()
    add_frame.pack_forget()
    country_frame.pack_forget()
    country_capital_frame.pack_forget()




root = Tk()
root.title('Flashcards')
root.geometry('800x600')
bg = PhotoImage(file="tk_background.png")
back_label = Label(root,Image = bg)
back_label.place(relwidth = 1 ,relheight = 1)
my_menu = Menu(root)
root.config(menu=my_menu)
countries_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Geography', menu = countries_menu)
countries_menu.add_command(label = 'Countries', command = countries)
countries_menu.add_command(label = 'Countries Capitals', command = country_capital)
countries_menu.add_separator()
countries_menu.add_command(label = 'Exit', command = root.destroy)
math_menu = Menu(my_menu)
my_menu.add_cascade(label = "Maths", menu = math_menu)
math_menu.add_command(label = 'Addition', command = add)
# math_menu.add_command(label = 'Subtraction')
# math_menu.add_command(label = 'Multiplication')
# math_menu.add_command(label = 'Division')


country_frame = Frame(root, width = 500, height = 500, bg = '#5d9eb0')
country_capital_frame = Frame(root, width= 500, height = 500, bg = '#5d9eb0')
add_frame = Frame(root, width=500, height = 500, bg = '#5d9eb0')
root.mainloop()