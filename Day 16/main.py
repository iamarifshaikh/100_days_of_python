# Class is a blueprint or a template that defines the structure and behavior of objects i.e. when the instance or an object will create they will use the attributes defined in a class and also the every object will  behave as it is defined in a class.

class Waiter:
# Attributes represent the characteristic, property or a particular type of data that is used to store the information related to object's state.    
    def __init__(self,name,age,isPresent):
        self.name = name
        self.age = age
        self.isPresent = isPresent
        
waiter1 = Waiter("Jain",23, False)
waiter2 = Waiter("Betty",19,True)

print(f"The age of a Jain is {waiter1.age}")

# While creating a class/template/blueprint we can also define the type of an attribute for type safety or while want to store the specific type of data.

class Item:
    def __init__(self, name: str, price: float):
        pass

# Not only can define the type but also can set the default value of a attribute as in some case we need to have default data or to intact the flow of a program.

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        pass 