from tkinter.constants import COMMAND
from tkinter.ttk import Treeview
import pyodbc
import tkinter as tk
from tkinter import messagebox
#import Productos.gen_prod


class _db():
    def __init__(self):
        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};''SERVER='+self.server+';' 'DATABASE='+self.db+';' 'Trusted_Connection=yes;')
        self._cursor = self.conn.cursor()
        
        self.validate = 0

    # Registrar productos
    def conn_submit(self, sql_prod, sql_alm, code,  name, price, provider, cost, itbis, estatus):
        try:
            self._cursor.execute(sql_prod, code, name, price, provider, cost, itbis, estatus)

            self._cursor.execute(sql_alm, code)

            self.conn.commit()
            self._cursor.close()
            self.conn.close()
            messagebox.showinfo(title='Registro de producto', message='Producto registrado exitosamente')
        except:
            messagebox.showerror(title='Registro de producto', message='Ha ocurrido un error al registrar producto')
            raise

    # Listar todos los productos en reporte
    def retrieve_prod(self, _table):
        try:
            self.sql = 'SELECT * FROM dbo.Productos'
            self._tree = _table

            for row in self._cursor.execute(self.sql):
                self._tree.insert('', 0, values= (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                
            self._cursor.close()
            self.conn.close()
        except:
                raise 

    # Inactivar producto
    def inactive_prod(self, treeview, _table):
        self._treeview = treeview
        self._table = _table
        try:
            self.item = self._treeview.item(self._treeview.selection())['values'][0]
            self.sql = '''UPDATE dbo.Productos SET Prod_Estatus='I' WHERE Prod_Codigo={}'''.format(self.item)
            self._cursor.execute(self.sql)
            self._cursor.commit()
            
            self._treeview.destroy()
            self._table()
                
            self._cursor.close()
            self.conn.close()
        except:
            raise

    # Listar todos los productos en reporte por almacen
    def retrieve_prod_alm(self, _table):
        try:
            self.sql_prod = 'SELECT Prod_Nombre, Prod_CostoUnidad, Alm_Producto, Alm_ValorInvertario, Alm_UnidadesDisponibles FROM dbo.Productos FULL OUTER JOIN dbo.Almacenes ON (Prod_Codigo = Alm_Producto)'
            self._tree = _table

            for row in self._cursor.execute(self.sql_prod):
                self._tree.insert('', 0, values= (row[2], row[0], row[1], row[3], row[4]))
            
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
    # Retorna el producto a editar
    def retrieve_edit_prod(self, heading_code, name, price, provider, cost, itbis):
        self.heading_code = heading_code
        self.name = name
        self.price = price
        self.provider = provider
        self.cost = cost
        self.itbis = itbis

        try:
            self.sql = 'SELECT Prod_Nombre, Prod_PrecioVenta, Prod_Proveedor, Prod_CostoUnidad, Prod_ITBIS FROM dbo.Productos WHERE Prod_Codigo={}'.format(self.heading_code)
            self.items = self._cursor.execute(self.sql)
            print(self.items)

            self._values = []

            for row in self.items:
                self._values.append(row)
                
            self.name.set( self._values[0][0])
            self.price.set( self._values[0][1])
            self.provider.set( self._values[0][2])
            self.cost.set( self._values[0][3])
            self.itbis.set( self._values[0][4])

            self._cursor.close()
            self.conn.close()
        except:
                raise 
   
    # Guardar producto editado
    def save_edit(self, name, price, provider, cost, itbis, item_code):

        self.name = name
        self.price = price
        self.provider = provider
        self.cost = cost
        self.itbis = itbis
        self.item_code = item_code

        self.sql = 'UPDATE dbo.Productos SET Prod_Nombre=?, Prod_PrecioVenta=?, Prod_Proveedor=?, Prod_CostoUnidad=?, Prod_ITBIS=? WHERE Prod_Codigo=?'
        self._values = (self.name, self.price, self.provider, self.cost, self.itbis, self.item_code)
        try:
            self._cursor.execute(self.sql, self._values)
            self.conn.commit()


            self._cursor.close()
            self.conn.close()
            messagebox.showinfo(title='Registro de producto', message='Producto editado se guardo exitosamente')
        except:
            messagebox.showinfo(title='Registro de producto', message='Ha ocurrido un error al registrar producto')
            raise

    # Recuperar todos los productos activos
    def retrieve_all_prod(self, _frame, _table):
        try:
            self.sql = '''SELECT Prod_codigo, Prod_Nombre  FROM dbo.Productos WHERE Prod_Estatus='A' '''
            self._tree = _table
            self._frame = _frame

            for row in self._cursor.execute(self.sql):
                self._tree.insert('', 0, values= (row[0], row[1]))
                
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
    # Calcular y obtener el numero total de productos
    def retrieve_total_prod(self):
        try:
            self.sql = '''SELECT Prod_codigo FROM dbo.Productos WHERE Prod_Estatus='A' '''
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total += 1
                
            self._cursor.close()
            self.conn.close()

            return self.total
        except:
                raise 
    
    # Calcular y obtener el valor total de todos los productos del inventario
    def retrieve_total_val_inv(self):
        try:
            self.sql = 'SELECT Alm_ValorInvertario FROM dbo.Almacenes WHERE Alm_ValorInvertario >= 0'
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total = self.total + row
                
            self._cursor.close()
            self.conn.close()

            return self.total
            #print(self.total)
        except:
                raise 

    # Calcular y obtener el numero total de productos disponibles
    def retrieve_total_uni_disp(self):
        try:
            self.sql = 'SELECT Alm_UnidadesDisponibles FROM dbo.Almacenes WHERE Alm_UnidadesDisponibles >= 0'
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total = self.total + row
                
            self._cursor.close()
            self.conn.close()

            return self.total
        except:
                raise 
    
    # Obtener todos los clientes
    def retrieve_all_clients(self, _table):
        try:
            self.sql = '''SELECT Cli_Codigo, Cli_Nombres, Cli_Apellidos, Cli_RNC_Cedula, Cli_Telefono, Cli_Direccion FROM dbo.Clientes'''
            self._tree = _table

            for row in self._cursor.execute(self.sql):
                self._tree.insert('', 0, values= (row[0], row[1], row[2], row[3], row[4], row[5]))
                
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
  
    def validate_code(self, _input, _frame):
        self.input = _input
        self._frame = _frame
        try:
            self.sql_ret = 'SELECT Prod_Codigo FROM dbo.Productos'
            self.code_array = []
            self.str_code_array = []

            for item in self._cursor.execute(self.sql_ret):
                self.code_array.append(item[0])
        
            for row in self.code_array:
                self._val = str(row)
                self.str_code_array.append(self._val)

            self.values = self.input in self.str_code_array
            #print(self.values)

            if self.values:
                #print("Esta registrado")
                tk.Label(self._frame, text='Se encuentra registrado', background='#EAEAEA', foreground='#E8222D', font=('Roboto Mono', 8), width=50).grid(row=1, column=2, sticky='w', ipady=5)
            else:
                tk.Label(self._frame, text='Correcto', background='#EAEAEA', foreground='#E8222D', font=('Roboto Mono', 8), width=50).grid(row=1, column=2, sticky='w', ipady=5)
                self.validate = 1
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
    def no_duplicate(self):
        return self.validate



