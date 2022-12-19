import tkinter as tk
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from crear_bd import crear_conexion
from insertar_datos import crear_datos
from consulta_usuario import obtener_usuarios
from consulta_orden import select_orden

class VerListaClientes(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        self.title('Supermark Lista de Clientes')
        
        
    def crear_widgets(self):
        width = 830 # Width 
        height = 300 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
        self.nb_clientes = ttk.Notebook(self)

        self.p1 = ttk.Frame(self.nb_clientes)
        self.nb_clientes.add(self.p1, text="Clientes")

        self.p2 = ttk.Frame(self.nb_clientes)
        self.nb_clientes.add(self.p2, text="Carrito del cliente")

        self.nb_clientes.pack(fill="both", expand="Yes")
    
        columns = ('id_usuario', 'apellido', 'nombre', 'compras_totales')

        self.lista_clientes = ttk.Treeview(self.p1, columns=columns, show='headings')
        self.lista_clientes.grid(row=1, column=1, sticky= (tk.N, tk.S, tk.E, tk.W))

        self.lista_clientes.heading('id_usuario', text= 'ID')
        self.lista_clientes.heading('apellido', text= 'Apellido')
        self.lista_clientes.heading('nombre', text= 'Nombre')
        self.lista_clientes.heading('compras_totales', text= 'Compras Totales')

        scrollbar_clientes = ttk.Scrollbar(self.p1, orient=tk.VERTICAL, command=self.lista_clientes.yview)
        self.lista_clientes.configure(yscroll=scrollbar_clientes.set)
        scrollbar_clientes.grid(row=1, column=2, sticky=(tk.N, tk.S))

        #cargar la lista de clientes
        conexion= crear_conexion("Supermarket.db")
        filas = obtener_usuarios(conexion)

        for fila in filas:
            self.lista_clientes.insert('', tk.END, values=(fila[0], fila[1], fila[2], fila[8]))


        columns = ('titulo', 'cantidad', 'subtotal')

        self.lista_carrito = ttk.Treeview(self.p2, columns=columns, show='headings')
        self.lista_carrito.grid(row=1, column=1, sticky= (tk.N, tk.S, tk.E, tk.W))

        self.lista_carrito.heading('titulo', text= 'Producto')
        self.lista_carrito.heading('cantidad', text= 'Cantidad')
        self.lista_carrito.heading('subtotal', text= 'Subtotal')

        scrollbar_carrito = ttk.Scrollbar(self.p2, orient=tk.VERTICAL, command=self.lista_carrito.yview)
        self.lista_carrito.configure(yscroll=scrollbar_carrito.set)
        scrollbar_carrito.grid(row=1, column=2, sticky=(tk.N, tk.S))

        ttk.Button(self.p1, text="Ver carrito del cliente", command=self.ver_carrito).grid(row=3, column=1, pady=8)

            
    def ver_carrito(self):
        #borrar las filas ya existentes
        for record in self.lista_carrito.get_children():
            self.lista_carrito.delete(record)

        usuario = self.lista_clientes.focus()
        valores = self.lista_clientes.item(usuario)
        if valores:
            valores_usuario = valores["values"]
            if valores_usuario:
                id_usuario = valores_usuario[0]
                if id_usuario:
                    conexion= crear_conexion("Supermarket.db")
                    carrito = select_orden(conexion, id_usuario)

                    #cargar el carrito del cliente seleccionado
                    for producto in carrito:
                        self.lista_carrito.insert('', tk.END, values=(producto[1], producto[2], producto[3]))
            
                    #cambiar de pestaña
                    self.nb_clientes.select(self.p2)
                else:
                    messagebox.showerror(message="Usuario invalido")
            else:
                messagebox.showerror(message="No seleccionaste un usuario")
        else:
            messagebox.showerror(message="No seleccionaste un usuario")