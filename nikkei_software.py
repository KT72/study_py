#GUI:tkinter

from tkinter import *
from tkinter import messagebox,ttk

def buttonClicked():
    messagebox.showinfo(root.title(),"ありがとうございます！")

root = Tk()
root.title("TextEdit")
root.geometry("300x50")

ttk.Button(text="押してください",command=buttonClicked).pack()

root.mainloop()
