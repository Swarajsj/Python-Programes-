# %%
class Demo:
    pass


D1 = Demo()  # object of the class demo
D1

# %%


class Myfirstprog:
    print('Welcome to object oriented programming')


C = Myfirstprog()  # object of the class MyfirstProg
C

# %%
# Adding attributes to a class


class Rectangle:
    length = 0  # attribute length
    width = 0  # attribute width


R1 = Rectangle()  # object of class Rectangle
print(Rectangle.length)  # acsess attributes length
print(R1.width)  # acsess attributes width

# %%
# Assigning value to an attribute


class Rectangle:
    length = int(input())
    width = int(input())


R2 = Rectangle()
R2.length = int(input())
R2.width = int(input())
print(R2.length*R2.width)

# %%
# Adding methode to a class
# Self parameter


class Methoddemo:
    def Display_message(Self):
        print('Welcome to methods in a class')


ob1 = Methoddemo()  # object of class
ob1.Display_message()  # calling method
