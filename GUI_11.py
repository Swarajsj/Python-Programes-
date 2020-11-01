# %%
# Listnox Widget Ans Textbox

from tkinter import*


class mybuttons:

    def __init__(self, root):

        # Creating frame
        self.f = Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        # Creating Label and placing it
        self.lbl = Label(
            self.f, text=' Click one or more of the following Universities below :', font='calibri 14')
        self.lbl.place(x=50, y=50)

        # Creating Listbox and placing it
        self.lb = Listbox(self.f, font='Arial 12 bold', fg='pink', bg='grey',
                          height=8, width=24, activestyle='underline', selectmode=MULTIPLE)
        self.lb.place(x=50, y=100)

        # Using for loop items sinto listbox
        for i in ['Lovely Professional University', 'Chandigarh University', 'Thapar University', 'IIT Bombay', 'IIT Madras', 'KIITS University', 'Delhi University']:
            self.lb.insert(END, i)

        # Bind the listbox select event
        self.lb.bind('<<ListboxSelect>>', self.on_select)

        # Create text box to display
        self.t = Text(self.f, width=30, height=10, wrap=WORD)
        self.t.place(x=300, y=100)

    def on_select(self, event):

        self.lst = []
        indexes = self.lb.curselection()
        for i in indexes:
            self.lst.append(self.lb.get(i))
            # Delete the previous content of the text box
            self.t.delete(0.0, END)
            # Insert New content intto the box
            self.t.insert(0.0, self.lst)


root = Tk()
mb = mybuttons(root)
root.mainloop()
