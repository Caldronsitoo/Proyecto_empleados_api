import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_empleados_api.settings')
django.setup()

from empleados.models import Empleado
from django.db import connection

try:
    # Probar conexiÃ³n
    with connection.cursor() as cursor:
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
        tables = [row[0] for row in cursor.fetchall()]
    
    print('âœ“ DJANGO SE CONECTÃ“ EXITOSAMENTE A SQL SERVER')
    print(f'Base de datos: Empleados_com')
    print(f'Tablas: {", ".join(tables)}')
    
    # Contar empleados
    count = Empleado.objects.count()
    print(f'\nEmpleados en base de datos: {count}')
    
except Exception as e:
    print(f'âœ— ERROR: {type(e).__name__}: {str(e)}')

