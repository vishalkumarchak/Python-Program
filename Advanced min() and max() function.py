# number = [1,2,3,4,5,6]
# print(min(number))
# print(max(number))

# names = ['vivek', 'harshit', 'arun', 'mohan']
# print(max(names, key= lambda items: len(items)))

student1 = {
    'harshit': {'score' : 60, 'age': 24},
    'vishal': {'score' : 80, 'age': 26},
    'vivek': {'score' : 75, 'age': 25}
}

print(max(student1, key= lambda item: student1[item]['score']))

student2 = [
   {'name': 'harshit','score' : 95, 'age': 23 },
    {'name' :'vishal','score' : 85, 'age': 22},
    {'name':'vivek','score' : 70, 'age': 28}
]
print(max(student2, key= lambda item: item.get('score'))['name'])