# %%
from tkinter import*


class mybotton:
    def __init__(self, root):
        self.f = Frame(root, height=400, width=500)
        self.f.propagate(0)
        self.f.pack()

        # Create 3 push buttonand bind them to button click method
        self.b1 = Button(self.f, text='Red', width=15, height=2,
                         command=lambda: self.buttonclick(1))
        self.b2 = Button(self.f, text='Green', width=15,
                         height=2, command=lambda: self.buttonclick(2))
        self.b3 = Button(self.f, text='Blue', width=15,
                         height=2, command=lambda: self.buttonclick(3))

        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

        # Method to be called when the button is clicked
    def buttonclick(self, num):
        # Set the background color of frame depending on the button clicked

        if num == 1:
            self.f['bg'] = 'red'
        if num == 2:
            self.f['bg'] = 'green'
        if num == 3:
            self.f['bg'] = 'blue'


root = Tk()
mb = mybotton(root)
root.mainloop()
