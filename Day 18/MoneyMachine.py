class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0
        self.moneyReceived = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def processPayemnt(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.moneyReceived += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.moneyReceived

    def makePayment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.processPayemnt()
        if self.moneyReceived >= cost:
            change = round(self.moneyReceived - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.moneyReceived = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.moneyReceived = 0
            return False
