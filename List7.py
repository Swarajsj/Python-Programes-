# %%
# Passing Value In List

import random


def print_list(lst):
    for x in lst:
        print(x, end=" ")


l1 = [10, 20, 30, 40, 50]
print_list(l1)
# %%
# Reverse the value in list


def reverse_list(lst):
    lst.reverse()
    return lst


l2 = [10, 20, 30, 40, 50]
reverse_list(l2)
# %%
# Import operator

print(random.random())
# %%
# Aliasing

a = [1, 2, 3]
b = a
b[0] = 5
a
# %%
# Cloning
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 5
print(a)
print(b)
