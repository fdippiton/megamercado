import tkinter as tk
from tkinter import Label, messagebox
from tkinter import Message, ttk
from tkinter.constants import ANCHOR, S, SEL
from tkinter.font import families
from typing import Collection

#from reportlab.lib.utils import c
from fonts import *
import pyodbc
from DB.index import _db


class gen_ped():
    def __init__(self, _frame):
        self._frame = _frame

        self._ped = 0

        self.Prod_Proveedor = tk.StringVar()
        self.Prod_Codigo = tk.IntVar(value='')
        self.Prod_Nombre = tk.StringVar()
        self.Prod_cantidad = tk.IntVar(value='')

        self._subtotal_total = []
        self._total_itbis = []
        self._total_total = []

        self.productos = []
        self.totales = []

        self.tree_Table = ttk.Treeview(self._frame, height=8, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings')
        


    def crear_ped(self):
        self.reg_prod_title = tk.Label(self._frame, text='Crear pedido', font=('Roboto Mono Bold', 15), bg='white', width=80)
        self.reg_prod_title.grid(row=0, column=0, columnspan=3, pady=50)

        #self.num_ped = tk.Label(self._frame, text='No. Pedido: '+str(self._ped)+'', bg='white', font=('Roboto Mono', 11)).grid(row=1, column=0)
        
        self.supplier = tk.Label(self._frame, text='Proveedor: ', font=('Roboto Mono', 11), bg='white', width=20, anchor='e').grid(row=1, column=1, sticky='e')
        self.db_prov  = _db()
        _providers = self.db_prov.retrieve_providers_menu()
        self.Prod_Proveedor.set('Ninguno')
        self.supplier = tk.OptionMenu(self._frame, self.Prod_Proveedor, *_providers).grid(row=1, column=2)


        self.code = tk.Label(self._frame, text='Codigo de producto', bg='white', font=('Roboto Mono', 11)).grid(row=2, column=0)
        self.db_pro  = _db()
        self.Prod_Codigo.set('Ninguno')
        _code = self.db_pro.retrieve_code_prod()
        self.codes = tk.OptionMenu(self._frame, self.Prod_Codigo, *_code).grid(row=3, column=0)
        

        # retrieve_name_prod
        self.name = tk.Label(self._frame, text='Nombre de producto', bg='white', font=('Roboto Mono', 11)).grid(row=2, column=1)
        self.db_pro_name  = _db()
        self.Prod_Nombre.set('Ninguno')
        _name = self.db_pro_name.retrieve_name_prod()
        self.names = tk.OptionMenu(self._frame, self.Prod_Nombre, *_name).grid(row=3, column=1)
        

        self.amount = tk.Label(self._frame, text='Cantidad', bg='white', font=('Roboto Mono', 11)).grid(row=2, column=2)
        self.cantidad = tk.Entry(self._frame, textvariable=self.Prod_cantidad, width=15, bg='#f2f4f6').grid(row=3, column=2)


        self.btn_añadir = tk.Button(self._frame, text='Añadir', font=('Roboto Mono', 11), bg='#21A7DA', width=15, pady=3, command= lambda: self.agregar_prod(self.tree_Table )).grid(row=4, column=0)
        self.btn_delete = tk.Button(self._frame, text='Limpiar', font=('Roboto Mono', 11), bg='#E10D0D', width=15, pady=3, command=self.limpiar).grid(row=4, column=1)

        #self.tree_Table = ttk.Treeview(self._frame, height=8, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings')
        self.tree_Table.grid(row=6, column=0, pady=5, columnspan=3)
        self.tree_Table.heading('#1', text='Código de producto', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre de producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#3', text='Cantidad', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#4', text='Costo unitario', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=125, stretch='NO')
        self.tree_Table.heading('#5', text='Subtotal', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#6', text='Itbis', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=100, stretch='NO')
        self.tree_Table.heading('#7', text='Total a pagar', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=145, stretch='NO')

        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=6, column=4, sticky='nsew')



        self.btn_procesar = tk.Button(self._frame, text='Procesar pedido', font=('Roboto Mono', 11), bg='#21A7DA', width=15, pady=3, command=self._pedir).grid(row=8, column=0, pady=10)
        self.btn_cancel = tk.Button(self._frame, text='Eliminar', font=('Roboto Mono', 11), bg='#E10D0D', width=15, pady=3, command=self.eliminar_elemento).grid(row=8, column=1, pady=10)

        self.btn_cancel = tk.Button(self._frame, text='Cancelar', font=('Roboto Mono', 11), bg='#E10D0D', width=15, pady=3, command=self.cancelar).grid(row=8, column=2, pady=10)


    def agregar_prod(self, _table):

        self._table = _table

        self._Proveedor = self.Prod_Codigo.get()
        self._Codigo = self.Prod_Codigo.get()
        self._Nombre = self.Prod_Nombre.get()
        self._cantidad = self.Prod_cantidad.get()

        #self.productos.append(self._Codigo, self._Nombre, self._cantidad)

        self._db_ = _db()
        self.sql = 'SELECT Prod_CostoUnidad FROM dbo.Productos WHERE Prod_Codigo = {}'.format(self._Codigo)

        self._cursor = self._db_.conn.cursor()
        self.cost = []
        for a in self._cursor.execute(self.sql):
            self.cost.append(a[0])
        
        self._subto = int(self.cost[0]) * self._cantidad
        self._itbis = (self._subto * 0.18)
        self._total = self._subto + (self._subto * 0.18)

        self._table.insert('', 0, values= (str(self._Codigo), self._Nombre, str(self._cantidad), str(self.cost[0]), str(self._subto), str(round(self._itbis, 2)), str(self._total)))

        self._subtotal_total.append(self._subto)
        self._total_itbis.append(self._itbis)
        self._total_total.append(self._total)

        self.sum_subtotal_total = sum(self._subtotal_total)
        self.sum_total_itbis = sum(self._total_itbis)
        self.sum_total_total = sum(self._total_total)

        self.sub = tk.Label(self._frame, text='Subtotal: '+str(self.sum_subtotal_total)+'').grid(row=7, column=0, pady=5)
        self.itbis = tk.Label(self._frame, text='Itbis: '+str(round(self.sum_total_itbis, 2))+'').grid(row=7, column=1, pady=5)
        self.total = tk.Label(self._frame, text='Total a pagar: '+str(self.sum_total_total)+'').grid(row=7, column=2, pady=5)

        self.productos.extend([[self._Codigo, self._Nombre, self._cantidad, self.cost, self._subto]])
        self.totales.extend([self.sum_total_total])
        


    def _pedir(self):

        self._db_ = _db()
        self._cursor = self._db_.conn.cursor()

        self.number_ped = []

        self.num_p = 'SELECT MAX(Ped_NoPedido) FROM Pedidos'
        for i in self._cursor.execute(self.num_p):
            self.b = int(i[0])
            self.number_ped.append(self.b + 1)
        
        self._Proveedor_ = self.Prod_Proveedor.get()
        self.prov_code = 'SELECT Prov_Codigo, Prov_Nombre FROM dbo.Proveedores'
        self.code_prov = []
        for i in self._cursor.execute(self.prov_code):
            if str(i[1]) == self._Proveedor_:
                print(i[1])
                self.code_prov.append(i[0])
        print(self.code_prov[0])

        self.sql = 'INSERT INTO dbo.Pedidos VALUES(?,?,?)'
        self._cursor.execute(self.sql, self.number_ped[0], self.totales[0], self.code_prov[0])
        

        for prod in self.productos:
            self.num_pedido = self.number_ped[0]
            self._Proveedor = self.Prod_Proveedor.get()
            self._Codigo = prod[0]
            self._Nombre = prod[1]
            self._cantidad = prod[2]
            self.cost = prod[3]
            self._subto = prod[4]
            
            self._val_in = []
            self._sql_in = 'SELECT Alm_Valorinventario FROM dbo.Almacenes WHERE (Alm_Producto = {})'.format(self._Codigo)
            
            try:
                for i in self._cursor.execute(self._sql_in):
                    if i[0] is None:
                        self._val_in.append(0)
                    else:
                        self._val_in.append(i[0])
                self._val = sum(self._val_in)
                print('Se obtuvo el valor de inventario')
                print(self._val)
            except:
                print('No se obtuvo el valor del inventario')
                raise


            self._uni = []
            self._sql_uni = 'SELECT Alm_UnidadesDisponibles FROM dbo.Almacenes WHERE (Alm_Producto = {})'.format(self._Codigo)
            
            try:
                for i in self._cursor.execute(self._sql_uni):
                    if i == None:
                        i = 0 
                        self._uni.append(i)
                    else:
                        self._uni.append(i)
                self._uni = sum(self._val_in)
                print('Se obtuvieron las unidades disponibles')
                print(self._uni)
            except:
                print('No se obtuvo las unidades disponibles')
                raise


            self._sql = 'INSERT INTO dbo.DetallePedido VALUES(?, ?, ?, ?, ?)'


            self.alm_inv_ = self._val +  self.cost[0]
            self.alm_uni_dis = self._uni + self._cantidad

 
            self._alm_val = 'UPDATE dbo.Almacenes SET Alm_ValorInventario=? WHERE Alm_Producto=?'
            self._alm_uni = 'UPDATE dbo.Almacenes SET Alm_UnidadesDisponibles=? WHERE Alm_Producto=?'


            try:
                #self._cursor.execute(self.sql, self.number_ped[0], self.sum_total_total, self.code_prov[0])
                self._cursor.execute(self._sql, self.num_pedido, self._cantidad, self._Codigo, self._Nombre, self._Codigo)
                self._cursor.execute(self._alm_val, self.alm_inv_, self._Codigo)
                self._cursor.execute(self._alm_uni, self.alm_uni_dis, self._Codigo)
                #self._cursor.execute(self._alm_val)
                #self._cursor.execute(self._alm_uni)
            except:
                print('No se insertaron bien los registros')
                raise
       
        self._db_.conn.commit()
        self._cursor.close()
        self._db_.conn.close()

    def limpiar(self):
        self.Prod_Proveedor.set('Ninguno')
        self.Prod_Codigo.set('Ninguno')
        self.Prod_Nombre.set('Ninguno')
        self.Prod_cantidad.set('')



    def eliminar_elemento(self):
        self.heading_selected_code = self.tree_Table.selection()[0]

        self.tree_Table.delete(self.heading_selected_code)

    def cancelar(self):

        self.Prod_Proveedor.set('Ninguno')
        self.Prod_Codigo.set('Ninguno')
        self.Prod_Nombre.set('Ninguno')
        self.Prod_cantidad.set('')

        self._subtotal_total.delete()
        self._total_itbis.delete()
        self._total_total.delete()

        self.heading_selected_code = self.tree_Table.get_children()
        for i in self.heading_selected_code:
            self.tree_Table.delete(i)

     