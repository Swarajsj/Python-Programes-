# %%
# Slicing Operator [Start:End]

s = "Lovely Professional University"
s[4:10]
s[::]  # entire string
s[0:len(s):2]
# %%
# Wap to print all lettrs from word1 that also appaer in word2

w1 = "USA North America"
w2 = "USA South America"
for letter in w1:
    if letter in w2:
        print(letter, end=' ')
# %%
# String Comparisation

s1 = 'abcd'
s2 = 'ABCD'
s1 < s2
s1 > s2
s1 = s2
# %%
# Upper Operator

s1 = 'swaraj'.upper()
s1
# %%
# Split Operator

s2 = 'My Name Is Swaraj'
s2.split()
