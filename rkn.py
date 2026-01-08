from tkinter import *
from tkinter import ttk
from tkinter import font


x = 0
"""
def cl ():
    global x
    x += 1
    label["text"] = x
"""
#окно
root = Tk()
root.title("test")
root.geometry("800x800")
root.configure(bg="grey")


#Кнопки
style = ttk.Style(root)
style.configure("TButton", font=('Arial', 14), height=100, )
btn1 = ttk.Button(text="Пополнить", width=15, style="TButton", )
btn1.place(x=400, y=200)
btn2 = ttk.Button(text="Вычесть", width=15, style="TButton")
btn2.place(x=200, y=200)


#Текст
style.configure("Big.TLabel" ,font=("Courier", 44), )
label = ttk.Label(text=x, style="Big.TLabel", background="grey" )
label.place(x=375, y=100)


root.mainloop()
