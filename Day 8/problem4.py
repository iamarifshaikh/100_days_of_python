logo = '''

   _____
  / ____|
 | |     __ _  ___  ___  ___ _ __
 | |    / _` |/ _ \/ __|/ _ \ '__|
 | |___| (_| |  __/\__ \  __/ |
  \_____\__,_|\___||___/\___|_|
  / ____(_)     | |
 | |     _ _ __ | |__   ___ _ __
 | |    | | '_ \| '_ \ / _ \ '__|
 | |____| | |_) | | | |  __/ |
  \_____|_| .__/|_| |_|\___|_|
          | |
          |_|
'''
print(logo)


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(initialMessage, shiftAmount, encryptOrDecrypt):
  finalMessage = ""
  if encryptOrDecrypt == "DECRYPT":
    shiftAmount *= -1
  for char in initialMessage:
    if char in alphabets:
     position = alphabets.index(char)
     newPosition = position + shiftAmount
     finalMessage += alphabets[newPosition]
    else:
      finalMessage += char
  print(f"Here's the {encryptOrDecrypt} result: {finalMessage}")

shouldContinue = True

while shouldContinue:
 direction = input("Type 'ENCRYPT' for encryption or 'DECRYPT' for decryption the message \n")

 message = input("Type your message.\n").lower()

 shift = int(input("How much you would like to shift?. \n"))

 shift = shift % 26

 ceaser(initialMessage = message, shiftAmount = shift, encryptOrDecrypt = direction)

 restart = input("Should you want to continue or end if want to then type YES else NO: ")

 if restart == "NO":
    shouldContinue = False
    print("Thank you for using cryptography app")