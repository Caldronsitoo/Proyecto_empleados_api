from django.contrib import admin
from .models import Empleado


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    """Interfaz de administración para el modelo Empleado."""
    list_display = ['idEmpleado', 'nombre', 'departamento', 'sueldo']
    search_fields = ['nombre', 'departamento']
    list_filter = ['departamento']
    ordering = ['idEmpleado']
