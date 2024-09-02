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
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: \n"))

computer_choice = random.randint(0, 2)

options = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
    print("Enter a valid number please.")
else:
    print(f"You chose: \n{options[user_choice]}")
    print(f"Computer chose: \n{options[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
