import mysql.connector

# # conexion = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password = "root",
# #     database="tienda"

# # )

# # if conexion.is_connected():
# #     print("conectado a la bd")

# # conexion.close()

# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password = "root",
#     database="tienda"
# )

# cursor = conexion.cursor()

# cursor.execute(

# """CREATE TABLE IF NOT EXISTS productos(
#     id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     nombre varchar(50) NOT NULL,
#     precio FLOAT NOT NULL)"""
# )

# conexion.commit()
# conexion.close()

# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password = "root",
#     database="tienda"
# )

# cursor = conexion.cursor()

# cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Teclado', 20)")
# conexion.commit()
# conexion.close()


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "root",
    database="tienda"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos")

for fila in cursor.fetchall():
    print(fila)
conexion.close()

