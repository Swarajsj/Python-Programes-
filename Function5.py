# %%
# Program to print the minimum value


def minimum(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return "Both the numbers are equal"


minimum(100, 100)
# %%
# Wap to find the distance between to points
#((x2-x1)**2 + (y2-y1)**2)**0.5


def distance(x1, x2, y1, y2):
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    d = (dx + dy)**0.5
    return d


distance(2, 4, 8, 10)
# %%
# Reason why we need functions
sum = 0
for i in range(1, 26):
    sum = sum + i
print(sum, end=' '"\n")
for i in range(50, 71):
    sum = sum + i
print(sum, end=' ')
