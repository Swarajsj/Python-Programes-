# %%
# Operator overloading


class over:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        print('The value of ob1 :', self.x)
        print('The value of ob2 :', other.x)
        print('The addition of two objects is :', end=' ')
        return (self.x+other.x)


ob1 = over(20)
ob2 = over(30)
ob3 = ob1 + ob2
print(ob3)

# %%
# operator overloading comparing two objects


class demo:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        print('Value of ob1 :', self.x)
        print('Value of ob2 :', other.x)
        print('Ob1 < ob2 :', end=' ')
        return self.x < other.x

    def __gt__(self, other):
        print('Ob1 > ob2 :', end=' ')
        return self.x > other.x

    def __le__(self, other):
        print('Ob1 <= ob2 :', end=' ')
        return self.x <= other.x


ob1 = demo(20)
ob2 = demo(30)
print(ob1 < ob2)
print(ob1 > ob2)
print(ob1 <= ob2)
