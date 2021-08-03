from menu import Menu
from coffee_maker import CoffeeMaker
from cash_register import CashRegister

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = CashRegister()


on = True

while on:
    options = menu.get_items()
    choice = input(f"What coffee interests you? ({options}): ")
    if choice == "off":
        on = False
    elif choice.isdigit():
        print("Sorry, that is not an option.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
