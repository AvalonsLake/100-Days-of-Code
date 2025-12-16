from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    user_choice = input(f"What would you like? {menu.get_items()} ")
    if user_choice in menu.get_items():
        drink = menu.find_drink(user_choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            print(f"We can make you a {drink.name}! It only costs ${drink.cost}")
            make_drink = input(f"Would you like a {drink.name}? Y/N ").lower()
            if make_drink == "y":
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)

            elif make_drink == "n":
                print("\n" * 30)
        else:
            print("Maybe you'd like something else to drink!")

    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Shutting down, have a great day!!")
        on = False
    else:
         print("I'm sorry, I don't understand. please enter a registered command")

