
import tkinter as tk
from tkinter import ttk
from tkinter.font import families


class reg_prod_view():
    def __init__(self, _frame):
        self._frame = _frame

    def reg_prod(self):
        # Creating product register
        self.reg_prod_title = tk.Label(self._frame, text='Registro de producto', font=('Segoe UI Semilight', 10), width=150).grid(row=1, column=1, ipady=6, sticky='ew')

            # Creating Code
        self.code = tk.Label(self._frame, text='Codigo', font=('Calibri', 10)).grid()
        self.cod_entry = tk.Entry(self._frame).grid()

            # Creating Name
        self.name = tk.Label(self._frame, text='Nombre', font=('Segoe UI Semilight', 10)).grid()
        self.name_entry = tk.Entry(self._frame).grid()

            # Creating Price
        self.sale_price = tk.Label(self._frame, text='Precio de Venta', font=('Segoe UI', 10)).grid()
        self.Sale_price_entry = tk.Entry(self._frame).grid()

            # Creating Supplier
        self.supplier = tk.Label(self._frame, text='Proveedor', font=('Segoe UI', 10)).grid()
        self.supp_entry = tk.Entry(self._frame).grid()

            # Creating Amount
        self.amount = tk.Label(self._frame, text='Cantidad', font=('Segoe UI', 10)).grid()
        self.amount_entry = tk.Entry(self._frame).grid()

            # Creating No. Almacen
        self.No_alm = tk.Label(self._frame, text='No. Almacen', font=('Segoe UI', 10)).grid()
        self.No_alm_entry = tk.Entry(self._frame).grid()

        # Creating buttons
        self.btn_register = tk.Button(self._frame, text='Registrar').grid()
        self.btn_delete = tk.Button(self._frame, text='Borrar todo').grid()