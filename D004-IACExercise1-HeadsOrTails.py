import random

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
elif coin == 0:
    print("Tails")
else:
    print("")
