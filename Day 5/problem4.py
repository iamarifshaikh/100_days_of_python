import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Symbols = ['!', '"', '#', '$', '%', '&', "'",
           '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '|', '~']

print("Welcome to password generator")

askLetter = int(input("How many letter would you like in your password? \n"))

askNumber = int(input("How many numbers would you like?"))

askSymbol = int(input("How many symbols would you like?"))

passwordList = []

for char in range(1, askLetter + 1):
 passwordList.append(random.choice(Letters))

for char in range(1, askNumber + 1):
 passwordList += random.choice(Numbers)

for char in range(1, askSymbol + 1):
  passwordList += random.choice(Symbols)

random.shuffle(passwordList)
print(passwordList)

password = ""

for char in passwordList:
  password += char

print(f"Here is your password: {password}")