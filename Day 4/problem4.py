import random

rock = '''
      _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock,paper,scissor]

user_choice = int(input("what do you choose? For Rock type 0, for Paper type 1, for Scissor type 2. \n"))

if user_choice >= 3 or user_choice < 0 :
 print("Your input is invalid")

else :
 print(hand[user_choice])

 bot_choice = random.randint(0,2)

 print("Computer Choice:")
 print(hand[bot_choice])

 if user_choice == 0 and bot_choice == 2:
   print('You win')
 elif user_choice == 2 and bot_choice == 1:
   print("You win")
 elif user_choice == bot_choice:
    print('Draw!')
 elif user_choice == 2 and bot_choice == 0:
   print("You lose")
 elif bot_choice > user_choice:
   print("You lose")
 elif user_choice > bot_choice:
   print("You win")