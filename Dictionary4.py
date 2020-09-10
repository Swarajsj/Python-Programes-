# %%

D3 = {}
D3["Laptop"] = "Mac"
D3["Count"] = 10
D3

# %%
A = "I want %(Count)d %(Laptop)s Laptop" % D3
A

# %%
# Comparing Two Dictionary

A = {"I", "India", "A", "America"}
B = {"I", "Italy", "A", "America"}
# A != B
# C = A
# C
# C == A
A = B
# %%
# Method of dictionary # keys()

asicode = {"A": 65, "B": 66, "C": 67, "D": 68}
# asicode.keys()
# asicode.values()
# asicode.items()
# asicode.clear()
asicode
asicode.get("B")
print(asicode.pop("C"))
asicode
