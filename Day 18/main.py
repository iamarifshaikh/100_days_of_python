from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine
from Menu import Menu, MenuItem

machine = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

isOn = True

maker.report()
machine.report()

while isOn:
    options = menu.getItems()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        maker.report()
        machine.report()
    else:
        drink = menu.findDrink(choice)
        if maker.isResourceSufficient(drink) and machine.makePayment(drink.cost):
            maker.makeCoffee(drink)
