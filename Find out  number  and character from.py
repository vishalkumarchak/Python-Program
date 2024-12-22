def find_numbers_and_characters(text):
    numbers = []
    characters = []
    
    for char in text:
        if char.isdigit():
            numbers.append(char)
        elif char.isalpha():
            characters.append(char)

    
    return numbers, characters

# Example usage
text = input("Enter the string: ")
numbers, characters = find_numbers_and_characters(text)
print("Numbers:", numbers)
print("Characters:", characters)

