import pyodbc

def obtener_conexion():
    conexion = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=AdventureWorks2022;'
    'UID=juanadmin;'
    'PWD=Juan.2511'
    )

    return conexion