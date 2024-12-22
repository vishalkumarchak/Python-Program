# add and delete data from dictionary
user_info = {
    'name' :'vivek',
    'age':24,
    'fav_movies' :['gadar', 'sole']
    } 
# print(user_info)

#how to add data
# user_info['fav_song'] = ['song1 , song2']
# print(user_info)

 
#pop method
# popped =user_info.pop('fav_movies')
# print(f'popped items is{popped}')  
# print(user_info)
# print(type(popped)) 

# popitem method
# popped_items = user_info.popitem()
# print(user_info)
# print(type(popped_items))



# update method 
more_info ={'name':'vivek parkhi', 'state':'Haryana', 'hobbies':['codding', 'reading', 'guitar']}
user_info.update(more_info)
print(user_info)
