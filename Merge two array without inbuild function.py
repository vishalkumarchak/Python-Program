def merge_arrays(arr1, arr2):
    merged_array = []
    
    for element in arr1:
        merged_array.append(element)
        
    for element in arr2:
        merged_array.append(element)
        
    return merged_array

arr1 = input("Enter the value of array1: ")
arr2 = input("Enter the value of array2: ")
result = merge_arrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
