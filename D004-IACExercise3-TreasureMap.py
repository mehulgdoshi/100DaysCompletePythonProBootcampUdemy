# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
if int(position[0]) < 1 or int(position[0]) > 3:
    print(f"{position} position is not valid")
elif int(position[1]) < 1 or int(position[1]) > 3:
    print(f"{position} position is not valid")
else:
    map[int(position[1]) - 1][int(position[0]) - 1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

