# %%
# accessibility
# private and public attributes


class Person:
    def __init__(self):  # construtor
        self.name = 'Swaraj'  # public attributes
        self.__bankaccno = 10101  # private attributes

    def Display(self):
        print('Name is :', self.name)
        print('Bank account no. :', self.__bankaccno)


p = Person()  # object of class
print(p.name)
p.Display()
print(p.__bankaccno)
# print(p.Person__bankaccno)
# p.Display

# %%
# passing an object as parameter to amethod


class test:
    a = 0
    b = 0

    def __init__(self, x, y):  # constructor
        self.a = x
        self.b = y

    def equal(self, abc):
        if abc.a == self.a and abc.b == self.b:
            return True
        else:
            False


obj1 = test(10, 20)
obj2 = test(10, 20)
obj3 = test(12, 90)
print('Obj1 == Obj2', obj1.equal(obj2))
print('Obj1 == Obj3', obj1.equal(obj3))
