"""
age = int(input("Enter your age :"))
if age >=20 :
    print("you can play :")
else :
    print("you can't play")
    """

# Nested if-else
winning_number = 35
user_input = input("guess a number b/w 1 to 100 :" )
user_input = int(user_input)
if user_input == winning_number :
    print("you win!!")
else :
    if user_input < winning_number:
        print("Too low")
    else:
        print("Too high")