# Program to print the pattern  * * * * *
#                               * * * *
#                               * * *
#                               * *
#                               *

num = 7
for i in range(1, 6, 1):
    num = num - 1
    for j in range(1, num, 1):
        print("*", end='  ')
    print()


# Program to print the pattern  1 2 3 4 5
#                               1 2 3 4
#                               1 2 3
#                               1 2
#                               1


num = 7
for i in range(1, 6, 1):
    num = num - 1
    for j in range(1, num, 1):
        print(j, end='  ')
    print()


# Program to print the pattern  5 4 3 2 1
#                               4 3 2 1
#                               3 2 1
#                               2 1
#                               1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='  ')
    print()
