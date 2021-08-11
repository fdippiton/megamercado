from tkinter.constants import COMMAND
from tkinter.ttk import Treeview
import pyodbc
import tkinter as tk
from tkinter import messagebox

from reportlab.lib.utils import prev_this_next
#import Productos.gen_prod


class _db():
    def __init__(self):
        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};''SERVER='+self.server+';' 'DATABASE='+self.db+';' 'Trusted_Connection=yes;')
        self._cursor = self.conn.cursor()
        

        # Para validacion de codigo de producto
        self.validate = 0

    # Registrar productos
    def conn_submit(self, sql_prod, sql_alm, code,  name, price, provider, cost, estatus):
        try:
            self._cursor.execute(sql_prod, code, name, price, provider, cost, estatus)

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
            self.sql_prod = 'SELECT Prod_Nombre, Prod_CostoUnidad, Alm_Producto, Alm_ValorInventario, Alm_UnidadesDisponibles FROM dbo.Productos FULL OUTER JOIN dbo.Almacenes ON (Prod_Codigo = Alm_Producto)'
            self._tree = _table

            for row in self._cursor.execute(self.sql_prod):
                self._tree.insert('', 0, values= (row[2], row[0], row[1], row[3], row[4]))
            
            self._cursor.close()
            self.conn.close()
        except:
                raise

    # Generar reporte de los productos x almacen
    def retrieve_rpt_prod_alm(self):
        try:
            #self.sql = '''SELECT * FROM dbo.Almacenes'''
            self.sql = 'SELECT Prod_Nombre, Prod_CostoUnidad, Alm_Producto, Alm_ValorInventario, Alm_UnidadesDisponibles FROM dbo.Productos FULL OUTER JOIN dbo.Almacenes ON (Prod_Codigo = Alm_Producto)'
            self.prods = []

            for row in self._cursor.execute(self.sql):
                self.prods.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prods
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
            self.sql = '''SELECT Prod_Codigo, Prod_Nombre  FROM dbo.Productos WHERE Prod_Estatus='A' '''
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
            self.sql = '''SELECT Prod_Codigo FROM dbo.Productos WHERE Prod_Estatus='A' '''
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total += 1
                
            self._cursor.close()
            self.conn.close()

            return self.total
        except:
                raise 
    
    # Generar reporte de productos productos 
    def retrieve_rpt_prod(self):
        try:
            self.sql = '''SELECT * FROM dbo.Productos'''
            self.prods = []

            for row in self._cursor.execute(self.sql):
                self.prods.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prods
        except:
                raise 

    # Generar reporte de proveedores
    def retrieve_rpt_prov(self):
        try:
            self.sql = '''SELECT * FROM dbo.Proveedores'''
            self.prov = []

            for row in self._cursor.execute(self.sql):
                self.prov.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prov
        except:
                raise 
    
    # Mostrar el total de proveedores
    def retrieve_total_prov(self):
        try:
            self.sql = '''SELECT Prov_Codigo FROM dbo.Proveedores WHERE Prov_Estatus='A' '''
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
            self.sql = 'SELECT Alm_ValorInventario FROM dbo.Almacenes WHERE Alm_ValorInventario >= 0'
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total = self.total + row
                
            self._cursor.close()
            self.conn.close()

            return self.total
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
    
    # Generar reporte de clientes
    def retrieve_rpt_cli(self):
        try:
            self.sql = '''SELECT Cli_Codigo, Cli_Direccion, Cli_Nombres, Cli_Apellidos, Cli_RNC_Cedula, Cli_Telefono  FROM dbo.Clientes'''
            self.cli = []

            for row in self._cursor.execute(self.sql):
                self.cli.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.cli
        except:
                raise 
    
        # Generar reporte de ventas
    def retrieve_rpt_sales(self, _table, _frame):
        self._frame = _frame
        self._table = _table
        try:
            #self.rpt = []
            self.sales = []
            self._prods = 'SELECT Prod_Codigo FROM dbo.Productos'

            self.total_sales = 0
            self.total_benefits = 0
            self.total_itbis = 0

            for row in self._cursor.execute(self._prods):
                self.sales.append(int(row[0]))

            for code in self.sales:
                self.sql = 'SELECT Det_Producto, Det_Cantidad, Prod_Codigo, Prod_Nombre, Prod_CostoUnidad, Prod_PrecioVenta  FROM DetalleFacturas INNER JOIN Productos ON (Det_Producto = Prod_Codigo) WHERE (Det_Producto = {} and Det_Cantidad > 0)'.format(code)
                self.sale_price = 0
                self.sale_amount = 0
                self.final_sales = 0
                self.costo = 0
                self.benefits = 0
                self.itbis = 0
                self._itbis = 0.18
                

                self.pro_c = ''
                self.pro_name = ''
                
                for row in self._cursor.execute(self.sql):
                    if row[1] == 0:
                        print('es cero')
                    else:
                        self.sale_amount = self.sale_amount + row[1]
                        self.sale_price = row[5]
                        self.costo = row[4]
                        self.final_sales = self.sale_price * self.sale_amount
                        self.itbis = float(self.final_sales) * self._itbis
                        self.benefits = self.final_sales - (self.costo * self.sale_amount) - int(self.itbis)
                        self.pro_c = row[0]
                        self.pro_name = row[3]

                
                if self.sale_amount == 0:
                    print('Esta vacio')
                else:
                    self.total_sales = self.total_sales + self.final_sales
                    self.total_benefits = self.total_benefits + self.benefits
                    self.total_itbis = self.total_itbis + self.itbis
                    self._table.insert('', 0, values=(self.pro_c, self.pro_name, self.sale_amount, self.costo, self.sale_price, self.itbis, self.final_sales))

                self.num_total_sale = tk.Label(self._frame, text='Total en ventas: '+str(self.total_sales)+'   Total itbis: '+str(self.total_itbis)+'   Ganancias totales: '+str(self.total_benefits)+'', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0)
                #self.num_total_benefits= tk.Label(self._frame, text='Ganancias: '+str(self.total_benefits)+'', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=1)
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
    
    # Obtener el total de clientes
    def retrieve_total_cli(self):
        try:
            self.sql = '''SELECT Cli_Codigo FROM dbo.Clientes WHERE Cli_Estatus='A' '''
            self.total = 0

            for row in self._cursor.execute(self.sql):
                self.total += 1
                
            self._cursor.close()
            self.conn.close()

            return self.total
        except:
                raise 

    # Obtener los proveedores
    def retrieve_providers(self, _table):
        try:
            self.sql = '''SELECT Prov_Codigo, Prov_Direccion, Prov_Nombre,  Prov_Tipo, Prov_Telefono, Prov_RNC FROM dbo.Proveedores'''
            self._tree = _table

            for row in self._cursor.execute(self.sql):
                self._tree.insert('', 0, values= (row[0], row[2], row[1], row[5], row[4], row[3]))
                
            self._cursor.close()
            self.conn.close()
        except:
                raise 
    
    def retrieve_providers_menu(self):
        try:
            self.sql = '''SELECT Prov_nombre  FROM dbo.Proveedores'''
            self.prov = []

            self._array_ = self._cursor.execute(self.sql)

            for row in self._array_:
                self.prov.append(str(row[0]))

            #for row in self._cursor.execute(self.sql):
                #self.prov.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prov
        except:
                raise 

    def retrieve_code_prod(self):
        try:
            self.sql = '''SELECT Prod_Codigo  FROM dbo.Productos'''
            self.prod = []

            self._array_ = self._cursor.execute(self.sql)

            for row in self._array_:
                self.prod.append(str(row[0]))

            #for row in self._cursor.execute(self.sql):
                #self.prod.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prod
        except:
                raise 
        
    
    def retrieve_name_prod(self):
        try:
            self.sql = '''SELECT Prod_Nombre  FROM dbo.Productos'''
            self.prod = []

            self._array_ = self._cursor.execute(self.sql)

            for row in self._array_:
                self.prod.append(str(row[0]))

            #for row in self._cursor.execute(self.sql):
                #self.prod.append(row)
                
            self._cursor.close()
            self.conn.close()

            return self.prod
        except:
                raise 

    
    
    """
   
    def reg_ped(self, num, total, provider):
        try:
            self.sql = 'INSERT INTO Pedidos VALUES(?, ?, ?)'

            self._cursor.execute(self.sql, num, total, provider)

            self._cursor.execute(sql_alm, code)

            self.conn.commit()
            self._cursor.close()
            self.conn.close()
            messagebox.showinfo(title='Registro de producto', message='Producto registrado exitosamente')
        except:
            messagebox.showerror(title='Registro de producto', message='Ha ocurrido un error al registrar producto')
            raise
    
     """

    # Validar el codigo de producto para evitar repeticion
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

            if self.values:
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



