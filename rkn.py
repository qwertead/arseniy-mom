from tkinter import *
from tkinter import ttk
from tkinter import font
"""
x = 0
def cl ():
    global x
    x += 1
    label["text"] = x
"""
#окно
root = Tk()
root.title("test на вич")
root.geometry("800x800")


#Кнопки
style = ttk.Style()
style.configure("Big.TButton", font=('Arial', 14))
btn1 = ttk.Button(text="Click", width=20, style="Big.TButton" )
btn1.place(x=10, y= 30)


#Текст
label = ttk.Label(text="Привет")
label.pack()


root.mainloop()