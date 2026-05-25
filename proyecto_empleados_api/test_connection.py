import pyodbc
import json

try:
    # Intentar con autenticación de Windows a SQLEXPRESS
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=localhost\\SQLEXPRESS;'
        'Database=Empleados_com;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    # Obtener tablas disponibles
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    tables = [row[0] for row in cursor.fetchall()]
    
    print('✓ CONEXIÓN EXITOSA A SQL SERVER')
    print(f'Instancia: SQLEXPRESS')
    print(f'Base de datos: Empleados_com')
    print(f'Tablas encontradas: {len(tables)}')
    for table in tables[:10]:  # Mostrar primeras 10 tablas
        print(f'  - {table}')
    if len(tables) > 10:
        print(f'  ... y {len(tables) - 10} más')
    
    cursor.close()
    conn.close()
except Exception as e:
    print(f'✗ ERROR: {type(e).__name__}: {str(e)}')
