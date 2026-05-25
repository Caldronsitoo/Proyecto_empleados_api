"""
Script para insertar empleados de prueba en la base de datos Empleados_com
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_empleados_api.settings')
django.setup()

from empleados.models import Empleado

# Datos de prueba
empleados_datos = [
    {'nombre': 'Juan PÃ©rez GarcÃ­a', 'departamento': 'Ventas', 'sueldo': 3500.00},
    {'nombre': 'MarÃ­a LÃ³pez RodrÃ­guez', 'departamento': 'Recursos Humanos', 'sueldo': 3200.00},
    {'nombre': 'Carlos MartÃ­nez Silva', 'departamento': 'TecnologÃ­a', 'sueldo': 4500.00},
    {'nombre': 'Ana FernÃ¡ndez GonzÃ¡lez', 'departamento': 'Finanzas', 'sueldo': 3800.00},
    {'nombre': 'Roberto SÃ¡nchez DÃ­az', 'departamento': 'Operaciones', 'sueldo': 3300.00},
]

try:
    # Limpiar empleados existentes (opcional)
    count_before = Empleado.objects.count()
    print(f'Empleados actuales: {count_before}')
    
    # Insertar nuevos empleados
    empleados_creados = []
    for datos in empleados_datos:
        empleado = Empleado.objects.create(**datos)
        empleados_creados.append(empleado)
        print(f'âœ“ Creado: {empleado.nombre} - {empleado.departamento} - ${empleado.sueldo}')
    
    # Verificar
    count_after = Empleado.objects.count()
    print(f'\nâœ“ Total de empleados: {count_after}')
    
    # Listar todos
    print('\n=== LISTADO DE EMPLEADOS ===')
    for emp in Empleado.objects.all():
        print(f'#{emp.idEmpleado}: {emp.nombre} ({emp.departamento}) - ${emp.sueldo}')
    
except Exception as e:
    print(f'âœ— ERROR: {type(e).__name__}: {str(e)}')

