# Program to print the fabonacci series upto 8

first = int(input("Enter value"))
second = int(input("Enter value"))
limit = int(input("Enter value"))
print(first, second, end=' ')
for i in range(limit):
    sum = first + second
    first = second
    second = sum
    print(sum, end=' ')
