"""
str = "Harry is a good boy"
print(len(str))
print(str[:])
print(str[::])
print(str[-4:-2])
print(str[::-1])      #string's  Reverce

print(str.isalnum())

print(str.isalpha())

print(str.endswith("boy"))

print(str.count("y"))

print(str.capitalize())
print(str.find("is"))

print(str.lower())

print(str.upper())

print(str.replace("is", "are"))
print(str.replace("Harry", "Mohan and Sohan"))

#format string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

age = 23
str = "my name is vivek, I am {}"
print(str.format(age))


first_name = "vivek"
last_name = "chak"
print(first_name +" "+last_name) #string ko add karna 

age = input("What is your age : ")
print("your age is :" + age )
"""
name = input("Enter your name : ")
print(name[::-1])
