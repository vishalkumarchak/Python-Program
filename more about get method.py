user = dict(name='vivek', age = 24)
# print(user.get('age'))

# None ki jagah kuchh bhi print kara sakte h
# print(user.get('fruits', "not found"))







user_info =  {'ask': 'vinod', "zone":{"month" :24, "day":{1:"mon", 2:"tue", 3:"wed", 4:"thur", 5:"fri", 6:"sat", 7:"sun" } }}

# user_info2 = 
print(user_info.get("ask"), end=", ")
print(user_info.get("month",24), end=", ")
print(user_info.get(4,"thur"))