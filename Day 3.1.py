print("Welcome to Python pizza Deliveries")
size = input("What size do you want ? S, M or L: ")
prpperoni =  input("Do you want pepperoni on  your pizza ? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == 'S':
    bill += 15
    if prpperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if prpperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'L':
    bill += 25
    if prpperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
else:
    print("Invalid Input !")
print(f"Your final bill is :{bill}")