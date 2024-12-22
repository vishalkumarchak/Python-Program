# some more methods to add data  in our list---->





# insert method
# fruites1 = ["apple", "mango", "grapes"]
# fruites1.insert(2, "orange")
# print(fruites1)


# # how to join (concatenate) two list
# fruites1 = ["apple", "mango", "grapes"]
# fruites2 =  ["orange","papaya"]
# fruites = fruites1 + fruites2
# print(fruites) 

# insert method
fruites1 = ["apple", "mango", "grapes"]
fruites2 =  ["orange","papaya"]
fruites1.extend(fruites2)
print(fruites1)




# difference  between append and extend method

# fruites1 = ["apple", "mango", "grapes"]
# fruites2 =  ["orange","papaya"]

# fruites1.extend(fruites2)
# print(fruites1)


fruites1.append(fruites2)
print(fruites1)

