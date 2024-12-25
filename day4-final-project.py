rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

Scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

import random

user = int(input("Lets play! so press 0 for Rock, press 1 for Paper or press 2 for Scissors \n"))

computer_number = random.randint(0,2)

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(Scissors)
else:
    print("Please pick the right number losser!")


print("Computer:")

if computer_number == 0:
    print(rock)
if computer_number == 1:
    print(paper)
if computer_number == 2:
    print(Scissors)

if user == computer_number:
    print("Its draw")
elif user == 2 and computer_number == 0 : 
    print("You Loose!")
elif user == 0 and computer_number == 2 : 
    print("You win!")
elif user == 1 and computer_number == 0 : 
    print("You win!")
elif user == 0 and computer_number == 1 : 
    print("You Loose!")
elif user == 2 and computer_number == 1 : 
    print("You win!")
elif user == 1 and computer_number == 2 : 
    print("You Loose!")

