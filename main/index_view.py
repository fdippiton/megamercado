# Modulo: vista principal objetos


import tkinter as tk
from tkinter import ttk
from tkinter.font import families


class main_view():
    def __init__(self, _frame):
        self._frame = _frame

    def main_page_view(self):
        # Creating title megamercado
        self.main_title_reg_pro = tk.Label(self._frame, text='MegaMercado', font=('Segoe UI semibold', 15), bg='#16ADB2', fg='white', width=150, anchor='s')
        self.main_title_reg_pro.grid(row=0, column=0, sticky='ew', ipady=10)

