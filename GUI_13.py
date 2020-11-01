# %%
# Upload Image using GUI

from tkinter import*
root = Tk()
# Create canvas as a child to root window
c = Canvas(bg='grey', height=700, width=1200)

file1 = PhotoImage(file="Raj.jpg")
file2 = PhotoImage(file="Raj1.jpg")

c.create_image(500, 200, anchor=CENTER, image=file1, activeimage=file2)
c.create_image(700, 200, anchor=CENTER, image=file2)
c.pack(expand=YES, fill=BOTH)
c.pack()
root.mainloop()
