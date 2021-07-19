import tkinter as tk
from Reportes import *
from Entradas import *


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        top=self.winfo_toplevel()
        top.resizable(height=None, width=None)

 

App_instance = App()
App_instance.master.title('Megamercado')
App_instance.master.geometry('500x400')
App_instance.mainloop()