import sqlite3
from crear_bd import crear_conexion 


def crear_datos(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()



conexion= crear_conexion("Supermarket.db")

#crear_datos(conexion,sql_tarjeta)
