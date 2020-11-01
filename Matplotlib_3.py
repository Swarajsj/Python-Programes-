# %%
# Ploting Bar Graph

import matplotlib.pyplot as plt
x = ['Swaraj', 'Pratigyan', 'Sneha']
y = [20, 13, 21]
plt.bar(x, y, align='center', color='r')
# Horizontal Bar Graph
#plt.barh(x,y , align='center',color = 'r')
plt.title('CA 3')
plt.ylabel('Marks')
plt.xlabel('Names')
plt.show()

# %%
# Ploting Piechart

marks = [12, 24, 30, 11, 7]
names = ['Charu', 'Garima', 'Swaraj', 'Aditi', 'Nishant']
plt.pie(marks, labels=names, startangle=90,
        autopct='%.1f%%', explode=(0.3, 0, 0.1, 0, 0))
plt.title('Ca 3 Marks')
plt.show()

# %%
# Ploting Histogram

x = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
plt.hist(x, bins=[0, 20, 40, 60, 80, 100])
plt.show()

# %%
#  Ploting Scatterplot

x = [5, 7, 8, 7, 2, 17, 2, 9, 11, 4, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
plt.show()
