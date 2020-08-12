# Program to print the pattern         *
#                                     * *
#                                    * * *
#                                   * * * *
#                                  * * * * *
#                                 * * * * * *
#                                * * * * * * *


n = int(input('Enter the number'))
k = 2*n-2
for i in range(0, n):
    for j in range(0, k):
        print(end=' ')
    k = k-1
    for z in range(0, i+1):
        print("*", end=' ')
    print()
