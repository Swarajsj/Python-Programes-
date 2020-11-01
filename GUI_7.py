# %%
# Checked Button

from tkinter import*


class mybuttons:

    def __init__(self, root):

        self.f = Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        # create intvar class variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        # create check box and bind them to display method

        self.c1 = Checkbutton(self.f, bg='yellow', fg='green', font=(
            'Georgia', 20, 'underline'), text='java', variable=self.var1, command=self.display)
        self.c2 = Checkbutton(self.f, bg='yellow', fg='green', font=(
            'Georgia', 20, 'underline'), text='python', variable=self.var2, command=self.display)
        self.c3 = Checkbutton(self.f, bg='yellow', fg='green', font=(
            'Georgia', 20, 'underline'), text='.net', variable=self.var3, command=self.display)
        # attach check boxes to the frame

        self.c1.place(x=50, y=100)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)

    def display(self):
        # retrieve the control variable values
        x = self.var1.get()  # 0,1
        y = self.var2.get()  # 0,1
        z = self.var3.get()  # 0,1

        # string is empty initially

        str = ''
        # catch user choice

        if x == 1:
            str += 'java'
        if y == 1:
            str += 'python'
        if z == 1:
            str += '.net'

        # display the user selection as a label
        lbl = Label(text=str, fg='blue').place(
            x=50, y=150, width=200, height=20)


root = Tk()
mb = mybuttons(root)
root.mainloop()
