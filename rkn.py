from tkinter import *
from tkinter import ttk
from tkinter import font
import time
x = 0
history = []



"""
def cl ():
    global x
    x += 1
    label["text"] = x
"""
# окно
root = Tk()
root.title("test")
root.geometry("800x800")
root.configure(bg="grey")


def neww():  # создание нового окна для пополнения
     
    global entry1
    global rootp
    rootp = Tk()
    rootp.geometry("400x400")
    rootp.configure(bg='grey')
    btnp = ttk.Button(rootp, text="Пополнить", width=30, command=cl1)
    btnp.place(x=100, y=350)
    lab1 = ttk.Label(rootp, text="Введите сумму", background="grey", font=('Arial', 20))
    lab1.place(x=110, y=50)
    entry1 = ttk.Entry(rootp)
    entry1.place(x=120, y=175, width=175, height=50)
    

def cl1():
    global rootp
    global x
    global entry1
    plus1 = entry1.get()
    try:
        
        label["text"] += x + int(plus1)
        history.append(['+', plus1])
        x = 0
        rootp.destroy()
    except ValueError:
        global rootv
        rootv = Tk()
        rootv.geometry('200x200')
        rootv.configure(bg='grey')
        labv = ttk.Label(rootv, background='grey', text="Введите цифры", font=('Arial', 20))
        labv.pack(anchor='center')
        btno = ttk.Button(rootv ,text='OK', width=10, command=d)
        btno.place(x=55, y=90)
def d():
    global rootv
    rootv.destroy()     

    
    


def newww():  # окно для вычитания
    global x
    global entry2
    global rootm
    rootm = Tk()
    rootm.geometry("400x400")
    rootm.configure(bg="grey")
    btnm = ttk.Button(rootm, text="Вычесть", width=30, command=cl2)
    btnm.place(x=100, y=350)
    lab2 = ttk.Label(rootm, text="Введите сумму", background="grey", font=('Arial', 20))
    lab2.place(x=110, y=50)
    entry2 = ttk.Entry(rootm)
    entry2.place(x=120, y=175, width=175, height=50)

def cl2():
        global x
        global rootm
        plus2 = entry2.get()
        try:
            label['text'] += x - int(plus2)
            history.append(['-', plus2])
            x = 0
            rootm.destroy()
            
        except ValueError:
            global rootv
            rootv = Tk()
            rootv.geometry('200x200')
            rootv.configure(bg='grey')
            labv = ttk.Label(rootv, background='grey', text="Введите цифры", font=('Arial', 20))
            labv.pack(anchor='center')
            btno = ttk.Button(rootv ,text='OK', width=10, command=d)
            btno.place(x=55, y=90)
def d():
    global rootv
    rootv.destroy() 
        
        
def trans():
    roott = Tk()
    roott.geometry('400x400')
    roott.configure(bg='grey')
    labt = ttk.Label(roott ,text='История KFC', background='grey', font=('Arial', 20))
    labt.pack()
    listbox = Listbox(roott, width=40, height=20)
    listbox.pack()
    for i in history:
         listbox.insert(0, i)
    

# Кнопки
style = ttk.Style(root)
style.configure("TButton", font=('Arial', 14), height=100, )
btn1 = ttk.Button(text="Пополнить", width=15, style="TButton", command=neww)
btn1.place(x=400, y=200)
btn2 = ttk.Button(text="Вычесть", width=15, style="TButton", command=newww)
btn2.place(x=200, y=200)
btn3 = ttk.Button(text='История KFC', command=trans)
btn3.place(x=50, y=50)

# Баланс
style.configure("Big.TLabel", font=("Courier", 44), )
label = ttk.Label(text=x, style="Big.TLabel", background="grey")
label.place(x=375, y=100)

root.mainloop()
