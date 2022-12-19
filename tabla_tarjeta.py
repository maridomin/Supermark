import sqlite3
from crear_bd import crear_conexion 

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_tarjeta_tabla= """CREATE TABLE IF NOT EXISTS tarjetacredito(
                            numero BIGINT PRIMARY KEY,
                            banco TEXT NOT NULL,
                            titular TEXT NOT NULL,
                            fechaCaducidad TEXT NOT NULL,
                            id_usuario INTEGER,
                            FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
                            );"""
 
                       
conexion = crear_conexion("Supermarket.db")
crear_tabla(conexion, sql_crear_tarjeta_tabla)

#esta es la creación de tabla para tarjeta de credito