# Program to print the pattern  *
#                               * *
#                               * * *
#                               * * * *
#                               * * * * *

num = 1
for i in range(1, 6, 1):
    num = num + 1
    for j in range(1, num, 1):
        print("*", end='  ')
    print()


# Program to print the pattern  1
#                               1 2
#                               1 2 3
#                               1 2 3 4
#                               1 2 3 4 5

num = 1
for i in range(1, 6, 1):
    num = num + 1
    for j in range(1, num, 1):
        print(j, end='  ')
    print()


# Program to print the pattern  A
#                               A B
#                               A B C
#                               A B C D
#                               A B C D E


for i in range(65, 70, 1):
    for j in range(65, i+1, 1):
        print(chr(j), end='  ')
    print()
