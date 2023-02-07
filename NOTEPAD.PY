from tkinter.filedialog import *
import tkinter as tk

canvas =tk.Tk()
canvas.geometry("400*600")
canvas.title("Notepad")

b1 = Button(convas, text="Open", bg = "white")
b1.pack(slide=LEFT)

b2 = Button(canvas, text="Save", bg = "white")
b2.pack(slide=LEFT)

canvas.mainloop()