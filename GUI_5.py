# %%
from tkinter import*


def buttonclick(xyz):
    print('Hello')


root = Tk()
f = Frame(root, height=200, width=300)
f.propagate(0)
f.pack()

b = Button(f, text='red', width=15, height=2, bg='yellow', fg='blue',
           activebackground='blue', activeforeground='green')
b1 = Button(f, text='blue', width=15, height=2, bg='yellow',
            fg='blue', activebackground='black', activeforeground='white')
b2 = Button(f, text='green', width=15, height=2, bg='yellow',
            fg='blue', activebackground='green', activeforeground='red')
b3 = Button(f, text='perpule', width=15, height=2, bg='yellow',
            fg='blue', activebackground='blue', activeforeground='orange')


#b .pack(fill = X , padx = 10 , pady = 15)
#b1.pack(fill = Y , padx = 50 , pady = 75)
#b .pack(fill = LEFT , padx = 10 , pady = 15)
#b1.pack(fill = RIGHT , padx = 10 , pady = 15)

#b .grid( row = 0 , column = 0 , padx = 10 , pady = 10)
#b1.grid( row = 2 , column = 1 , padx = 10 , pady = 10)
#b2.grid( row = 0 , column = 2 , padx = 10 , pady = 10)
#b3.grid( row = 1 , column = 3 , padx = 10 , pady = 10)

#b.place(x=50, y=30, width=100, height=50)
#b1.place(x=20, y=100, width=100, height=50)

b.bind("<Button>-1", buttonclick)
b1.bind("<Button>-1", buttonclick)
b2.bind("<Button>-1", buttonclick)
b3.bind("<Button>-3", buttonclick)

root.mainloop()
