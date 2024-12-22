# i=0
# while i<=10
#    print("vivek parkhi")
#    i +=1

# for loop with range function
# for i in range(11):
    # print(f"vivek parkhi {i}")

# Sum from 1 to 10(any number)
# 1+2+3+4+......+10

"""number = input("Enter the number :")
number = int(number)
total = 0
for i in range(1,number+1):
  total += i
print(total)"""

# ask user a number like ---->1356 
#calculate sum of digit

total = 0
num = input("Enter the number :")
for i in range(0,len(num)):
    total = total+int(num[i])
print(total)
