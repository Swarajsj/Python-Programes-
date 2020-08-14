# %%
# Paramemter with default agrument


def greet(name, msg='Welcome to function'):
    print("Hello", name, msg)


greet("Ishan")

# %%
# Program to print the area of circle by function


def areacricle(r):
    pi = 3.14
    area = pi*r*r
    print(area)


a = int(input("Enter value :"))
areacricle(a)
# %%
# Global and Local Variable
p = 20  # Global Var


def demo():
    q = 10  # Local Var
    print(q)
    print(p)


demo()
print(p)
