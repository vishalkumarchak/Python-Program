# fibonacci series:- The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence typically looks like this:
# 0  1  1  2  3  5  8  13  21  34

def fibonacci_seq(n):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if n==1 :
        print(a,end =",")
    elif n==2:
     print(a,b, end=",")
    else :
        print(a,b, end=",")
        for i in range(n-2):
            c = a + b   
            a = b
            b = c
            print(b, end=",")
x = int(input("Enter your number: "))
fibonacci_seq(x)