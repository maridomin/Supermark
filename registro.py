import tkinter 
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from crear_bd import crear_conexion
from consulta_usuario import validar_usuario
from insertar_datos import crear_datos


class CrearCuenta(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        self.title('Supermark Registrar Nueva Cuenta')
         
        width = 400 # Width 
        height = 250 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
               
    def crear_widgets(self):
        ttk.Label(self, text= "Nombre").grid(row=0, column=0, padx=30, pady=5, ipadx=20, ipady=7)
        ttk.Label(self, text= "Apellido").grid(row=1, column=0, padx=30, pady=5, ipadx=20, ipady=7)
        ttk.Label(self, text= "Email").grid(row=2, column=0, padx=30, pady=5, ipadx=20, ipady=7)
        ttk.Label(self, text= "DNI").grid(row=3, column=0, padx=30, pady=5, ipadx=20, ipady=7)
        ttk.Label(self, text= "Contraseña").grid(row=4, column=0, padx=30, pady=5, ipadx=20, ipady=7)
        
        self.entry_nombres= tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_nombres).grid(row=0, column=1)
        
        self.entry_apellidos = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_apellidos).grid(row=1, column=1)
        
         
        self.entry_email = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_email).grid(row=2, column=1)
        
        self.entry_dni = tkinter.IntVar()
        ttk.Entry(self, textvariable=self.entry_dni).grid(row=3, column=1)
        
        self.entry_pass = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_pass).grid(row=4, column=1)
        
        self.button_confirmar= Button(self, text="Confirmar", command=self.crear_usuario).grid(row=5, column=1)
        
        
    def crear_usuario(self):
        ruta = "Supermarket.db"
        conexion = crear_conexion(ruta)
        consulta = f"INSERT INTO usuario(nombres, apellidos,email,dni,pass) VALUES('{self.entry_nombres.get()}', '{self.entry_apellidos.get()}', '{self.entry_email.get()}', {self.entry_dni.get()}, '{self.entry_pass.get()}')"
        crear_datos(conexion, consulta)
        messagebox.showinfo(message="usuario creado correctamente")