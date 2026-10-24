import tkinter as tk
import random


lives = 10
hidden = ""

root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x300")

def get_guess():
    global guess
    guess = guess_entry.get()
    

word_label = tk.Label(root, text=hidden, font=("Helvetica", 16))
word_label.pack(pady=20)  

guess_button = tk.Button(
    root,
    width=10,
    height=2, 
    text="Guess",
    command=get_guess
)
guess_button.place(x=150, y=200)


guess_entry = tk.Entry(root, width=40)
guess_entry.place(x=100, y=150)

while lives > 0:
    word = "py"
    guess = ""
    length = len(word)
    correct_letters = []
    false_letters = []

    if guess in word:
        correct_letters.append(guess)
    else:
        false_letters.append(guess)
        lives -= 1

    for letter in word:
        if letter in correct_letters:
            word_label.config(text=letter)

def change_hidden():
    for _ in range(length):
        hidden += "_"

root.mainloop()