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


class listar_facturas():
    def __init__(self, _frame):
        self._frame = _frame

        #self.num_total_cli = self.total_cli()
        #self.str_num_total_cli = str(self.num_total_cli)
    
    def list_fac_title(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=330, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de facturas', font=('Roboto Mono Bold', 10), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=320, pady=5, sticky='ew')

    def show_facturas(self):
        self.tree_Table = ttk.Treeview(self._frame, height=14, columns=('#1', '#2', '#3', '#4', '#5', '#6'), show='headings', style='estilos.Treeview')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Numero de factura', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#2', text='Fecha', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#3', text='Subtotal', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=157, stretch='NO')
        self.tree_Table.column('#4', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#4', text='Total itbis', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#5', text='Total', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#6', text='Cliente', anchor='center')
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Roboto Mono Bold', 9))
        style.configure('estilos.Treeview', font=('Roboto Mono', 8), background='#78fee0')


        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        #self.num_total_clientes = tk.Label(self._frame, text='Número total de clientes: '+self.str_num_total_cli+'', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0, pady=5)
        tk.Button(self._frame, text='Generar reporte', command=self.gen_reporte_fact, font=('Roboto Mono', 8)).grid(row=5, column=0, pady=25)


        self._retrieve_ped = _db()
        self._retrieve_ped.retrieve_all_facturas(self._frame, self.tree_Table)

    # Numero total de clientes
    # def total_ped(self):
        #self.total_cli_db = _db()
       # self.total = self.total_cli_db.retrieve_total_cli()
        #return(self.total)

    # Generar reporte de clientes
    def gen_reporte_fact(self):
        self.rpt_db = _db()
        self._facts = self.rpt_db.retrieve_rpt_fac()

        self.date = datetime.today().strftime('%Y-%m-%d')

        rpt_num = random.randint(1, 10000)
        try:
            rpt = canvas.Canvas('Listado de facturas rpt-'+str(rpt_num)+'.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(243, 750, 'MEGAMERCADO')
            rpt.drawString(245, 735, 'Listado de facturas')
            rpt.drawString(255, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte: rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(50, 650, 'Numero de factura')
            rpt.drawString(125, 650, 'Fecha')
            rpt.drawString(200, 650, 'Subtotal')
            rpt.drawString(275, 650, 'Total itbis')
            rpt.drawString(350, 650, 'Total')
            rpt.drawString(425, 650, 'Cliente')
            rpt.line(30, 645, 500, 645)

            self.count = 630
            for fac in self._facts:
                rpt.drawString(50, self.count, str(fac[0]))
                rpt.drawString(125, self.count, str(fac[1]))
                rpt.drawString(200, self.count, str(fac[2]))
                rpt.drawString(275, self.count, str(fac[3]))
                rpt.drawString(350, self.count, str(fac[4]))
                rpt.drawString(425, self.count, str(fac[6]))
                self.count = self.count - 10

            
            #self.num_cli = str(self.total_cli())
            #self._ct = self.count - 20
            #rpt.drawString(50, self._ct, 'Número total de clientes:  ')
            #rpt.drawString(130, self._ct, self.num_cli)
            
            rpt.save()
            os.startfile('Listado de facturas rpt-'+str(rpt_num)+'.pdf')
        except:
            raise