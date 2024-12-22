# fromkeys method

user = dict.fromkeys(('name', 'age', 'hight'), 'unknown') 
# user = dict.fromkeys(('name', 'age'), ['unknown',24]) 
# user = dict.fromkeys((range(1,10)), 'unknown')
print(user)


# get method 
d = {'name':'vivek', 'age':24}
print(d.get('name'))

# if "name" in d:
#     print("present")
# else:
#     print("not present")
if d.get("name"):
    print("present")
else:
    print("not present")
 # if none  ---->False    else ----->True


# clear method
# d.clear()
# print(d)

d1 = d.copy()
print(d1)


# equlity check karne keliye is use karte h
# print(d is d1)