# Using a Set
def unique_elements(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5]
unique = unique_elements(arr)
print(unique)



# Using a Dictionary to Count Occurrences
def unique_elements(arr):
    counts = {}
    for item in arr:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return [item for item in counts if counts[item] == 1]

arr = [1, 2, 2, 3, 4, 4, 5]
unique = unique_elements(arr)
print(unique)
