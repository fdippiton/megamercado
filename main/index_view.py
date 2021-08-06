# Template header

import tkinter as tk
from tkinter import ttk
from tkinter.font import families


class main_bar():
    def __init__(self, _frameLogo, _frameUser):
        self._frameLogo = _frameLogo
        self._frameUser = _frameUser

    def main_bar_view(self):
        self.main_title_reg_pro = tk.Label(self._frameLogo, text='MEGAMERCADO', font=('Roboto Mono Bold', 13), bg='#37648B', fg='white')
        
        self.main_title_reg_pro.grid()
        
        self.user_log = tk.Button(self._frameUser, text='Usuario ADM', font=('Roboto Mono Semibold', 12), bg='#37648B', fg='white', relief="flat")
        self.user_log.grid(row=0, column=0, padx=20)

        # self.user_log.place(relx=0.72, rely=0.11)
        # Creating title megamercado
        # self.main_title_reg_pro = tk.Label(self._frameLogo, text='MEGAMERCADO', font=('Roboto Mono Bold', 15), bg='#37648B', fg='white')
        # self.main_title_reg_pro.grid()
        # self.user_log = tk.Label(self._frameUser, text='Usuario ADM', font=('Roboto Mono Bold', 15), bg='#37648B', fg='white')
        # self.user_log.grid()
        





