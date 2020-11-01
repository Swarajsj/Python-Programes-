# %%
# Graphical User Interface (GUI)

from tkinter import*
root = Tk()
root.title('GUI')
root.geometry('800x600')
root.mainloop()

# %%
# Create Canvas as child root window
root = Tk()
root.title('My Window')
c = Canvas(root, bg='grey', height=700, width=1200, cursor='pencil')
# Create a line in canvas
id = c.create_line(50, 50, 200, 50, 200, 150, 50, 150, width=4, fill='yellow')
# Create an oval in canvas
id = c.create_oval(100, 100, 300, 500, width=5, fill='Yellow',
                   outline='red', activefill='pink')
# Create a polygon in canvas
id = c.create_polygon(100, 100, 400, 400, 400, 300, width=3,
                      fill="blue", outline='red', activefill='light blue')
# Create a rectangle in canvas
id = c.create_rectangle(400, 100, 700, 600, width=2,
                        fill='red', outline='black', activefill='purple')
# Create some text in canvas
fnt = ('Times', 40, 'bold italic underline')
id = c.create_text(500, 100, text='My Canvas', font=fnt,
                   fill='red', activefill='orange')
c.pack()
root.mainloop()
