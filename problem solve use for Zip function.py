# l1 = [1,2,3]
# l2 = [4,5,6]
# def avg_finder(l1, l2):
#     average =[] 
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg_finder([1,2,3],[4,5,6]))

def avg_finder(*args):
    average =[] 
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(avg_finder([1,2,3],[4,5,6],[7,8,9]))


avg_finder2 = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder([1,2,3],[4,5,6],[7,8,12]))

    