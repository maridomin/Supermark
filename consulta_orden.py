import sqlite3
from crear_bd import crear_conexion

def select_orden(conexion, id_usuario):
    cursor=conexion.cursor()
    cursor.execute(f"SELECT id_usuario, titulo, cantidad, subtotal FROM orden WHERE id_usuario = {id_usuario}")
    filas = cursor.fetchall()
    return filas

def borrar_ordenes(conexion, id_usuario):
    cursor=conexion.cursor()
    cursor.execute(f"DELETE FROM orden WHERE id_usuario={id_usuario}")
    conexion.commit()
    return True

conexion= crear_conexion("Supermarket.db")
#print(select_producto(conexion))