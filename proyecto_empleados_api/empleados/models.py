from django.db import models


class Empleado(models.Model):
    """
    Modelo de base de datos para representar un empleado.
    
    Campos:
    - idEmpleado: Clave primaria autoincremental
    - nombre: Nombre del empleado (requerido)
    - departamento: Departamento al que pertenece (requerido)
    - sueldo: Salario del empleado con validación de valor positivo
    """
    
    idEmpleado = models.AutoField(primary_key=True, verbose_name="ID Empleado")
    nombre = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre completo del empleado")
    departamento = models.CharField(max_length=100, verbose_name="Departamento", help_text="Departamento del empleado")
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sueldo", help_text="Sueldo del empleado")
    
    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['idEmpleado']
    
    def __str__(self):
        return f"{self.nombre} - {self.departamento}"
