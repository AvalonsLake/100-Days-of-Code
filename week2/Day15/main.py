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
}
profit = 0

def check_resource(drink, resevoir):
    if drink["cost"] == 1.5:
        if drink["ingredients"]["water"] > resevoir["water"]:
            print("We're sorry, there's not enough water to make your drink!")
            make_coffe(MENU, resources)
        elif drink["ingredients"]["coffee"] > resevoir["coffee"]:
            print("We're sorry, there's not enough coffee to make your drink!")
            make_coffe(MENU, resources)

    else:
        if drink["ingredients"]["water"] > resevoir["water"]:
            print("We're sorry, there's not enough water to make your drink!")
            make_coffe(MENU, resources)
        elif drink["ingredients"]["milk"] > resevoir["milk"]:
            print("We're sorry, there's not enough milk to make your drink!")
            make_coffe(MENU, resources)
        elif drink["ingredients"]["coffee"] > resevoir["coffee"]:
            print("We're sorry, there's not enough coffee to make your drink!")
            make_coffe(MENU, resources)

def transaction(price):
    global profit
    print("please insert coins")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    sum = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    if price > sum:
        print("Sorry, that's not enough money. You've been refunded!")
    else:
        profit += price
        sum -= price
        print(f"Thank you for your business! Your change is ${round(sum, 2)}")

def update_resources(drink, resevoir):
    if drink["cost"] == 1.5:
        resevoir["water"] -= drink["ingredients"]["water"]
        resevoir["coffee"] -= drink["ingredients"]["coffee"]
    else:
        resevoir["water"] -= drink["ingredients"]["water"]
        resevoir["milk"] -= drink["ingredients"]["milk"]
        resevoir["coffee"] -= drink["ingredients"]["coffee"]


def make_coffe(items, resources):
    on = True
    while on:
        user_drink = input("What would you like? (espresso, latte, cappuccino): ").lower()
        if user_drink == "espresso":
            print("You chose espresso")
            check_resource(items["espresso"], resources)
            transaction(items["espresso"]["cost"])
            update_resources(items["espresso"], resources)
            print(f"Here's your {user_drink}. Enjoy!")

        elif user_drink == "latte":
            print("You chose latte")
            check_resource(items["latte"], resources)
            transaction(items["latte"]["cost"])
            update_resources(items["latte"], resources)
            print(f"Here's your {user_drink}. Enjoy!")

        elif user_drink == "cappuccino":
            print("You chose cappuccino")
            check_resource(items["cappuccino"], resources)
            transaction(items["cappuccino"]["cost"])
            update_resources(items["cappuccino"], resources)
            print(f"Here's your {user_drink}. Enjoy!")

        elif user_drink == "off":
            print("shutting down, have a good day!")
            return
        elif user_drink == "report":
            print(f"water: {resources['water']}\n "
                  f"milk: {resources['milk']}\n "
                  f"coffee: {resources['coffee']}\n"
                  f"Profit: ${profit}")
        else:
            print("I'm sorry, I didn't understand that. Please enter a registered command")


make_coffe(MENU, resources)