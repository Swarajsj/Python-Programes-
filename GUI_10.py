# %%
# Spinbox Widget

from tkinter import*


class mybuttons:

    def __init__(self, root):

        self.f = Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.val1 = IntVar()
        self.val2 = StringVar()

        # Creating Spinbox
        self.s1 = Spinbox(self.f, from_=5, to=15, textvariable=self.val1, width=25, fg='orange', bg='pink',
                          font=('Arial', 14, 'bold'))
        self.s2 = Spinbox(self.f, values=('Jalandhar', 'Phagwara', 'Delhi', 'Hyderabad', 'Bangalore', 'Mumbai', 'Chennai', 'Kolkata'),
                          textvariable=self.val2, width=25, fg='red', bg='light green', font=('Arial', 14, 'bold'))
        # Creating Button
        self.b = Button(self.f, text='Get Values From Spinboxes',
                        command=self.display)

        self.s1.place(x=50, y=50)
        self.s2.place(x=50, y=100)
        self.b.place(x=50, y=150)

    def display(self):

        a = self.val1.get()
        s = self.val2.get()

        # Creating Label

        lbl1 = Label(text='Selected value :' + str(a)).place(x=50, y=200)
        lbl2 = Label(text='Selected City :' + s).place(x=50, y=220)


root = Tk()
mb = mybuttons(root)
root.mainloop()
