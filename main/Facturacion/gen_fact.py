
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

import tkinter as tk
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
import pyodbc



class gen_factura():
    def __init__(self, _frame):
        self._frame = _frame
        self.ITBIS=0.18
        self.fecha= datetime.now().strftime("%Y-%m-%d")

        self.server = 'DESKTOP-4IOJCET'
        self.db = 'MegaMercado'
        self.usuario = 'DESKTOP-4IOJCET\MSI'
        self.contrasena = ''
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};''SERVER='+self.server+';' 'DATABASE='+self.db+';' 'Trusted_Connection=yes;')
        self._cursor = self.conn.cursor()

        self.productoCod= tk.StringVar()
        self.cantidadVar=tk.IntVar()
        self.Clivar=tk.StringVar()
        self.Clivar.trace_add('write',self.callbackClientes)

        self.productoCod.trace_add('write', self.callback)
    
    def gen_prod(self):
        #self.Clivar=tk.StringVar()
        #self.Clivar.trace_add('write',self.callbackClientes)
        self.t1=tk.Label(self._frame, text= "Facturacion", font=("Roboto Mono",20,BOLD), bg="white").place(x=400, y=20)
        self.t2=tk.Label(self._frame, text= self.fecha, font=("Roboto Mono",12), bg="white").place(x=440, y=55)
        self.t3=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t3.place(x=427, y=75)
        self.t4=tk.Label(self._frame, text= "Codgio cliente:", font=("Roboto Mono",12), bg="white").place(x=195, y=130)
        self.t5=tk.Label(self._frame, text= "Codigo producto:", font=("Roboto Mono",12), bg="white").place(x=185, y=165)
        self.t6=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t6.place(x=600, y=165)
        self.t7=tk.Label(self._frame, text= "Cantidad:", font=("Roboto Mono",12), bg="white").place(x=255, y=200)
        self.t8=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t8.place(x=600, y=200)
        self.t9=tk.Label(self._frame, text= "Producto:", font=("Roboto Mono",12), bg="white").place(x=500, y=165)
        self.t10=tk.Label(self._frame, text= "Precio:", font=("Roboto Mono",12), bg="white").place(x=520, y=200)
        self.t11=tk.Label(self._frame, text= "Nombre:", font=("Roboto Mono",12), bg="white").place(x=520, y=133)
        self.t12=tk.Label(self._frame, text= "", font=("Roboto Mono",12), bg="white")
        self.t12.place(x=600, y=133)
        self.t13=tk.Label(self._frame, text= '', font=("Roboto Mono",8, BOLD), fg='red', bg="white")
        self.t13.place(x=125, y=205)
        
        #RESUMENES
        self.Total=0.0
        frame=tk.Frame(self._frame,width=141,height=100)
        frame.config(bg="white",highlightbackground="gray",highlightthickness=1)
        frame.place(x=667,y=417)
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
        self.entryCli=tk.Entry(self._frame, validate="key", validatecommand=(frame.register(self.validate_Codigos), '%S','%P'),textvariable=self.Clivar, width=18,  font=("Roboto Mono",8), bg="#f9f9f9")
        self.entryCli.focus()
        self.entryCli.place(x=355,y=135,height=23)
        self.entryProd=tk.Entry(self._frame,validate="key", validatecommand=(frame.register(self.validate_Codigos), '%S','%P'), textvariable=self.productoCod,width=18,  font=("Roboto Mono",8), bg="#f9f9f9")
        self.entryProd.place(x=355,y=168,height=23)
        self.entryCant=tk.Entry(self._frame,validate="key", validatecommand=(frame.register(self.validate_entry), '%S','%P'),textvariable=self.cantidadVar,width=18,  font=("Roboto Mono",8), bg="#f9f9f9").place(x=355,y=203,height=23)
        #SCROLLBAR
        tree_scrollbar=Scrollbar(self._frame)
        tree_scrollbar.place(x=808,y=280,relheight=0.295)

        #TABLAS
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Roboto Mono', 8)) 
        style.configure("mystyle.Treeview.Heading", font=('Roboto Mono', 9, BOLD)) 
        self.grid1= ttk.Treeview(self._frame, height=5, columns=("#1","#2","#3","#4","#5","#6","#7"), show="headings",style="mystyle.Treeview",yscrollcommand=tree_scrollbar.set)
        tree_scrollbar.config(command=self.grid1.yview)
        self.grid1.place(x=130,y=280)
        self.grid1.column("#1",width=75,anchor=CENTER)
        self.grid1.heading("#1", text="Codigo", anchor=CENTER)
        self.grid1.column("#2",width=100,anchor=CENTER)
        self.grid1.heading("#2", text="Producto", anchor=CENTER)
        self.grid1.column("#3",width=100,anchor=CENTER)
        self.grid1.heading("#3", text="Precio", anchor=CENTER)
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
        self.generar=tk.Button(self._frame, text="Generar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#56ABFF",command=self.AgregarFactura, activebackground="#56ABFF",activeforeground="#f9f9f9")
        self.generar.place(x=355,y=450,width=100,height=40)
        self.limpiar=tk.Button(self._frame, text="Limpiar",font=("Roboto Mono",10,BOLD),fg="#f9f9f9",bg="#56ABFF",command=self.limpiarTodo, activebackground="#56ABFF",activeforeground="#f9f9f9")
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
            cur.commit()
            cur.close()
        except TclError:
            pass
        except UnboundLocalError:
            pass 

    def buscarNombreCliente(self):
        try:
            codigo=self.entryCli.get()
            lista=[]
            cur=self.conn.cursor()
            sql="select Cli_Codigo from Clientes"
            cur.execute(sql)
            x=cur.fetchall()
            for i in x:
                 lista.append(int(i[0]))
            if codigo=="":
                self.t12.config(text="")
            elif int(codigo) not in lista:
                self.t12.config(text="No existe")
            else: 
                cur=self.conn.cursor()
                sql="Select Cli_Nombres,Cli_Apellidos from Clientes where Cli_Codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                    self.t12.config(text=str(i[0]+' '+str(i[1])))
            cur.commit()
            cur.close()
        except TclError:
            pass
        except UnboundLocalError:
            pass
    
    def callback(self,var, indx, mode):
        self.buscarNombreProducto()

    def callbackClientes(self,var, indx, mode):
        self.buscarNombreCliente()

    def validate_entry(self,text,new_text):
        if len(new_text) > 5:
            return False
        return text.isdecimal()
    
    def validate_Codigos(self,text,new_text):
        if len(new_text) > 11:
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
            self.t3.config(text="No. Factura: "+str(variable+1))
        cur.commit()
        cur.close()

    def agregar(self):
        if self.cantidadVar.get()>0:
          self.t13.config(text='')
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
                Total=subtotal+porcentajeITIBIS
                self.grid1.insert('',END,values=(codigo,i[0],i[1],cantidad,subtotal,porcentajeITIBIS,Total))
            self.productoCod.set("")
            self.cantidadVar.set(0)
            self.entryProd.focus()
            self.Resumenes()
            cur.commit()
            cur.close()
          except pyodbc.ProgrammingError:
            self.ventanaError()
        elif self.cantidadVar.get()==0:
            self.t13.config(text='Inserte Cantidad')
        

    def Resumenes(self):
        self.TotalC=0
        self.TotalSub=0.00
        self.TotalITBS=0.00
        self.TotalT=0.00
        for child in self.grid1.get_children():
            self.TotalC +=int((self.grid1.item(child, 'values')[3]))
            self.TotalSub +=float((self.grid1.item(child, 'values')[4]))
            self.TotalITBS +=float((self.grid1.item(child, 'values')[5]))
            self.TotalT +=float((self.grid1.item(child, 'values')[6]))
        self.valorITBISt.config(text=self.TotalITBS)
        self.valortotalt.config(text=self.TotalT)
        self.valorsubtotalt.config(text=self.TotalSub)
        self.valorcantidadt.config(text=self.TotalC)

    def AgregarFactura(self):
        self.TotalC =0.00
        self.TotalSub =0.00
        self.TotalITBS =0.00
        self.TotalT =0.00
        self.clienteCodig=self.Clivar.get()
        cur=self.conn.cursor()
        sql='Select * From Clientes where Cli_Codigo={}'.format(self.clienteCodig)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
            clienteN=i[2]
            ApellidoCliente=i[3]
            CedulaRNC=i[4]
            Direccion=i[1]
            Telefono=i[-2]
        clienteNombre=clienteN+' '+ApellidoCliente
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
            self.Factura=1
        else:
            self.Factura=variable+1
    
        for child in self.grid1.get_children():
                self.TotalC +=int((self.grid1.item(child, 'values')[3]))
                self.TotalSub +=float((self.grid1.item(child, 'values')[4]))
                self.TotalITBS +=float((self.grid1.item(child, 'values')[5]))
                self.TotalT +=float((self.grid1.item(child, 'values')[6]))
        if self.TotalC==0.0:
            self.ventanaInfo()
        else:
            sql="INSERT INTO Factura (Fact_NoFactura,Fact_Fecha,Fact_Subtotal,Fact_TotalITBIS,Fact_Total,Fact_Cliente) values(?,?,?,?,?,?)"
            try:
                cur.execute(sql,self.Factura,self.fecha,self.TotalSub,self.TotalITBS,self.TotalT,self.clienteCodig)
                self.agregarDetalleFact(self.Factura)
                self.pdf(self.Factura,self.TotalC,self.TotalSub,self.TotalITBS,self.TotalT,clienteNombre, CedulaRNC, Direccion,Telefono)
                self.limpiarTodo()
                self.ventanaExitosa()
                self.ObtenerNoFactura()
            except pyodbc.ProgrammingError:
                self.ventanaError()
        cur.commit()
        cur.close()

    def agregarDetalleFact(self,Factura):
        cur=self.conn.cursor()
        sql='INSERT INTO DetalleFacturas (Det_NoFactura,Det_Producto,Det_Cantidad,Det_NoAlmacen) values(?,?,?,?)'     
        for child in self.grid1.get_children():
            self.CodigoProducto=int(self.grid1.item(child,'values')[0])
            self.Cantidad=int(self.grid1.item(child, 'values')[3])
            self.NoAlmacen=self.CodigoProducto
            cur.execute(sql,Factura,self.CodigoProducto,self.Cantidad,self.NoAlmacen)
        cur.commit()
        cur.close()
    
    def limpiarTodo(self):
        self.Clivar.set("")
        self.productoCod.set("")
        self.cantidadVar.set(0)
        for child in self.grid1.get_children():
            self.grid1.delete(child)
        self.valorITBISt.config(text=0.00)
        self.valortotalt.config(text=0.00)
        self.valorsubtotalt.config(text=0.00)
        self.valorcantidadt.config(text=0.00)
        
    def ventanaError(self):
        messagebox.showerror(message="No hay ningun producto agregado",title="Error")

    def ventanaInfo(self):
        messagebox.showinfo(message="Agregue productos para generar factura",title="Informacion")
        self.pdf()

    def ventanaExitosa(self):
        messagebox.showinfo(message="Se ha generado la factura de manera exitosa",title="Informacion")

    def eliminar(self):
        x=self.grid1.selection()
        for row in x:
            self.grid1.delete(row)
        self.Resumenes()
    #CREATE PDF
    def pdf(self,Factura,TotalCantidad, TotalSub, TotalITBIS,TotalT,clienteNombre, CedulaRNC, Direccion,Telefono):
        lista=list()
        titulos=list(('Codigo','Producto','Precio','Cantidad','Subtotal','ITBIS','Total'))
        lista.append(titulos)
        for child in self.grid1.get_children():
            lista.append(self.grid1.item(child,'values'))

        File_Name=self.fecha+' NoFactura '+str(Factura)+'.pdf'
        styles = getSampleStyleSheet()
        Title= 'MegaMercado'
        Sub_Title= self.fecha
        Sub_Title1='No. Factura: '+ str(Factura)
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
        elems.append(paragraph.Paragraph(self.fecha,stylep))
        elems.append(paragraph.Paragraph("Cliente: "+ clienteNombre + ' Cedula/RNC: ' +  str(CedulaRNC),stylep))
        elems.append(paragraph.Paragraph("Direccion: " + str(Direccion)+' Telefono: ' + str(Telefono),stylep))
        elems.append(table)
        elems.append(paragraph.Paragraph("Cantidad Total: " + str(int(TotalCantidad)),stylep))
        elems.append(paragraph.Paragraph("Subtotal: "+ str(TotalSub),stylep))
        elems.append(paragraph.Paragraph("ITBIS Total: "+ str(TotalITBIS),stylep))
        elems.append(paragraph.Paragraph("Total: "+ str(TotalT),stylep))
        pdf.build(elems)
        subprocess.Popen([File_Name], shell=True)


    """
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


    """
