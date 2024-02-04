from art import logo, vs
from data import data
import random
import os


# Function to clear the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Takes the account data and returns it in a printable and readable format
def formatData(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


# Check the answer
def checkAnswer(guess, aFollower, bFollower):
    if aFollower > bFollower:
        return guess == "a"
    else:
        return guess == "b"


# Display the art
print(logo)

score = 0
gameShouldContinue = True

accountTwo = random.choice(data)

while gameShouldContinue:
    # Generating a random account from the data
    accountOne = accountTwo
    accountTwo = random.choice(data)

    # In case both the accounts are the same, regenerate accountTwo also making account B becomes the account A
    while accountOne == accountTwo:
        accountTwo = random.choice(data)

    print(f"A: {formatData(accountOne)}")
    print("                                                                      ")
    print(vs)
    print("                                                                      ")
    print(f"B: {formatData(accountTwo)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    aFollower = accountOne["followers"]
    bFollower = accountTwo["followers"]
    isCorrect = checkAnswer(guess, aFollower, bFollower)

    clear()
    if isCorrect:
        score += 1
        print(f"You are right! Current Score: {score}.")
    else:
        gameShouldContinue = False
        print(f"Sorry! That's wrong. Final Score: {score}")
