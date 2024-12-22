# set data type
# unordered collection off unique items

s = {1,2,3,2}
print(s)
l = [1,2,3,4,5,5,5,5,6,7,7,8] 
# remove duplicate
# s1 = list(set(l))
# print(s1)
 
# s.add(4)
# s.add(9)
# s.remove(1)
# s.discard(5) # discard method se set me se any element ko remove kar sakte h

# s.clear()
# s2 = s.copy()
# print(s2)


# in keyword in sets and for loop
s3 = {"a", "b", "c"}
# in keyword to check data present or not present
if 'a'in s3:
    print('data present')
else:
    print('data not present')

# for loop
for item in s3:
    print(item)


# Set math
# union
# intersection
s1 = {1,2,3,4}
s2 ={3,4,5,6}
union_set = s1|s2
print(union_set)
intersection_set = s1 & s2 
print(intersection_set)