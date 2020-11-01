# %%
# Radio Button

from tkinter import*


class mybuttons:

    def __init__(self, root):

        self.f = Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        # Create intvar class variable
        self.var = IntVar()

        self.r1 = Radiobutton(self.f, bg='yellow', fg='green', font=(
            'Georgia', 20, 'underline'), text='Male', variable=self.var, value=1, command=self.display)
        self.r2 = Radiobutton(self.f, bg='red', fg='black', font=(
            'Georgia', 20, 'underline'), text='Female', variable=self.var, value=2, command=self.display)

        # Attach radio buttons to the frame
        self.r1.place(x=50, y=100)
        self.r2.place(x=200, y=100)

    def display(self):

        # Retrive the control variable
        x = self.var.get()
        # String is empty initially
        str = ''
        # Catch user choice
        if x == 1:
            str += 'You Selected :) Male'
        if x == 2:
            str += 'You Selected :) Female'

        # Craete Label
        lbl = Label(text=str, fg='blue').place(
            x=50, y=150, width=200, height=20)


root = Tk()
mb = mybuttons(root)
root.mainloop()
