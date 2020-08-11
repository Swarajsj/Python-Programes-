# Program to print the even numbers from 0 to 1 and add them

sum = 0
for i in range(0, 11, 1):
    if i % 2 == 0:
        print(i)
        sum = sum + i
print(sum)
