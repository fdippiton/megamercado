#from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter.font import families
from index_view import main_view as mv # Importacion del template header

class Application:
    def __init__(self, master):
        self.main_win = master 
        self.main_win.title('Registrar producto')
        self.main_win.geometry('1200x600')
        self.main_win.configure(bg='White')

        # Creating Frames
        header_main_page = tk.Frame(self.main_win)
        header_main_page.grid(column=0, row=0)

        menu_main_page = tk.Frame(self.main_win)
        menu_main_page.grid(column=0, row=1)

        # Importacion del objeto header y pasarle el frame en donde estara
        header = mv(header_main_page)
        header.main_page_view()


if __name__ == '__main__':
    master = tk.Tk()
    _App = Application(master)
    master.mainloop()
    



