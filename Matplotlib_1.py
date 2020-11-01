# %%
# Matplotlib Library
import matplotlib.pyplot as plt
import matplotlib
# %%
# Ploting a graph

import matplotlib.pyplot as pt
pt.plot([1.5, 2, 3, 4], [3, 8, 10, 25])
pt.show()

# %%
# Title , Xlable & Ylabel methods in graph

pt.plot([1, 2, 3, 4, 9], [3, 8, 10, 25, 29])
pt.title('Rain in December')
pt.xlabel('Days in December')
pt.ylabel('Rain in Inches')
pt.show()

# %%
# Different types of lines in graph

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# Solid dots
#plt.plot([1,2,3,4] , [1,4,9,16],'ro')
# Dash line
#plt.plot([1,2,3,4] , [1,4,9,16],'b--')
# Square dots
#plt.plot([1,2,3,4] , [1,4,9,16],'ys')
# Triangle dots
#plt.plot([1,2,3,4] , [1,4,9,16],'g^')

plt.show()

# %%
# Taking Cordinates from the text file

x = []
y = []

readFile = open('Coordinates.txt', 'r')
data = readFile.read().split()

for i in data:
    val = i.split(',')
    x.append(val[0])
    y.append(val[1])

print(data)
print(x)
print(y)
pt.plot(x, y)
pt.show()

# %%
# Creating Subplot

fig = pt.figure()

rect = fig.patch
rect.set_facecolor('yellow')  # Backgroung color where will be drawen

x = [3, 7, 8, 12]
y = [5, 13, 2, 8]
graph1 = fig.add_subplot(1, 1, 1, facecolor='black')  # (1,1,1 = row,col,index)
graph1.plot(x, y, 'green', linewidth=4.0)
pt.show()
