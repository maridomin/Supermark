import tkinter 

from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from producto import AgregarProducto
from admin_clientes import VerListaClientes

class Panel(Toplevel):
    
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        self.title('Supermark Bienvenido Administrador')

        #color ventana
        #self.configure(bg='#FFEBCD')
                
    def crear_widgets(self):
        width = 400 # Width 
        height = 250 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
        self.button1= Button(self)
        self.button1["text"] = "Ver Lista De Productos"
        self.button1["command"] = self.crear_producto 
        self.button1.grid(padx=30, pady=15, ipadx=100, ipady=30)

        self.button2= Button(self)
        self.button2["text"] = "Ver Lista De Clientes"
        self.button2["command"] = self.lista_clientes 
        self.button2.grid(padx=30, pady=15, ipadx=100, ipady=30) 
    
    def crear_producto(self):
        AgregarProducto(self.root)

    def lista_clientes(self):
        VerListaClientes(self.root)