from tkinter import *
from PIL import ImageTk
from random import randint, shuffle

# Constants
FLASHCARD_FOLDER = 'flashcard/'
FLAG_FOLDER = 'flags/'
CAPITAL_FILE = 'Capitals.txt'
BACKGROUND_IMAGE = 'tk_background.png'

def math_random():
    global num1, num2, add_image_1, add_image_2
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    card_1 = f'{FLASHCARD_FOLDER}{num1}.jpg'
    card_2 = f'{FLASHCARD_FOLDER}{num2}.jpg'

    add_image_1 = ImageTk.PhotoImage(Image.open(card_1))
    add_image_2 = ImageTk.PhotoImage(Image.open(card_2))

    add_1.config(image=add_image_1)
    add_2.config(image=add_image_2)

def answer_add():
    answer = num1 + num2
    if int(add_answer.get()) == answer:
        response = 'Correct!'
    else:
        response = f'Incorrect! The answer was {answer}'
    answer_message.config(text=response)
    add_answer.delete(0, 'end')
    math_random()

def add():
    hide_all_frame()
    add_frame.pack()
    add_label = Label(add_frame, text='Addition Flashcard', font=('Comic Sans MS', 20, 'bold'))
    add_label.pack(pady=15)
    pic_frame = Frame(add_frame, width=600, height=600)
    pic_frame.pack()

    global num1, num2, add_1, add_2, add_image_1, add_image_2, add_answer, answer_message

    num1 = randint(1, 10)
    num2 = randint(1, 10)

    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sign = Label(pic_frame, text='+', font=('Comic Sans MS', 30, 'italic'))

    add_1.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    add_2.grid(row=0, column=2)
    card_1 = f'{FLASHCARD_FOLDER}{num1}.jpg'
    card_2 = f'{FLASHCARD_FOLDER}{num2}.jpg'

    add_image_1 = ImageTk.PhotoImage(Image.open(card_1))
    add_image_2 = ImageTk.PhotoImage(Image.open(card_2))

    add_1.config(image=add_image_1)
    add_2.config(image=add_image_2)

    add_answer = Entry(add_frame, font=('Comic Sans MS', 20, 'bold', 'italic'))
    add_answer.pack(pady=50)

    add_answer_btn = Button(add_frame, text='Answer', font=('Comic Sans MS', 20, 'bold', 'italic'), command=answer_add)
    add_answer_btn.pack()

    answer_message = Label(add_frame, text='', font=('Comic Sans MS', 20, 'bold', 'italic'))
    answer_message.pack(pady=40)

def random_country():
    global our_countries, rando, country_image
    our_countries = open("filenames.txt").read().splitlines()

    rando = randint(0, len(our_countries) - 1)
    country = f'{FLAG_FOLDER}{our_countries[rando]}'
    print(country)
    country_image = ImageTk.PhotoImage(Image.open(country))
    show_country.config(image=country_image)

def country_answer():
    answer = answer_input.get().title()
    answer = f'Flag of {answer}.gif'
    print(answer)
    if answer == our_countries[rando]:
        response = "Correct!"
    else:
        response = f"Incorrect, the answer was {our_countries[rando].split()[-1].split('.')[0]}"

    answer_label.config(text=response)
    answer_input.delete(0, END)
    random_country()

# Add other functions...

root = Tk()
root.title('Flashcards')
root.geometry('800x600')
bg = PhotoImage(file=BACKGROUND_IMAGE)
back_label = Label(root, Image=bg)
back_label.place(relwidth=1, relheight=1)
my_menu = Menu(root)
root.config(menu=my_menu)
countries_menu = Menu(my_menu)
my_menu.add_cascade(label='Geography', menu=countries_menu)
countries_menu.add_command(label='Countries', command=random_country)
countries_menu.add_command(label='Countries Capitals', command=country_answer)
countries_menu.add_separator()
countries_menu.add_command(label='Exit', command=root.destroy)
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Maths", menu=math_menu)
math_menu.add_command(label='Addition', command=add)

country_frame = Frame(root, width=500, height=500, bg='#5d9eb0')
country_capital_frame = Frame(root, width=500, height=500, bg='#5d9eb0')
add_frame = Frame(root, width=500, height=500, bg='#5d9eb0')

root.mainloop()
