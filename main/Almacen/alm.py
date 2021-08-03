
import tkinter as tk
from tkinter import messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db


class reg_alm_view():
    def __init__(self, _frame):
        self._frame = _frame

        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        
    def show_list(self):
        self.tree_Table = ttk.Treeview(self._frame, height=20, columns=('#1', '#2'), show='headings')
        self.tree_Table.grid(row=3, column=0)
        self.tree_Table.heading('#1', text='Codigo', anchor='center')
        self.tree_Table.column('#1', minwidth=0, width=140, stretch='NO')
        self.tree_Table.heading('#2', text='Nombre', anchor='center')
        self.tree_Table.column('#2', minwidth=0, width=140, stretch='NO')
