from tkinter import *
import pandas
import random

current_card ={}
to_learn = {}
#csv data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient ="records")
else:
    to_learn = data.to_dict(orient="records")

#next card
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_card['French'], fill= "black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(3000, func= flip_card)


#flip card
def flip_card():
    canvas.itemconfig(card_title, text= "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background,image = card_back_img )


#is known/ remove cards from the words_to_learn deck that is guessed correctly
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

#Window setup
window = Tk()
window.title("Flash card Language Learner")
window.config(padx=50, pady=50, bg="lime")

flip_timer = window.after(3000, func= flip_card)



#UI setup

canvas = Canvas(width=800, height=526, bg="lime", highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400,150,text="Title", font=('Ariel',40,"italic"))
card_word = canvas.create_text(400,263,text="Word", font=('Ariel',60,"bold"))
canvas.grid(column=0 , row=0, columnspan=2)

#buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image= cross_img, bg="lime", command= next_card)
unknown_button.grid(column= 0, row=1)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image= right_img, bg="lime", command= is_known)
known_button.grid(column= 1, row=1)

next_card()

window.mainloop()

