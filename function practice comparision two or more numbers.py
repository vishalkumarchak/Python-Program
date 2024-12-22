# Use for if-else statement
def number(a,b):
    if a>b:
        return a
    else:
        return b

a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
greater = number(a,b)
print(f"{greater} is a greater")



# USe for Nested if-else
def number(a,b,c):
    if a>b>c:
        return a
    else:
        if b>c:
            return b
        return c

a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
c =int(input("Enter third number: "))

greaterz = number(a,b,c)
print(f"{greater} is a greater")


# Use for if-elif-else statement 
def number(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
c =int(input("Enter third number: "))

bigger = number(a,b,c)
print(f"{bigger} is a greater")

