# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1.lower() + name2.lower()
count1 = 0
count2 = 0

count1 += combined_names.count('t')
count1 += combined_names.count('r')
count1 += combined_names.count('u')
count1 += combined_names.count('e')
count2 += combined_names.count('l')
count2 += combined_names.count('o')
count2 += combined_names.count('v')
count2 += combined_names.count('e')

num_str = str(count1) + str(count2)
num = int(num_str)

if num < 10 or num > 90:
    print(f"Your score is {num}, you go together like coke and mentos.")
elif num >= 40 and num <= 50:
    print(f"Your score is {num}, you are alright together.")
else:
    print(f"Your score is {num}.")