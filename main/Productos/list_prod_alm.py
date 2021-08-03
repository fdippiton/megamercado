import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db


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
        self.lis_prod_title.grid(row=0, column=0, columnspan=2, padx=330, pady=40, sticky='ew')

        self.lis_prod_title = tk.Label(self._frame, text='Listado de productos x almacen', font=('Roboto Mono', 13), bg='white')
        self.lis_prod_title.grid(row=1, column=0, columnspan=2, padx=330, pady=5, sticky='ew')


    # Mostrar todos los productos en el treeview
    def show_list_prod_alm(self):
        self.tree_Table = ttk.Treeview(self._frame, height=15, columns=('#1', '#2', '#3', '#4', '#5'), show='headings')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='No. Almacén', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=190, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre de producto', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=190, stretch='NO')
        self.tree_Table.heading('#3', text='Costo unitario', anchor='center')
        self.tree_Table.column('#3', minwidth=0, width=190, stretch='NO')
        self.tree_Table.heading('#4', text='Valor de inventario', anchor='center')
        self.tree_Table.column('#4', minwidth=0, width=190, stretch='NO')
        self.tree_Table.heading('#5', text='Unidades disponibles', anchor='center')
        self.tree_Table.column('#5', minwidth=0, width=190, stretch='NO')

        self.num_total_inv_title = tk.Label(self._frame, text='Valor de inventario: '+self.str_num_total_inv+'', bg='white').grid(row=4, column=0)
        self.num_total_uni_title = tk.Label(self._frame, text='Unidades disponibles: '+self.str_num_total_uni+'', bg='white').grid(row=5, column=0)

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