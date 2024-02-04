give_me_names = input("tell me the name of your friends - ")

names = give_me_names.split(",")

nameLength = len(names)

makeChoice = random.randint(0, nameLength-1)

whomToPay = names[makeChoice]

print(whomToPay + " is gonna pay for meal")