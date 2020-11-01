# %%
# Entry Button

from tkinter import*


class mybuttons:

    def __init__(self, root):

        self.f = Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        # Create label

        self.l1 = Label(text='Enter Username :)')
        self.l2 = Label(text='Enter Password :)')

        # Create entry widget fro user name
        self.e1 = Entry(self.f, width=25, fg='red',
                        bg='pink', font=('Arial', 16))
        # Create entry widget for password , the text in widget replace by *
        self.e2 = Entry(self.f, width=25, fg='orange',
                        bg='light blue', font=('Arial', 14), show='*')
        # When user press enter , bind that event to display method
        self.e1.bind('<Return>', self.display)
        self.e2.bind('<Return>', self.display)

        # Place label and entry widget in rhe frame
        self.l1.place(x=50, y=100)
        self.l2.place(x=50, y=150)
        self.e1.place(x=200, y=100)
        self.e2.place(x=200, y=150)

    def display(self, event):

        str1 = self.e1.get()
        str2 = self.e2.get()

        # Display the value using label

        lbl1 = Label(text='Your Name Is :' + str1).place(x=50, y=200)
        lbl2 = Label(text='Your Password Is :' + str2).place(x=50, y=220)


root = Tk()
mb = mybuttons(root)
root.mainloop()
