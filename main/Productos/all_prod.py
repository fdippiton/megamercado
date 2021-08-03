import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db



class _products():
    def __init__(self, _frame):
        self._frame = _frame

        self.Prod_Codigo = tk.IntVar()
        self.Prod_Nombre = tk.StringVar()
        self.Prod_PrecioVenta = tk.IntVar()
        self.Prod_Proveedor = tk.StringVar()
        self.Prod_CostoUnidad = tk.IntVar()
        self.Prod_ITBIS = tk.IntVar()

        # Treeview para mostrar todos los productos
        self.tree_Table = ttk.Treeview(self._frame, height=11, columns=('#1', '#2'), show='headings')

    # Titulos de esta vista
    def prod_titles(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white', width=18)
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=380, pady=20, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Editar productos', font=('Roboto Mono', 13), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=380, pady=5, sticky='ew')

    # Mostrar todos los productos en el treeview
    def show_prod(self):
        self.tree_Table.grid(row=3, column=0, columnspan=2, pady=50)
        self.tree_Table.heading('#1', text='Codigo', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=250, stretch='NO')
        self.tree_Table.heading('#2', text='Producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=250, stretch='NO')
       
        self._retrieve_all = _db()
        self._retrieve_all.retrieve_all_prod(self._frame, self.tree_Table)
        self.edit_btn = tk.Button(self._frame, text='Editar', font=('Roboto Mono', 12), bg='white', width=15, command=self.update_view).grid(row=6, column=0, columnspan=2, pady=15)


    # Mostrar la vista de edicion
    def update_view(self):
        self.heading_selected_code = self.tree_Table.item(self.tree_Table.selection())['values'][0]
        self.update_product = _db()
        
        for widget in self._frame.winfo_children():
            widget.destroy()
 
        self.reg_prod_title = tk.Label(self._frame, text='Editar producto', font=('Roboto Mono', 15), bg='white', width=20, pady=50)
        self.reg_prod_title.grid(row=0, column=0, columnspan=2, padx=360, pady=30, sticky='ew')

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


        self.btn_update = tk.Button(self._frame, text='Guardar', font=('Roboto Mono', 12), bg='#21A7DA', width=15, pady=3, command= lambda: self.save_edit_btn(self.heading_selected_code)).grid(row=9, column=0, columnspan=2, pady=(60, 60))
        self.btn_cancel = tk.Button(self._frame, text='Cancelar', font=('Roboto Mono', 12), bg='#E10D0D', width=15, pady=3, command=self.show_prod).grid(row=9, column=1, columnspan=2, pady=(60, 60))

        self.update_product.retrieve_edit_prod(self.heading_selected_code, self.Prod_Nombre, self.Prod_PrecioVenta, self.Prod_Proveedor, self.Prod_CostoUnidad, self.Prod_ITBIS)


    # Guardar el producto editado en la DB
    def save_edit_btn(self, item_code):
        self.item_code = item_code

        self.nameP = self.Prod_Nombre.get()
        self.price =  self.Prod_PrecioVenta.get()
        self.supplierP = self.Prod_Proveedor.get()
        self.costo = self.Prod_CostoUnidad.get()
        self.itbisP = self.Prod_ITBIS.get()

        try:
            self._edit_db = _db()
            self._edit_db.save_edit(self.nameP, self.price, self.supplierP, self.costo, self.itbisP, self.item_code)
        except:
            raise

