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
        self.tree_Table = ttk.Treeview(self._frame, height=15, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), show='headings')
        self.tree_Table.grid(row=3, column=0, pady=5)
        self.tree_Table.heading('#1', text='Código de producto', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre de producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#3', text='Unidades vendidas', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#4', text='Costo', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=130, stretch='NO')
        self.tree_Table.heading('#5', text='Precio de venta', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=145, stretch='NO')
        self.tree_Table.heading('#6', text='Itbis', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=110, stretch='NO')
        self.tree_Table.heading('#7', text='Ventas *Itbis incluidos', anchor='center')
        self.tree_Table.column('#7', minwidth=0, width=145, stretch='NO')
        
        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.tree_Table.yview, width=20)
        self.scroll_tree.grid(row=3, column=1, sticky='nsew')

        #self.num_total_prod_title = tk.Label(self._frame, text='Total en ventas:', bg='white', font=('Roboto Mono Bold', 8)).grid(row=4, column=0)
        tk.Button(self._frame, text='Generar reporte', font=('Roboto Mono', 8)).grid(row=6, column=0, pady=20)
        

        self._retrieve_sales = _db()
        self._retrieve_sales.retrieve_rpt_sales(self.tree_Table, self._frame)

