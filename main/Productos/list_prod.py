import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db


class listar_prod():
    def __init__(self, _frame):
        self._frame = _frame

        self.num_total = self.total_prod()
        self.str_num_total = str(self.num_total)

    # Titulos de esta vista
    def list_prod(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=380, pady=20, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de productos', font=('Roboto Mono', 13), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=380, pady=5, sticky='ew')

    # Mostrar el listado de productos
    def show_list(self):
        self.tree_Table = ttk.Treeview(self._frame, height=15, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Codigo', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#3', text='Precio de venta', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#4', text='Proveeedor', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#5', text='Costo de unidad', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#6', text='Itbis', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#7', text='Estatus', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=140, stretch='NO')

        self.num_total_prod_title = tk.Label(self._frame, text='Numero total de productos: '+self.str_num_total+'', bg='white').grid(row=4, column=0)

        self._retrieve = _db()
        self._retrieve.retrieve_prod(self.tree_Table)

        self.update_status(self.tree_Table)

    # Inactivar producto
    def update_status(self, _tree):
        self._inactive = _db()
        self._tree = _tree
        self.btn_update = tk.Button(self._frame, text='Inactivar', font=('Roboto Mono', 10), bg='#21A7DA', width=10, pady=1, command= lambda: self._inactive.inactive_prod(self._tree, self.show_list))
        self.btn_update.grid(row=5, column=0, pady=30)

    # Retorna el numero total de productos
    def total_prod(self):
        self.total_db = _db()
        self.total = self.total_db.retrieve_total_prod()
        return(self.total)


    



















































        
        """
        # Mostrar productos
        try:
            self.sql = 'SELECT * FROM dbo.Productos'

            for row in self._retrieve._cursor.execute(self.sql):
                self.tree_Table.insert('', 0, values= (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            self._cursor.close()
            self.conn.close()
        except:
                raise 

        """




    '''
    # Mostrar productos en terminal
        def retrieve_prod(self):
            try: 
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};''SERVER='+self.server+';' 'DATABASE='+self.db+';' 'Trusted_Connection=yes;')

            print('conexion exitosa')
        except :
            print('Error al intentar conectarnos')
        
        try:
            _cursor = conexion.cursor()
            for row in _cursor.execute('SELECT * FROM dbo.Productos'):
                print(row.Prod_Codigo, row.Prod_Nombre)
            _cursor.close()
            conexion.close()

            
        except:
            messagebox.showinfo(title='Registro de producto', message='Error')


    '''
        

