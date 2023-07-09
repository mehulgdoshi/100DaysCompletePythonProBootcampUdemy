# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

if int(two_digit_number) < 10:
    two_digit_number = int(two_digit_number) * 10

number = str(two_digit_number)
total = int(number[0]) + int(number[1])
print(total)


