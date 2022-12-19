#import imp
import tkinter 
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from crear_bd import crear_conexion
from consulta_usuario import validar_usuario
from panel_admin import Panel
from panel_usuario import Paneluser

class Login(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        self.title('Supermark Entrar a Cuenta')
        
        width = 400 # Width 
        height = 250 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def crear_widgets(self):
        ttk.Label(self, text= "Nombre").grid(row=1, column=0, padx=30, pady=20, ipadx=20, ipady=10)
        ttk.Label(self, text= "Apellido").grid(row=2, column=0, padx=30, pady=10, ipadx=20, ipady=10)
        ttk.Label(self,text="Contraseña").grid(row=3, column=0, padx=30, pady=10, ipadx=20, ipady=10)
        
        
        self.entry_nombres = tkinter.StringVar()
        ttk.Entry(self, textvariable= self.entry_nombres).grid(row=1, column=1)
        
        self.entry_apellidos = tkinter.StringVar()
        ttk.Entry(self, textvariable= self.entry_apellidos).grid(row=2, column=1)
        
        self.entry_pass = tkinter.StringVar()
        ttk.Entry(self, textvariable= self.entry_pass).grid(row=3, column=1)
        
        ttk.Button(self, text="ingresar", command=self.verificar_datos).grid(row=4, column=1)
    
    def abrir_paneluser(self):
        Paneluser(self.root)

    def abrir_paneladmin(self):
        Panel(self.root)

    class Usuario():
        def __init__(self,id_usuario,apellido,nombre,email,dni,tipo_usuario,condicional):
            self.__id_usuario=id_usuario
            self.__apellidos=apellido
            self.__nombres=nombre
            self.__email=email
            self.__dni=dni
            self.__tipo_usuario=tipo_usuario
            self.__condicional=condicional

        #getters y setters
        def getIdUsuario(self):
            return self.__id_usuario
        def getApellidos(self): 
            return self.__apellidos
        def getNombres(self):
            return self.__nombres
        def getEmail(self):
            return self.__email
        def getDni(self):
            return self.__dni
        def getTipoUsuario(self):
            return self.__tipo_usuario
        def getCondicional(self):
            return self.__condicional

        def setIdUsuario(self,id):
            self.__id_usuario=id
        def setApellidos(self,apellido):
            self.__apellido=apellido
        def setNombres(self,nombre):
            self.__nombre=nombre
        def setEmail(self,email):
            self.__email=email
        def setDni(self,dni):
            self.__dni=dni
        def setEmail(self,email):
            self.__email=email
        def setTipoUsuario(self,tipo_usuario):
            self.__tipo_usuario=tipo_usuario
        def setCondicional(self,condicional):
            self.__condicional=condicional

        ########
    
    def verificar_datos(self):
        ruta = "Supermarket.db"
        conexion = crear_conexion(ruta)
        consulta = f"SELECT * FROM usuario WHERE nombres = '{self.entry_nombres.get()}' and apellidos = '{self.entry_apellidos.get()}' and pass= '{self.entry_pass.get()}'"
        respuesta=validar_usuario(conexion, consulta)
        #global usuario para sacar el id_usuario cuando loguea y guardarlo asi lo uso para identificar carrito y compras del usuario en la db
        global usuario
        usuario = self.Usuario(respuesta[0][0], respuesta[0][1], respuesta[0][2], respuesta[0][3], respuesta[0][4], respuesta[0][6], respuesta[0][7])
        if respuesta != [ ]:
            if respuesta[0][7] == 1: #revisando el "pseudo booleano" para ver si el q se loguea es adm o usuario
                self.abrir_paneluser() #reemplazar esta linea con el codigo para ir al panel usuario (hecho)
            else:
                self.abrir_paneladmin() #reemplazar esta linea con el codigo para ir al panel adm (hecho)
        else:
            messagebox.showerror(message='usuario incorrecto')
        

conexion= crear_conexion("Supermarket.db")