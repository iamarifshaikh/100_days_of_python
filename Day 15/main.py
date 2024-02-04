from menu import COFFEE, RESOURCE

profit = 0
isOn = True


def isResourceSufficient(orderIngredients):
    """Returns True when orders can be made,False if ingredients are insufficient"""
    isEnough = True
    for item in orderIngredients:
        if orderIngredients[item] >= RESOURCE[item]:
            print(f"{item} not enough!")
            isEnough = False
    return isEnough


def processPayment():
    """Return the total calculated from coins inserted."""
    print("Please insert the coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def isPaymentReceived(received, cost):
    """Return True when the payment received, or False if money is insufficient"""
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Here is $ {change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded!")
        return False


def makeCoffee(drinkName, requiredIngredients):
    """Deduct the required ingredient from the resources"""
    for item in requiredIngredients:
        RESOURCE[item] -= requiredIngredients[item]
    print(f"Here is your drink {drinkName} ☕")
    return True


while isOn:
    choice = input("What do you want?: ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {RESOURCE['water']}")
        print(f"Milk: {RESOURCE['milk']}")
        print(f"Coffee: {RESOURCE['coffee']}")
        print(f"Money: $ {profit}")
    else:
        if choice in COFFEE:
            drink = COFFEE[choice]
            if isResourceSufficient(drink["ingredients"]):
                payment = processPayment()
                if isPaymentReceived(payment, drink["cost"]):
                    makeCoffee(choice, drink["ingredients"])
            else:
                continue
        else:
            print("Invalid choice. Please select a valid drink.")
