import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
lives = 6
placeholder = ''

for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
correct_letter = []
game_over = False

while not game_over:
    user_guess = input("Enter your guess ").lower()
    display = ""
    if user_guess in chosen_word:
        print(f"Your guess is correct and you have {lives} lives")

    for letter in chosen_word:
        if  user_guess == letter:
            display += letter
            correct_letter.append(user_guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("You win the game !!")
        game_over = True

    elif user_guess not  in chosen_word:
        lives -= 1
        print(f"Your Lost a chance and you have {lives} lives")
        if lives == 0:
            print("You lose")
            game_over = True
    print(stages[lives])