import sys
import datetime
import sqlite3
from sqlite3 import Error
while True:#Mientras sea verdad continuara
    print("Menu")# Mostrar "Menu"
    print("1-Registar una venta")#Mostrar "1-Registar una venta"
    print("2-Consultar una venta")#Mostrar "2- Consultar Una venta" 
    print("3-Reporte de ventas atravez de fechas")#Mostrar "3-Reporte de ventas atravez de fechas"
    print("0-Salir")#Mostrar "0-Salir"
    opcion =int(input("Elige una opcion"))#Leer opcion como entero
    if opcion ==1:# Si opcion es igual a 1 hacer
        elegir=0
        try:#Tratar de cumplir con
            with sqlite3.connect("Prueba.db") as conn:#Conectarse a Prueba.db
                print("Conexión establecida")#Mostrar "Conexion establecida"
                mi_cursor = conn.cursor() #mi_cursor = conn.cursor()
                fecha_registro=input("Dime una fecha (dd/mm/aaaa): ")#Leer fecha registro
                fecha_converter = datetime.datetime.strptime(fecha_registro, "%d/%m/%Y").date()#Convertir fecha_registro a fecha de datetime
                fecha_actual = datetime.datetime.combine(fecha_converter, datetime.datetime.min.time())#Es importante complementar la fecha con la parte horaria
                folio=int(input("Escribe el folio: "))#Leer folio como entero
                while elegir != '1':#Mientras sea diferente de 1 podemos registrar otra variable
                    descripcion=input("Escribe el nombre del articulo: ")#Leer descripcion
                    cantidad = int(input("Escribe la cantidad de piezas:  "))#Leer cantidad como entero
                    precio = float(input("Escribe el precio:  "))#Leer precio como decimal
                    valores = {"folio": folio, "Descripcion":descripcion,"Precio":precio*cantidad, "fecha_Registro": fecha_actual}#crear un dicconario valores para conectarse a los comadnos SQL
                    mi_cursor.execute("INSERT INTO Articulo VALUES(:folio,:Descripcion ,:Precio,:fecha_Registro);", valores)#Insertar valores en comando sql en la tabla Articulo
                    print(f"Registro\nDescripcon= {descripcion}\n Cantidad: {cantidad}\tPago total: {precio*cantidad}\n")#Mostrar los valores capturados en los datos.
                    elegir=input("Deseas capturar mas datos? 0-Si | 1-NO")#Variable que indica si deseamos capturar mas datos
        except Error as e:#Errores de SQL
            print (e)#Muestra los erroes de SQL
        except:#errores del sistema
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")#Errores de sistema
        finally:#Finalmente seccion que de todos modos seguira despues de try
            if (conn):#Si hay conecion entonces
                conn.close()#cerrar conexion
                print("Se ha cerrado la conexión")#Mostrar "Se ha cerrado la conexión"
        
    elif opcion ==2:#Sino opcion es igual a 2 entero
        try:#Tratar entonces
            with sqlite3.connect("Prueba.db") as conn:#conectarse a Prueba.db
                mi_cursor = conn.cursor()#mi_cursor = conn.cursor()
                buscar=int(input("Escribe el folio a buscar: "))#Leer buscar entero
                criterios = {"buscar":buscar}#crear variable criterios tipo diccionario
                mi_cursor.execute("SELECT ID,DESCRIPCION,PRECIO,FECHA_CAPTURADA FROM ARTICULO WHERE id=:buscar;", criterios)#Solicitar una consulta trar los datos ientras sea el ID
                registros = mi_cursor.fetchall()#registros = mi_cursor.fetchall()
                if registros:#Si registros contiene datos hacer
                    for folio, descripcion,precio, fecha_registro in registros:#Para folio, descripcion,precio, fecha_registro recorre en registros
                        print(f"\nFecha de registro = {fecha_registro} \nfolio = {folio}\tNombre del producto= {descripcion}\t\nTotal={precio}\t\n")#Muestra todos los articulos comprados 
                else:#Sino
                    print("No se ha encontrado")#Mostrar  
        except sqlite3.Error as e:#Errores de SQL
            print (e)#Mostrar erroes de SQL
        except Exception:#Errores del sistema
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")#Mostrar errores del sistema
        finally:#Finalmente
            if (conn):#Si hay conexion entonces
                conn.close()#cerrar conexion
    elif opcion ==3:#Si opcion es igual a 3 entero
        print("Reporte atravez de fecha")
        fecha_consultar = input("Dime una fecha (dd/mm/aaaa): ")#Escribir fecha
        fecha_consultar = datetime.datetime.strptime(fecha_consultar, "%d/%m/%Y").date()#Convertir fecha_registro a fecha de datetime
        try:#tratar de
            with sqlite3.connect("Prueba.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:#Abrir conexion
                mi_cursor = conn.cursor()#mi_cursor = conn.cursor()
                criterios = {"fecha":fecha_consultar}#Crear un diccionario criterios para almacenar fecha 
                mi_cursor.execute("SELECT ID,DESCRIPCION,PRECIO,FECHA_CAPTURADA FROM ARTICULO WHERE DATE(FECHA_CAPTURADA)=:fecha;",criterios)#Consultar los datos con la fecha
                registros = mi_cursor.fetchall()#Traer todos los registros del diccionario
                if registros:#Si hay conexion
                    for folio, descripcion,precio, fecha_registro in registros:#Para folio, descripcion,precio, fecha_registro recorrer en registros
                        print(f"Fecha de registro = {fecha_registro} \nfolio = {folio}\tNombre del producto= {descripcion}\t\nTotal={precio}\t\n")#Mostrar datos de los detalles de las compras
                else:#sino
                    print("No se ha encontrado")#Mostrar "No se ha encontrado"
        except sqlite3.Error as e:#Error de SQL
            print (e)#Mostrar errores de SQL
        except Exception:#Error del sistema
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")#Mostrar error del sistema
        finally:#Finalmente continuar
            if (conn):#Si tiene conexion entonces
                conn.close()#Cerrar conexion
                print("Se ha cerrado la conexión")#Mostrar "Se ha cerrado la conexión"
    elif opcion ==0:#Sino opcion es igual a 0 entonces
        break #Destruir ciclio while
    else:#Sino
        print("Error----No se encuentra la opcion a elegir")#Mostrar "Error----No se encuentra la opcion a elegir"