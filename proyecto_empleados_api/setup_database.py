import pyodbc

try:
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=localhost\\SQLEXPRESS;'
        'Database=Empleados_com;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    # Crear tabla empleado
    print('Creando tabla [empleado]...')
    try:
        cursor.execute("""
            IF OBJECT_ID('dbo.empleado', 'U') IS NULL
            CREATE TABLE [dbo].[empleado] (
                [idEmpleado] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
                [nombre] VARCHAR(100) NOT NULL,
                [departamento] VARCHAR(100) NOT NULL,
                [sueldo] DECIMAL(10, 2) NOT NULL,
                CONSTRAINT CK_empleado_sueldo CHECK ([sueldo] > 0)
            )
        """)
        conn.commit()
        print('✓ Tabla [empleado] creada')
    except Exception as e:
        print(f'⚠ Tabla [empleado]: {str(e)[:80]}')
    
    # Crear tabla django_migrations
    print('Creando tabla [django_migrations]...')
    try:
        cursor.execute("""
            IF OBJECT_ID('dbo.django_migrations', 'U') IS NULL
            CREATE TABLE [dbo].[django_migrations] (
                [id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
                [app] VARCHAR(255) NOT NULL,
                [name] VARCHAR(255) NOT NULL,
                [applied] DATETIME DEFAULT GETDATE() NOT NULL
            )
        """)
        conn.commit()
        print('✓ Tabla [django_migrations] creada')
    except Exception as e:
        print(f'⚠ Tabla [django_migrations]: {str(e)[:80]}')
    
    # Verificar tablas creadas
    print('\nVerificando tablas...')
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    tables = [row[0] for row in cursor.fetchall()]
    print(f'Tablas en Empleados_com: {", ".join(tables) if tables else "ninguna"}')
    
    cursor.close()
    conn.close()
    
    print('\n✓ Base de datos configurada exitosamente')
    
except Exception as e:
    print(f'✗ ERROR: {type(e).__name__}: {str(e)}')
