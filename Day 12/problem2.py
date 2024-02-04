from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guessAnswer(guess, answer, turns):
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You Got It! The answer is {answer}")


def setDifficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def startGame():
    print("Welcome to the number guessing game")

    print(
        "Let's start I'm thinking of a number between 1 to 100.  You have to guess the number"
    )

    answer = randint(1, 100)

    turns = setDifficulty()

    guess = 0

    while guess != answer:
        guess = int(input("Guess the number: "))

        print(f"You have {turns} attempts remaining to guess the number.")

        turns = guessAnswer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess and you lose")
            return
        elif guess != answer:
            print("Try again")


startGame()
