# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of squares from 1 to 10

# list create karne ka simple method----->
# square = []
# for i in range(1,11):
#     square. append(i**2)
# print(square)

# comprehension method------>
# square2 = [i**2 for i in range(1,11)]
# print(square2)


negative = []
for i in range(1,11):
 negative.append(-i)
print(negative)

new_negative = [-i for i in range(1,11)]
print(new_negative)
 

name = ['Harshit', 'Mohit', 'Rohit', 'Vivek']
new_list = []
for names in name:
  new_list.append(names[0])
print(new_list)


name2 = ['Harshit', 'Mohit', 'Rohit', 'Vivek']
new_list2 = [i[0] for i in name]
print(new_list2)

