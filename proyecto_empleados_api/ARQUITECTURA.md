# ðŸ—ï¸ ARQUITECTURA Y ESTRUCTURA DEL PROYECTO

## Diagrama de Arquitectura

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        CLIENTE (React/Angular)                   â”‚
â”‚                 Puerto 5173 (React) / 4200 (Angular)             â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                 â”‚
                    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                    â”‚  HTTP/REST â”‚            â”‚
                    â”‚  (CORS)    â”‚            â”‚
                    â”‚            â”‚            â”‚
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  SERVIDOR DJANGO (Puerto 8080)                  â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚
â”‚  â”‚              Django REST Framework Layer                  â”‚  â”‚
â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚
â”‚  â”‚  â”‚ URLs (proyecto_empleados_api/urls.py, empleados/urls.py)       â”‚ â”‚  â”‚
â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚
â”‚  â”‚                     â”‚                                     â”‚  â”‚
â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚
â”‚  â”‚  â”‚ Vistas (empleados/views.py)                        â”‚ â”‚  â”‚
â”‚  â”‚  â”‚ - ListarEmpleadosView (GET, POST)                 â”‚ â”‚  â”‚
â”‚  â”‚  â”‚ - DetalleEmpleadoView (GET, PUT, PATCH, DELETE)  â”‚ â”‚  â”‚
â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚
â”‚  â”‚                     â”‚                                     â”‚  â”‚
â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚
â”‚  â”‚  â”‚ Serializers (empleados/serializers.py)             â”‚ â”‚  â”‚
â”‚  â”‚  â”‚ - EmpleadoSerializer                              â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * ValidaciÃ³n de nombre (min 3 caracteres)       â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * ValidaciÃ³n de departamento (min 3 caracteres) â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * ValidaciÃ³n de sueldo (>0)                     â”‚ â”‚  â”‚
â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚
â”‚  â”‚                     â”‚                                     â”‚  â”‚
â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚
â”‚  â”‚  â”‚ Modelos (empleados/models.py)                      â”‚ â”‚  â”‚
â”‚  â”‚  â”‚ - Empleado                                        â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * idEmpleado (PK, AutoField)                   â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * nombre (CharField, max 100)                  â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * departamento (CharField, max 100)            â”‚ â”‚  â”‚
â”‚  â”‚  â”‚   * sueldo (DecimalField, 10,2)                  â”‚ â”‚  â”‚
â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                         â”‚
                    â”Œâ”€â”€â”€â”€â–¼â”€â”€â”€â”€â”
                    â”‚  MySQL   â”‚
                    â”‚ (rh_db)  â”‚
                    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Estructura de Directorios Detallada

```
C:\Escritorio\Software\proyecto_empleados_api\
â”‚
â”œâ”€â”€ ðŸ“ venv/                                      # Ambiente virtual Python
â”‚   â”œâ”€â”€ Include/
â”‚   â”œâ”€â”€ Lib/site-packages/                        # Paquetes instalados
â”‚   â”œâ”€â”€ Scripts/                                  # Ejecutables (python, pip, etc)
â”‚   â””â”€â”€ pyvenv.cfg
â”‚
â”œâ”€â”€ ðŸ“ empleados/                                 # APLICACIÃ“N DJANGO
â”‚   â”‚
â”‚   â”œâ”€â”€ ðŸ“ migrations/                            # Migraciones de BD
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ 0001_initial.py                       # Primera migraciÃ³n
â”‚   â”‚
â”‚   â”œâ”€â”€ __init__.py                               # Inicializador de mÃ³dulo
â”‚   â”œâ”€â”€ admin.py                                  # âœ… Interfaz admin
â”‚   â”œâ”€â”€ apps.py                                   # ConfiguraciÃ³n de app
â”‚   â”œâ”€â”€ models.py                                 # âœ… Modelo Empleado
â”‚   â”œâ”€â”€ serializers.py                            # âœ… Serializador con validaciones
â”‚   â”œâ”€â”€ tests.py                                  # Tests unitarios
â”‚   â”œâ”€â”€ urls.py                                   # âœ… Rutas de la app
â”‚   â””â”€â”€ views.py                                  # âœ… Vistas CRUD
â”‚
â”œâ”€â”€ ðŸ“ proyecto_empleados_api/                                 # CONFIGURACIÃ“N GENERAL
â”‚   â”‚
â”‚   â”œâ”€â”€ __pycache__/                              # CachÃ© de Python
â”‚   â”œâ”€â”€ __init__.py                               # âœ… ConfiguraciÃ³n PyMySQL
â”‚   â”œâ”€â”€ asgi.py                                   # ConfiguraciÃ³n ASGI
â”‚   â”œâ”€â”€ settings.py                               # âœ… ConfiguraciÃ³n principal
â”‚   â”‚                                             #    - MySQL
â”‚   â”‚                                             #    - REST Framework
â”‚   â”‚                                             #    - CORS
â”‚   â”œâ”€â”€ urls.py                                   # âœ… Rutas principales
â”‚   â””â”€â”€ wsgi.py                                   # ConfiguraciÃ³n WSGI
â”‚
â”œâ”€â”€ ðŸ“„ manage.py                                  # CLI de Django
â”œâ”€â”€ ðŸ“„ db.sqlite3                                 # BD SQLite (NO SE USA)
â”‚
â”œâ”€â”€ ðŸ“„ requirements.txt                           # âœ… Dependencias Python
â”œâ”€â”€ ðŸ“„ README.md                                  # âœ… DocumentaciÃ³n rÃ¡pida
â”œâ”€â”€ ðŸ“„ GUIA_COMPLETA_API_EMPLEADOS.md             # âœ… GuÃ­a pedagÃ³gica completa
â”‚
â”œâ”€â”€ ðŸ“„ create_database.sql                        # âœ… Script BD MySQL
â”œâ”€â”€ ðŸ“„ datos_ejemplo.sql                          # âœ… Datos de prueba
â”‚
â”œâ”€â”€ ðŸ“„ PostmanCollection.json                     # âœ… ColecciÃ³n de pruebas
â”œâ”€â”€ ðŸ“„ init_project.py                            # âœ… Script inicializador
â””â”€â”€ ðŸ“„ ARQUITECTURA.md                            # Este archivo
```

---

## Flujo de Datos (Request/Response)

### 1. Listar Empleados (GET)

```
Cliente (React/Angular)
    â”‚
    â”œâ”€ GET http://localhost:8080/api/empleados/
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                                                                   â”‚
                          SERVIDOR DJANGO                          â”‚
                                                                   â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€> urls.py: ruta vacÃ­a '' â†’ ListarEmpleadosView
    â”‚
    â”œâ”€> ListarEmpleadosView.list()
    â”‚    â”œâ”€> queryset = Empleado.objects.all()
    â”‚    â”œâ”€> serializer = EmpleadoSerializer(queryset, many=True)
    â”‚    â””â”€> Response(serializer.data)
    â”‚
    â”œâ”€> MySQL: SELECT * FROM empleado
    â”‚
    â””â”€â”€> Response JSON
    
Cliente recibe:
{
    "mensaje": "Empleados listados correctamente",
    "total": 3,
    "datos": [
        {"idEmpleado": 1, "nombre": "Juan", "departamento": "TI", "sueldo": "3500.00"},
        {"idEmpleado": 2, "nombre": "MarÃ­a", "departamento": "RRHH", "sueldo": "3200.00"},
        {"idEmpleado": 3, "nombre": "Carlos", "departamento": "Ventas", "sueldo": "2800.00"}
    ]
}
```

### 2. Crear Empleado (POST)

```
Cliente (React/Angular)
    â”‚
    â”œâ”€ POST http://localhost:8080/api/empleados/
    â”œâ”€ Content-Type: application/json
    â””â”€ Body: {"nombre": "Ana", "departamento": "Marketing", "sueldo": 3000.00}
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                                                                   â”‚
                          SERVIDOR DJANGO                          â”‚
                                                                   â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€> urls.py: ruta vacÃ­a '' â†’ ListarEmpleadosView
    â”‚
    â”œâ”€> ListarEmpleadosView.create()
    â”‚    â”œâ”€> serializer = EmpleadoSerializer(data=request.data)
    â”‚    â”œâ”€> serializer.is_valid(raise_exception=True)
    â”‚    â”‚    â”œâ”€> validate_nombre() âœ… "Ana" >= 3 caracteres
    â”‚    â”‚    â”œâ”€> validate_departamento() âœ… "Marketing" >= 3 caracteres
    â”‚    â”‚    â””â”€> validate_sueldo() âœ… 3000.00 > 0
    â”‚    â””â”€> serializer.save() â†’ Empleado.objects.create()
    â”‚
    â”œâ”€> MySQL: INSERT INTO empleado VALUES (...)
    â”‚
    â””â”€â”€> Response JSON (201 Created)

Cliente recibe:
{
    "mensaje": "Empleado creado exitosamente",
    "datos": {
        "idEmpleado": 4,
        "nombre": "Ana",
        "departamento": "Marketing",
        "sueldo": "3000.00"
    }
}
```

### 3. Obtener Detalles (GET {id})

```
Cliente
    â”‚
    â”œâ”€ GET http://localhost:8080/api/empleados/1/
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                                                                   â”‚
                          SERVIDOR DJANGO                          â”‚
                                                                   â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€> urls.py: '1/' â†’ DetalleEmpleadoView
    â”‚
    â”œâ”€> DetalleEmpleadoView.retrieve()
    â”‚    â”œâ”€> instance = get_object_or_404(Empleado, idEmpleado=1)
    â”‚    â”œâ”€> serializer = EmpleadoSerializer(instance)
    â”‚    â””â”€> Response(serializer.data)
    â”‚
    â”œâ”€> MySQL: SELECT * FROM empleado WHERE idEmpleado = 1
    â”‚
    â””â”€â”€> Response JSON (200 OK)
```

### 4. Actualizar Empleado (PUT {id})

```
Cliente
    â”‚
    â”œâ”€ PUT http://localhost:8080/api/empleados/1/
    â””â”€ Body: {"nombre": "Juan Carlos", "departamento": "TI Senior", "sueldo": 4500.00}
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                          SERVIDOR DJANGO                          â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€> DetalleEmpleadoView.update()
    â”‚    â”œâ”€> instance = get_object_or_404(Empleado, idEmpleado=1)
    â”‚    â”œâ”€> serializer = EmpleadoSerializer(instance, data, partial=False)
    â”‚    â”œâ”€> serializer.is_valid(raise_exception=True) âœ… Todas validaciones
    â”‚    â””â”€> serializer.save() â†’ instance.save()
    â”‚
    â”œâ”€> MySQL: UPDATE empleado SET ... WHERE idEmpleado = 1
    â”‚
    â””â”€â”€> Response JSON (200 OK)
```

### 5. Eliminar Empleado (DELETE {id})

```
Cliente
    â”‚
    â”œâ”€ DELETE http://localhost:8080/api/empleados/1/
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                          SERVIDOR DJANGO                          â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€> DetalleEmpleadoView.destroy()
    â”‚    â”œâ”€> instance = get_object_or_404(Empleado, idEmpleado=1)
    â”‚    â”œâ”€> instance.delete()
    â”‚    â””â”€> Response({"mensaje": "..."})
    â”‚
    â”œâ”€> MySQL: DELETE FROM empleado WHERE idEmpleado = 1
    â”‚
    â””â”€â”€> Response JSON (200 OK)
```

---

## SeparaciÃ³n de Responsabilidades (MVC/MTV)

### MTV = Model-Template-View (en Django)
En REST API usamos: Model-Serializer-View

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        MODELO (Model)                        â”‚
â”‚                    empleados/models.py                       â”‚
â”‚                                                              â”‚
â”‚  class Empleado(models.Model):                              â”‚
â”‚    - idEmpleado (AutoField)                                 â”‚
â”‚    - nombre (CharField)                                     â”‚
â”‚    - departamento (CharField)                               â”‚
â”‚    - sueldo (DecimalField)                                  â”‚
â”‚                                                              â”‚
â”‚  Responsabilidad: Definir la estructura de datos            â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                            â–³
                            â”‚
                   RelaciÃ³n directa
                            â”‚
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  SERIALIZADOR (Serializer)                   â”‚
â”‚              empleados/serializers.py                        â”‚
â”‚                                                              â”‚
â”‚  class EmpleadoSerializer(ModelSerializer):                 â”‚
â”‚    - Convierte Modelo â†” JSON                               â”‚
â”‚    - Valida datos de entrada                               â”‚
â”‚    - Transforma datos de salida                            â”‚
â”‚                                                              â”‚
â”‚  Responsabilidad: TransformaciÃ³n y validaciÃ³n de datos      â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                            â–³
                            â”‚
                   RelaciÃ³n directa
                            â”‚
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                   VISTA (View)                              â”‚
â”‚              empleados/views.py                             â”‚
â”‚                                                              â”‚
â”‚  class ListarEmpleadosView(ListCreateAPIView):             â”‚
â”‚    - Procesa peticiones HTTP                               â”‚
â”‚    - Coordina Modelo â†” Serializer                         â”‚
â”‚    - Retorna respuestas JSON                              â”‚
â”‚                                                              â”‚
â”‚  class DetalleEmpleadoView(RetrieveUpdateDestroyAPIView):  â”‚
â”‚    - CRUD individual (GET, PUT, PATCH, DELETE)            â”‚
â”‚                                                              â”‚
â”‚  Responsabilidad: LÃ³gica de negocio y coordinaciÃ³n         â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Flujo de ValidaciÃ³n

```
Cliente envÃ­a JSON
    â”‚
    â”œâ”€> EmpleadoSerializer(data=request.data)
    â”‚
    â”œâ”€> serializer.is_valid()
    â”‚    â”‚
    â”‚    â”œâ”€â”€â†’ validate_nombre()
    â”‚    â”‚    â”œâ”€ Â¿EstÃ¡ vacÃ­o? â†’ Error
    â”‚    â”‚    â”œâ”€ Â¿< 3 caracteres? â†’ Error
    â”‚    â”‚    â””â”€ âœ… OK â†’ Retorna nombre
    â”‚    â”‚
    â”‚    â”œâ”€â”€â†’ validate_departamento()
    â”‚    â”‚    â”œâ”€ Â¿EstÃ¡ vacÃ­o? â†’ Error
    â”‚    â”‚    â”œâ”€ Â¿< 3 caracteres? â†’ Error
    â”‚    â”‚    â””â”€ âœ… OK â†’ Retorna departamento
    â”‚    â”‚
    â”‚    â”œâ”€â”€â†’ validate_sueldo()
    â”‚    â”‚    â”œâ”€ Â¿<= 0? â†’ Error
    â”‚    â”‚    â””â”€ âœ… OK â†’ Retorna sueldo
    â”‚    â”‚
    â”‚    â””â”€> Â¿Errores? â†’ Response 400 Bad Request
    â”‚
    â”œâ”€> serializer.save()
    â”‚    â””â”€> Empleado.objects.create(...)
    â”‚
    â””â”€> Response 201 Created âœ…
```

---

## ConfiguraciÃ³n de CORS

```
Cliente (React)
Puerto 5173
    â”‚
    â””â”€ Request a http://localhost:8080/api/empleados/
    
    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                                                                   â”‚
                  Middleware CORS (Django)                         â”‚
                                                                   â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â”œâ”€ Â¿Origen: http://localhost:5173?
    â”‚  â””â”€> âœ… En CORS_ALLOWED_ORIGINS
    â”‚
    â”œâ”€ AÃ±ade headers:
    â”‚  â”œâ”€ Access-Control-Allow-Origin: http://localhost:5173
    â”‚  â”œâ”€ Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE
    â”‚  â”œâ”€ Access-Control-Allow-Headers: Content-Type
    â”‚  â””â”€ Access-Control-Allow-Credentials: true
    â”‚
    â””â”€> Permite la solicitud âœ…
```

---

## Stack TecnolÃ³gico

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚          FRONTEND COMPATIBLE            â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ â€¢ React (puerto 5173)                   â”‚
â”‚ â€¢ Angular (puerto 4200)                 â”‚
â”‚ â€¢ Vanilla JavaScript                    â”‚
â”‚ â€¢ Axios / Fetch API                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
            â†“ CORS â†“
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚      BACKEND (SERVIDOR)                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ â€¢ Django 6.0.5                          â”‚
â”‚ â€¢ Django REST Framework 3.17.1          â”‚
â”‚ â€¢ django-cors-headers 4.9.0             â”‚
â”‚ â€¢ Puerto 8080                           â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
            â†“ ORM â†“
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚      BASE DE DATOS                      â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ â€¢ MySQL 5.7+                            â”‚
â”‚ â€¢ Database: rh_db                       â”‚
â”‚ â€¢ Tabla: empleado                       â”‚
â”‚ â€¢ PyMySQL 1.2.0 (conector)              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Ciclo de Vida de una PeticiÃ³n (Request Lifecycle)

```
1. CLIENTE ENVÃA PETICIÃ“N
   â”‚
   â”œâ”€> GET /api/empleados/
   â”œâ”€> Origen: http://localhost:5173
   â””â”€> Headers: Content-Type: application/json

2. SERVIDOR RECIBE (Django)
   â”‚
   â”œâ”€> MIDDLEWARE: CorsMiddleware
   â”‚   â””â”€> âœ… Verifica origen permitido
   â”‚
   â”œâ”€> MIDDLEWARE: SecurityMiddleware
   â”‚   â””â”€> âœ… Valida seguridad
   â”‚
   â”œâ”€> MIDDLEWARE: SessionMiddleware
   â”‚   â””â”€> âœ… Gestiona sesiÃ³n
   â”‚
   â”œâ”€> MIDDLEWARE: CommonMiddleware
   â”‚   â””â”€> âœ… Procesamiento comÃºn
   â”‚
   â””â”€> MIDDLEWARE: CSRF Protection
       â””â”€> âœ… (Deshabilitado para API REST)

3. ENRUTAMIENTO (URL Routing)
   â”‚
   â”œâ”€> urls.py verifica: /api/empleados/
   â”œâ”€> Encuentra: path('api/empleados/', include('empleados.urls'))
   â””â”€> Delega a empleados/urls.py

4. APLICACIÃ“N (empleados/urls.py)
   â”‚
   â”œâ”€> '' â†’ ListarEmpleadosView.as_view()
   â””â”€> Instancia: ListarEmpleadosView()

5. VISTA (views.py)
   â”‚
   â”œâ”€> GET â†’ lista() method
   â”œâ”€> queryset = Empleado.objects.all()
   â”œâ”€> serializer = EmpleadoSerializer(queryset, many=True)
   â””â”€> Response(serializer.data, status=200)

6. SERIALIZADOR (serializers.py)
   â”‚
   â”œâ”€> Convierte [Empleado1, Empleado2, ...] a JSON
   â”œâ”€> Aplica transformaciones
   â””â”€> Retorna lista de diccionarios

7. RESPUESTA HTTP
   â”‚
   â”œâ”€> Status: 200 OK
   â”œâ”€> Headers: 
   â”‚   â”œâ”€ Content-Type: application/json
   â”‚   â”œâ”€ Access-Control-Allow-Origin: http://localhost:5173
   â”‚   â””â”€ Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE
   â”‚
   â””â”€> Body:
       {
           "mensaje": "Empleados listados correctamente",
           "total": 3,
           "datos": [...]
       }

8. CLIENTE RECIBE RESPUESTA
   â”‚
   â”œâ”€> JavaScript procesa JSON
   â”œâ”€> Actualiza UI
   â””â”€> âœ… Completo
```

---

## Errores Comunes y Soluciones

| Error | Causa | SoluciÃ³n |
|-------|-------|----------|
| CORS Error | Origen no permitido | Agregar a `CORS_ALLOWED_ORIGINS` |
| 404 Not Found | URL incorrecta | Verificar rutas en urls.py |
| 400 Bad Request | ValidaciÃ³n fallida | Revisar datos enviados |
| 500 Server Error | Error en Django | Ver logs del servidor |
| Connection refused | MySQL no corre | Iniciar servicio MySQL |
| Migration error | Modelo con conflictos | Borrar migraciones y empezar |

---

## Buenas PrÃ¡cticas Implementadas

âœ… **SeparaciÃ³n de responsabilidades**: Models, Views, Serializers, URLs separados
âœ… **ValidaciÃ³n a dos niveles**: Serializador + Modelo
âœ… **Uso de generics**: ListCreateAPIView, RetrieveUpdateDestroyAPIView
âœ… **Respuestas consistentes**: Mismo formato JSON en todas las respuestas
âœ… **CORS configurado**: Permite peticiones desde aplicaciones frontend
âœ… **DocumentaciÃ³n**: Docstrings en todas las clases y mÃ©todos
âœ… **Base de datos relacional**: MySQL con constraints
âœ… **Migraciones**: Control de versiones de BD con Django migrations
âœ… **Admin panel**: Interfaz admin para gestionar datos
âœ… **Manejo de errores**: Respuestas HTTP apropiadas

---

**Documento actualizado: Mayo 2026**
**VersiÃ³n: 1.0**

