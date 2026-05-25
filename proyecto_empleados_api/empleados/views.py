from rest_framework import generics, status
from rest_framework.response import Response
from .models import Empleado
from .serializers import EmpleadoSerializer


class ListarEmpleadosView(generics.ListCreateAPIView):
    """
    Vista para listar todos los empleados y crear nuevos empleados.
    
    GET: Retorna lista de todos los empleados
    POST: Crea un nuevo empleado con los datos proporcionados
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
    def list(self, request, *args, **kwargs):
        """Personaliza la respuesta para listar empleados."""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'mensaje': 'Empleados listados correctamente',
            'total': len(serializer.data),
            'datos': serializer.data
        }, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        """Personaliza la respuesta al crear un empleado."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'mensaje': 'Empleado creado exitosamente',
            'datos': serializer.data
        }, status=status.HTTP_201_CREATED)


class DetalleEmpleadoView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener, actualizar o eliminar un empleado específico.
    
    GET: Retorna los detalles de un empleado específico
    PUT: Actualiza todos los campos del empleado
    PATCH: Actualiza parcialmente los campos del empleado
    DELETE: Elimina el empleado
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'idEmpleado'
    lookup_url_kwarg = 'pk'
    
    def retrieve(self, request, *args, **kwargs):
        """Personaliza la respuesta para obtener detalles de un empleado."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'mensaje': 'Empleado obtenido correctamente',
            'datos': serializer.data
        }, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        """Personaliza la respuesta al actualizar un empleado."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'mensaje': 'Empleado actualizado exitosamente',
            'datos': serializer.data
        }, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        """Personaliza la respuesta al eliminar un empleado."""
        instance = self.get_object()
        nombre_empleado = instance.nombre
        self.perform_destroy(instance)
        return Response({
            'mensaje': f'Empleado "{nombre_empleado}" eliminado exitosamente'
        }, status=status.HTTP_200_OK)
