# %%
# display class attributes and method
# dir(instance of class)


class Displaydemo:
    #name = 'abc'
    #age = '10'
    def read(self):
        name = input('Enter name of student')
        print(name)
        age = input('Enter age of student')
        print(age)


d2 = Displaydemo()  # object of class
d2.read()
# directiry in python !!!
dir(Displaydemo)
# %%
# constructor


class Box:
    width = 0
    height = 0
    depth = 0
    volume = 0

    def __init__(self):  # constuctor
        self.width = 5
        self.height = 5
        self.depth = 5
        print(self.width*self.height*self.depth)

    def vol(self):
        print('Width :', self.width)
        print('Height :', self.height)
        print('Depth :', self.depth)
        return self.width*self.height*self.depth


b1 = Box()
print('Volume of cube is = ', b1.vol())
