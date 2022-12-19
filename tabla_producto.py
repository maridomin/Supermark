import sqlite3
from crear_bd import crear_conexion 

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_producto_tabla= """CREATE TABLE IF NOT EXISTS producto(
                            idproducto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            idcategoria TEXT NOT NULL,
                            titulo TEXT NOT NULL,
                            stock INTEGER NOT NULL,
                            descripcion TEXT,
                            precio FLOAT NOT NULL);""" # NOT NULL significa q no se puede dejar vacio el campo, la descripcion puede dejarse vacia



                       
conexion = crear_conexion("Supermarket.db")
crear_tabla(conexion, sql_crear_producto_tabla)

#esta es la creación de tabla para producto (lista de productos)





#codigo viejo mas abajo

#import sqlite3
#conexion = sqlite3.connect('producto.db')

#cursor = conexion.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS producto(idproducto INTEGER PRIMARY KEY AUTOINCREMENT,idcategoria TEXT,titulo TEXT,descripcion TEXT,precio DECIMAL)")

#cursor.execute("INSERT INTO producto VALUES(1,'frutas','manzanas','manzanas frescas neuquen por kilo',250)")
#cursor.execute("INSERT INTO producto VALUES(2,'bebidas','agua mineral','agua mineral 1.5 litros',150)")
#cursor.execute("INSERT INTO producto VALUES(1,'verduras','papas','papas por kilo',150)")
#cursor.execute("INSERT INTO producto VALUES(2,'bebidas','gaseosa coca cola','gaseosa coca cola 1.5 litros',250)")

#conexion.close()