from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
temp_card = {}
to_learn = {}

# ---------------------------- Flash card generate ------------------------------- #
try:
    file = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    org_file = pd.read_csv('./data/french_words.csv')
    to_learn = org_file.to_dict(orient='records')
else:
    to_learn = file.to_dict(orient='records')


def next_card():
    global temp_card, timer
    window.after_cancel(timer)
    temp_card = choice(to_learn)
    french_word = temp_card['French']
    canvas.itemconfig(image_canvas, image=card_front)
    canvas.itemconfig(title_canvas, text='French', fill='black')
    canvas.itemconfig(word_canvas, text=french_word, fill='black')
    timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(image_canvas, image=card_back)
    canvas.itemconfig(title_canvas, text='English', fill='white')
    canvas.itemconfig(word_canvas, text=temp_card['English'], fill='white')

def is_known():
    to_learn.remove(temp_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn.csv', index=False)
    print(len(to_learn))
    next_card()

# -------------------------------------------------------------------------- #

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
canvas.grid(row=0, column=0, columnspan=2)


card_back = PhotoImage(file='./images/card_back.png')
card_front = PhotoImage(file='./images/card_front.png')
image_canvas = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_canvas = canvas.create_text(400, 150, text='', font=("Ariel", 40, 'italic'))
word_canvas = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

# Button
cross_image = PhotoImage(file='./images/wrong.png')
cross = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
cross.grid(row=1, column=0)

tick_image = PhotoImage(file='./images/right.png')
tick = Button(image=tick_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
tick.grid(row=1, column=1)
next_card()

window.mainloop()
