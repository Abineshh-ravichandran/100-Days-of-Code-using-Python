print("Welcome to the tip calculator! ")
total_amt = float(input("What was the total bill ? $ "))
tip = int(input("How much tip would you like to give? 10,12, or 15?  "))
split = int(input("How many people to split the bill? "))
tip_added = total_amt * (tip/100)
total_amt += tip_added
final_amt = total_amt/split
print(f"Each person should pay : ${round(final_amt,2)}")



