import tkinter as tk, tkinter
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from crear_bd import crear_conexion
from insertar_datos import crear_datos
from consulta_producto import select_producto

#codigo prueba para agregar producto

class AgregarProducto(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        self.title('Supermark Aquí puedes Actualizar y Modificar datos de Productos')

        
        width = 1220 # Width 
        height = 540 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def crear_widgets(self):
        columns = ('idproducto', 'idcategoria', 'titulo', 'stock', 'descripcion', 'precio')

        self.lista_productos = ttk.Treeview(self, columns=columns, show='headings')
        self.lista_productos.grid(row=1, column=1, sticky= (tk.N, tk.S, tk.E, tk.W))

        self.lista_productos.heading('idproducto', text= 'ID')
        self.lista_productos.heading('idcategoria', text= 'Categoria')
        self.lista_productos.heading('titulo', text= 'Titulo')
        self.lista_productos.heading('stock', text= 'Stock')
        self.lista_productos.heading('descripcion', text= 'Descripcion')
        self.lista_productos.heading('precio', text= 'Precio')


        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.lista_productos.yview)
        self.lista_productos.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        
        ttk.Label(self, text= "Categoria").grid(row=8, column=1)
        ttk.Label(self, text= "Titulo").grid(row=10, column=1)
        ttk.Label(self, text= "Stock").grid(row=12, column=1)
        ttk.Label(self, text= "Descripcion").grid(row=14, column=1)
        ttk.Label(self, text= "Precio").grid(row=16, column=1)

        self.entry_idcategoria = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_idcategoria).grid(row=9, column=1)
        
        self.entry_titulo = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_titulo).grid(row=11, column=1)
                 
        self.entry_stock = tkinter.IntVar()
        ttk.Entry(self, textvariable=self.entry_stock).grid(row=13, column=1)
        
        self.entry_descripcion = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_descripcion).grid(row=15, column=1)
        
        self.entry_precio = tkinter.IntVar()
        ttk.Entry(self, textvariable=self.entry_precio).grid(row=17, column=1)

        self.button_agregar= Button(self, text="Agregar", command=self.crear_producto).grid(row=18, column=1, pady=5)
        self.button_modificar= Button(self, text="Modificar", command=self.modificar_producto).grid(row=19, column=1, pady=5)
        self.button_borrar= Button(self, text="Borrar", command=self.borrar_producto).grid(row=20, column=1, pady=5)

        self.lista_productos.bind('<ButtonRelease-1>', self.rellenar_campos)

        #cargar los productos
        self.cargar_productos()
    
    def cargar_productos(self):
        #borrar las filas ya existentes
        for record in self.lista_productos.get_children():
            self.lista_productos.delete(record)

        conexion= crear_conexion("Supermarket.db")
        filas = select_producto(conexion)

        for fila in filas:
            self.lista_productos.insert('', tk.END, values=fila)


    def crear_producto(self):
        ruta = "Supermarket.db"
        conexion = crear_conexion(ruta)
        consulta = f"INSERT INTO producto(idcategoria, titulo,stock,descripcion,precio) VALUES('{self.entry_idcategoria.get()}', '{self.entry_titulo.get()}', {self.entry_stock.get()}, '{self.entry_descripcion.get()}', {self.entry_precio.get()})"
        crear_datos(conexion, consulta)
        self.cargar_productos()
        messagebox.showinfo(message="Producto agregado correctamente")
    
    def modificar_producto(self):
        __producto = self.lista_productos.focus()
        producto = self.lista_productos.item(__producto)
        valores_producto = producto["values"]
        if valores_producto:
            resp=messagebox.askquestion(message="¿Seguro que queres modificar el producto?")
            if resp == "yes":
                ruta = "Supermarket.db"
                conexion = crear_conexion(ruta)
                consulta = f"UPDATE producto SET idcategoria = '{self.entry_idcategoria.get()}', titulo = '{self.entry_titulo.get()}', stock = {self.entry_stock.get()}, descripcion = '{self.entry_descripcion.get()}', precio = {self.entry_precio.get()} WHERE idproducto={valores_producto[0]}"
                crear_datos(conexion, consulta)
                self.cargar_productos()
                messagebox.showinfo(message="Producto modificado correctamente")
        else:
            messagebox.showerror(message="No seleccionaste un producto")
    
    def borrar_producto(self):
        __producto = self.lista_productos.focus()
        producto = self.lista_productos.item(__producto)
        valores_producto = producto["values"]
        if valores_producto:
            resp=messagebox.askquestion(message="¿Seguro que queres borrar el producto?")
            if resp == "yes":
                ruta = "Supermarket.db"
                conexion = crear_conexion(ruta)
                consulta = f"DELETE FROM producto WHERE idproducto={valores_producto[0]}"
                crear_datos(conexion, consulta)
                self.cargar_productos()
                messagebox.showinfo(message="Producto borrado correctamente")
        else:
            messagebox.showerror(message="No seleccionaste un producto")


    def rellenar_campos(self, arg):
        __producto = self.lista_productos.focus()
        producto = self.lista_productos.item(__producto)
        valores_producto = producto["values"]
        if valores_producto:
            self.entry_idcategoria.set(valores_producto[1])
            self.entry_titulo.set(valores_producto[2])
            self.entry_stock.set(valores_producto[3])
            self.entry_descripcion.set(valores_producto[4])
            self.entry_precio.set(valores_producto[5])

