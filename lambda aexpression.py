
def add(a,b):
     return a+b
print(add(3,4))

add2 = lambda a,b :a+b
print(add(3,4)) 

multiply = lambda a,b: a*b
print(multiply(3,4)) 

# def is_even(a):
#      if a%2==0: 
#           return True
#      return False
# print(is_even(3))


def is_even(a):
     return a%2==0
print(is_even(6))

iseven =lambda a : a%2 ==0
print(iseven(3))


func = lambda s : True if len(s)>5 else False
print(func("vivekparkhi"))
        