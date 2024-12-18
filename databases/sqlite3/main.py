import sqlite3

# conexion = sqlite3.connect("mi_base.db")
# cursor = conexion.cursor()
# cursor.execute(


# """CREATE TABLE IF NOT EXISTS  productos(

# id INTEGER PRIMARY KEY,
# nombre TEXT NOT NULL,
# precio REAL NOT NULL
# )
# """
# )

# conexion.commit()
# conexion.close()

# conexion = sqlite3.connect("mi_base.db")
# cursor = conexion.cursor()

# cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Teclado', 20)")
# conexion.commit()
# conexion.close()

# conexion = sqlite3.connect("mi_base.db")
# cursor = conexion.cursor()

# cursor.execute("SELECT * FROM productos")
# print(cursor.fetchall())
# conexion.close()

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("UPDATE productos SET precio = 25 WHERE id = 'Teclado'")
cursor.execute("DELETE FROM productos WHERE nombre = 'Teclado'")

conexion.commit()
conexion.close()