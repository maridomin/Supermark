import sqlite3
from crear_bd import crear_conexion

def validar_usuario(conexion,consulta):
    cursor=conexion.cursor()
    cursor.execute(consulta)
    filas = cursor.fetchall()
    if len(filas)>0:
        return filas
    else: 
        return
        
def obtener_usuarios(conexion):
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    filas = cursor.fetchall()
    return filas

conexion= crear_conexion("Supermarket.db")