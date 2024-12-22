# show Ticket pricing

age = int(input("Enter age :"))

if age==0:
    print("you can't watch")
elif age>0 and age <=3:
    print("Ticket price : Free")

elif age>3 and age<=10:
     print("Ticket price : 150")

elif age>10 and age<=60:
    print("Ticket price : 250")

else:
    print("Ticket price : 200")