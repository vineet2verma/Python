# Gui Create
# Title Create
# icon image 

from cProfile import label
from tkinter import *

win = Tk()

win.title("2")
# win.iconbitmap("C:\Python\icons\youtube.ico")
win.maxsize(width=600, height=400)
win.minsize(width=400, height=300)

lbl = Label(win, text="Label")
# lbl.grid()    # GRID USE ROW AND COLUMN
lbl.place(x=10, y=20)
# lbl.pack()      # 

win.mainloop()
