#from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter.font import families
from typing import Text
from index_view import main_view as mv # Importacion del template header()
from Productos.gen_prod import reg_prod_view as rp



""" Definir los frames con la estructura siguiente:

        self.NombreFrame = tk.Frame(self.main_win)
        self.NombreFrame.grid(column=1, row=1) Si es un frame dentro content
        self.NombreFrame.grid(column=#, row=#) Si es otro tipo de frame

    Importar los modulos
    from NombreCarpeta.NombreArchivo import nombreFuncion as abreviacion
    Ejemplo:  from Productos.gen_prod import reg_prod_view as rp

    Creacion de funciones para mostrar los modulos

    NombreFrame es el lugar en donde se colocara el contenido
    def NombreFuncion(self):
        self.NombreFrame.grid_forget()  #Para limpiar el contenido anterior
        self.NombreFrame.grid()         #Para mostrar el contenido nuevo en ese espacio
        self._reg = rp(self.NombreFrame) # Instanciar la clase o modulo
        self._reg.reg_prod()                   # Llamar metodo de la clase

    Ejemplo: 
    def show_reg_prod(self):
        self.content_main_page.grid_forget()
        self.content_main_page.grid()
        self._reg = rp(self.content_main_page)
        self._reg.reg_prod()

"""
class Application:
    def __init__(self, master):
        self.main_win = master 
        self.main_win.title('Registrar producto')
        self.main_win.geometry('1200x600')
        self.main_win.configure(bg='White')

        # CREATING FRAMES
        # Header frame
        self.header_main_page = tk.Frame(self.main_win)
        self.header_main_page.grid(column=0, row=0)

        # Menu Frame
        self.menu_main_page = tk.Frame(self.main_win)
        self.menu_main_page.grid(column=0, row=1)

        # Content frame
        self.content_main_page = tk.Frame(self.main_win)
        self.content_main_page.grid(column=0, row=1)

        # Registro de producto frame
        self.reg_prod_page = tk.Frame(self.main_win)
        self.reg_prod_page.grid(column=1, row=1)



        # Importacion del objeto header y pasarle el frame en donde estara
        self.header = mv(self.header_main_page)
        self.header.main_page_view()

        # Boton de ejemplo para mostrar otro frame
        self.btn = tk.Button(self.content_main_page, text='Registrar producto', command=self.show_reg_prod)
        self.btn.grid()

    # Mostrar registro de produto
    def show_reg_prod(self):
        self.content_main_page.grid_forget()    # Borrar el contenido anterior de ese espacio
        self.content_main_page.grid()           # Mostrar ese mismo frame vacio
        self._reg = rp(self.content_main_page)  # Llamar e instaciar la clase que contiene la plantilla de registro de producto y pasarle el lugar donde la quiero poner
        self._reg.reg_prod()                    # Llamar el metodo que contiene la plantilla



if __name__ == '__main__':
    master = tk.Tk()
    _App = Application(master)
    master.mainloop()
    



