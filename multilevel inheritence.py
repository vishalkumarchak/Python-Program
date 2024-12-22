# multilevel inheritence
# method resolution order
# method overriding
# isinstance()
# issubclass()

class Phone:   # base clss/parent class
    def __init__(self, brand, modal_name, price):
        self.brand = brand
        self.modal_name = modal_name
        self._price = max(price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}---")
    def full_name(self):
        return f"{self.brand} {self.modal_name}" 

class Smartphone(Phone): # derived class/child class
    def __init__(self, brand, modal_name, price, ram, internal_memory, rear_camera):
        super().__init__( brand, modal_name, price)
        self.ram =ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class New_smartphone(Smartphone):
    def __init__(self, brand, modal_name, price, ram, internal_memory, rear_camera,front_camera):
       super().__init__( brand, modal_name, price, ram, internal_memory, rear_camera)
       self.front_camera = front_camera

phone1 = Phone("Nokia","1100",1000)
smartphone =Smartphone("Redmi","9power", 12000, "6 GB","128 GB","48 MP")
new_smartphone =New_smartphone("Vivo","9 Pro", 12000, "6 GB","128 GB","48 MP", "8 MP")
print(phone1.full_name())
print(smartphone.full_name() + f" and price is {smartphone._price}")
print(new_smartphone.full_name() + f" and price is {smartphone._price}")
# isinstance()
print(isinstance(smartphone,Phone))
# print(help(Smartphone))

# issubclass()
print(issubclass(Phone,Smartphone))
print(issubclass(Smartphone, Phone))