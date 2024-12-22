#objective
# what is a class
# how to create an class
# what is  init method , constructor
# what are attributes, instance variable
# how to create our object
# __init__ method constructor h

class Person:
    def __init__(self, first_name, last_name, age):
        # instan variable
        self.newfirst_name = first_name
        self.newlast_name = last_name
        self.age =age
    
p1 = Person('vishal', 'chak', 23)
p2 = Person('vivek', 'parkhi', 24)
p3 = Person('arun', 'mugdal',26)

print(p1.newfirst_name)
print(p2.newfirst_name)
print(p3.newfirst_name)


#create a laptop class with attributes like brand name, modal name, price
# create two object/instance of your laptop class

class Laptop:
    def __init__(self, brand, modal, price):
        self.brand =brand
        self.modal = modal
        self.price = price
        self.laptop_name = brand +' '+ modal
    
    def apply_discount(self,num):
        offer_price=self.price *(num/100)
        return self.price -offer_price
    
l1 =Laptop('DELL','latitude E7450', 75000)
l2 =Laptop('HP','hE7450', 63000)
print(l1.laptop_name)


laptop1= Laptop('DELL','latitude E7450', 75000)
print(laptop1.apply_discount(5))

    