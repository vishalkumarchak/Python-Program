#common methods to delete data from List

# pop() method
fruits =["apple", "mango", "grapes", "papaya","kiwi", "pear"]
fruits.pop(1)   # list se any index value remove kar sakte h 
print(fruits)


# delete operate bhi same work karta h--> del
fruits =["apple", "mango", "grapes", "papaya","kiwi", "pear"]
del fruits[1]
print(fruits)


# remove method ()
fruits =["apple", "mango", "grapes", "papaya","kiwi", "pear"]
fruits.remove("papaya")   
print(fruits)