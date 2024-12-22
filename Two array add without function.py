array1 = [1, 2, 3]
array2 = [4, 5, 6]

if len(array1) != len(array2):
    print("Arrays must have the same length")
else:
    result = []

    for i in range(len(array1)):
        result.append(array1[i] + array2[i])

    print("Resultant array:", result)



    
# Define the two arrays of different lengths
array1 = [1, 2, 3]
array2 = [4, 5, 6, 7, 8]

max_length = max(len(array1), len(array2))

# Pad the shorter array with zeros
padded_array1 = array1 + [0] * (max_length - len(array1))
padded_array2 = array2 + [0] * (max_length - len(array2))

result = []

for i in range(max_length):
    result.append(padded_array1[i] + padded_array2[i])

print("Resultant array:", result)

