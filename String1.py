# %%
# String Class

s1 = str()
s2 = str('Hello')
print(s2)

s1 = ""
s2 = "Hello"
print(s1, s2)
# %%
# Traversing with for loop

s = "India"
for ch in s:
    print(ch, end=' ')


s = "ILovePython"
for ch in range(0, len(s), 1):
    print(s[ch], end=' ')
# %%
# Traversing with while loop

s = "India"
i = 0
while i < len(s):
    print(s[i], end=' ')
    i = i + 1
# %%
# Immutable string

str1 = " I Love Python"
str1[0] = "U"
print(str1)
