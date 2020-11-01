# %%
# Frames
# used to diplay buttons, check buttons or menus

from tkinter import*
root = Tk()
root.title('My Frame')

f = Frame(root, height=400, width=500, bg='pink', cursor='cross')

f.pack()
root.mainloop()

# %%
# Buttons


def buttonclick(self):
    print('Hello GUI')


root = Tk()
f = Frame(root, height=200, width=300)
# Let the frame will nott shrink
f.propagate(0)
# Attach frame with root window
f.pack()

b = Button(f, text='My button', width=15, height=2, bg='pink',
           fg='blue', activebackground='grey', activeforeground='red')

b.pack()
b.bind('<Button-1>', buttonclick)
root.mainloop()

# %%
# Button by using class


class mybutton:

    def __init__(self, root):
        # Create frame
        self.f = Frame(root, height=200, width=300)
        # Let frame not shrink
        self.f.propagate(0)
        # Attach the frame to root window
        self.f.pack()
        # Create push button
        self.b = Button(self.f, text='My button', width=15, height=2, bg='Yellow', fg='blue',
                        activebackground='green', activeforeground='red', command=self.buttonclick)
        # Attach the button to frame
        self.b.pack()

    def buttonclick(self):
        print('GUI')


root = Tk()
mb = mybutton(root)
root.mainloop()
