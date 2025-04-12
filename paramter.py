# Key Features:
# Constructor (__init__): Initializes the object with id, name, manufacturer, and price.

# String Representation (__str__): Makes it easier to print the object in a readable format.

class medicine:
    def __init__(self,id,name,manufacturer,price):
        self.id=id
        self.name=name
        self.manufacturer=manufacturer
        self.price=price 
        
    def __str__(self):
        return f"medicine id: {self.id}, medicine name: {self.name}, manufacturer: {self.manufacturer}, price: {self.price}"
