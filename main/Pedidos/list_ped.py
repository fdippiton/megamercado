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
from DB.index import _db
from reportlab.pdfgen import canvas
import os

import random

class listar_pedidos():
    def __init__(self, _frame):
        self._frame = _frame

        #self.num_total_cli = self.total_cli()
        #self.str_num_total_cli = str(self.num_total_cli)
    
    def list_ped_title(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=360, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de pedidos', font=('Roboto Mono Bold', 10), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=330, pady=5, sticky='ew')

    def show_pedidos(self):
        self.tree_Table = ttk.Treeview(self._frame, height=14, columns=('#1', '#2', '#3'), show='headings', style='estilo_ped.Treeview')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Número de pedido', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=315, stretch='NO')
        self.tree_Table.heading('#2', text='Monto total', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=315, stretch='NO')
        self.tree_Table.heading('#3', text='Proveedor', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=315, stretch='NO')
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Roboto Mono Bold', 9))
        style.configure('estilo_ped.Treeview', font=('Roboto Mono', 8))


        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        #self.num_total_clientes = tk.Label(self._frame, text='Número total de clientes: '+self.str_num_total_cli+'', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0, pady=5)
        tk.Button(self._frame, text='Generar reporte', command=self.gen_reporte_ped, font=('Roboto Mono', 8)).grid(row=5, column=0, pady=23)


        self._retrieve_ped = _db()
        self._retrieve_ped.retrieve_all_pedidos(self._frame, self.tree_Table)

    # Numero total de clientes
    # def total_ped(self):
        #self.total_cli_db = _db()
       # self.total = self.total_cli_db.retrieve_total_cli()
        #return(self.total)

    # Generar reporte de clientes
    def gen_reporte_ped(self):
        self.rpt_db = _db()
        self._ped = self.rpt_db.retrieve_rpt_ped()

        self.date = datetime.today().strftime('%Y-%m-%d')

        rpt_num = random.randint(1, 10000)
        try:
            rpt = canvas.Canvas('Listado de pedidos rpt-'+str(rpt_num)+'.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(243, 750, 'MEGAMERCADO')
            rpt.drawString(245, 735, 'Listado de pedidos')
            rpt.drawString(255, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte: rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(50, 650, 'Número de pedidos')
            rpt.drawString(125, 650, 'Monto total')
            rpt.drawString(200, 650, 'Proveedor')
            rpt.line(30, 645, 500, 645)

            self.count = 630
            for ped in self._ped:
                rpt.drawString(50, self.count, str(ped[0]))
                rpt.drawString(125, self.count, str(ped[1]))
                rpt.drawString(200, self.count, str(ped[3]))
                self.count = self.count - 10

            
            #self.num_cli = str(self.total_cli())
            #self._ct = self.count - 20
            #rpt.drawString(50, self._ct, 'Número total de clientes:  ')
            #rpt.drawString(130, self._ct, self.num_cli)
            
            rpt.save()
            os.startfile('Listado de pedidos rpt-'+str(rpt_num)+'.pdf')
        except:
            raise