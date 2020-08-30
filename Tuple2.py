# %%
# Passing variable length agrument to tuple


def createup(*abc):
    print(abc)


createup(123)
# %%


def sum_all(*args):
    s = 0
    for i in args:
        s = s + i
    print(s)


sum_all(1, 2, 3)
# %%

a = (1, 2, 3,)
for i in a:
    print(i)
# %%
# List and tuple

l1 = [1, 2, 3, 4]
t1 = tuple(l1)
t1
# %%
# Sort tuple

t2 = (2, 4, 1, 3)
l2 = list(t2)
l2.sort()
t2 = tuple(l2)
t2
