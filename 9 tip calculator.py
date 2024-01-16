print("Welcome to the tip calculator.")

# total bill
bill = int(input("your is tour total bill : "))
#for tip
tip_percent = int(input("What percentage tip would you like to give? 10, 12, 15 "))
seprated = int(input("how many people to split the bill? "))

# code for calculating
total_bill = bill + (bill*tip_percent)/100

print(f"each person should pay: {total_bill/seprated} ")