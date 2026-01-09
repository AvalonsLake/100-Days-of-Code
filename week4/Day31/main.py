from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------------- Functions ---------------------------------- #
def get_flashcard():
    global current_card
    current_card = to_learn[randint(0, len(to_learn) - 1)]
    french_word = current_card["French"]

    canvas.itemconfig(flashcard, image=flashcard_front)
    canvas.itemconfig(flash_language, text="French", fill="black")
    canvas.itemconfig(flash_word, text=french_word, fill="black")

    window.after(3000, flip_flashcard)

def flip_flashcard():
    english_word = current_card["English"]

    canvas.itemconfig(flashcard, image=flashcard_back)
    canvas.itemconfig(flash_language, text="English", fill="white")
    canvas.itemconfig(flash_word, text=english_word, fill="white")

def known_word():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    get_flashcard()


# ---------------------------------- GUI Setup ---------------------------------- #

window = Tk()
window.title("Flashy Flashcards!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(700, 600)

# ------ Images ------ #
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# ------ Flashcard ------ #

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

flashcard = canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)
flash_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
flash_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# ------ Buttons ------ #

wrong_btn = Button(window, image=wrong, borderwidth=0, highlightthickness=0, command=get_flashcard)
wrong_btn.grid(row=1, column=0)
right_btn = Button(window, image=right, borderwidth=0, highlightthickness=0, command=known_word)
right_btn.grid(row=1, column=1)


get_flashcard()


window.mainloop()
