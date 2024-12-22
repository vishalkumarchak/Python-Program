# i = 3
# while i<=10:
#     print(f"hello world {i}")
#     i = i +1

# # Sum of numbers
# total = 0
# i = 1
# while i<=10:
#     total += i       # total = taotal + i
#     i += 1 
# print (total)


# any numbers digit sum
number = input("Enter a number: ")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)




name = input("Enter your name :")
temp_var= ""
i = 0
while i< len(name):
     if name[i] is not temp_var:
       temp_var += name[i] 
       print(f"{name[i]} : {temp_var.count(name[i])}")
     i += 1

    