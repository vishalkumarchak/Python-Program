# winning_number = 47
# guess =1
# number = int(input("guess a number b/w 1 to 100 :"))
# game_over = False

# while not game_over:
#     if  number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times ")
#         game_over = True
    
#     else:
#         if number < winning_number:
#             print("too low")
#             guess +=1
#             number = int(input("guess gain:"))
#         else:
#             print("too high")
#             guess +=1
#             number = int(input("guess gain:"))


# DRY principle of codding( means code ko kam karna)
# import random --->in built function hai
import random
winning_number = random.randint(1,100)
guess =1
number = int(input("guess a number b/w 1 to 100 :"))
game_over = False
print(winning_number)

while not game_over:
    if  number == winning_number:
        print(f"you win, and you guessed this number in {guess} times ")
        game_over = True
        
    else:
        if number < winning_number:
            print("too low")

        else:
            print("too high")
            
    guess +=1
    number = int(input("guess again:"))
