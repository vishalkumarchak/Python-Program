#Using an Iterative Approach
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Enter the number: "))
print(f"The factorial of {number} is {factorial_iterative(number)}")

#Using a Recursive Approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter the number: "))
print(f"The factorial of {number} is {factorial_recursive(number)}")



#Using the math Library
import math

number = int(input("Enter the number: "))
print(f"The factorial of {number} is {math.factorial(number)}")
