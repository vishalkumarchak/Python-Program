# make flexible function
# * operator
# * args
def total(a,b):
    return a+b
print(total(2,3))

def all_total(*args):
    total = 0
    for i in args:
        total += i   # total = total + i
    return total
    
print(all_total(1, 2, 3, 4))




# # args with normal parameter
# def multiply_nums(num, * args):
#     multiply = 1
#     print(num)
#     print(args)
#     for i in args:
#         multiply *= i     # multiply = multiply * i
#     return multiply
# print(multiply_nums(2,4,3,4))




def multiply_nums(* args):
    multiply = 1 
    print(args)   # ([2,3,4])
    for i in args:
        multiply *= i     
    return multiply
num = [2,3,4]
print(multiply_nums(*num))  # unpack ho jayega