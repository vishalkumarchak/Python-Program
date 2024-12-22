# multiple inheritence 
class A:
    def class_a_method(self):
        return "I\'m just a class A method"
    def hello(self):
        return "hello from class A"

class B:
    def class_b_method(self):
        return "I\'m just a class B method"
    def hello(self):
        return "hello from class B"

class C(A,B):
    pass

class_c = C()
print(class_c.class_a_method())
print(class_c.class_b_method())
print(class_c.hello())
# print(help(C))

print(C.mro())