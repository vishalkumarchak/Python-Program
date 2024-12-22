# def is_armstrong_number(num):
#     num_str = str(num)
#     num_len = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
#     return sum_of_powers == num



num = str(int(input("Enter an Number: ")))
digit_sum = 0

for i in num:
    digit_sum += int(i)**len(num)
    
if int(num) == digit_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# number = int(input("Enter the Number: "))
# if is_armstrong_number(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")



# num = int(input("Enter a number: "))
# sum = 0

# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
