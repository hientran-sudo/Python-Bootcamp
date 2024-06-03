from tkinter import *
import pandas as pd
import random


data = pd.read_csv(r'data/french_words.csv')
learn = data.to_dict(orient="records")
current = {}

def next_card(): 
    global current, flip_timer
    window.after_cancel(flip_timer) 
    current = random.choice(learn)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current['French'])
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current['English'])
    
    
window = Tk()
window.title("Flash card")
window.config(padx=50,pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

front = canvas.create_image(400, 263, image=card_front)
back = canvas.create_image(400, 263, image=card_back)

title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="images/wrong.png")
unknown = Button(image=cross, command=next_card)
unknown.grid(row=2, column=0)

tick = PhotoImage(file="images/right.png")
known = Button(image=tick, command=next_card)
known.grid(row=2, column=1)

window.mainloop()