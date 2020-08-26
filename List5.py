# %%
# without using list comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(l1)):
    l1[i] = l1[i] + 10
l1
# %%
# Using list comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l1 = [x+10 for x in l1]
l1
# %%
# Using list comprehension if even

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l1 = [x for x in l1 if x % 2 == 0]
l1
# %%
# append = to add an element at the end of the list

l2 = ['R', 'A', 'J']
l2.append('U')
l2
# %%
# Clear the list

l2 = ['R', 'A', 'J']
l2.clear()
l2
