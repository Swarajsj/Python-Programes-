# Program to find grtr thn two numbers


def greater(x, y):
    if x > y:
        print('X is greater')
    else:
        print('Y is greater')


a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
greater(a, b)


# Practice

i = 0
for x in range(1, 3):
    j = 0
    for y in range(-2, 0):
        j = j+y
        i = i+j
print(i)
