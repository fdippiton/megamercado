
import tkinter as tk
from tkinter import Label, messagebox
from tkinter import Message, ttk
from tkinter.constants import S
from tkinter.font import families
from fonts import *
import pyodbc
from DB.index import _db

from tkinter import ttk
from tkinter import *
from tkinter.constants import CENTER, LEFT, NONE, NUMERIC, S
from tkinter.font import BOLD, Font
from datetime import datetime


class gen_factura():
    def __init__(self, _frame):
        self._frame = _frame
        self.fecha= datetime.now().strftime("%Y-%m-%d")

        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};''SERVER='+self.server+';' 'DATABASE='+self.db+';' 'Trusted_Connection=yes;')
        self._cursor = self.conn.cursor()

        self.productoCod= tk.StringVar()
        self.cantidadVar=tk.IntVar()
    
    def gen_prod(self):
        self.productoCod.trace_add('write',self.callback)
        # TEXTOS
        self.t1=tk.Label(self._frame, text= "Facturación", font=("Roboto Mono", 15, BOLD), bg="white").place(x=400, y=20)
        self.t2=tk.Label(self._frame, text= self.fecha, font=("Roboto Mono", 10), bg="white").place(x=440, y=55)
        self.t3=tk.Label(self._frame, text= "", font=("Roboto Mono", 10), bg="white")
        self.t3.place(x=427, y=75)
        self.t4=tk.Label(self._frame, text= "Codigo cliente:", font=("Roboto Mono", 11), bg="white").place(x=195, y=130)
        self.t5=tk.Label(self._frame, text= "Codigo producto:", font=("Roboto Mono",11), bg="white").place(x=185, y=165)
        self.t6=tk.Label(self._frame, text= "", font=("Roboto Mono",11), bg="white")
        self.t6.place(x=600, y=165)
        self.t7=tk.Label(self._frame, text= "Cantidad:", font=("Roboto Mono",11), bg="white").place(x=255, y=200)
        self.t8=tk.Label(self._frame, text= "", font=("Roboto Mono",11), bg="white")
        self.t8.place(x=600, y=200)
        self.t9=tk.Label(self._frame, text= "Producto:", font=("Roboto Mono",11), bg="white").place(x=500, y=165)
        self.t10=tk.Label(self._frame, text= "Precio:", font=("Roboto Mono",11), bg="white").place(x=520, y=200)
        
        # RESUMENES
        frame=tk.Frame( self._frame, width=141,height=100)
        frame.config(bg="white",highlightbackground="gray",highlightthickness=1)
        frame.place(x=667,y=416)
        self.VarCantT=IntVar()
        self.VarSubT=IntVar()
        self.VarITBIST=IntVar()
        self.VarTotT=IntVar()
        self.cantidadt=tk.Label(frame, text= "Cantidad:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=0)
        self.subtotalt=tk.Label(frame, text= "Subtotal:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=25)       
        self.ITBISt=tk.Label(frame, text= "ITBIS:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=50)
        self.totalt=tk.Label(frame, text= "Total:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=75)
        self.valorcantidadt=tk.Label(frame, textvariable= self.VarCantT, font=("Roboto Mono",10), bg="white").place(x=100,y=12, anchor=E)
        self.valorsubtotalt=tk.Label(frame, textvariable= self.VarSubT, font=("Roboto Mono",10), bg="white").place(x=100,y=37, anchor=E)
        self.valorITBISt=tk.Label(frame, textvariable= self.VarITBIST, font=("Roboto Mono",10), bg="white").place(x=100,y=60, anchor=E)
        self.valortotalt=tk.Label(frame, textvariable= self.VarTotT, font=("Roboto Mono",10), bg="white").place(x=100,y=85,height=10, anchor=E)
        
        # ENTRYS
        self.entryCli=tk.Entry(self._frame, validate="key", validatecommand=(frame.register(self.validate_Codigos), '%S','%P'), width=18,  font=("Roboto Mono",8), bg="#f9f9f9")
        self.entryCli.focus()
        self.entryCli.place(x=355,y=135,height=23)
        self.entryProd=tk.Entry(self._frame,validate="key", validatecommand=(frame.register(self.validate_Codigos), '%S','%P'), textvariable=self.productoCod,width=18,  font=("Roboto Mono",8), bg="#f9f9f9")
        self.entryProd.place(x=355,y=168,height=23)
        self.entryCant=tk.Entry(self._frame,validate="key", validatecommand=(frame.register(self.validate_entry), '%S','%P'),textvariable=self.cantidadVar,width=18,  font=("Roboto Mono",8), bg="#f9f9f9").place(x=355,y=203,height=23)
        
        # TABLAS
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Roboto Mono', 8)) 
        style.configure("mystyle.Treeview.Heading", font=('Roboto Mono', 9, BOLD)) 
        self.grid1= ttk.Treeview(self._frame, height=5, columns=("#0","#1","#2","#3","#4","#5"), style="mystyle.Treeview")
        self.grid1.place(x=130,y=280)
        self.grid1.column("#0",width=75,anchor=CENTER)
        self.grid1.heading("#0", text="Codigo", anchor=CENTER)
        self.grid1.column("#1",width=100,anchor=CENTER)
        self.grid1.heading("#1", text="Producto", anchor=CENTER)
        self.grid1.column("#2",width=100,anchor=CENTER)
        self.grid1.heading("#2", text="Precio", anchor=CENTER)
        self.grid1.column("#3",width=100,anchor=CENTER)
        self.grid1.heading("#3", text="Cantidad", anchor=CENTER)
        self.grid1.column("#4",width=100,anchor=CENTER)
        self.grid1.heading("#4", text="Subtotal", anchor=CENTER)
        self.grid1.column("#5",width=100,anchor=CENTER)
        self.grid1.heading("#5", text="ITBIS", anchor=CENTER)
        self.grid1.column("#6",width=100,anchor=CENTER)
        self.grid1.heading("#6", text="Total", anchor=CENTER)

        self.scroll_tree = tk.Scrollbar(self._frame, orient='vertical', command=self.grid1.yview, width=20)
        self.scroll_tree.place(x=809, y=280)

        # BOTONES 
        self.agregar=tk.Button(self._frame, text="Agregar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#41ba10", command=self.agregar, activebackground="#41ba10",activeforeground="#f9f9f9")
        self.agregar.place(x=355,y=240,width=100)
        self.eliminar=tk.Button(self._frame, text="Eliminar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#f00", command=self.eliminar,activebackground="#f00",activeforeground="#f9f9f9")
        self.eliminar.place(x=480,y=240,width=100)
        self.generar=tk.Button(self._frame, text="Generar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#21A7DA", activebackground="#56ABFF",activeforeground="#f9f9f9")
        self.generar.place(x=355,y=450,width=100,height=40)
        self.limpiar=tk.Button(self._frame, text="Limpiar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#21A7DA", activebackground="#56ABFF",activeforeground="#f9f9f9")
        self.limpiar.place(x=480,y=450,width=100,height=40)
        self.ObtenerNoFactura()


    def buscarNombreProducto(self):
        try:
            codigo=self.productoCod.get()
            lista=[]
            cur=self.conn.cursor()
            sql="select Prod_Codigo from Productos"
            cur.execute(sql)
            x=cur.fetchall()
            for i in x:
                lista.append(int(i[0]))
            if codigo=="":
                self.t6.config(text="")
                self.t8.config(text="")
            elif int(codigo) not in lista:
                self.t6.config(text="No existe")
                self.t8.config(text="No existe")
            else: 
                cur=self.conn.cursor()
                sql="Select Prod_Nombre,Prod_PrecioVenta from Productos where Prod_codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                    self.t6.config(text=str(i[0]))
                    self.t8.config(text="$"+str(i[1]))   
        except TclError:
            pass
        except UnboundLocalError:
            pass


    def callback(self,var, indx, mode):
        self.buscarNombreProducto()

    def validate_entry(self,text,new_text):
        if len(new_text) > 5:
            return False
        return text.isdecimal()
    
    def validate_Codigos(self,text,new_text):
        if len(new_text) > 9:
            return False
        return text.isdecimal()

    def ObtenerNoFactura(self):
        cur=self.conn.cursor()
        sql="Select TOP 1 Fact_NoFactura from Factura Order by Fact_NoFactura desc"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable=i[0]
        sql="select count(*) from Factura"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable1=i[0]
        if variable1==0:
            self.t3.config(text="No. Factura: 1")
        else:
            self.t3.config(text='No. Factura: '+str(variable)+'')

    def agregar(self):
        if self.cantidadVar.get()>0:
          try:
            codigo=self.productoCod.get()
            ITBS=float(self.ITBIS)
            cantidad=int(self.cantidadVar.get())
            cur=self.conn.cursor()
            sql="Select Prod_Nombre,Prod_PrecioVenta from Productos where Prod_Codigo={}".format(codigo)
            cur.execute(sql)
            x=cur.fetchall()
            for i in x:
                subtotal=cantidad*float(i[1])
                porcentajeITIBIS= subtotal*ITBS
                Total=subtotal-porcentajeITIBIS
                self.grid1.insert('',END, text=codigo,values=(i[0],i[1],cantidad,subtotal,porcentajeITIBIS,Total))
                self.productoCod.set("")
                self.cantidadVar.set(0)
                self.entryProd.focus()
          except pyodbc.ProgrammingError:
            print("exploto")
    
    def eliminar(self):
        x=self.grid1.selection()
        for row in x:
            self.grid1.delete(row)



