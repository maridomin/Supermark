import sqlite3

from crear_bd import crear_conexion

conexion= crear_conexion("Supermarket.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?)", (None,'martinez','pablo','pablom@hotmail.com',32030618,'pablopass','admin',0))
cursor.execute("INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?)", (None,'dominguez','maria','mariad@hotmail.com',33150813,'mariapass','admin',0))
cursor.execute("INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?)", (None,'morales','marcela','marcelam@hotmail.com',28150587,'marcelapass','admin',0))
cursor.execute("INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?)", (None,'mamani','miguel','miguelm@hotmail.com',35057648,'miguelpass','usuario',1))
cursor.execute("INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?)", (None,'1','1','miguelm3@hotmail.com',350576489,'1','usuario',1))
conexion.commit() #nunca olvidar el conexion.commit() al final de los cursor.execute que sino no se guardan los datos insertados a la db
#el usuario 4 es para testear el funcionamiento del usuario comun (no adm)
#el None hace q se genere el id primary q se autoincrementa, sin llorar x la columna q faltaria segun xd

conexion.close()

#insertando usuarios en la db