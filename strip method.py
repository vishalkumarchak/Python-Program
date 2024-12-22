#strip() method
name = "    vishal  chak    "
print(name)
print(name.lstrip())   #  left space remove use for lstrip() method
print(name.rstrip())   #  right space remove use for rstrip() method
print(name.strip())   #   left and righ space remove use for strip() method
print(name.replace(" ",""))  # all space remove use for .replace() method

#replace() method
mystr = "she is a beautiful and she is a good dancer" 
# print(mystr.replace("is","was"))

# find() method 
print(mystr.find("good"))



# center() method
name = "vivek"
print(name.center(9,"*"))

# name = input("Enter your name: ")
# print(name.center(len(name)+8, "*"))

string ="Vivekchak"
mystr = string.replace("V","v")
print(mystr)