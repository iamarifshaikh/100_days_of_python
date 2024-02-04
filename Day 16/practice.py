# To make our blueprint more desirable We can also do some validation so that the information can be obtained properly or as intend to be


class Item:
    discount = 0.8
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    
    def calculateTotalPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        # self.price = self.price * Item.discount
        self.price = self.price * self.discount

