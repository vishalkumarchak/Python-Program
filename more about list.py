# generate lists with range function
# something more about pop() method
# index method
# pass list to a function


# generate lists with range function
# number = list(range(1,11)) 
# print(number)


# something more about pop() method
# number = list(range(1,11)) 
# print(number)
# number.pop()
# print(number)
# popped_item = number.pop()
# print(popped_item)


# num = [1,2,3,3,4,5,6,7,1,8,9,1]
# print(num.index(1, 9))

num1 = [1,2,3,4,5,6,7,8]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
num1.reverse()
print(negative_list(num1))








