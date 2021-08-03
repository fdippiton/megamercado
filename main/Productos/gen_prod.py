
import tkinter as tk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db


class reg_prod_view():
    def __init__(self, _frame):
        self._frame = _frame

        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        

        self.Prod_Codigo = tk.IntVar()
        self.Prod_Nombre = tk.StringVar()
        self.Prod_PrecioVenta = tk.IntVar()
        self.Prod_Proveedor = tk.StringVar()
        self.Prod_CostoUnidad = tk.IntVar()
        self.Prod_ITBIS = tk.IntVar()
        self.Prod_Cantidad = tk.IntVar()
        self.Prod_NoAlmacen = tk.IntVar()

    
    # vista de registrar producto
    def reg_prod(self):
        # Creating product register
        self.reg_prod_title = tk.Label(self._frame, text='Registro de producto', font=('Roboto Mono', 15), bg='white')
        self.reg_prod_title.grid(row=0, column=0, columnspan=2, padx=360, pady=72, sticky='ew')

            # Creating Code
        self.code = tk.Label(self._frame, text='Código: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.code.grid(row=1, column=0, sticky='e', pady=7)
        self.Prod_code  = tk.Entry(self._frame, textvariable=self.Prod_Codigo, width=50).grid(row=1, column=1, sticky='w', padx=5, pady=7)

            # Creating Name
        self.name = tk.Label(self._frame, text='Nombre: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.name.grid(row=2, column=0, sticky='e', pady=7)
        self.Prod_name = tk.Entry(self._frame, textvariable=self.Prod_Nombre, width=50).grid(row=2, column=1, sticky='w', padx=5, pady=7)

            # Creating Price
        self.sale_price = tk.Label(self._frame, text='Precio de Venta: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.sale_price.grid(row=3, column=0, sticky='e', pady=7)
        self.Prod_price = tk.Entry(self._frame, textvariable= self.Prod_PrecioVenta, width=50).grid(row=3, column=1, sticky='w', padx=5, pady=7)

            # Creating Supplier
        self.supplier = tk.Label(self._frame, text='Proveedor: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.supplier.grid(row=4, column=0, sticky='e', pady=7)
        self.Prod_supplier = tk.Entry(self._frame, textvariable=self.Prod_Proveedor, width=50).grid(row=4, column=1, sticky='w', padx=5, pady=7)


            # Creating cost
        self.cost = tk.Label(self._frame, text='Costo de unidad: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.cost.grid(row=5, column=0, sticky='e', pady=7)
        self.Prod_cost = tk.Entry(self._frame, textvariable=self.Prod_CostoUnidad, width=50).grid(row=5, column=1, sticky='w', padx=5, pady=7)

            # Creating itbis
        self.itbis = tk.Label(self._frame, text='Itbis: ', font=('Roboto Mono', 12), bg='white', width=20, anchor='e')
        self.itbis.grid(row=6, column=0, sticky='e', pady=7)
        self.Prod_itbis = tk.Entry(self._frame, textvariable=self.Prod_ITBIS, width=50).grid(row=6, column=1, sticky='w', padx=5, pady=7)

             # Creating buttons
        self.btn_register = tk.Button(self._frame, text='Registrar', font=('Roboto Mono', 12), bg='#21A7DA', width=15, pady=3, command=self._submit).grid(row=9, column=0, columnspan=2, pady=(30, 30))
        self.btn_delete = tk.Button(self._frame, text='Borrar todo', font=('Roboto Mono', 12), bg='#E10D0D', width=15, pady=3, command=self.borrar_todo).grid(row=9, column=1, columnspan=2, pady=(30, 30))

    
    # Guardar formulario en la base de datos
    def _submit(self):
        self.codigo = self.Prod_Codigo.get()
        self.nameP = self.Prod_Nombre.get()
        self.price =  self.Prod_PrecioVenta.get()
        self.supplierP = self.Prod_Proveedor.get()
        self.costo = self.Prod_CostoUnidad.get()
        self.itbisP = self.Prod_ITBIS.get()

        self.sql = 'INSERT INTO dbo.Productos(Prod_Codigo, Prod_Nombre, Prod_PrecioVenta, Prod_Proveedor, Prod_CostoUnidad, Prod_ITBIS, Prod_Estatus) VALUES (?, ?, ?, ?, ?, ?, ?)'
        self.sql_alm = 'INSERT INTO dbo.Almacenes(Alm_Producto) VALUES (?)'
        try:
            self.conexion = _db()
            self.conexion.conn_submit(self.sql, self.sql_alm, self.codigo, self.nameP, self.price, self.supplierP, self.costo, self.itbisP, 'A')
            self.borrar_todo()
        except:
            raise

    # Limpiar los campos del formulario
    def borrar_todo(self):
        self.Prod_Codigo.set('')
        self.Prod_Nombre.set('')
        self.Prod_PrecioVenta.set('')
        self.Prod_Proveedor.set('')
        self.Prod_CostoUnidad.set('')
        self.Prod_ITBIS.set('')
        self.Prod_Cantidad.set('')
        self.Prod_NoAlmacen.set('')

