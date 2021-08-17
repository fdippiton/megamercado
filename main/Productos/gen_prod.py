
import re
import tkinter as tk
from tkinter import Label, messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from typing import Text
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

        self.Prod_Codigo = tk.IntVar(value='')
        self.Prod_Nombre = tk.StringVar()
        self.Prod_PrecioVenta = tk.IntVar(value='')
        self.Prod_Proveedor = tk.StringVar()
        self.Prod_CostoUnidad = tk.IntVar(value='')
        #self.Prod_ITBIS = tk.IntVar(value='')

        self.Precio_venta = ''
        self.Costo_uni = ''

        #self.valid_values = False


        self.reg_cod = self._frame.register(self.validar_codigo) 
        self.reg_nom = self._frame.register(self.validar_nombre)
        self.reg_price = self._frame.register(self.validar_precio)
        #self.reg_prov = self._frame.register(self.validar_proveedor)
        self.reg_cost = self._frame.register(self.validar_costo)
        #self.reg_itbis = self._frame.register(self.validar_itbis)

        self.comment = tk.Label(self._frame, text='', background='White', foreground='#E8222D', font=('Roboto Mono', 8), width=50)
        self.comment.grid(row=1, column=2, sticky='w', ipady=5)
        self.valid_name = tk.Label(self._frame, text='', background='white', foreground='#E8222D', font=('Roboto Mono', 8), width=50)
        self.valid_name.grid(row=2, column=2, sticky='w', ipady=5)
        self.valid_price = tk.Label(self._frame, text='', background='white', foreground='#E8222D', font=('Roboto Mono', 8), width=50)
        self.valid_price.grid(row=3, column=2, sticky='w', ipady=5)
        self.valid_cost = tk.Label(self._frame, text='', background='white', foreground='#E8222D', font=('Roboto Mono', 8), width=50)
        self.valid_cost.grid(row=5, column=2, sticky='w', ipady=5)
                    
        

    # vista de registrar producto
    def reg_prod(self):
        # Creating product register
        self.reg_prod_title = tk.Label(self._frame, text='Registro de producto', font=('Roboto Mono Bold', 15), bg='white', width=80)
        self.reg_prod_title.grid(row=0, column=0, columnspan=3, pady=72)

        # Creating Code
        self.code = tk.Label(self._frame, text='Código: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        self.code.grid(row=1, column=0, sticky='e', pady=7)
        self.Prod_code  = tk.Entry(self._frame, textvariable=self.Prod_Codigo, width=45, bg='#f2f4f6', validate='all', validatecommand=(self.reg_cod, '%S', '%P')).grid(row=1, column=1, sticky='w', padx=5, pady=7, ipady=4)
         # Creating Name
        self.name = tk.Label(self._frame, text='Nombre: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        self.name.grid(row=2, column=0, sticky='e', pady=7)
        self.Prod_name = tk.Entry(self._frame, textvariable=self.Prod_Nombre, width=45, bg='#f2f4f6', validate='all', validatecommand=(self.reg_nom, '%S', '%P')).grid(row=2, column=1, sticky='w', padx=5, pady=7, ipady=4)

          
        # Creating Price
        self.sale_price = tk.Label(self._frame, text='Precio de Venta: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        self.sale_price.grid(row=3, column=0, sticky='e', pady=7)
        self.Prod_price = tk.Entry(self._frame, textvariable= self.Prod_PrecioVenta, width=45, bg='#f2f4f6', validate='all', validatecommand=( self.reg_price, '%S', '%P')).grid(row=3, column=1, sticky='w', padx=5, pady=7, ipady=4)

        # Creating Supplier
        self.supplier = tk.Label(self._frame, text='Proveedor: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        self.supplier.grid(row=4, column=0, sticky='e', pady=7)
        #self.Prod_supplier = tk.Entry(self._frame, textvariable=self.Prod_Proveedor, width=45, bg='#f2f4f6', validate='all', validatecommand=(self.reg_prov, '%P')).grid(row=4, column=1, sticky='w', padx=5, pady=7, ipady=4)

        self.db_prov  = _db()
        _providers = self.db_prov.retrieve_providers_menu()
 
        self.Prod_Proveedor.set('Ninguno')
        self.supplier = tk.OptionMenu(self._frame, self.Prod_Proveedor, *_providers).grid(row=4, column=1, sticky='w', padx=5, pady=7, ipady=4)
        

        # Creating cost
        self.cost = tk.Label(self._frame, text='Costo de unidad: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        self.cost.grid(row=5, column=0, sticky='e', pady=7)
        self.Prod_cost = tk.Entry(self._frame, textvariable=self.Prod_CostoUnidad, width=45, bg='#f2f4f6', validate='all', validatecommand=(self.reg_cost, '%S', '%P')).grid(row=5, column=1, sticky='w', padx=5, pady=7, ipady=4)
        
        # Creating itbis
        #self.itbis = tk.Label(self._frame, text='Itbis: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e')
        #self.itbis.grid(row=6, column=0, sticky='e', pady=7)
        #self.Prod_itbis = tk.Entry(self._frame, textvariable=self.Prod_ITBIS, width=45, bg='#f2f4f6', validate='all', validatecommand=(self.reg_itbis, '%P')).grid(row=6, column=1, sticky='w', padx=5, pady=5, ipady=4)
        
        # Creating buttons
        self.btn_register = tk.Button(self._frame, text='Registrar', font=('Roboto Mono', 11), bg='#21A7DA', width=15, pady=3, command=self._submit).grid(row=9, column=0, columnspan=2, pady=(45, 45))
        self.btn_delete = tk.Button(self._frame, text='Borrar todo', font=('Roboto Mono', 11), bg='#E10D0D', width=15, pady=3, command=self.borrar_todo).grid(row=9, column=1, columnspan=2, pady=(45, 45))

    # Guardar formulario en la base de datos
    def _submit(self):
        #if self.valid_values == True:


            try:
                self.codigo = self.Prod_Codigo.get()
                self.nameP = self.Prod_Nombre.get()
                self.price = self.Prod_PrecioVenta.get()
                self.supplierP = self.Prod_Proveedor.get()
                self.costo = self.Prod_CostoUnidad.get()
                #self.itbisP = self.Prod_ITBIS.get()


                self.sql = 'INSERT INTO dbo.Productos(Prod_Codigo, Prod_Nombre, Prod_PrecioVenta, Prod_Proveedor, Prod_CostoUnidad, Prod_Estatus) VALUES (?, ?, ?, ?, ?, ?)'
                self.sql_alm = 'INSERT INTO dbo.Almacenes(Alm_Producto) VALUES (?)'
                self.conn_provider = _db()
                
                # Obtener codigo de proveedor
                self._code_ = self.conn_provider.retrieve_code_prov(self.supplierP)
                self.conexion = _db()
                self.conexion.conn_submit(self.sql, self.sql_alm, self.codigo, self.nameP, self.price, self._code_, self.costo, 'A')
                self.borrar_todo()
            except:
                messagebox.showerror(title='Registro de producto', message='Complete la informacion correctamente')
                #raise
        #else:
            #messagebox.showerror(title='Registro de producto', message='Complete la informacion correctamente')


    # Limpiar los campos del formulario
    def borrar_todo(self):
        self.Prod_Codigo.set('')
        self.Prod_Nombre.set('')
        self.Prod_PrecioVenta.set('')
        self.Prod_Proveedor.set('Ninguno')
        self.Prod_CostoUnidad.set('')
        #self.Prod_ITBIS.set('')


    # Validacion de codigo
    def validar_codigo(self, _input, new):
        if len(new) < 1:
            self.comment.config(text='Invalido! Esta vacio')

        else:
            self.new_conn = _db()
            self.new_conn.validate_code(new, self._frame)
            self.value = self.new_conn.no_duplicate()
            if self.value == 1:
                self.comment.config(text='')
            else:
                self.comment.config(text='Se encuentra registrado')
            
            if len(new) > 11:
                return False
            else:
                self.comment.config(text='')
        return _input.isdecimal()

    # Validacion de nombre
    def validar_nombre(self, _input, new):
        if len(new) < 1:
            self.valid_name.config(text='Invalido! Esta vacio')
        else:
            self.valid_name.config(text='')
        #return False
        return _input.isalnum()


    
    # Validar precio
    def validar_precio(self, _input, new):
        # Precio de venta
        self.Precio_venta = new
        self.uni_cost = ''

        try:
            if self.Costo_uni == '':
                self.Costo_uni = 0
                self.uni_cost = self.Costo_uni
            else:
                self.uni_cost = int(self.Costo_uni)
            
        
            if len(new) < 1:
                self.valid_price.config(text='Invalido! Esta vacio')
                #return False
            else:
                self.valid_price.config(text='')
                self.num = int(new)
                if self.num == 0:
                    self.valid_price.config(text='El precio no puede ser cero')
                    #return False
                else:
                    if self.num  <= self.uni_cost:
                        self.valid_price.config(text='El precio de venta no \n puede ser menor que el costo')
                    else:
                        self.valid_price.config(text='')
                        return True
        except:
            self.valid_price.config(text='No se aceptan letras')
            return False
                        
        return _input.isdecimal()
    
    
    def validar_costo(self, _input, new):
        # Costo de unidad
        self.Costo_uni = new
         
        #self.input = new
        self.sale_price = 0
        
        try:
            if self.Precio_venta == '':
                self.Precio_venta = 0
                self.sale_price = int(self.Precio_venta)
            else:
                self.sale_price = int(self.Precio_venta)
                
            
            if len(new) < 1:
                self.valid_cost.config(text='Invalido! Esta vacio')
                #return False
            else:
                self.valid_cost.config(text='')
                #if self.input.isdecimal():
                self.num = int(new)
                if (self.num <= self.sale_price) and  self.num != '':
                    self.valid_cost.config(text='')
                    #return True
                else:
                    self.valid_cost.config(text='El costo no puede ser \n mayor que el precio de venta')
                #else:
                #self.valid_cost.config(text='')
                return True
        except:
            self.valid_cost.config(text='No se acepta letras')
            return False
    
        return _input.isdecimal()

