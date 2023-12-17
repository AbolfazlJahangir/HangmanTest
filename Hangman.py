import random

words = ["apple", "orange", "benana", "lemon", "watermelon", "blueberry", "strawberry"]

word = random.choice(words)
letter_word = [letter for letter in word]
len_word = len(word)

print("Guess the word! HINT: word is a name of a fruit")

guid_answer = ["_" for i in range(len_word)]

print("".join(guid_answer))
print()

for i in range(len_word+2):
    guess = input("Enter a letter to guess: ")
    if guess in word:
        if letter_word.count(guess) == 1:
            index_guess = word.index(guess)
            guid_answer[index_guess] = guess
        else:
            while guid_answer.count(guess) != letter_word.count(guess):
                for index, item in enumerate(letter_word):
                    if item == guess:
                        guid_answer[index] = item
                
    if guid_answer == letter_word:
        print("Congratulations, You won!")
        exit()
    print("".join(guid_answer))

print(f"The word was {word}")