# In day 7 I'll create a hangman game where the user need to guess the alphabet and will have 6 lives each lives will be deduct on wrong guess

import random
from art import logo, stages
from words import words

# TODO-1: - Update the word list to use the 'words' from words.py

choose = random.choice(words)
length = len(choose)

endOfGame = False
lives = 6

# TODO-3: - Import the logo from art.py and print it at the start of the game.
print(logo)

# Testing code
# print(f'Pssst, the solution is {choose}.')

# Create blanks
display = []
for _ in range(length):
    display += "_"

while not endOfGame:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(length):
        letter = choose[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in choose:
        # TODO-5: - If the letter is not in the choose, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word.")

        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        endOfGame = True
        print("You win.")

    # TODO-2: - Import the stages from art.py and make this error go away.
    print(stages[lives])
