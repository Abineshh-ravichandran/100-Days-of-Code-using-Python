print(
    ''''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."|` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
******************************************************************************* '''
)
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure ")
choice = input("Do you want to move left L or right R? ")
if choice == 'L':
    print("You have came near a lake .\nThere is a Island in the middle of the lake")
    next_choice = input("Do you want to swim  S or wait W? ")
    if next_choice == "W":
        print("You arrived at the Island.\n The Island has three doors with differnt colours ")
        door = input("Which door do you want to enter in? Red R, or Blue B or Yellow Y ")
        if door == "b" or "B":
            print("Oops!! Eaten by beasts. Game over.")
        elif door == "r" or "R":
            print("Oops !! Burned by fire. Game Over ")
        elif door == 'y' or "Y":
            print("Hurray !! You Win !")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game over ")
else:
    print("Fall into a hole. Game Over")
