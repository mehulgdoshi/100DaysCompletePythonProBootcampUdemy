import os
os.system('cls||clear') #To clear the terminal screen
print("Welcome to the secret auction program.")
ans = "yes"
name = ""
bid = 0
auction = {}
while ans.lower() == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    ans = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if ans.lower() != "yes":
        break
    else:
        os.system('cls||clear') #To clear the terminal screen

highest_bid = 0
highest_bidder = ""
for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid = auction[bidder]
        highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


