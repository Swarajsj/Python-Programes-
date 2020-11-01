# %%

from tkinter import*
root = Tk()
c = Canvas(root, bg='grey', height=800, width=1200)

# Create arcs in canvas

id = c.create_arc(100, 100, 400, 300, width=3, start=270,
                  extent=180, outline='red', style='arc')
id = c.create_arc(500, 200, 800, 300, width=3, start=90,
                  extent=180, outline='blue', style='arc')
id = c.create_arc(400, 400, 400, 600, width=3, start=0,
                  extent=180, outline='purple', style='arc')
id = c.create_arc(800, 300, 800, 600, width=3, start=180,
                  extent=180, outline='pink', style='arc')
id = c.create_arc(900, 600, 1200, 600, width=3, start=180,
                  extent=180, outline='yellow', style='arc')
id = c.create_arc(700, 700, 1600, 800, width=3, start=90,
                  extent=90, outline='black', style='arc')

c.pack()
root.mainloop()
# %%

root = Tk()
c = Canvas(root, bg='grey', height=800, width=1200)

# Pieslice , chord
id = c.create_arc(100, 100, 400, 300, width=3, start=270,
                  extent=180, outline='red', style='arc')
id = c.create_arc(100, 50, 240, 210, width=3, start=90,
                  extent=180, outline='blue', style='chord')
id = c.create_arc(400, 500, 600, 800, width=3, start=90,
                  extent=90, outline='purple', style='pieslice')

c.pack()
root.mainloop()
