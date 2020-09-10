# %%
# Inheritance
# Single inheritance (X -> Y)


class a:  # parent class
    print('Hello i am in base class :)')


class b(a):  # child class
    print('I am in drived class (: ')


obj = b()  # object of class

# %%
# Single inheritance (X -> Y)


class parent:
    def setcordinate(self, x, y):
        self.x = x
        self.y = y


class child(parent):
    def draw(self):
        print('Locate point x1 :', self.x, 'on x axis')
        print('Locate point y1 :', self.y, 'on y axis')


c = child()
c.setcordinate(10, 20)
c.draw()

# %%
# Multilevel inheritance (X -> Y -> Z)


class a:
    name = ''
    age = 0


class b(a):
    height = ''


class c(b):
    weight = ''

    def read(self):
        self.name = input("Enter name :)")
        self.age = input('Enter age :)')
        self.height = input("Enter height :)")
        self.weight = input('Enter weight :)')

    def display(self):
        print('Enter the following details (:')
        print('Name :)', self.name)
        print('Age :)', self.age)
        print('Height :)', self.height)
        print('weight :)', self.weight)


c1 = c()
c1.read()
c1.display()
