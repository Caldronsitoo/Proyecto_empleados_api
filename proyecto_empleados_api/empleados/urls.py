from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    # Listar todos los empleados y crear nuevos
    path('', views.ListarEmpleadosView.as_view(), name='listar-crear-empleados'),
    
    # Obtener, actualizar y eliminar un empleado específico
    path('<int:pk>/', views.DetalleEmpleadoView.as_view(), name='detalle-empleado'),
]
