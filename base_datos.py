import sqlite3

# 1. Creamos la base de datos en la memoria
conexion = sqlite3.connect(':memory:')
cursor = conexion.cursor()

# 2. Creamos la tabla de Clientes
cursor.execute('''
    CREATE TABLE Clientes (
        nombre TEXT,
        tipo_cliente TEXT,
        saldo INTEGER
    )
''')

# 3. Guardamos los 3 clientes
cursor.execute("INSERT INTO Clientes VALUES ('Carlos', 'estudiante', 150)")
cursor.execute("INSERT INTO Clientes VALUES ('Andy', 'vip', 500)")
cursor.execute("INSERT INTO Clientes VALUES ('Juan', 'normal', 200)")

# 4. Hacemos la consulta SQL para buscar solo al VIP
cursor.execute("SELECT * FROM Clientes WHERE saldo = 200")

# 5. Mostramos el resultado
resultado = cursor.fetchall()
print("El cliente con saldo 200 es:", resultado)