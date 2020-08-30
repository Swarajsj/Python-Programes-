# %%
# The Inverse Zip (*) function


def print_all(country, capital):
    print(country)
    print(capital)


args = ('India', 'Delhi')
print_all(*args)

# %%
# Example 2

x = [('Apple', 500000), ('Dell', 40000)]
laptop, prize = zip(*x)
print(laptop)
print(prize)
