# Program to print sum of the digit of a given number

num = int(input("Enter the number"))
sum = 0
r = 0
while num > 0:
    r = num % 10
    num = num // 10
    sum = sum + r
print(sum)
