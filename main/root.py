#from tkinter import ttk
import tkinter as tk
from tkinter import Label, Menu, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
from typing import Text
from index_view import main_bar  # Importacion del template header()
from Productos.gen_prod import reg_prod_view as rp
from Registrar.register_main import register_view



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
        self.main_win.title('Megamercado')
        self.main_win.geometry('1200x600')
        self.main_win.rowconfigure(0, weight=1)
        self.main_win.columnconfigure(0, weight=1)
        self.main_win.configure(bg='white')
        # CREATING FRAMES
        
        # Page 1 / Registro de Administrador-cliente-proveedor frames
        # Frame container
        self.container = tk.Frame(self.main_win, width=1200, height=600, bg='white')
        self.container.grid(row=0, column=0)
        #Frame logo image
        self.logo_image = tk.Frame(self.container, width=600, height=600, bg='white')
        self.logo_image.grid(row=0, column=0)
        # Frame registrar
        self.register = tk.Frame(self.container, width=600, height=600, bg='white')
        self.register.grid(row=0, column=1)

        #self.main_register = register_view(self.logo_image, self.register)
        #self.main_register.register_users()

        # Page 2 Frames - Registrar adm

        # Page 3 Frames - Registrar cliente

        # Page 4 Frames - Registrar proveedor

        # Page 5 Frames - Iniciar sesion adm

        # Page Main Frames
            # Main page container
        self.main_page_container = tk.Frame(self.main_win, width=1200, height=600, bg='#37648B')
        self.main_page_container.grid()

            # Top bar logo
        self.top_bar_logo = tk.Frame(self.main_page_container, width=200, height=80, bg='#37648B')
        self.top_bar_logo.grid(row=0, column=0, pady=24)
            
            # Top bar user
        self.top_bar_user = tk.Frame(self.main_page_container, width=1000, height=80, bg='#37648B')
        self.top_bar_user.grid(row=0, column=1, sticky='e', padx=30)

            # Menu Frame
        self.menu_frame = tk.Frame(self.main_page_container, width=200, height=520, bg='#37648B')
        self.menu_frame.grid(row=1, column=0)

            # Main content
        self.main_content = tk.Frame(self.main_page_container, width=1000, height=520, bg='white')
        self.main_content.grid(row=1, column=1)


        self.header = main_bar(self.top_bar_logo, self.top_bar_user)
        self.header.main_bar_view()

            # Menu
        self.menu_treeview = ttk.Treeview(self.menu_frame, height=25)
        self.style = ttk.Style()
        self.style.configure('Treeview', font=('Roboto Mono', 10), background='#37648B')
        self.menu_treeview.grid()
        
        self.ag_prod = self.menu_treeview.insert('', tk.END, text='Productos')
        self.menu_treeview.insert(self.ag_prod, tk.END, text='Añadir producto')
        self.menu_treeview.insert(self.ag_prod, tk.END, text='Listar productos')
        self.menu_treeview.insert(self.ag_prod, tk.END, text='Listar productos x almacen')
        
        self.ped = self.menu_treeview.insert('', tk.END, text='Pedidos')
        self.menu_treeview.insert(self.ped, tk.END, text='Crear pedido')
        self.menu_treeview.insert(self.ped, tk.END, text='Listar pedidos')
        
        self.ventas = self.menu_treeview.insert('', tk.END, text='Ventas')
        self.menu_treeview.insert(self.ventas, tk.END, text='Reporte de ventas')
        
        self.facturacion = self.menu_treeview.insert('', tk.END, text='Facturacion')
        self.menu_treeview.insert(self.facturacion, tk.END, text='Generar factura')
        self.menu_treeview.insert(self.facturacion, tk.END, text='Listar facturas')
        


        # EN PROCESO DE DESARROLLO
            # Main content
        self.left_btn_frame = tk.Frame(self.main_content, width=500, height=80)
        self.left_btn_frame.grid(row=0, column=0, sticky='e')
        self.right_btn_frame = tk.Frame(self.main_content, width=500, height=80)
        self.right_btn_frame.grid(row=0, column=1, sticky='w')

        self.clients = tk.Button(self.left_btn_frame, text='Clientes')
        self.clients.grid()
        self.suppliers = tk.Button(self.right_btn_frame, text='Proveedores')
        self.suppliers.grid()
        self.suppliers = tk.Button(self.main_content, text='Almacen')
        self.suppliers.grid(row=1, column=0, columnspan=2, padx=350, pady=30)
        self.logo_title = tk.Label(self.main_content, text='MEGAMERCADO')
        self.logo_title.grid(padx=350, pady=30)
        self.logo_title_inf = tk.Label(self.main_content, text='Calidad y Confianza')
        self.logo_title_inf.grid(padx=350, pady=30) 

        

    # Mostrar registro de producto
   
    def show_reg_prod(self):
        self.content_main_page.grid_forget()    # Borrar el contenido anterior de ese espacio
        self.content_main_page.grid()           # Mostrar ese mismo frame vacio
        self._reg = rp(self.content_main_page)  # Llamar e instaciar la clase que contiene la plantilla de registro de producto y pasarle el lugar donde la quiero poner
        self._reg.reg_prod()                    # Llamar el metodo que contiene la plantilla


        
if __name__ == '__main__':
    master = tk.Tk()
    _App = Application(master)
    master.mainloop()
    



