from tkinter import *
from tkinter import ttk
from tkinter import font


class wind:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.configure(bg="grey")
        self.__x = 0

        self.style = ttk.Style()
        self.style.configure("TButton", font=('Arial', 14), height=100, )
        
        
        self.btn1 = ttk.Button(
            text="Пополнить",
            width=15,
            style="TButton"

        )
        self.btn2 = ttk.Button(
            text="Вычесть",
            width=15,
            style="TButton"
        )
        self.label = ttk.Label(
            text=self.__x,
            font=("Courier", 44),
            background="grey"
        )

        self.btn1.place(x=400, y=200)
        self.btn2.place(x=200, y=200)
        self.label.place(x=375, y=100)
        self.root.mainloop()



app = wind()
