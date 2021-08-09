from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, pyodbc
from pyodbc import *
from datetime import date, datetime,timedelta
Fecha= datetime.now().strftime("%Y-%m-%d")

Validacion=False
Error=False
class Ui_MainWindow(object):
   
    def __init__(self):
        self.conexionBD=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};'
                                'SERVER=DESKTOP-4IOJCET;'
                                'DATABASE=MegaMercado;'
                                'Trusted_Connection=yes;')
        print("Base de datos conectada")
        
    def RegistrarProveedorSQL(self, codigo,direccion,nombres,apellidos,RnC,telefono,Status):
        cur = self.conexionBD.cursor()
        sql= "INSERT INTO Clientes (Cli_Codigo,Cli_Direccion,Cli_Nombres,Cli_Apellidos,Cli_RNC_Cedula,Cli_Telefono,Cli_Estatus) Values(?,?,?,?,?,?,?)"
        cur.execute(sql,codigo,direccion,nombres,apellidos,RnC,telefono,Status)
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEditApe.clear()
        self.ventanaExitosa()
        cur.commit()
        cur.close()  

    def EliminaProveedorSql(self,codigo):
        cur = self.conexionBD.cursor()
        sql='''UPDATE Clientes Set Cli_Estatus='I' WHERE Cli_Codigo = {}'''.format(codigo)
        self.ejecuccionExitosa(sql,cur)
        a = cur.rowcount
        cur.commit()    
        cur.close()
        return a 

    def ActualizarProvSql(self,direccion,nombres,apellidos,RnC,telefono,codigo):
        cur= self.conexionBD.cursor()
        sql ='''UPDATE Clientes SET Cli_Direccion = '{}', Cli_Nombres = '{}', Cli_Apellidos = '{}', Cli_RNC_Cedula= '{}',Cli_Telefono= '{}'
        WHERE Cli_Codigo = '{}' '''.format(direccion,nombres,apellidos,RnC,telefono,codigo)
        self.ejecuccionExitosa(sql,cur)
        a = cur.rowcount
        cur.commit()    
        cur.close()
        return a 

    def traerTodo(self,codigo):
        cur=self.conexionBD.cursor()
        sql="Select * from Clientes WHERE Cli_Codigo={}".format(codigo)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
                return self.lineEdit_5.setText(str(i[2])),self.lineEditApe.setText(str(i[3])),self.lineEdit_8.setText(str(i[4])),self.lineEdit_9.setText(str(i[1])),self.lineEdit_6.setText(str(i[5]))

    def ActualizarProv(self):
        global Validacion
        global Error
        variable=''
        variable1=''
        variable2=''
        Validacion=False
        telefonos= ["849","829","809"]
        cur= self.conexionBD.cursor()
        apellidos=self.lineEditApe.text().strip()
        codigo= self.lineEdit_7.text()
        direccion=self.lineEdit_9.text().strip()
        nombres= self.lineEdit_5.text().strip()
        telefono=self.lineEdit_6.text().strip()
        RnC=self.lineEdit_8.text().strip()
        try:    
                sql="SELECT CLi_Estatus from Clientes where Cli_Codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        variable3=(str(i[0]))
                        
                sql="SELECT Cli_RNC_Cedula from Clientes where Cli_RNC_Cedula={} and Cli_Codigo<>{}".format(RnC,codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        variable=(str(i[0]))
                sql1="SELECT Cli_Telefono from Clientes where Cli_Telefono={} and Cli_Codigo<>{}".format(telefono,codigo)
                cur.execute(sql1)
                x=cur.fetchall()
                for i in x:
                        variable1=(str(i[0]))
                sql="SELECT Cli_Codigo from Clientes where Cli_Codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        variable2=(str(i[0]))
                   
        except pyodbc.ProgrammingError: 
                pass
        try:
                if self.verificarCodgioExist(codigo)==False:
                        self.ventanaErrorCod()
                elif variable3=="I":
                        self.RecuperarProveedorSQL(codigo)
                elif nombres=="" or direccion=="" or apellidos=="":
                        self.ventanaError2()
                elif variable==self.lineEdit_8.text():
                        self.ventanaError1_1()
                elif (len(self.lineEdit_9.text())==0 or len(self.lineEdit_5.text())==0) :
                        self.ventanaError2()
                elif len(self.lineEdit_6.text())!=10:
                        self.ventanaError3()
                elif len(self.lineEdit_8.text())!=11:
                        self.ventanaError4()
                elif telefono[:3] not in telefonos:
                        self.ventanaErrorTel()
                elif variable1==self.lineEdit_6.text():
                        self.ventanaTelefono()
                        if Validacion:
                                self.ActualizarProvSql(direccion,nombres,apellidos,RnC,telefono,codigo)
                else: 
                        self.ventanaConfirmacion_1()
                        if Validacion: 
                                self.ActualizarProvSql(direccion,nombres,apellidos,RnC,telefono,codigo)
                Error=False
        except pyodbc.ProgrammingError: 
               self.ventanaError2()
        cur.commit()
        cur.close()

    def RegistrarProv(self):
        global Validacion
        variable=''
        variable1=''
        Validacion=True
        telefonos= ["849","829","809"]
        cur= self.conexionBD.cursor()
        try:
                codigo=int(self.obtenerUltimoProv())+1
        except TypeError:
                codigo=1
        Status='A'
        apellidos=self.lineEditApe.text().strip()
        direccion= self.lineEdit_9.text().strip()
        nombres= self.lineEdit_5.text().strip()
        telefono=self.lineEdit_6.text().strip()
        RnC=self.lineEdit_8.text().strip()
        try:   
                sql="SELECT Cli_RNC_Cedula from Clientes where Cli_RNC_Cedula={}".format(RnC)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        variable=(str(i[0]))
                sql1="SELECT Cli_Telefono from Clientes where Cli_Telefono={}".format(telefono)
                cur.execute(sql1)
                x=cur.fetchall()
                for i in x:
                        variable1=(str(i[0]))
                if nombres=="" or direccion=="" or apellidos=="":
                        self.ventanaError2()
                elif variable==self.lineEdit_8.text():
                        self.ventanaError1_1()
                elif len(self.lineEdit_6.text())!=10:
                        self.ventanaError3()
                elif len(self.lineEdit_8.text())!=11:
                        self.ventanaError4()
                elif telefono[:3] not in telefonos:
                        self.ventanaErrorTel()
                elif variable1==self.lineEdit_6.text():
                        self.ventanaTelefono()
                        if Validacion:
                                self.RegistrarProveedorSQL(codigo,direccion,nombres,apellidos,RnC,telefono,Status)
                else:
                        self.RegistrarProveedorSQL(codigo,direccion,nombres,apellidos,RnC,telefono,Status)
        except pyodbc.ProgrammingError:
               self.ventanaError2()
        cur.commit()
        cur.close()
                
    def EliminiarProveedor(self):
        global Validacion
        global Error
        Validacion=False
        codigo=self.lineEdit_7.text()
        try: 
                self.VerifacionBorrado(codigo)
                if self.verificarCodgioExist(codigo)==False:
                        self.ventanaErrorCod()
                elif Error==False:
                        self.ventanaConfirmacion(codigo)
                        self.borrarCampos()
                else:
                        self.borrarCampos()
                if Validacion:
                        self.EliminaProveedorSql(codigo)
        except pyodbc.ProgrammingError: 
                self.ventanaError2()
        Error=False
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(440, 65, 400, 31))
        self.label.setStyleSheet("font: 0 15pt \"Roboto Mono\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(275, 200, 101, 21))
        self.label_2.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 480, 181, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(33, 167, 218);\n"
"font: 63 13pt \"Roboto Mono\";\n"
"font-weight: bold;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton4 = QtWidgets.QPushButton(self.frame)
        self.pushButton4.setGeometry(QtCore.QRect(600, 480, 181, 51))
        self.pushButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton4.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(49, 210, 49);\n"
"font: 63 13pt \"Roboto Mono\";\n"
"font-weight: bold;\n"
"")
        self.pushButton4.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(480, 30, 240, 41))
        self.label_4.setStyleSheet("font: 75 20pt \"Roboto Mono\";\n"
"font-weight: bold")
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 200, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(246, 250, 130, 21))
        self.label_5.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(235, 300, 171, 21))
        self.label_6.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(243, 350, 131, 21))
        self.label_7.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 400, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 300, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 350, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 480, 181, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("""
QPushButton{       
color:rgb(255, 255, 255);
background-color: rgb(225, 13, 13);
font: 63 13pt \"Roboto Mono\";
font-weight: bold;}
""")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(254, 400, 131, 31))
        self.label_8.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(290, 140, 101, 51))
        self.label_3.setStyleSheet("font: 12pt \"Roboto Mono\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(390, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEditApe = QtWidgets.QLineEdit(self.frame)
        self.lineEditApe.setGeometry(QtCore.QRect(390, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono ")
        font.setPointSize(9)
        self.lineEditApe.setFont(font)
        self.lineEditApe.setText("")
        self.lineEditApe.setObjectName("lineEditApe")
        self.verticalLayout.addWidget(self.frame)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_5, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_8)
        #Restrigciones en los entradas de datos
        self.lineEdit_5.setMaxLength(50)
        self.lineEdit_6.setMaxLength(10)
        self.lineEdit_8.setMaxLength(11)
        self.lineEdit_9.setMaxLength(70)
        regex = QtCore.QRegExp("[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]*")
        RegEx1= QtCore.QRegExp("[0-9]*")
        validator = QtGui.QRegExpValidator(regex, self.lineEdit_5)
        validatorInt= QtGui.QRegExpValidator(RegEx1, self.lineEdit_6)
        validatorInt2= QtGui.QRegExpValidator(RegEx1, self.lineEdit_8)
        validatorInt3= QtGui.QRegExpValidator(RegEx1, self.lineEdit_7)
        self.lineEdit_5.setValidator(validator)
        self.lineEditApe.setValidator(validator)
        self.lineEdit_6.setValidator(validatorInt)
        self.lineEdit_8.setValidator(validatorInt2)
        self.lineEdit_7.setValidator(validatorInt3)
        #Borde Estilo
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.pushButton4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEdit_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEdit_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEdit_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEdit_8.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEdit_9.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.lineEditApe.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=1))
        self.pushButton.clicked.connect(self.RegistrarProv)
        self.pushButton_3.clicked.connect(self.EliminiarProveedor)
        self.pushButton4.clicked.connect(self.ActualizarProv)
        self.fecha = QtWidgets.QLabel(self.frame)
        self.fecha.setGeometry(QtCore.QRect(520, 95, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(12)
        self.fecha.setFont(font)
        self.fecha.setText(Fecha)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(8)
        font.setBold(True)
        QToolTip.setFont(QFont('Roboto Mono', 8))
        #Icono
        imagen = QtWidgets.QLabel(self.frame)
        pixmap = QPixmap('icon .png')
        imagen.setPixmap(pixmap)
        imagen.resize(50,50)
        imagen.setGeometry(550, 150, 271, 31)
        imagen.setToolTip("1. Este campo no se necesita a la hora de registrar\n2. Si desea eliminar solo introduzca el codigo \n3. Si desea recuperar un cliente, solo introduzca\n   el codigo y ejecute actualizar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro de Clientes"))
        self.label.setText(_translate("MainWindow", "Registro de Clientes"))
        self.label_2.setText(_translate("MainWindow", "Nombres:"))
        self.pushButton.setText(_translate("MainWindow", "Registrar"))
        self.label_4.setText(_translate("MainWindow", "MEGAMERCADO"))
        self.label_5.setText(_translate("MainWindow", "Apellidos:"))
        self.label_6.setText(_translate("MainWindow", "RNC/Cedula:"))
        self.label_7.setText(_translate("MainWindow", "Dirección:"))
        self.pushButton_3.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton4.setText(_translate("MainWindow", "Actualizar"))
        self.label_8.setText(_translate("MainWindow", "Teléfono:"))
        self.label_3.setText(_translate("MainWindow", "Código:"))    
 
    def ventanaErrorCod(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El codigo " + self.lineEdit_7.text()+ " no existe")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_() 

    def ventanaErrorTel(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El telefono "+ self.lineEdit_6.text()+ " no es existe")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_() 

    def ventanaError1_1(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El RNC del cliente ya existe.")
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText("El RNC "+ self.lineEdit_8.text() + " ya esta registrado en la Base de datos.")
                msg.exec_()

    def ventanaError2(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error en los datos.")
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText("Verifique que los campos no estan vacios")
                msg.exec_()

    def ventanaError3(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error en los datos.")
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText("El campo telefono debe de tener 10 digitios")
                msg.exec_()

    def ventanaError4(self):
                msg= QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error en los datos.")
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText("El campo RNC debe de tener 11 digitios")
                msg.exec_()

    def ventanaExitosa(self):
                msg= QMessageBox()
                msg.setWindowTitle("Accion ejectuada")
                msg.setText("La accion ha sido realizada con exito")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

    def ventanaTelefono(self):
                msg= QMessageBox()
                msg.setWindowTitle("Validacion de accion")
                msg.setText("El telefono "+ self.lineEdit_6.text() + " ya esta registardo ¿Seguro que quiere usar este telefono?")
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.buttonClicked.connect(self.ventanaConfButton)
                msg.exec_()

    def ventanaConfirmacion(self,codigo):
                self.traerTodo(codigo)
                msg= QMessageBox()
                msg.setWindowTitle("Validacion de accion")
                msg.setText("¿Estas seguro que deseas eliminar el cliente de codigo?")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.buttonClicked.connect(self.ventanaConfButton)
                msg.exec_() 

    def ventanaConfirmacion_1(self):
                msg= QMessageBox()
                msg.setWindowTitle("Validacion de accion")
                msg.setText("¿Estas seguro que deseas cambiar los datos del clientes de codigo " + self.lineEdit_7.text()+ ", nombre "+ self.ObtenerNombre()
                +" y cedula/RNC "+ self.ObtenerRNC_Cedula()+"?")
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.buttonClicked.connect(self.ventanaConfButton)
                msg.exec_()

    def ventanaConfButton(self,i):
                global Validacion
                if i.text()=='&Yes':
                        Validacion=True
                else:
                        Validacion=False

    def obtenerUltimoProv(self):
                sql='Select TOP 1 Cli_Codigo from Clientes Order by Cli_Codigo desc'
                cur = self.conexionBD.cursor()
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        return i[0]

    def ObtenerNombre(self):
                codigo=self.lineEdit_7.text()
                cur = self.conexionBD.cursor()
                sql="SELECT Cli_Nombres from Clientes where Cli_Codigo={}".format(codigo)
                try:
                        cur.execute(sql)
                except pyodbc.ProgrammingError:
                        self.ventanaError2()
                x=cur.fetchall()
                for i in x:
                        return str(i[0])
                cur.commit()
                cur.close()
                
    def ObtenerRNC_Cedula(self):
                codigo=self.lineEdit_7.text()
                cur = self.conexionBD.cursor()
                sql="SELECT Cli_RNC_Cedula from Clientes where Cli_Codigo={}".format(codigo)
                try:
                        cur.execute(sql)
                except pyodbc.ProgrammingError:
                        self.ventanaError2()
                registros= cur.fetchall()
                for i in registros:
                        return str(i[0])
                cur.commit()
                cur.close()

    def VerifacionBorrado(self,codigo):
                var=''
                global Error
                cur=self.conexionBD.cursor()
                sql="SELECT Cli_Estatus from Clientes where Cli_Codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        var=str(i[0])
                if var=='I':
                        msg= QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("El cliente de codigo " + codigo + " ya esta eliminado, no se puede realizar la accion")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                        Error=True
                        var=''
                cur.commit()
                cur.close()

    def recuperarProveedor(self,codigo):
                var=''
                global Error
                cur=self.conexionBD.cursor()
                sql="SELECT Cli_Estatus from Clientes where Cli_Codigo={}".format(codigo)
                cur.execute(sql)
                x=cur.fetchall()
                for i in x:
                        var=str(i[0])
                if var=='I':
                        self.traerTodo(codigo)
                        msg= QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("El cliente de codigo " + codigo + " esta eliminado ¿Desea recuperarlo?")
                        msg.setIcon(QMessageBox.Question)
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        msg.buttonClicked.connect(self.ventanaConfButton)
                        msg.exec_()
                        var=''

    def RecuperarProveedorSQL(self,codigo):
            global Validacion
            cur=self.conexionBD.cursor()
            self.recuperarProveedor(codigo)
            if Validacion:
                msg= QMessageBox()
                msg.setWindowTitle("Accion ejectuada")
                msg.setText("El cliente ha sido recuperado de manera exitosa")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                sql= '''UPDATE Clientes Set Cli_Estatus='A' WHERE Cli_Codigo = {}'''.format(codigo)
                self.borrarCampos()
                cur.execute(sql)
                cur.commit()
                cur.close()
            else:
                self.borrarCampos()

    def ejecuccionExitosa(self,sql,cur):
                cur.execute(sql)
                self.borrarCampos()
                self.ventanaExitosa()

    def verificarCodgioExist(self,codigo):
        cur=self.conexionBD.cursor()
        sql="select count(Prov_Codigo) from Proveedores where Prov_Codigo={}".format(codigo)
        cur.execute(sql)
        x=cur.fetchall()
        for i in x:
                if i[0]==0:
                       return False
    
    def borrarCampos(self):
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEditApe.clear()
             
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())