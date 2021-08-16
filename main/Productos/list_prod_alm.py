import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from datetime import datetime
from DB.index import _db
from reportlab.pdfgen import canvas
import os

import random

class listar_prod_alm():
    def __init__(self, _frame):
        self._frame = _frame

        # Convertir en string el valor total del inventario
        self.num_total_inv = self.total_inv()
        self.str_num_total_inv = str(self.num_total_inv)

        # Convertir en string el numero total de unidades disponibles
        self.num_total_uni = self.total_uni_disp()
        self.str_num_total_uni = str(self.num_total_uni)
    
    # Titlulo de esta vista
    def list_prod_alm(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=350, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de productos x almacen', font=('Roboto Mono Bold', 10), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=350, pady=5, sticky='ew')


    # Mostrar todos los productos en el treeview
    def show_list_prod_alm(self):
        self.tree_Table = ttk.Treeview(self._frame, height=12, columns=('#1', '#2', '#3', '#4', '#5'), show='headings', style='estilo_alm.Treeview')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='No. Almacén', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=189, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre de producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=189, stretch='NO')
        self.tree_Table.heading('#3', text='Costo unitario', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=189, stretch='NO')
        self.tree_Table.heading('#4', text='Valor de inventario', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=189, stretch='NO')
        self.tree_Table.heading('#5', text='Unidades disponibles', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=189, stretch='NO')
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Roboto Mono Bold', 9))
        style.configure('estilo_alm.Treeview', font=('Roboto Mono', 8), background='#78fee0')

        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        self.num_total_inv_title = tk.Label(self._frame, text='Valor de inventario: '+self.str_num_total_inv+'', bg='white',  font=('Roboto Mono Bold', 8)).grid(row=4, column=0, pady=5)
        self.num_total_uni_title = tk.Label(self._frame, text='Unidades disponibles: '+self.str_num_total_uni+'', bg='white',  font=('Roboto Mono Bold', 8)).grid(row=5, column=0, pady=9)

        tk.Button(self._frame, text='Generar reporte', command=self.gen_reporte_pro_all, font=('Roboto Mono', 8)).grid(row=6, column=0, pady=7)


        self._retrieve = _db()
        self._retrieve.retrieve_prod_alm(self.tree_Table)

    # Obtener el valor total de inventario
    def total_inv(self):
        self.total_inv_db = _db()
        self.total = self.total_inv_db.retrieve_total_val_inv()
        return(self.total)

    # Obtener el numero total de unidades disponibles en almacen
    def total_uni_disp(self):
        self.total_uni_db = _db()
        self.total_uni = self.total_uni_db.retrieve_total_uni_disp()
        return(self.total_uni)

    # Generar reporte de todos los productos por almacen
    def gen_reporte_pro_all(self):
        self.rpt_db = _db()
        self.prod_alm = self.rpt_db.retrieve_rpt_prod_alm()

        self.date = datetime.today().strftime('%Y-%m-%d')
        rpt_num = random.randint(1, 10000)
        
        try:
            rpt = canvas.Canvas('Listado de productos x almacen rpt-'+str(rpt_num)+'.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(243, 750, 'MEGAMERCADO')
            rpt.drawString(230, 735, 'Listado de productos x almacen')
            rpt.drawString(262, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte: rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(50, 650, 'No. Almacen')
            rpt.drawString(120, 650, 'Nombre de Producto')
            rpt.drawString(210, 650, 'Costo unitario')
            rpt.drawString(290, 650, 'Valor de inventario')
            rpt.drawString(370, 650, 'Unidades disponibles')
            rpt.line(30, 645, 470, 645)

            self.count = 630
            for prods in self.prod_alm:
                rpt.drawString(50, self.count, str(prods[2]))
                rpt.drawString(120, self.count, str(prods[0]))
                rpt.drawString(210, self.count, str(prods[1]))
                rpt.drawString(290, self.count, str(prods[3]))
                rpt.drawString(370, self.count, str(prods[4]))
                self.count = self.count - 10

            
            rpt.save()
            os.startfile('Listado de productos x almacen rpt-'+str(rpt_num)+'.pdf')
        except:
            raise
