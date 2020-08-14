# %%
# Returing multiple values


def plus(num1, num2):
    return num1+num2, num1-num2


plus(10, 5)
# %%
# Assign returned multiple value to variable(s)


def demo(num1):
    return num1**2, num1**3


square, cube = demo(8)
print(square, cube)
# %%
# calculate the factorial by recursion


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


fact(5)

# %%
# Practice


def fun(n):
    if n > 100:
        return n-5
    return fun(fun(n+11))


fun(45)

# %%
def say(message,times =1):
    print(message*times)
say('hello')
say('world',5)