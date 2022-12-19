import sqlite3

from crear_bd import crear_conexion

conexion= crear_conexion("Supermarket.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO producto VALUES (?,?,?,?,?,?)", (None,'frutas','manzanas',5,'manzanas frescas neuquen por kilo',250))
cursor.execute("INSERT INTO producto VALUES (?,?,?,?,?,?)", (None,'bebidas','agua mineral',5,'agua mineral 1.5 litros',150))
cursor.execute("INSERT INTO producto VALUES (?,?,?,?,?,?)", (None,'verduras','papas',5,'papas por kilo',150))
cursor.execute("INSERT INTO producto VALUES (?,?,?,?,?,?)", (None,'bebidas','gaseosa coca cola',5,'gaseosa coca cola 1.5 litros',250))
conexion.commit()
#nunca olvidar el conexion.commit() al final de los cursor.execute que sino no se guardan los datos insertados a la db
#el None hace q se genere el id primary q se autoincrementa, sin llorar x la columna q faltaria segun xd

conexion.close()

#insertando productos en la db