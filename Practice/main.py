import csv

class Item:
    discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0,f"Price{price} is not greater than or equal to zero!"
        assert quantity >= 0,f"Price {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculateTotalPrice(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount

    @classmethod
    def instantiateFromCSV(cls):
        with open('data.csv','r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def isInteger(self):


    def __repr__(self):
        return  f"Item('{self.name}',{self.price},{self.quantity})"

