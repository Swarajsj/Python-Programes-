# Program to print the pattern  1
#                               1 2
#                               1 2 3
#                               1 2 3 4
#                               1 2 3
#                               1 2
#                               1


for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
        print(j, end='  ')
    print()
for x in range(5, 1, -1):
    for y in range(1, x-1, 1):
        print(y, end='  ')
    print()
