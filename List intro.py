#list intro
# Data structure
#  ordered collection of items
# you can store anything in list int, float, string

number =[1,2,3,4,5,6] 
print(number[2])

words = ["word1","word2","word3"]
print(words[:2])

mixed = [1,2,3,4,"vivek", "parkhi", 3.5,None]
print(mixed[-1])

# mixed[2] = "two"
# mixed[0:] = "two"
mixed[3:] = ["one", "two", "three"]
print(mixed)