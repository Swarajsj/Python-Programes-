# Program to find the prime number or not

x = int(input("Enterthe values :"))
y = x//2


def prime(x, y):
    c = 0
    for i in range(2, y+1, 1):
        if x % i == 0:
            c += 1
    if c == 0:
        print("Prime")
    else:
        print("Not Prime")


prime(x, y)
