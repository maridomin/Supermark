import sqlite3
from crear_bd import crear_conexion 
from datetime import date

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_orden_tabla= """CREATE TABLE IF NOT EXISTS orden(
                            idorden INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_usuario INTEGER NOT NULL,
                            titulo TEXT NOT NULL,
                            cantidad INTEGER NOT NULL,
                            subtotal DECIMAL NOT NULL,
                            fechahora DATETIME NOT NULL);"""

#FOREIGN KEY Y REFERENCES ES PARA IMPORTAR COLUMNA DE OTRA TABLA DE LA DB


                       
conexion = crear_conexion("Supermarket.db")
crear_tabla(conexion, sql_crear_orden_tabla)


#esta es la creación de tabla para orden (de compra)