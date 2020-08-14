# %%
# Program to print the complex roots
# if d > 0 : equation has two real roots
# if d = 0 : equation has one real roots
# if d < 0 : equation has two complex roots
# formula : ax**2 + bx + c , d = b**2-4ac


def quad_d(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        return "Equation has two real roots"
    elif d < 0:
        return "Equation has one complex roots"
    else:
        return "Equation has one real roots"


quad_d(1, 7, 5)

# %%
# Break statement in functions

for i in range(9):
    if i > 3:
        break
    print(i)

# %%
# Continue statement in functions

for i in range(9):
    if i == 3:
        continue
    print(i)
