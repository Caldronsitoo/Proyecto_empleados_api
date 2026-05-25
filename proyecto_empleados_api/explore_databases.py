import pyodbc

try:
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=localhost\\SQLEXPRESS;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    # Obtener todas las bases de datos
    cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4 ORDER BY name")
    databases = [row[0] for row in cursor.fetchall()]
    
    print('=' * 60)
    print('BASES DE DATOS DISPONIBLES EN SQL SERVER (SQLEXPRESS)')
    print('=' * 60)
    
    for db in databases:
        print(f'\n📦 Base de datos: {db}')
        try:
            cursor.execute(f"SELECT TABLE_NAME FROM [{db}].INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
            tables = [row[0] for row in cursor.fetchall()]
            if tables:
                print(f'   Tablas: {len(tables)}')
                for table in tables[:5]:
                    print(f'     - {table}')
                if len(tables) > 5:
                    print(f'     ... y {len(tables) - 5} más')
            else:
                print('   (Sin tablas)')
        except Exception as e:
            print(f'   Error al leer tablas: {str(e)[:80]}')
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f'ERROR: {type(e).__name__}: {str(e)}')
