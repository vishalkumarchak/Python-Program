fruits = ['mamgo', 'orange','apple']
#sort
fruits.sort()
print(fruits)


fruits =['mamgo', 'orange','apple']
print(sorted(fruits))


# Advanced  sorting
guitars =[
    {'modal':'yama f380', 'price':8400},
    
   {'modal':'faith napture', 'price':7000},
    
    {'modal':'faith apollo venus', 'price':6000},
    
    {'modal':'taylor t380', 'price':7500}
]
print(sorted(guitars,key=lambda item: item['price'], reverse=True))