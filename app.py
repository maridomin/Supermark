import tkinter 

from tkinter import ttk, Button, Frame, messagebox, Tk
from login import Login
from registro import CrearCuenta

class App(Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        root.title('Supermark Inicio')

        #color ventana
        #root.configure(bg='#FFEBCD')

        width = 600 # Width 
        height = 300 # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def crear_widgets(self):
        self.button= Button(self)
        self.button["text"] = "Login"
        self.button["command"] = self.abrir_login 
        self.button.grid(padx=125, pady=50, ipadx=150, ipady=25)
        
        self.button1= Button(self)
        self.button1["text"] = "Registro"
        self.button1["command"] = self.abrir_registro 
        self.button1.grid(padx=125, pady=10, ipadx=150, ipady=25)
        
        
    def abrir_login(self):
        Login(self.root)
        
    
    def abrir_registro(self):
        CrearCuenta(self.root)
    
    
root=Tk()
app= App(root)
app.mainloop()