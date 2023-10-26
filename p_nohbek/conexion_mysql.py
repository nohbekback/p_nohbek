import mysql.connector

#creamos la conexion
""" mysql_db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        db="p_bbdd_nohbek"
    )
print(mysql_db)
if connection.is_connected():
        print("conexion exitosa")
        info_server=connection.get_server_info()
        print(info_server)
mysql_cursor=mysql_db.cursor()
mysql_cursor.execute("CREATE DATABASE p_bbdd_nohbek")
row=cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Exception as ex:
print(ex)

#cerramos la conexion
finally:
if connection.is_connected():
   connection.close()
   print("Conexion finalizada.")
 """