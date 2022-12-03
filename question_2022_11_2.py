
class B(): # in second variant B(A0)
    x = 'I am B class'
    y = 'I exist only in B'
    xx = 'I am B class, really'

class A0():  # A0(object)
    x = 'I am A0 class'
    xx = 'I am A0 class! not B class'

class A(A0):
    x = 'I am A class, my father A0 class'


class C(A, B):
    z = "I am C class, my parents A class and B class "

c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am A class, my father A0 class
print(c.xx)  #I am A0 class! not B class, If second variant - must be: 'I am B class, really'

print(C.mro()) 
print(C.__mro__) 
print(b:=B)
print(b.xx)
