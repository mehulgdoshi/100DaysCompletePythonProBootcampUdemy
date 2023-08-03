from data import resources, profit, MENU


def print_report():
    """displays the resources that are available"""
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${'{:.2f}'.format(profit)}
    """)


def check_resources(user_prompt):
    """Check quantity available in the balance.
    Return True if sufficient quantity is available in the inventory, otherwise return False
    """
    if user_prompt == "latte" or user_prompt == "cappuccino":
        if MENU[user_prompt]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if MENU[user_prompt]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[user_prompt]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def process_coins():
    """"Accepting the coins and returning calculated total amount"""
    print("Please insert coins.")
    total_amount = int(input("How many quarters?: ")) * 0.25
    total_amount += int(input("How many dimes?: ")) * 0.1
    total_amount += int(input("How many nickles?: ")) * 0.05
    total_amount += int(input("How many pennies?: ")) * 0.01
    return total_amount


def make_coffee(user_prompt):
    """Making coffee and updating the resources inventory"""
    resources["water"] -= MENU[user_prompt]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_prompt]["ingredients"]["coffee"]
    if user_prompt == "latte" or user_prompt == "cappuccino":
        resources["milk"] -= MENU[user_prompt]["ingredients"]["milk"]
    print(f"Here is your {user_prompt}. Enjoy!")


def add_resources():
    """Adding quantities to the resources inventory"""
    resources["water"] += 300
    resources["coffee"] += 200
    resources["milk"] += 100


turn_off = False
while not turn_off:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        turn_off = True
    elif prompt == "report":
        print_report()
    elif prompt in ['espresso', 'latte', 'cappuccino']:
        resources_sufficient = check_resources(prompt)
        if not resources_sufficient:
            update_inventory = input("Add more quantity to the resource inventory? Type 'y' or 'n': ").lower()
            if update_inventory == 'y':
                add_resources()
            else:
                turn_off = True

        if not turn_off:
            print(f"The price of {prompt} is ${'{:.2f}'.format(MENU[prompt]['cost'])}")
            amount_paid = process_coins()

            if amount_paid < MENU[prompt]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += round(MENU[prompt]["cost"], 2)
                make_coffee(prompt)
                if amount_paid > MENU[prompt]["cost"]:
                    change = round(amount_paid - MENU[prompt]["cost"], 2)
                    print(f"Here is ${change} dollars in change.")