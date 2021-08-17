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


class listar_proveedores():
    def __init__(self, _frame):
        self._frame = _frame

        self.num_total_prov = self.total_prov()
        self.str_num_total_prov = str(self.num_total_prov)

    def list_prov_title(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=330, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de proveedores', font=('Roboto Mono Bold', 10), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=330, pady=5, sticky='ew')


    def show_list_prov(self):
        self.tree_Table = ttk.Treeview(self._frame, height=13, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings', style='estilo_prov.Treeview')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Código', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=100, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#3', text='Dirección', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=157, stretch='NO')
        self.tree_Table.heading('#4', text='RNC/Cédula', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=100, stretch='NO')
        self.tree_Table.heading('#5', text='Teléfono', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=90, stretch='NO')
        self.tree_Table.heading('#6', text='Tipo', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=245, stretch='NO')
        self.tree_Table.heading('#7', text='Estatus', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=93, stretch='NO')
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Roboto Mono Bold', 9))
        style.configure('estilo_prov.Treeview', font=('Roboto Mono', 8), background='#78fee0')

        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        self.num_total_prov = tk.Label(self._frame, text='Número total de proveedores: '+self.num_total_prov+'', bg='white',  font=('Roboto Mono Bold', 8)).grid(row=4, column=0, pady=5)
        tk.Button(self._frame, text='Generar reporte', command=self.gen_reporte_prov, font=('Roboto Mono', 8)).grid(row=5, column=0, pady=20)
        
        self._retrieve_prov = _db()
        self._retrieve_prov.retrieve_providers(self.tree_Table)

    def total_prov(self):
        self.total_prov_db = _db()
        self.total = str(self.total_prov_db.retrieve_total_prov())
        return self.total 


    # Generar reporte de proveedores
    def gen_reporte_prov(self):
        self.rpt_db = _db()
        self._prov = self.rpt_db.retrieve_rpt_prov()

        self.date = datetime.today().strftime('%Y-%m-%d')

        rpt_num = random.randint(1, 10000)
        
        try:
            rpt = canvas.Canvas('Listado de proveedores rpt-'+str(rpt_num)+'.pdf')

            rpt.setLineWidth(.3)
            rpt.setFont('Times-Roman', 8)

            rpt.drawString(243, 750, 'MEGAMERCADO')
            rpt.drawString(237, 735, 'Listado de proveedores')
            rpt.drawString(262, 720, str(self.date))

            rpt.drawString(500, 780, 'Usuario ADM')
            rpt.drawString(500, 765, 'Fecha: '+str(self.date)+'')
            rpt.drawString(500, 750, 'Reporte: rpt-'+str(rpt_num)+'')
            rpt.drawString(500, 735, 'Pagina:')  
        
            rpt.drawString(35, 650, 'Codigo')
            rpt.drawString(95, 650, 'Nombre')
            rpt.drawString(160, 650, 'Direccion')
            rpt.drawString(250, 650, 'RNC/Cedula')
            rpt.drawString(330, 650, 'Telefono')
            rpt.drawString(380, 650, 'Tipo')
            rpt.drawString(510, 650, 'Estatus')
            rpt.line(30, 645, 540, 645)

            self.count = 630
            for prods in self._prov:
                rpt.drawString(20, self.count, str(prods[0]))
                rpt.drawString(80, self.count, str(prods[2]))
                rpt.drawString(170, self.count, str(prods[1]))
                rpt.drawString(250, self.count, str(prods[5]))
                rpt.drawString(320, self.count, str(prods[4]))
                rpt.drawString(380, self.count, str(prods[3]))
                rpt.drawString(510, self.count, str(prods[6]))
                self.count = self.count - 10

            
            self.num_prov = str(self.total_prov())
            self._ct = self.count - 20
            rpt.drawString(20, self._ct, 'Numero total de proveedores:')
            rpt.drawString(130, self._ct, self.num_prov)
            
            rpt.save()
            os.startfile('Listado de proveedores rpt-'+str(rpt_num)+'.pdf')
        except:
            raise
