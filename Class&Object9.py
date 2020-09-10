# %%
# Multiple inheritance


class a:
    a1 = 0


class b:
    b1 = 0


class c (a, b):
    c1 = 0

    def read(self):
        print('Enter the following values')
        self.a1 = input("Enter value of a1 :")
        self.b1 = input("Enter value of b1 :")
        self.c1 = input("Enter value of c1 :")

    def display(self):
        print('Enter values are as follows')
        print("a1 :", self.a1)
        print("b1 :", self.b1)
        print("c1 :", self.c1)


ob1 = c()
ob1.read()
ob1.display()

# %%
# method overriding


class a:
    i = 0

    def dis(self):
        print("I am in super class ")


class b(a):
    i = 0

    def dis(self):
        print('I am in sub class')


d1 = b()
d1.dis()

# to overcome method overriding to have to use super class()


class a:  # base class
    i = 0

    def dis(self):
        print("I am in super class ")


class b(a):  # super class
    i = 0

    def dis(self):
        print('I am in sub class')
        super().dis()  # call display of base class


d1 = b()
d1.dis()
