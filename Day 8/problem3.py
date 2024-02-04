alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' for encryption or 'decode' for decryption the message \n")
message = input("Type your message.\n").lower()
shift = int(input("How much you would like to shift?. \n"))

def encrypt(plainText, shiftAmount):
    cipherText = ""
    for letter in plainText:
        position = alphabets.index(letter)
        newPosition = position + shiftAmount
        encryptedText = alphabets[newPosition]
        cipherText += encryptedText
    print(f'The Encrypted Text for {plainText} is {cipherText}')

def decrypt(cipherText, shiftAmount):
  plainText = ""
  for letter in cipherText:
    position = alphabets.index(letter)
    newPosition = position -shiftAmount
    plainText += alphabets[newPosition]
  print(f"Here is the decryped text: {plainText}")

if direction == "encode":
  encrypt(plainText = message, shiftAmount = shift)
elif direction == "decode":
  decrypt(cipherText = message, shiftAmount = shift)