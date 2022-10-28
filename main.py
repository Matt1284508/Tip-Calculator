###################################################
#### 100 DAYS OF CODE | Day 1 - Tip Calculator ####
###################################################


# Welcome the user
print("Welcome to the tip calculator!")

# Collect total bill amount
bill = input("What is the total bill? \n $") 

# Collect total percentage of tip
tip_percentage = input("What percentage of tip would you like to leave? \n")
tip_coverted = "1." + str(tip_percentage)

# Collect number of people splitting the bill
people = input("How many people will split the bill? \n")

# Calculate total bill w/ tip
bill_with_tip = float(bill) * float(tip_coverted)

# Split total bill among total people
per_person = bill_with_tip / int(people)

# Present bill per person
print(f"Each person should pay ${round(per_person, 2)}")