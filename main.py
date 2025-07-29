import random
import json
from tkinter import *

a = ['a', 'b', 'c']

words = json.loads(open('words.json').read())['words']

word = random.choice(words)

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Mistakes Left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You've found the word! It was {word}!")
else:
    print(f"You are out of guesses! The word was {word}!")
