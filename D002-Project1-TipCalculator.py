print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)

amount_per_person = (total_bill + tip_amount) / number_of_people

# To round the decimal place to two digits (append 0 in case only one digit)
amount_per_person = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${amount_per_person}")
