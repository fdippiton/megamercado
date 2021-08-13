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
from Facturacion.gen_fact import gen_factura

from root import App_main

from tkinter import filedialog
import os
import subprocess

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
        self.container = tk.Frame(self.main_win, width=1200, height=600, bg='white')
        self.container.grid(row=0, column=0)
        
        #Frame de la imagen del logo
        self.logo_image = tk.Frame(self.container, width=600, height=600, bg='white')
        self.logo_image.grid(row=0, column=0)
        
        # Frame registrar
        self.register = tk.Frame(self.container, width=600, height=600, bg='white')
        self.register.grid(row=0, column=1)


        self._logo_image = tk.PhotoImage(file='../megaImage.gif', width=600)
        self._image_label = tk.Label(self.logo_image, image=self._logo_image, width=600,  height=600, bg='white').grid(column=0, row=0)

        # Register title
        self.register_title = tk.Label(self.register, text=' ', font=('Roboto Mono Bold', 15), bg='white', width=50, height=2, anchor='n')
        self.register_title.grid(row=0, column=1, sticky='we', pady=(1, 5))

        # Administrator
        self.adm = tk.Button(self.register, text='Administrador', font=('Roboto Mono', 12), bg='white', width=15, command=self._main_view)
        self.adm.grid(row=1, column=1, pady=(1, 20))

        # Client
        #self.client = tk.Button(self.register, text='Cliente', font=('Roboto Mono', 12), bg='white', width=15, command=self.start_cli)
        #self.client.grid(row=2, column=1, pady=(1, 20))

        # Supplier
        #self.prov = tk.Button(self.register, text='Proveedor', font=('Roboto Mono', 12), bg='white', width=15, command=self.start_prov)
        #self.prov.grid(row=3, column=1, pady=(1, 40))
        
        # Supplier account
        #self.prov = tk.Label(self.register, text='Administrador ¿Ya tienes una cuenta?', font=('Roboto Mono', 10), bg='white')
        #self.prov.grid(row=4, column=1)

        # Login
        #self.login = tk.Button(self.register, text='Iniciar sesion', font=('Roboto Mono', 9), bg='white', fg='#4731D4')
        #self.login.grid(row=5, column=1, pady=(2, 20))

    def _main_view(self):
        for widget in self.container.winfo_children(): # Toma todos los widgets de ese frame
            widget.destroy()                             # Destruye los widgets

        self.container.grid()
        self._main = App_main(self.container)
        self._main.main_()


        
if __name__ == '__main__':
    master = tk.Tk()
    _App = Application(master)
    master.mainloop()
    
