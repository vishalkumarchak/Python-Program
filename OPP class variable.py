# class variable
# circle
# area
# circum
class Circle :
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    
    def calc_circumfrence(self):
        return 2*Circle.pi*self.radius
c = Circle (4)
c1 = Circle(5)

print(c.calc_circumfrence())
print(c1.calc_circumfrence())


# next example

class Laptop:
    discount_percent = 5
    def __init__(self, brand, modal, price):
        self.brand =brand
        self.modal = modal
        self.price = price
        self.laptop_name = brand +' '+ modal
    
    def apply_discount(self):
        offer_price=self.price *(Laptop.discount_percent/100)
        return self.price -offer_price
    
l1 =Laptop('DELL','latitude E7450', 75000)
l2 =Laptop('HP','hE7450', 63000)
print(l1.laptop_name)
# Laptop.discount_percent =0
print(l2.apply_discount())
        
