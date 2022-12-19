from calendar import c
from fileinput import filename
import tkinter 
from tkinter import Scrollbar, ttk, Button, Frame, messagebox, Tk, Toplevel
import tkinter as tk
from crear_bd import crear_conexion
from consulta_producto import select_producto, select_producto_by_id
from insertar_datos import crear_datos
from consulta_orden import *
import time
#from datetime import date, time, datetime


class Paneluser(Toplevel):
    
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.title('Bienvenido a Supermark, elija los productos y realice su compra')

        width = 1220 # Width 
        height = 370 # Height

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen
 
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
 
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.nb = ttk.Notebook(self)

        self.p1 = ttk.Frame(self.nb)
        self.crear_tabla()
        self.nb.add(self.p1, text="Ver Productos")
       
        self.p2 = ttk.Frame(self.nb)
        self.crear_tabla2()
        self.nb.add(self.p2, text="Carrito")

        self.nb.pack(fill="both", expand="Yes")
    
    def crear_tabla(self):
        columns = ('idproducto', 'idcategoria', 'titulo', 'stock', 'descripcion', 'precio')

        self.tree = ttk.Treeview(self.p1, columns=columns, show='headings')
        self.tree.grid(row=1, column=1, sticky= (tk.N, tk.S, tk.E, tk.W))

        self.tree.heading('idproducto', text= 'ID')
        self.tree.heading('idcategoria', text= 'Categoria')
        self.tree.heading('titulo', text= 'Titulo')
        self.tree.heading('stock', text= 'Stock')
        self.tree.heading('descripcion', text= 'Descripcion')
        self.tree.heading('precio', text= 'Precio')

        #self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado)

        scrollbar = ttk.Scrollbar(self.p1, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))

        conexion= crear_conexion("Supermarket.db")
        filas = select_producto(conexion)

        for fila in filas:
            self.tree.insert('', tk.END, values=fila)

        ttk.Label(self.p1, text="Ingresa la cantidad").grid(row=3, column=1, pady=7)

        self.entry_cantidad = tk.IntVar()
        ttk.Entry(self.p1, textvariable=self.entry_cantidad).grid(row=4, column=1, pady=7)
        ttk.Button(self.p1, text="Comprar", command=self.comprar_producto).grid(row=5, column=1, pady=7)

    def crear_tabla2(self):
        columns = ('titulo', 'cantidad', 'subtotal')

        self.tree2 = ttk.Treeview(self.p2, columns=columns, show='headings')
        self.tree2.grid(row=1, column=1, sticky= (tk.N, tk.S, tk.E, tk.W))

        self.tree2.heading('titulo', text= 'Titulo')
        self.tree2.heading('cantidad', text= 'Cantidad')
        self.tree2.heading('subtotal', text= 'Subtotal')

        #self.tree2.bind('<<TreeviewSelect>>', self.item_seleccionado)

        scrollbar = ttk.Scrollbar(self.p2, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))    

        ttk.Button(self.p2, text="Finalizar Compra", command=self.finalizar_compra).grid(row=3, column=1, pady=14)

        self.cargar_orden()

    def cargar_orden(self):
        #borrar las filas ya existentes
        for record in self.tree2.get_children():
            self.tree2.delete(record)
        
        from login import usuario
        #agregar las filas de la tabla orden
        conexion= crear_conexion("Supermarket.db")
        filas = select_orden(conexion, usuario.getIdUsuario())

        for fila in filas:
            self.tree2.insert('', tk.END, values=(fila[1], fila[2], fila[3]))


    def comprar_producto(self):
        carrito = self.tree2.get_children()
        if len(carrito) == 30:
            messagebox.showerror(message="El carrito esta lleno (maximo 30 productos)!")
            return

        producto = self.tree.focus()
        valores = self.tree.item(producto)
        if valores:
            valores_producto = valores["values"]
            if valores_producto:
                id_producto = valores_producto[0]
            else:
                messagebox.showerror(message="No seleccionaste un producto")
        else:
            messagebox.showerror(message="No seleccionaste un producto")

        if self.entry_cantidad.get() <= 0:
            messagebox.showerror(message="La cantidad debe ser mayor que 0")
            return

        ruta = "Supermarket.db"
        conexion = crear_conexion(ruta)
        consulta = f"SELECT * FROM producto WHERE idproducto = {id_producto}"
        fila= select_producto_by_id(conexion,consulta)
        if len(fila) == 0:
            messagebox.showerror(message="Producto no encontrado")
        else:
            from login import usuario
            if fila[0][3]>= self.entry_cantidad.get():
                resp=messagebox.askquestion(message=f"{fila[0][2]} -- {fila[0][4]} -- ${fila[0][5]}")
                if resp == "yes":
                    id_usuario = usuario.getIdUsuario()
                    consulta = f"INSERT INTO orden(id_usuario, titulo, cantidad, subtotal, fechahora) VALUES({id_usuario}, '{fila[0][2]}', {self.entry_cantidad.get()}, {fila[0][5]} * {self.entry_cantidad.get()}, '{time.strftime('%d-%m-%Y - %H:%M:%S')}')"
                    crear_datos(conexion,consulta)
                    self.cargar_orden()
            else:
                messagebox.showerror(message="Cantidad insuficiente")

    def finalizar_compra(self):
        from login import usuario
        #imprimir la orden
        conexion= crear_conexion("Supermarket.db")
        id_usuario = usuario.getIdUsuario()
        filas = select_orden(conexion, id_usuario)
        if len(filas) >= 1:
            orden = "Compraste los siguientes productos\n\n"
            total = 0
            hora = time.strftime('%d-%m-%Y - %H:%M:%S')
            for fila in filas:
                orden+= f"Producto: {fila[1]} - Cantidad: {fila[2]}\n\n"
                total+= int(fila[3])

                #agregar la compra a la tabla para el admin
                crear_datos(conexion, f"INSERT INTO compras (id_usuario, titulo, cantidad, subtotal, fechahora) VALUES({id_usuario}, '{fila[1]}', {fila[2]}, {fila[3]}, '{hora}')")

        
            orden+= f"Sub total: ${total}\n\n"
            orden+= "Gracias por tu compra!"

            #actualizar el valor compras_totales del cliente
            crear_datos(conexion, f"UPDATE usuario SET compras_totales = compras_totales + 1 WHERE id_usuario={id_usuario}")

            #enviarle un mensaje al cliente
            messagebox.showinfo(message=orden)
        
            #borrar las ordenes de compra
            borrar_ordenes(conexion, id_usuario)
        else:
            messagebox.showerror(message="El carrito esta vacio")