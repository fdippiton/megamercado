import tkinter as tk
from tkinter import Label, messagebox
from tkinter import Message, ttk
from tkinter.constants import ANCHOR, S, SEL
from tkinter.font import families
from typing import Collection, Text

#from reportlab.lib.utils import c
from fonts import *
import pyodbc
from DB.index import _db

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD, Font
from datetime import datetime
from reportlab.lib.enums import  TA_CENTER
from reportlab.platypus import SimpleDocTemplate, paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import subprocess

Fecha= datetime.now().strftime("%Y-%m-%d")
ListaProductos=[]
class gen_ped():
    ITBIS=0.18
    def __init__(self, _frame):
        self._frame = _frame

        self.conexionBD=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};'
                                'SERVER=DESKTOP-4IOJCET;'
                                'DATABASE=MegaMercado;'
                                'Trusted_Connection=yes;')
        
        self.tree_scrollbar=Scrollbar(self._frame)
        self.grid1= ttk.Treeview(self._frame, height=5, columns=("#1","#2","#3","#4","#5","#6","#7"), show="headings",style="mystyle.Treeview",yscrollcommand=self.tree_scrollbar.set)
        self.cantidadVar=tk.StringVar()
        

    def crear_pedido(self):
        #TEXTO
        #self.cantidadVar=tk.StringVar()
        self.t1=tk.Label(self._frame, text= "Pedidos", font=("Roboto Mono",20,BOLD), bg="white").place(x=433, y=20)
        self.t2=tk.Label(self._frame, text= Fecha, font=("Roboto Mono",12), bg="white").place(x=440, y=55)
        self.t3=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t3.place(x=427, y=75)
        self.t4=tk.Label(self._frame, text= "Proveedor:", font=("Roboto Mono",10), bg="white").place(x=249, y=130)
        self.t5=tk.Label(self._frame, text= "Producto:", font=("Roboto Mono",10), bg="white").place(x=256, y=165)
        self.t6=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t6.place(x=600, y=165)
        self.t7=tk.Label(self._frame, text= "Cantidad:", font=("Roboto Mono",10), bg="white").place(x=255, y=200)
        self.t8=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t8.place(x=600, y=200)
        self.t10=tk.Label(self._frame, text= "Precio:", font=("Roboto Mono",10), bg="white").place(x=520, y=165)
        self.t12=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t12.place(x=600, y=133)
        self.t13=tk.Label(self._frame, text= '', font=("Roboto Mono",8, BOLD), fg='red', bg="white")
        self.t13.place(x=125, y=205)
        
        #RESUMENES
        self.Total=0.0
        frame=tk.Frame(self._frame,width=141,height=100)
        frame.config(bg="white",highlightbackground="gray",highlightthickness=1)
        frame.place(x=667,y=410)
        self.cantidadt=tk.Label(frame, text= "Cantidad:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=0)
        self.subtotalt=tk.Label(frame, text= "Subtotal:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=25)       
        self.ITBISt=tk.Label(frame, text= "ITBIS:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=50)
        self.totalt=tk.Label(frame, text= "Total:", font=("Roboto Mono",9,BOLD), bg="white").place(x=0,y=75)
        self.valorcantidadt=tk.Label(frame, text="", font=("Roboto Mono",10), bg="white")
        self.valorcantidadt.place(x=65,y=12, anchor=W)
        self.valorsubtotalt=tk.Label(frame, text="" , font=("Roboto Mono",10), bg="white")
        self.valorsubtotalt.place(x=65,y=37, anchor=W)
        self.valorITBISt=tk.Label(frame, text="" , font=("Roboto Mono",10), bg="white")
        self.valorITBISt.place(x=65,y=60, anchor=W)
        self.valortotalt=tk.Label(frame, text="" , font=("Roboto Mono",10), bg="white")
        self.valortotalt.place(x=65,y=85,height=10, anchor=W)
        
        #ENTRYS
        self.ComboBOXProv=ttk.Combobox(self._frame, value=self.obtenerValoresComboX(),width=18, font=("Roboto Mono",9))
        self.ComboBOXProv.place(x=355,y=135)
        self.ComboBOXProv.bind("<<ComboboxSelected>>", self.obtenerValor)
        self.ComboBOXProvPro=ttk.Combobox(self._frame, width=18,font=("Roboto Mono",9))
        self.ComboBOXProvPro.place(x=355,y=168)
        self.ComboBOXProvPro.bind("<<ComboboxSelected>>", self.obtenerValorPrecio)
        self.entryCant=tk.Entry(self._frame,validate="key", validatecommand=(frame.register(self.validate_entry), '%S','%P'),textvariable=self.cantidadVar,width=18,  font=("Roboto Mono",8), bg="#f9f9f9").place(x=355,y=203,height=23)
        #SCROLLBAR
        #tree_scrollbar=Scrollbar(self._frame)
        self.tree_scrollbar.place(x=808,y=280,relheight=0.225)
        
        #TABLAS
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Roboto Mono', 8)) 
        style.configure("mystyle.Treeview.Heading", font=('Roboto Mono', 9, BOLD)) 
        #self.grid1= ttk.Treeview(self._frame, height=5, columns=("#1","#2","#3","#4","#5","#6","#7"), show="headings",style="mystyle.Treeview",yscrollcommand=tree_scrollbar.set)
        self.tree_scrollbar.config(command=self.grid1.yview)
        self.grid1.place(x=130,y=280)
        self.grid1.column("#1",width=75,anchor=CENTER)
        self.grid1.heading("#1", text="Codigo", anchor=CENTER)
        self.grid1.column("#2",width=100,anchor=CENTER)
        self.grid1.heading("#2", text="Producto", anchor=CENTER)
        self.grid1.column("#3",width=100,anchor=CENTER)
        self.grid1.heading("#3", text="Costo", anchor=CENTER)
        self.grid1.column("#4",width=100,anchor=CENTER)
        self.grid1.heading("#4", text="Cantidad", anchor=CENTER)
        self.grid1.column("#5",width=100,anchor=CENTER)
        self.grid1.heading("#5", text="Subtotal", anchor=CENTER)
        self.grid1.column("#6",width=100,anchor=CENTER)
        self.grid1.heading("#6", text="ITBIS", anchor=CENTER)
        self.grid1.column("#7",width=100,anchor=CENTER)
        self.grid1.heading("#7", text="Total", anchor=CENTER)
        
        #BOTONES 
        self.agregar=tk.Button(self._frame, text="Agregar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#41ba10", command=self.agregar, activebackground="#41ba10",activeforeground="#f9f9f9")
        self.agregar.place(x=355,y=240,width=100)
        self.eliminar=tk.Button(self._frame, text="Eliminar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#f00", command=self.eliminar,activebackground="#f00",activeforeground="#f9f9f9")
        self.eliminar.place(x=480,y=240,width=100)
        self.generar=tk.Button(self._frame, text="Generar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#21A7DA",command=self.AgregarFactura, activebackground="#56ABFF",activeforeground="#f9f9f9")
        self.generar.place(x=355,y=450,width=100,height=40)
        self.limpiar=tk.Button(self._frame, text="Limpiar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#21A7DA",command=self.limpiarTodo, activebackground="#56ABFF",activeforeground="#f9f9f9")
        self.limpiar.place(x=480,y=450,width=100,height=40)
        self.ObtenerNoFactura()
        
    def validate_entry(self,text,new_text):
        if len(new_text) > 5:
            return False
        return text.isdecimal()
    
    def validate_Codigos(self,text,new_text):
        if len(new_text) > 11:
            return False
        return text.isdecimal()

    def ObtenerNoFactura(self):
        cur=self.conexionBD.cursor()
        sql="Select TOP 1 Ped_NoPedido from Pedidos Order by Ped_NoPedido desc"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable=i[0]
        sql="select count(*) from Pedidos"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable1=i[0]
        if variable1==0:
            self.t3.config(text="No. Pedido: 1")
        else:
            self.t3.config(text="No. Pedido: "+str(variable+1))
        cur.commit()
        cur.close()

    def agregar(self):
        try:
         valorCantidad=int(self.cantidadVar.get())
         valorCodigoProd=self.ComboBOXProvPro.get()
         if valorCantidad>0:
          self.t13.config(text='')
          codigo=self.obtenerCodigoProduct(valorCodigoProd)
          ITBS=float(self.ITBIS)
          cantidad=int(self.cantidadVar.get())
          cur=self.conexionBD.cursor()
          sql="Select Prod_Nombre,Prod_CostoUnidad from Productos where Prod_Codigo={}".format(codigo)
          cur.execute(sql)
          x=cur.fetchall()
          for i in x:
                subtotal=round(cantidad*float(i[1]),2)
                porcentajeITIBIS= round(subtotal*ITBS,2)
                Total=round(subtotal+porcentajeITIBIS,2)
                self.grid1.insert('',END,values=(codigo,i[0],i[1],cantidad,subtotal,porcentajeITIBIS,Total))
          self.cantidadVar.set('0')
          self.Resumenes()
          cur.commit()
          cur.close()
         elif valorCantidad==0:
            self.t13.config(text='Inserte Cantidad')
        except TypeError:
            self.ventanaError()
        except ValueError:
            self.t13.config(text='Inserte Cantidad')
        
    def obtenerValoresComboX(self):
        cur=self.conexionBD.cursor()
        sql="Select Prov_Nombre from Proveedores"
        cur.execute(sql)
        x=cur.fetchall()
        lista=[]
        for i in x:
            lista.append(i[0])
        return lista
    
    def obtenerValoresComboXPRODCUTO(self,valor):
        global ListaProductos
        cur=self.conexionBD.cursor()
        sql="Select Prov_Codigo from Proveedores Where Prov_Nombre='{}'".format(valor)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            provCodigo=int(i[0])
        sql="Select Prod_Nombre from Productos Where Prod_Proveedor={}".format(provCodigo)
        cur.execute(sql)
        x=cur.fetchall()
        ListaProductos=[]
        for i in x:
            ListaProductos.append(i[0])
        self.ComboBOXProvPro.config(value=ListaProductos)

    def obtenerValor(self,e):
        self.ComboBOXProvPro.set('')
        self.t6.config(text='')
        valor=self.ComboBOXProv.get()
        self.obtenerValoresComboXPRODCUTO(valor)

    def obtenerValorPrecio(self,e):
        valor=self.ComboBOXProvPro.get()
        self.obtenerPrecio(valor)

    def obtenerPrecio(self, valor):
        cur=self.conexionBD.cursor()
        sql="Select Prod_CostoUnidad from Productos Where Prod_Nombre='{}'".format(valor)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            prodcutoPrecio=int(i[0])
        self.t6.config(text='$'+ str(prodcutoPrecio)+'.00')
    
    def obtenerCodigoProduct(self,valor):
        cur=self.conexionBD.cursor()
        sql="Select Prod_Codigo from Productos Where Prod_Nombre='{}'".format(valor)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            return int(i[0])

    def Resumenes(self):
        self.TotalC=0
        self.TotalSub=0.00
        self.TotalITBS=0.00
        self.TotalT=0.00
        for child in self.grid1.get_children():
            self.TotalC +=int((self.grid1.item(child, 'values')[3]))
            self.TotalSub +=round(float((self.grid1.item(child, 'values')[4])),2)
            self.TotalITBS +=round(float((self.grid1.item(child, 'values')[5])),2)
            self.TotalT +=round(float((self.grid1.item(child, 'values')[6])),2)
        self.valorITBISt.config(text=self.TotalITBS)
        self.valortotalt.config(text=self.TotalT)
        self.valorsubtotalt.config(text=self.TotalSub)
        self.valorcantidadt.config(text=self.TotalC)

    def AgregarFactura(self):
        self.TotalC =0.00
        self.TotalSub =0.00
        self.TotalITBS =0.00
        self.TotalT =0.00
        valor=self.ComboBOXProv.get()
        cur=self.conexionBD.cursor()
        sql="Select Prov_Codigo from Proveedores Where Prov_Nombre='{}'".format(valor)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            provCodigo=int(i[0])
        sql='Select * From Proveedores where Prov_Codigo={}'.format(provCodigo)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            ProveedorNombre=i[2]
            CedulaRNC=i[5]
            Direccion=i[1]
            Telefono=i[4]
        sql="Select TOP 1 Ped_NoPedido from Pedidos Order by Ped_NoPedido desc"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable=i[0]
        sql="select count(*) from Pedidos"
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            variable1=i[0]
        if variable1==0:
            self.Factura=1
        else:
            self.Factura=variable+1
    
        for child in self.grid1.get_children():
                self.TotalC +=int((self.grid1.item(child, 'values')[3]))
                self.TotalSub +=round(float((self.grid1.item(child, 'values')[4])),2)
                self.TotalITBS +=round(float((self.grid1.item(child, 'values')[5])),2)
                self.TotalT +=round(float((self.grid1.item(child, 'values')[6])),2)
        for child in self.grid1.get_children():
                self.codigo=int((self.grid1.item(child, 'values')[0]))
                self.cantidad=int((self.grid1.item(child, 'values')[3]))
                self.AgregarUnidadesAlmacen(self.codigo,self.cantidad)

        if self.TotalC==0.0:
            self.ventanaInfo()
        else:
            sql="INSERT INTO Pedidos (Ped_NoPedido,Ped_MontoTotal,Ped_Proveedor) values(?,?,?)"
            try:
                cur.execute(sql,self.Factura,self.TotalSub,provCodigo)
                self.agregarDetalleFact(self.Factura)
                self.pdf(self.Factura,self.TotalC,self.TotalSub,self.TotalITBS,self.TotalT,ProveedorNombre, CedulaRNC, Direccion,Telefono)
                self.limpiarTodo()
                self.ventanaExitosa()
                self.ObtenerNoFactura()
            except pyodbc.ProgrammingError:
                self.ventanaError()
        cur.commit()
        cur.close()

    def agregarDetalleFact(self,Factura):
        cur=self.conexionBD.cursor()
        sql='INSERT INTO DetallePedido (DetP_NoPedido,DetP_Cantidad,DetP_Producto,DetP_ProDescrp,Ped_NoAlmacen) values(?,?,?,?,?)'     
        for child in self.grid1.get_children():
            self.CodigoProducto=int(self.grid1.item(child,'values')[0])
            self.Cantidad=int(self.grid1.item(child, 'values')[3])
            self.Descripcion=self.grid1.item(child,'values')[1]
            self.NoAlmacen=1
            cur.execute(sql,Factura,self.Cantidad,self.CodigoProducto,self.Descripcion,self.CodigoProducto)
        cur.commit()
        cur.close()

    def AgregarUnidadesAlmacen(self,valor,cantidad):
        cur=self.conexionBD.cursor()
        sql='Select Alm_UnidadesDisponibles from Almacenes Where Alm_Producto={}'.format(valor)     
        cur.execute(sql)
        x=cur.fetchall()
        uni = 0

        for i in x:
            uni = i[0]
        if uni == None:
            uni = 0
            
        total=uni+cantidad
        sql='UPDATE Almacenes Set Alm_UnidadesDisponibles={} Where Alm_Producto={}'.format(total,valor)
        cur.execute(sql)
        cur.commit()
        cur.close()
            
        con = self.conexionBD.cursor()
        sql_uni_cost = 'Select Prod_CostoUnidad from Productos Where Prod_Codigo={}'.format(valor)
        con.execute(sql_uni_cost)
        cost_producto = con.fetchall()
        _value = 0
        for a in cost_producto:
            _value = a[0]
        
        valor_inv = int(_value) * total
        sql_valor_inv = 'UPDATE Almacenes Set Alm_ValorInventario={} Where Alm_Producto={}'.format(valor_inv, valor)
        con.execute(sql_valor_inv)
        con.commit()
        con.close()

    

    def limpiarTodo(self):
        self.ComboBOXProv.set('')
        self.ComboBOXProvPro.set('')
        self.cantidadVar.set(0)
        self.t6.config(text='')
        for child in self.grid1.get_children():
            self.grid1.delete(child)
        self.valorITBISt.config(text=0.00)
        self.valortotalt.config(text=0.00)
        self.valorsubtotalt.config(text=0.00)
        self.valorcantidadt.config(text=0.00)
        
    def ventanaError(self):
        messagebox.showerror(message="No hay ningun producto agregado",title="Error")

    def ventanaInfo(self):
        messagebox.showinfo(message="Agregue productos para generar pedido",title="Informacion")
        self.pdf()

    def ventanaExitosa(self):
        messagebox.showinfo(message="Se ha generado la pedido de manera exitosa",title="Informacion")

    def eliminar(self):
        x=self.grid1.selection()
        for row in x:
            self.grid1.delete(row)
        self.Resumenes()
    #CREATE PDF
    def pdf(self,Factura,TotalCantidad, TotalSub, TotalITBIS,TotalT,clienteNombre, CedulaRNC, Direccion,Telefono):
        lista=list()
        titulos=list(('Codigo','Producto','Costo','Cantidad','Subtotal','ITBIS','Total'))
        lista.append(titulos)
        for child in self.grid1.get_children():
            lista.append(self.grid1.item(child,'values'))

        File_Name=Fecha+' NoPedido '+str(Factura)+'.pdf'
        pdf= SimpleDocTemplate(File_Name, pagesize=letter)
        style= TableStyle([('BACKGROUND',(0,0), (-1,0), colors.ReportLabBlueOLD),
                            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                            ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            ('FONTNAME',(0,0),(-1,0),'Courier'),
                            ('BOTTOMPADDING',(0,0),(-1,0),12),
                            ('GRID',(0,1),(-1,-1),1,colors.black)])
        table=Table(lista)
        
        table.setStyle(style)
        elems=[]
        stylep= ParagraphStyle('stylep',spaceBefore=6, alignment=TA_CENTER)
        elems.append(paragraph.Paragraph("MEGAMERCADO",stylep))
        elems.append(paragraph.Paragraph(Fecha,stylep))
        elems.append(paragraph.Paragraph('No. Pedido: '+ str(Factura),stylep))
        elems.append(paragraph.Paragraph("Proveedor: "+ clienteNombre + ' Cedula/RNC: ' +  str(CedulaRNC),stylep))
        elems.append(paragraph.Paragraph("Direccion: " + str(Direccion)+' Telefono: ' + str(Telefono),stylep))
        elems.append(table)
        elems.append(paragraph.Paragraph("Cantidad Total: " + str(int(TotalCantidad)),stylep))
        elems.append(paragraph.Paragraph("Subtotal: "+ str(TotalSub),stylep))
        elems.append(paragraph.Paragraph("ITBIS Total: "+ str(TotalITBIS),stylep))
        elems.append(paragraph.Paragraph("Total: "+ str(TotalT),stylep))
        pdf.build(elems)
        subprocess.Popen([File_Name], shell=True)       