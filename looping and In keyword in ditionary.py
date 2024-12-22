# in keyword and iterations in dictonary 

user_info = {
    'name' :'vivek',
    'age':24,
    'fav_movies' :['gadar', 'sole']
    }
print(user_info)


# # check if key exist in dictionary
# if 'name' in user_info:
#   print('present')
# else:
#   print('not present')


# check if values exist in dictionary
# if 'vivek' in user_info.values():    #use for values() method
#   print('present')
# else:
#   print('not present')


# Loops in dictionaries

# for i in  user_info:
#   print(i)

# for i in user_info.values():
#   print(i)

# values method
# user_info2 =user_info.values()
# print(user_info2)
# print(type(user_info2))

# for i in user_info:
#     print(user_info[i])

# user_info_keys =user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# items method
# user_items =user_info.items()
# print(user_items)

for i,j in user_info.items():
    print(f'keys are {i} and values are {j}')


