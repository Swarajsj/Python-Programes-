# %%
# Find the area of the circle by class


class Circle:
    def Circle_area(self, radius):
        return 3.14*radius**2


ob2 = Circle()  # object of class
print(ob2.Circle_area(5))

# %%


class Rectangle1:
    def Area_rectangle(self, length, width):
        return length*width


ob3 = Rectangle1()  # object of class
print(ob3.Area_rectangle(5, 4))

# %%
# Self parameter withinstance variable


class Practice:
    x = 5

    def show(Self, x):
        print(x)
        x = 30
        print(x)
        print(x)


ob = Practice()  # object of class
ob.show(50)

# %%
# Self parameter with method


class Self_demo:
    def methode_a(Self):
        print('Now in method a')
        print('I am method a')

    def method_b(Self):
        print('In methode b calling methode a')
        Self.methode_a()  # calling methode a


a = Self_demo()  # object of class
a.method_b()  # calling method_b
