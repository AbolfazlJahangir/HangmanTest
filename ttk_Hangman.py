from tkinter import *
import random

words = ["apple", "orange", "benana", "lemon", "watermelon", "blueberry", "strawberry"]

word = random.choice(words)
letter_word = [letter for letter in word]
len_word = len(word)

guid_answer = ["_" for i in range(len_word)]

count = 0
def start():
    global count

    count += 1

    if count == 1:
        lbl1.config(text="HINT: The word is a name of a fruit", font=("consolas", 20))
        lbl2.config(text=f"{''.join(guid_answer)} --> {len_word} letters")

status = 0
i = 0
def get_guess():
    global word, guess, letter_word, len_word, guid_answer, status, i

    for i in range(len_word+2):
        guess = guess_entry.get()
        if guess in word:
            if letter_word.count(guess) == 1:
                index_guess = word.index(guess)
                guid_answer[index_guess] = guess
            else:
                while guid_answer.count(guess) != letter_word.count(guess):
                    for index, item in enumerate(letter_word):
                        if item == guess:
                            guid_answer[index] = item
                            
        lbl2.config(text=f"{''.join(guid_answer)} --> {len_word} letters")
        guess_entry.delete(0,END)

        if guid_answer == letter_word:
            lbl1.config(text="Congratulations, You won!")
            status = 1
            break
    if status == 0:
        lbl1.config(text=f"You lost! the word was {word}")


def play_again():
    global word, count, letter_word, len_word, guid_answer, status

    word = random.choice(words)
    letter_word = [letter for letter in word]
    len_word = len(word)
    guid_answer = ["_" for i in range(len_word)]
    status = 0
    count = 0
    i = 0

    lbl1.config(text="WELCOM TO THE HANGMAN")
    lbl2.config(text="click the start button!")


window = Tk()
window.title("GAME : HANGMAN")
window["bg"] = "blue"

lbl1 = Label(window, text="WELCOM TO THE HANGMAN", font=("consolas", 30), bg='#F41')
lbl1.pack(side="top")

lbl2 = Label(window, text="click the start button!", font=("consolas", 15), bg='#F41')
lbl2.pack()

start_button = Button(window, text="START", width=5, height=2, font=("consolas", 20), command=start)
start_button.pack()

guess_entry = Entry(window, width=16)
guess_entry.pack(padx=5, pady=5)
button_guess = Button(window, text="GUESS", font=("consolas", 15), command=get_guess)
button_guess.pack()

reset_button = Button(window, text="Restart", font=('consolas', 15), command=play_again)
reset_button.pack()

exit_button = Button(window, text="Exit", font=('consolas', 15), command=exit)
exit_button.pack()

window.geometry("600x500")
window.mainloop()