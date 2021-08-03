import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db


class listar_clientes():
    def __init__(self, _frame):
        self._frame = _frame

        #self.num_total_inv = self.total_inv()
        #self.str_num_total_inv = str(self.num_total_inv)

        #self.num_total_uni = self.total_uni_disp()
        #self.str_num_total_uni = str(self.num_total_uni)
    
    def list_cli_title(self):
        self.lis_prod_title = tk.Label(self._frame, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='white')
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=330, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de clientes', font=('Roboto Mono', 13), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=330, pady=5, sticky='ew')

        #self.btn_retrieve = tk.Button(self._frame, text='Listar productos', font=('Roboto Mono', 12), bg='#21A7DA', width=20, pady=3, command=self.show_list).grid(row=9, column=0, sticky='e', pady=185, padx=90)

    def show_list_cli(self):
        self.tree_Table = ttk.Treeview(self._frame, height=20, columns=('#1', '#2', '#3', '#4', '#5', '#6'), show='headings')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Codigo', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=160, stretch='NO')
        self.tree_Table.heading('#2', text='Nombres', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=160, stretch='NO')
        self.tree_Table.heading('#3', text='Apellidos', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=160, stretch='NO')
        self.tree_Table.heading('#4', text='RNC/Cedula', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=160, stretch='NO')
        self.tree_Table.heading('#5', text='Telefono', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=160, stretch='NO')
        self.tree_Table.heading('#6', text='Direccion', anchor='center')
        self.tree_Table.column('#6', minwidth=0, width=160, stretch='NO')

        #self.num_total_clientes = tk.Label(self._frame, text='Valor de inventario: '+self.str_num_total_inv+'', bg='white').grid(row=4, column=0)
        
        self._retrieve_cli = _db()
        self._retrieve_cli.retrieve_all_clients(self.tree_Table)

    #Valor total de inventario
    # def total_inv(self):
        #self.total_inv_db = _db()
        #self.total = self.total_inv_db.retrieve_total_val_inv()
        #return(self.total)
 
    # def total_uni_disp(self):
        #self.total_uni_db = _db()
        #self.total_uni = self.total_uni_db.retrieve_total_uni_disp()
        #return(self.total_uni)