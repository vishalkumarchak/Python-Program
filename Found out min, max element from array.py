def find_min_max(arr):
    if not arr:
        return None, None
    
    min_element = arr[0]
    max_element = arr[0]
    
    for num in arr[1:]:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num
    
    return min_element, max_element

array = input("Enter the value: ")
min_element, max_element = find_min_max(array)
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")  
