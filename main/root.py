#from tkinter import ttk
import tkinter as tk
from tkinter import Label, Menu, Menubutton, ttk
from tkinter.constants import ANCHOR, COMMAND, RAISED, S
from tkinter.font import families
from fonts import *
from typing import Text
from index_view import main_bar  # Template header
from Productos.gen_prod import reg_prod_view as rp # Template registro de producto
from Productos.list_prod import listar_prod as lp # Template listar productos
from Productos.list_prod_alm import listar_prod_alm  # Template listar productos
from Productos.all_prod import _products             # Productos 
from Ventas.rpt_ventas import rpt_ventas
from Registrar.register_main import register_view # Template principal registrar usuarios
from Clientes.cli import listar_clientes
from Almacen.alm import reg_alm_view
from Proveedores.prov import listar_proveedores

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
        

        # CREACION DE FRAMES
        
#   -------------------------- PAGE 1 ----------------------------------------------
        # Registro de Administrador-cliente-proveedor frames
        # Frame container
        self.container = tk.Frame(self.main_win, width=1200, height=600, bg='yellow')
        self.container.grid(row=0, column=0)
        
        #Frame de la imagen del logo
        self.logo_image = tk.Frame(self.container, width=600, height=600, bg='white')
        self.logo_image.grid(row=0, column=0)
        
        # Frame registrar
        self.register = tk.Frame(self.container, width=600, height=600, bg='white')
        self.register.grid(row=0, column=1)

        # FUNCION QUE EJECUTA LA PAGINA 1
        #self.main_register = register_view(self.logo_image, self.register)
        #self.main_register.register_users()

# ----------------------------- PAGE 2 --------------------------------------

        # Frames - Registrar adm

# ----------------------------- PAGE 3 ---------------------------------------
        # Frames - Registrar cliente


# ----------------------------- PAGE 4 ---------------------------------------
        # Page 4 Frames - Registrar proveedor


# ----------------------------- PAGE 5 ---------------------------------------
        # Page 5 Frames - Iniciar sesion adm



# ----------------------------- PAGINA PRINCIPAL ---------------------------------------
    # Page Main Frames
            # Contenedor de la pagina principal
        self.main_page_container = tk.Frame(self.main_win, width=1200, height=600, bg='#263859')
        self.main_page_container.grid()

            # Contenedor del logo 'MEGAMERCADO' de la barra superior
        self.top_bar_logo = tk.Frame(self.main_page_container, width=200, height=30, bg='#263859')
        self.top_bar_logo.grid(row=0, column=0, pady=24)
            
            # Contendor de la barra superior 
        self.top_bar_user = tk.Frame(self.main_page_container, width=1000, height=30, bg='#263859')
        self.top_bar_user.grid(row=0, column=1, sticky='e', padx=20)

            # Contenedor del Menu 
        self.menu_frame = tk.Frame(self.main_page_container, width=200, height=570, bg='#263859')
        self.menu_frame.grid(row=1, column=0, sticky='n', pady=30)

            # Contenedor del contenido principal - Main content
        self.main_content = tk.Frame(self.main_page_container, width=1000, height=570, bg='white')
        self.main_content.grid(row=1, column=1)

    # Implementacion del template - Barra superior
        self.header = main_bar(self.top_bar_logo, self.top_bar_user)
        self.header.main_bar_view()


# -------------------------------- MENU ---------------------------------------------------
        # MENU BAR
        self.btn_inicio = tk.Button(self.menu_frame, text='Inicio', command=self.main_view, font=('Roboto Mono Semibold', 10), borderwidth=2)
        self.btn_inicio.grid(padx=40, pady=10, ipadx=47, ipady=5)
        
        # Productos menu
        self.menu_prod = tk.Menubutton(self.menu_frame, text='Productos', relief=RAISED, font=('Roboto Mono Semibold', 10), borderwidth=2)
        self.menu_prod.grid( pady=10, ipadx=35, ipady=5)

        self.menu_prod.menu = tk.Menu(self.menu_prod, tearoff=0)
        self.menu_prod['menu'] = self.menu_prod.menu

        self.ag_prod = tk.IntVar()
        self.lis_prod = tk.IntVar()
        self.all_prods = tk.IntVar()
        self.menu_prod.menu.add_checkbutton(label='Añadir productos', variable=self.ag_prod, command=self.show_reg_prod, font=('Roboto Mono', 9))
        self.menu_prod.menu.add_checkbutton(label='Editar productos', variable=self.all_prods, font=('Roboto Mono', 9), command=self.show_all_prod)
        self.menu_prod.menu.add_checkbutton(label='Listar productos', variable=self.lis_prod, command=self.show_list_prod, font=('Roboto Mono', 9))
        self.menu_prod.menu.add_checkbutton(label='Listar productos x almacén', variable=self.lis_prod, font=('Roboto Mono', 9), command=self.show_list_prod_alm)

        # Pedidos
        self.menu_ped = tk.Menubutton(self.menu_frame, text='Pedidos', relief=RAISED, font=('Roboto Mono Semibold', 10), borderwidth=2)
        self.menu_ped.grid( pady=10, ipadx=45, ipady=5)

        self.menu_ped.menu = tk.Menu(self.menu_ped, tearoff=0)
        self.menu_ped['menu'] = self.menu_ped.menu

        self.cr_ped = tk.IntVar()
        self.lis_ped = tk.IntVar()
        self.menu_ped.menu.add_checkbutton(label='Crear pedido', variable=self.cr_ped, font=('Roboto Mono', 9))
        self.menu_ped.menu.add_checkbutton(label='Listar pedidos', variable=self.lis_ped,  font=('Roboto Mono', 9))
        
        # Ventas
        self.menu_ven = tk.Menubutton(self.menu_frame, text='Ventas', relief=RAISED,  font=('Roboto Mono Semibold', 10), borderwidth=2)
        self.menu_ven.grid( pady=10, ipadx=50, ipady=5)

        self.menu_ven.menu = tk.Menu(self.menu_ven, tearoff=0)
        self.menu_ven['menu'] = self.menu_ven.menu

        self.rpt_ven = tk.IntVar()
        self.menu_ven.menu.add_checkbutton(label='Reporte de ventas', variable=self.rpt_ven,  font=('Roboto Mono', 9), command=self.show_rpt_ventas)

        # Facturacion
        self.menu_fac = tk.Menubutton(self.menu_frame, text='Facturacion', relief=RAISED, font=('Roboto Mono Semibold', 10), borderwidth=2)
        self.menu_fac.grid( pady=10, ipadx=27, ipady=5)

        self.menu_fac.menu = tk.Menu(self.menu_fac, tearoff=0)
        self.menu_fac['menu'] = self.menu_fac.menu

        self.gen_fact = tk.IntVar()
        self.lis_fact = tk.IntVar()
        self.menu_fac.menu.add_checkbutton(label='Generar factura', variable=self.gen_fact,  font=('Roboto Mono', 9))
        self.menu_fac.menu.add_checkbutton(label='Listar factura', variable=self.lis_fact,  font=('Roboto Mono', 9))
       
        

    # IMPLEMENTACION DE LA VISTA PRINCIPAL
        self.main_view()


# ----------------- FUNCIONES PARA MOSTRAR LAS DEMAS VISTAS ---------------------------------

    # Muestra la imagen del logo y lema
    def ImageLogo(self):
        self.frame1 = tk.Frame(self.main_content, bg='white', width=550)
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.label1 = tk.Label(self.frame1,text="MEGAMERCADO", font=('Roboto Mono', 35), bg='white').place(relx=0.40, rely=0.65)
        self.label2 = tk.Label(self.frame1,text="Calidad y Confianza", font=('Roboto Mono', 20), bg='white').place(relx=0.53, rely=0.76)
    
    # Muestran los botones de clientes, Proveedores y almacen
    def button(self):
        self.Btn1 = tk.Button(self.frame1, text="Clientes", bg="#EAEAEA", font=('Roboto Mono Semibold', 12), command=self.show_all_cli, width=18, height=2, borderwidth=1).place(relx=0.20,rely=0.20)
        self.Btn2 = tk.Button(self.frame1, text="Proveedores", bg="#EAEAEA", font=('Roboto Mono Semibold', 12), command=self.show_all_providers, width=18, height=2, borderwidth=1).place(relx=0.50,rely=0.20)
        self.Btn3 = tk.Button(self.frame1, text="Almacén", bg="#EAEAEA", font=('Roboto Mono Semibold', 12), width=18, height=2, borderwidth=1).place(relx=0.35,rely=0.45)
        

    # Mostrar registrar producto
    def show_reg_prod(self):
        self.remove_frames()  # Limpia el frame main-content
        self.main_content.grid() # Muestra el main-content limpio
        self._reg = rp(self.main_content)  # Instaciar la clase que contiene la vista y pasarle el frame en que se mostrara
        self._reg.reg_prod() #Mostrar la vista en el frame

    # Mostrar todos los productos resumido
    def show_all_prod(self):
        self.remove_frames()
        self.main_content.grid()
        self._pro = _products(self.main_content)   
        self._pro.prod_titles()   
        self._pro.show_prod()          

    # Mostrar la lista de productos
    def show_list_prod(self):
        self.remove_frames()
        self.main_content.grid()    
        self._lis = lp(self.main_content)  
        self._lis.list_prod()
        self._lis.show_list()
    
     # Mostrar la lista de productos x almacen
    def show_list_prod_alm(self):
        self.remove_frames()
        self.main_content.grid()    
        self._lis_alm = listar_prod_alm(self.main_content)  
        self._lis_alm.list_prod_alm()
        self._lis_alm.show_list_prod_alm()

    # Mostar reporte de ventas
    def show_rpt_ventas(self):
        self.remove_frames()
        self.main_content.grid()   
        self.rpt = rpt_ventas(self.main_content)
        self.rpt.rpt_ventas_title()
        self.rpt.show_rpt_ventas()
        
    # Mostrar la vista principal
    def main_view(self):
        self.remove_frames()
        self.main_content.grid()
        self.ImageLogo()
        self.button()

    # Mostrar la lista de clientes
    def show_all_cli(self):
        self.remove_frames()
        self.main_content.grid()
        self._cli = listar_clientes(self.main_content)
        self._cli.list_cli_title()
        self._cli.show_list_cli()

    # Mostrar todos los proveedores
    def show_all_providers(self):
        self.remove_frames()
        self.main_content.grid()
        self._prov = listar_proveedores(self.main_content)
        self._prov.list_prov_title()
        self._prov.show_list_prov()

    # Limpiar el main-content frame principal
    def remove_frames(self):
        for widget in self.main_content.winfo_children(): # Toma todos los widgets de ese frame
            widget.destroy()                             # Destruye los widgets

        
if __name__ == '__main__':
    master = tk.Tk()
    _App = Application(master)
    master.mainloop()
    



