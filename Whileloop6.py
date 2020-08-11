# Program to print the factorial of a given number

num = int(input("Enter the value "))
fact = 1
a = 1
while fact <= num:
    a = a * fact
    fact += 1
print(a)
