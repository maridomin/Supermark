import sqlite3
from crear_bd import crear_conexion 

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_usuario_tabla= """CREATE TABLE IF NOT EXISTS usuario(
                            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                            apellidos TEXT NOT NULL,
                            nombres TEXT NOT NULL,
                            email TEXT NOT NULL,
                            dni INTEGER NOT NULL,
                            pass TEXT NOT NULL,
                            tipo_usuario TEXT DEFAULT usuario NOT NULL,
                            condicional INTEGER DEFAULT 1 NOT NULL,
                            compras_totales INTEGER DEFAULT 0 NOT NULL);""" #condicional es un "pseudo booleano" para admin = 0 o usuario = 1
 
                       
conexion = crear_conexion("Supermarket.db")
crear_tabla(conexion, sql_crear_usuario_tabla)

#esta es la creación de tabla para usuarios (falta agregar rol de admins o asi)