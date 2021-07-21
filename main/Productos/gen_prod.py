
import tkinter as tk
from tkinter import ttk
from tkinter.font import families


class main_view():
    def __init__(self, _frame):
        self._frame = _frame

    def main_page_view(self):
        # Creating title megamercado
        self.main_title_reg_pro = tk.Label(self._frame, text='MegaMercado', font=('Segoe UI semibold', 15), bg='#16ADB2', fg='white', width=150, anchor='s')
        self.main_title_reg_pro.grid(row=0, column=0, sticky='ew', ipady=10)

        # Creating product register
        self.reg_prod_title = tk.Label(self._frame, text='Registro de productos', font=('Segoe UI Semilight', 10), bg='#16ADB2', fg='white', width=150).grid(row=1, column=0, ipady=6, sticky='ew')
        #self.btn_reg_prod_quit = Button(self._frame, text='X').grid(row=0, column=3, sticky=NE)

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