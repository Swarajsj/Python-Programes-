# %%
# Menu Widget

from tkinter import*


class mymenudemo:
    def __init__(self, root):
        # Create Menubar
        self.menubar = Menu(root)
        # Attach the menubar to the root window
        root.config(menu=self.menubar)
        # Create file menu
        self.filemenu = Menu(root, tearoff=0)
        # Create menu item in file menu
        self.filemenu.add_command(label='New', command=self.donothing)
        self.filemenu.add_command(label='Open', command=self.donothing)
        self.filemenu.add_command(label='Save', command=self.donothing)
        # Add a horizontal line as seperator
        self.filemenu.add_separator()
        # Create another item below seperator
        self.filemenu.add_command(label='Exit', command=root.destroy)
        # Add menu with the name file
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        # Create edit menu
        self.editmenu = Menu(root, tearoff=0)
        # Create menu item in edit menu
        self.menubar.add_command(label='Cut', command=self.donothing)
        self.menubar.add_command(label='Copy', command=self.donothing)
        self.menubar.add_command(label='Paste', command=self.donothing)
        # Add the edit menu with a name edit to the menubar
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)

    def donothing(self):
        pass


root = Tk()
# Title for root window
root.title('A menu example')
# Create object
obj = mymenudemo(root)
# Define the size of root window
root.geometry('600x350')
root.mainloop()
