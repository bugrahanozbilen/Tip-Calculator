print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))

tip = input("How much tip would you like to give? 10,12, or 15?")

split = input("How many people to split the bill?")

check = (((int(tip) / 100) * float(bill)) + float(bill)) / int(split)

c = float(check)

print (f"Each person should pay ${c:.2f}")