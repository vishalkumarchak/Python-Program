# we use enumerate function with for loop to track position of our
#item is iterable


# how we can do this without enumerate function
name=('vivek', 'vishal', 'mohit')
# pos = 0
# for char in name:
#     print (f'{pos} : {char}')
#     pos +=1



# with numerate function
for pos, char in enumerate(name):
     print (f'{pos} : {char}') 
