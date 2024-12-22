# world counter
def world_counter(name):
    count ={}   
    for i in name:
     count[i]= name.count(i)
    return count
name = input("Enter any character :")
print(world_counter(name))