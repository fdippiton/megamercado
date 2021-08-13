import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db
import os

from datetime import datetime
import random


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics



class rpt_ventas():
    def __init__(self, _frame):
        self._frame = _frame

        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
    
    
    def rpt_ventas_title(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=330, pady=20, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Reporte de ventas', font=('Roboto Mono', 13), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=330, pady=5, sticky='ew')

        #self.btn_retrieve = tk.Button(self._frame, text='Listar productos', font=('Roboto Mono', 12), bg='#21A7DA', width=20, pady=3, command=self.show_list).grid(row=9, column=0, sticky='e', pady=185, padx=90)

    def show_rpt_ventas(self):
        self.tree_Table = ttk.Treeview(self._frame, height=15, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'), show='headings')
        self.tree_Table.grid(row=3, column=0, pady=5)
        self.tree_Table.heading('#1', text='Código de producto', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre de producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#3', text='Unidades vendidas', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#4', text='Costo', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=80, stretch='NO')
        self.tree_Table.heading('#5', text='Precio de venta', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=120, stretch='NO')
        self.tree_Table.heading('#6', text='Subtotal', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=80, stretch='NO')
        self.tree_Table.heading('#7', text='Total itbis', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=100, stretch='NO')
        self.tree_Table.heading('#8', text='Ventas *Itbis incluidos', anchor='center')
        self.tree_Table.column('#8', minwidth=0, width=145, stretch='NO')
        
        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        #self.num_total_prod_title = tk.Label(self._frame, text='Total en ventas:', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0)
        tk.Button(self._frame, text='Generar reporte', font=('Roboto Mono', 8), command=self.gen_reporte_sales_).grid(row=6, column=0, pady=20)
        

        self._retrieve_sales = _db()
        self._retrieve_sales.retrieve_rpt_sales(self.tree_Table, self._frame)
        
           # Generar reporte de todos los productos por almacen
    def gen_reporte_sales_(self):
        self.rpt_db = _db()
        self.sales = self.rpt_db.rpt_venta_productos_array()
        self.sales_totals = self.rpt_db.rpt_venta_totales_productos_array()
        

        self.date = datetime.today().strftime('%Y-%m-%d')
        
        rpt_num = random.randint(1, 10000)

        try:
            rpt = canvas.Canvas('Reporte de ventas.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(243, 750, 'MEGAMERCADO')
            rpt.drawString(245, 735, 'Reporte de ventas')
            rpt.drawString(255, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte: rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(30, 650, 'Codigo de producto')
            rpt.drawString(120, 650, 'Nombre')
            rpt.drawString(190, 650, 'Unidades vendidas')
            rpt.drawString(280, 650, 'Costo')
            rpt.drawString(340, 650, 'Precio de venta')
            rpt.drawString(410, 650, 'Subtotal')
            rpt.drawString(460, 650, 'Total itbis')
            rpt.drawString(510, 650, 'Ventas *Itbis incluido')
            
            rpt.line(30, 645, 590, 645)

            self.count = 630
            for field in self.sales:
                rpt.drawString(30, self.count, str(field[0]))
                rpt.drawString(120, self.count, str(field[1]))
                rpt.drawString(190, self.count, str(field[2]))
                rpt.drawString(280, self.count, str(field[3]))
                rpt.drawString(340, self.count, str(field[4]))
                rpt.drawString(410, self.count, str(field[5]))
                rpt.drawString(460, self.count, str(field[6]))
                rpt.drawString(510, self.count, str(field[7]))
                self.count = self.count - 10

            self._ct = self.count - 20
            rpt.drawString(50, self._ct, 'Subtotal en ventas:  '+str(self.sales_totals[0][0])+'')
            rpt.drawString(200, self._ct, 'Total itbis:  '+str(self.sales_totals[0][1])+'')
            rpt.drawString(300, self._ct, 'Ganacias totales:  '+str(self.sales_totals[0][2])+'')
            
            rpt.save()
            os.startfile('Reporte de ventas.pdf')
        except:
            raise
        

