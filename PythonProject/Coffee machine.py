quarter_value = 0.25
dime_value = 0.10
nickle_value = 0.05
pennie_value = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Cannot make drink. Not enough {ingredient}.")
            return False
    return True

def transaction(inserted_coins, drink_cost):
    if inserted_coins < drink_cost:
        print("Sorry, not enough money. Money refunded.")
        return False
    change = round(inserted_coins - drink_cost, 2)
    print(f"Here is ${change} in change.")
    resources["money"] += drink_cost
    return True

action = True
while action:
    promot = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if promot in MENU:
        if check_resources(promot):
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            
            inserted_coins = (quarters * quarter_value) + (dimes * dime_value) + (nickles * nickle_value) + (pennies * pennie_value)
            drink_cost = MENU[promot]["cost"]
            
            if transaction(inserted_coins, drink_cost):
                print(f"Here is your {promot}.")
                # Deduct the required ingredients from the resources
                for ingredient, amount in MENU[promot]["ingredients"].items():
                    resources[ingredient] -= amount
        else:
            print("Cannot make your drink due to insufficient ingredients.")
    elif promot == "off":
        action = False
    elif promot == "report":
        print(resources) 
