# check two condition as a same time 
# and, or 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if  age >=21 and (name [0]=='a' or name[0]=='A'):
    print("condition  true")
else:
    print("condition  false")

# num1= int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 >15 and  num2 >30 :
    # print("condition  true")
# else:
    # print("condition  false")    

num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 >15 or num2 >30 :
    print("condition  true")
else:
    print("condition  false")