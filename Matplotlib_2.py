# %%
# Enhance the graph

import matplotlib.pyplot as pt
fig = pt.figure()

rect = fig.patch
rect.set_facecolor('green')

x = [3, 7, 8, 12]
y = [5, 13, 2, 8]

graph1 = fig.add_subplot(1, 1, 1, facecolor='black')
graph1.plot(x, y, 'red', linewidth=4.0)

graph1.tick_params(axis='x', color='white')
graph1.tick_params(axis='y', color='yellow')

graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('b')
graph1.spines['bottom'].set_color('b')

graph1.set_title('random graph', color='white')
graph1.set_xlabel('this is the x axis', color='white')
graph1.set_ylabel('this is the y axis')

pt.show()

# %%
# Plot multiset of cordinates in subplot
# add multiple lines and multiple graph


fig = pt.figure()

rect = fig.patch
rect.set_facecolor('green')

x = [3, 7, 8, 12]
y = [5, 13, 2, 8]

x2 = [0, 4, 7, 10]
y2 = [3, 7, 1, 12]

x3 = [2, 4, 6, 8]
y3 = [13, 5, 8, 2]


graph1 = fig.add_subplot(1, 1, 1, facecolor='black')
graph1.plot(x, y, 'red', linewidth=4.0)

graph1.plot(x2, y2, 'yellow', linewidth=2.0)

graph1.plot(x3, y3, 'orange', linewidth=6.0)

graph1.tick_params(axis='x', color='white')
graph1.tick_params(axis='y', color='white')

graph1.spines['top'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
graph1.spines['bottom'].set_color('w')

graph1.set_title('random graph', color='white')
graph1.set_xlabel('this is the x axis', color='white')
graph1.set_ylabel('this is the y axis')

pt.show()

# %%
# Draw multiple subgraph in a single graph


fig = pt.figure()

rect = fig.patch
rect.set_facecolor('green')

x = [0, 7, 8, 12]
y = [5, 13, 2, 8]

x2 = [0, 4, 7, 12]
y2 = [3, 7, 1, 12]

x3 = [0, 4, 6, 12]
y3 = [13, 5, 8, 2]

# number of rows, number of columns, index of the graph.
fig.add_subplot(4, 1, 4)
pt.plot(x, y, 'b--')
fig.add_subplot(4, 1, 3)
pt.plot(x2, y2, 'y--')
fig.add_subplot(4, 1, 2)
pt.plot(x3, y3, 'r--')
fig.add_subplot(4, 1, 1)
pt.plot(x3, y3, 'r--')
pt.show()
