from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Empleado.
    Convierte objetos del modelo a JSON y viceversa.
    Incluye validaciones básicas para asegurar integridad de datos.
    """
    
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']
        read_only_fields = ['idEmpleado']
    
    def validate_nombre(self, value):
        """Validación: El nombre no puede estar vacío y debe tener al menos 3 caracteres."""
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("El nombre es requerido y no puede estar vacío.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value.strip()
    
    def validate_departamento(self, value):
        """Validación: El departamento no puede estar vacío y debe tener al menos 3 caracteres."""
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("El departamento es requerido y no puede estar vacío.")
        if len(value) < 3:
            raise serializers.ValidationError("El departamento debe tener al menos 3 caracteres.")
        return value.strip()
    
    def validate_sueldo(self, value):
        """Validación: El sueldo debe ser un valor positivo (mayor que 0)."""
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser un valor positivo (mayor que 0).")
        return value
    
    def validate(self, data):
        """Validación a nivel del objeto completo (después de validar campos individuales)."""
        return data
