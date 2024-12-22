# Python program to find the
# maximum of two numbers

def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = input("Enter the first number : ")
b = input("Enter the second number : ")
print(maximum(a, b))
