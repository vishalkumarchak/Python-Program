# instance method
class Person:
    def __init__(self, first_name, last_name, age):
        # instan variable
        self.newfirst_name = first_name
        self.newlast_name = last_name
        self.age =age
    
    def full_name(self,name,a,b):
        c = a + b
        return f"{self.newfirst_name} {self.newlast_name}, {self.age},{name},{c}"
    
    def is_above_18(self):
        return self.age>18
    
p1 = Person('vishal', 'chak', 23)
p2 = Person('vivek', 'parkhi', 24)

print(p1.full_name("Ankit",3,4))
print(p2.full_name("Ankit",5,7))
print(p1.is_above_18())


