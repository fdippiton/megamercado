import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db
from datetime import datetime


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics

import os
import random


class listar_prod():
    def __init__(self, _frame):
        self._frame = _frame

        # Convertir numero total de productos en string
        self.num_total = self.total_prod()
        self.str_num_total = str(self.num_total)

    # Titulos de esta vista
    def list_prod(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=380, pady=20, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de productos', font=('Roboto Mono Bold', 10), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=380, pady=5, sticky='ew')

    # Mostrar el listado de productos
    def show_list(self):
        self.tree_Table = ttk.Treeview(self._frame, height=11, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Codigo', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#3', text='Precio de venta', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#4', text='Proveeedor', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#5', text='Costo de unidad', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#6', text='Itbis', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=135, stretch='NO')
        self.tree_Table.heading('#7', text='Estatus', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=135, stretch='NO')


        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')


        self.num_total_prod_title = tk.Label(self._frame, text='Numero total de productos: '+self.str_num_total+'', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0)
        tk.Button(self._frame, text='Generar reporte', command=self.gen_reporte, font=('Roboto Mono', 8)).grid(row=6, column=0, pady=15)
        
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

    # Generar reporte
    def gen_reporte(self):
        self.rpt_db = _db()
        self._prods = self.rpt_db.retrieve_rpt_prod()
        self.date = datetime.today().strftime('%Y-%m-%d')
 
        rpt_num = random.randint(1, 10000)

        try:
            rpt = canvas.Canvas('Listado de productos.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(250, 750, 'MEGAMERCADO')
            rpt.drawString(237, 735, 'Listado de productos')
            rpt.drawString(262, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte:  rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(30, 650, 'Codigo')
            rpt.drawString(90, 650, 'Nombre')
            rpt.drawString(150, 650, 'Precio de venta')
            rpt.drawString(250, 650, 'Proveedor')
            rpt.drawString(320, 650, 'Costo de unidad')
            rpt.drawString(420, 650, 'Itbis')
            rpt.drawString(470, 650, 'Estatus')
            rpt.line(30, 645, 500, 645)

            self.count = 630
            for prods in self._prods:
                rpt.drawString(20, self.count, str(prods[0]))
                rpt.drawString(80, self.count, str(prods[1]))
                rpt.drawString(170, self.count, str(prods[2]))
                rpt.drawString(250, self.count, str(prods[3]))
                rpt.drawString(320, self.count, str(prods[4]))
                rpt.drawString(420, self.count, str(prods[5]))
                rpt.drawString(470, self.count, str(prods[6]))
                self.count = self.count - 10
                #self._count = self._count - 50

            self.num_prod = str(self.total_prod())
            self._ct = self.count - 20
            rpt.drawString(20, self._ct, 'Numero total de productos:')
            rpt.drawString(130, self._ct, self.num_prod)

            rpt.save()
            os.startfile('Listado de productos.pdf')
        except:
            raise



















































        
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
        

