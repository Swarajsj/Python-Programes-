# %%
# Python program to display a message in the frame
from tkinter import*


class mybuttons:

    def __init__(self, root):
        self.f = Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        # Create message
        self.m = Message(self.f, text='This is a message that has more than one line',
                         width=200, font=('Roman', 20, 'bold italic'), fg='black')
        # Attach message to the frame
        self.m.pack(side=RIGHT)


root = Tk()
mb = mybuttons(root)
root.mainloop()

# %%
# Pyhton program to display a label upon clicking a push button


class mybuttons:

    def __init__(self, root):
        self.f = Frame(root, height=500, width=500)
        self.f.pack()

        self.b1 = Button(self.f, text='click me', width=15,
                         height=2, command=self.buttonclick)

        self.b1.grid(row=0, column=1)

    # Event handler method
    def buttonclick(self):
        # Create Label with some text
        self.lbl = Label(self.f, text='welcome to python', width=20, height=2, font=(
            'courier', 30, 'bold underline'), fg='blue', bg='yellow')
        # Attach the label on the frame
        self.lbl.grid(row=2, column=0)


root = Tk()
mb = mybuttons(root)
root.mainloop()
