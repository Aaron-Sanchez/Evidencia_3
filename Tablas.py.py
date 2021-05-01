import sqlite3
from sqlite3 import Error
import sys

try:#Tratar continuar
    with sqlite3.connect("Prueba.db") as conexion:#Abrir conexion
        mi_cursor = conexion.cursor()#mi_cursor = conexion.cursor()
        mi_cursor.execute("CREATE TABLE ARTICULO(ID INTEGER ,DESCRIPCION TEXT NOT NULL,PRECIO FLOAT NOT NULL,FECHA_CAPTURADA  TIMESTAMP NOT NULL);")#Ejecutar comando de sql para crear tabla
        
        print("Tabla creada")#Tabla "Creada"
except sqlite3.Error as e:#Error de sql
    print(e)#mostrar Error de sql
except:#Error de sistema
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")#Mostrar error del sistema
finally:#finalmente
    if (conexion):#Si hay conexion
        conexion.close()#cerrar coneion
        print("Se ha cerrado la conexión")#Mostrar "Se ha cerrado la conexión"

