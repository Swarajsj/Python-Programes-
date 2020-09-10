# %%
# destructor method


class demo:
    def __init__(self):
        print('Welcome')

    def __del__(self):
        print("Destructor executed sucessfully !!")


ob1 = demo()
ob2 = ob1
ob3 = ob1
print('Id of ob1 =', id(ob1))
print('Id of ob2 =', id(ob2))
print('Id of ob3 =', id(ob3))
del ob3
del ob2
del ob1
print('Id of ob1 =', id(ob1))
print('Id of ob2 =', id(ob2))
print('Id of ob3 =', id(ob3))

# %%
# destructor is called only onces


class demo:
    def __init__(self):
        print('Welcome')

    def __del__(self):
        print("Destructor executed sucessfully !!")


ob1 = demo()
ob2 = ob1
ob3 = ob1
print('Id of ob1 =', id(ob1))
print('Id of ob2 =', id(ob2))
print('Id of ob3 =', id(ob3))
#del ob3
del ob2
del ob1

# %%
# class member


class a:
    pass


class b:
    pass


class c:
    pass


ob1 = a()
ob2 = b()
ob3 = c()
isinstance(ob1, a)
# isinstance(ob2,b)
# isinstance(ob3,c)

# %%
# method overloading


class overload:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)


o1 = overload()
o1.add(100, 200, 300)
# o1.add(100,200)
