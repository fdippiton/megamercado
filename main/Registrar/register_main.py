
import tkinter as tk
from tkinter import ttk
from tkinter.constants import COMMAND
from tkinter.font import families
import os


# PAGE 1 - Registrarse
class register_view():
    def __init__(self, _frameLeft, _frameRight):
        self._frameLeft = _frameLeft
        self. _frameRight =  _frameRight

    def register_users(self):
        self._logo_image = tk.PhotoImage(file='../megaImage.gif', width=600)
        self._image_label = tk.Label(self._frameLeft, image=self._logo_image, width=600,  height=600, bg='white').grid(column=0, row=0)

        # Register title
        self.register_title = tk.Label(self._frameRight, text='Registrar', font=('Roboto Mono Bold', 15), bg='white', width=50, height=2, anchor='n')
        self.register_title.grid(row=0, column=1, sticky='we', pady=(1, 5))

        # Administrator
        self.adm = tk.Button(self._frameRight, text='Administrador', font=('Roboto Mono', 12), bg='white', width=15, command=self.show_main_page)
        self.adm.grid(row=1, column=1, pady=(1, 20))

        # Client
        self.client = tk.Button(self._frameRight, text='Cliente', font=('Roboto Mono', 12), bg='white', width=15)
        self.client.grid(row=2, column=1, pady=(1, 20))

        # Supplier
        self.prov = tk.Button(self._frameRight, text='Proveedor', font=('Roboto Mono', 12), bg='white', width=15)
        self.prov.grid(row=3, column=1, pady=(1, 40))
        
        # Supplier account
        self.prov = tk.Label(self._frameRight, text='Administrador ¿Ya tienes una cuenta?', font=('Roboto Mono', 10), bg='white')
        self.prov.grid(row=4, column=1)

        # Login
        self.login = tk.Button(self._frameRight, text='Iniciar sesion', font=('Roboto Mono', 9), bg='white', fg='#4731D4')
        self.login.grid(row=5, column=1, pady=(2, 20))

    # def show_main_page(self):
        #path = r'C:\Users\MSI\Desktop\Megamercado\Megamercado\main\root.py'
        #os.sye(r'C:\Users\MSI\Desktop\Megamercado\Megamercado\main\root.py')
