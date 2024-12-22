#user = ['vivek', 24, ['sole', 'gadar)'], ['awakening', 'fairy tale']]
# this list contains user name age fav movies fav tunes

# how to create dictionary
user1 = {'name':'vivek', 'age':24}
print(user1)


#second method to create dictionary
user = dict(name = 'vivek', age =24)
print(user)
print(type(user))

# how to access data from dictionary
print(user['name'])
print(user['age'])

#which  type of data dictinary can store
# Anything 
# numbers, strings, lists, ditonary

user_info = {
    'name' :'vivek',
    'age':24,
    'fav_movies' :['gadar', 'sole']
    }
print(user_info)

# how to add data to empty dictinary

user_info2 = {}
user_info2['name'] ='mohit'
user_info2['name2'] ='mohan'
print(user_info2)
