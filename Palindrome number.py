def is_palindrome(word):
    return  word == word[::-1]
word = input("Guess any word :")
print(is_palindrome(word))



def is_palindrome(number):
     reversed_number = number[::-1]
     if number == reversed_number:
         return True
     else:
        return False
    
number = input("Enter a number: ")
print(is_palindrome(number))