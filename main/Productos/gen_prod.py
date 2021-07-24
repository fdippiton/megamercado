
import tkinter as tk
from tkinter import ttk
from tkinter.font import families
from fonts import *


class reg_prod_view():
    def __init__(self, _frame):
        self._frame = _frame

    def reg_prod(self):
        # Creating product register
        self.reg_prod_title = tk.Label(self._frame, text='Registro de producto', font=('Roboto Mono', 15), width=40, height=2, bg='white', anchor='s').grid(row=1, column=2, ipady=6, pady=15, sticky='ew')

            # Creating Code
        self.code = tk.Label(self._frame, text='Código: ', font=('Roboto Mono', 12), bg='white').grid(row=2, column=1, sticky='e')
        self.cod_entry = tk.Entry(self._frame, width=70).grid(row=2, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

            # Creating Name
        self.name = tk.Label(self._frame, text='Nombre: ', font=('Roboto Mono', 12), bg='white').grid(row=3, column=1, sticky='e')
        self.name_entry = tk.Entry(self._frame, width=70).grid(row=3, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

            # Creating Price
        self.sale_price = tk.Label(self._frame, text='Precio de Venta: ', font=('Roboto Mono', 12), bg='white').grid(row=4, column=1, sticky='e')
        self.Sale_price_entry = tk.Entry(self._frame, width=70).grid(row=4, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

            # Creating Supplier
        self.supplier = tk.Label(self._frame, text='Proveedor: ', font=('Roboto Mono', 12), bg='white').grid(row=5, column=1, sticky='e')
        self.supp_entry = tk.Entry(self._frame, width=70).grid(row=5, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

            # Creating Amount
        self.amount = tk.Label(self._frame, text='Cantidad: ', font=('Roboto Mono', 12), bg='white').grid(row=6, column=1, sticky='e')
        self.amount_entry = tk.Entry(self._frame, width=70).grid(row=6, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

            # Creating No. Almacen
        self.No_alm = tk.Label(self._frame, text='No. Almacén: ', font=('Roboto Mono', 12), bg='white').grid(row=7, column=1, sticky='e')
        self.No_alm_entry = tk.Entry(self._frame, width=70).grid(row=7, column=2, ipady=8, ipadx=5, pady=12, sticky='w')

        # Creating buttons
        self.btn_register = tk.Button(self._frame, text='Registrar', font=('Roboto Mono', 12), bg='#21A7DA', width=20, pady=5).grid(row=9, column=2, sticky='w')
        self.btn_delete = tk.Button(self._frame, text='Borrar todo', font=('Roboto Mono', 12), bg='#E10D0D', width=20, pady=5).grid(row=9, column=2, sticky='e')