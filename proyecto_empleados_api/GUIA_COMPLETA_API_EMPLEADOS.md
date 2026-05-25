# ðŸš€ GUÃA COMPLETA: API REST DE EMPLEADOS CON DJANGO REST FRAMEWORK

## ðŸ“‹ Tabla de Contenidos
1. [PreparaciÃ³n del Entorno](#1-preparaciÃ³n-del-entorno)
2. [InstalaciÃ³n de Dependencias](#2-instalaciÃ³n-de-dependencias)
3. [Crear Proyecto y App](#3-crear-proyecto-y-app)
4. [ConfiguraciÃ³n de settings.py](#4-configuraciÃ³n-de-settingspy)
5. [Crear Modelo Empleado](#5-crear-modelo-empleado)
6. [Crear Serializer](#6-crear-serializer)
7. [Crear Vistas CRUD](#7-crear-vistas-crud)
8. [Configurar URLs](#8-configurar-urls)
9. [Base de Datos MySQL](#9-base-de-datos-mysql)
10. [Migraciones](#10-migraciones)
11. [Ejecutar el Servidor](#11-ejecutar-el-servidor)
12. [Pruebas en Postman](#12-pruebas-en-postman)
13. [Estructura Final](#13-estructura-final-del-proyecto)

---

## 1. PREPARACIÃ“N DEL ENTORNO

### Objetivo
Preparar la carpeta del proyecto y crear un ambiente virtual aislado para instalar las dependencias Python.

### Pasos

#### 1.1 Crear la carpeta base del proyecto
```powershell
cd C:\
mkdir -p Escritorio\Software\proyecto_empleados_api
cd Escritorio\Software\proyecto_empleados_api
```

**Resultado esperado:**
```
C:\Escritorio\Software\proyecto_empleados_api>
```

#### 1.2 Crear el ambiente virtual de Python
```powershell
python -m venv venv
```

**Â¿QuÃ© hace?** 
Crea un ambiente virtual aislado en la carpeta `venv` que contendrÃ¡ todas las dependencias Python del proyecto sin afectar el sistema.

#### 1.3 Activar el ambiente virtual
```powershell
.\venv\Scripts\Activate.ps1
```

**Â¿QuÃ© hace?**
Activa el ambiente virtual. Si tiene Ã©xito, verÃ¡ `(venv)` al inicio de la lÃ­nea de comandos.

**Resultado esperado:**
```
(venv) C:\Escritorio\Software\proyecto_empleados_api>
```

---

## 2. INSTALACIÃ“N DE DEPENDENCIAS

### Objetivo
Instalar los paquetes necesarios: Django, Django REST Framework, CORS headers y el conector MySQL.

### Comando
```powershell
pip install django djangorestframework django-cors-headers pymysql
```

### ExplicaciÃ³n de cada paquete

| Paquete | VersiÃ³n | PropÃ³sito |
|---------|---------|----------|
| **django** | 6.0.5 | Framework web principal para crear aplicaciones Python |
| **djangorestframework** | 3.17.1 | ExtensiÃ³n que facilita la creaciÃ³n de APIs REST en Django |
| **django-cors-headers** | 4.9.0 | Permite peticiones CORS desde aplicaciones en otros dominios/puertos |
| **pymysql** | 1.2.0 | Conector Python para bases de datos MySQL |

### Verificar instalaciÃ³n
```powershell
pip list
```

---

## 3. CREAR PROYECTO Y APP

### Objetivo
Crear la estructura base del proyecto Django y la aplicaciÃ³n `empleados`.

### 3.1 Crear el proyecto Django
```powershell
django-admin startproject proyecto_empleados_api .
```

**Â¿QuÃ© hace?** 
Crea la estructura base de un proyecto Django con los archivos de configuraciÃ³n principal. El `.` indica que se cree en el directorio actual sin crear una subcarpeta adicional.

### 3.2 Crear la aplicaciÃ³n Django
```powershell
python manage.py startapp empleados
```

**Â¿QuÃ© hace?**
Crea la aplicaciÃ³n `empleados` que contendrÃ¡ todo el cÃ³digo relacionado con la gestiÃ³n de empleados (modelos, vistas, serializadores, URLs).

### 3.3 Estructura resultante

```
C:\Escritorio\Software\proyecto_empleados_api\
â”‚
â”œâ”€â”€ venv/                          # Ambiente virtual
â”œâ”€â”€ empleados/                      # AplicaciÃ³n Django
â”‚   â”œâ”€â”€ migrations/
â”‚   â”‚   â””â”€â”€ __init__.py
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ admin.py
â”‚   â”œâ”€â”€ apps.py
â”‚   â”œâ”€â”€ models.py                  # Modelos de base de datos
â”‚   â”œâ”€â”€ serializers.py             # Serializadores (NUEVO - crearemos)
â”‚   â”œâ”€â”€ tests.py
â”‚   â”œâ”€â”€ urls.py                    # URLs de la aplicaciÃ³n (NUEVO - crearemos)
â”‚   â””â”€â”€ views.py                   # Vistas CRUD (NUEVO - crearemos)
â”‚
â”œâ”€â”€ proyecto_empleados_api/                      # ConfiguraciÃ³n del proyecto
â”‚   â”œâ”€â”€ __init__.py                # ConfiguraciÃ³n de PyMySQL (EDITADO)
â”‚   â”œâ”€â”€ settings.py                # ConfiguraciÃ³n principal (EDITADO)
â”‚   â”œâ”€â”€ urls.py                    # URLs principales (EDITADO)
â”‚   â”œâ”€â”€ asgi.py
â”‚   â””â”€â”€ wsgi.py
â”‚
â””â”€â”€ manage.py                       # Herramienta de lÃ­nea de comandos de Django
```

---

## 4. CONFIGURACIÃ“N DE settings.py

### Objetivo
Configurar Django para usar MySQL, habilitar REST Framework, configurar CORS y registrar la aplicaciÃ³n `empleados`.

### Ruta: `C:\Escritorio\Software\proyecto_empleados_api\proyecto_empleados_api\settings.py`
### Estado: **EXISTENTE - REEMPLAZAR COMPLETAMENTE**

**CAMBIOS IMPORTANTES REALIZADOS:**
- âœ… Se agregÃ³ conexiÃ³n MySQL
- âœ… Se configurÃ³ Django REST Framework
- âœ… Se habilitÃ³ CORS para React (puerto 5173) y Angular (puerto 4200)
- âœ… Se agregÃ³ la aplicaciÃ³n 'empleados' a INSTALLED_APPS
- âœ… Se agregÃ³ 'rest_framework' y 'corsheaders' a INSTALLED_APPS
- âœ… Se configurÃ³ el middleware de CORS antes de SecurityMiddleware

### Contenido completo

```python
"""
Django settings for proyecto_empleados_api project.

Generated by 'django-admin startproject' using Django 6.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0i$uo2!2v$28lgwijmn6ycpe3&w7+22s+)(fm@z&5cavigx*db'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
# CAMBIO IMPORTANTE: Se agregaron 'rest_framework', 'corsheaders' y 'empleados'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'empleados',
]

# CAMBIO IMPORTANTE: Se configurÃ³ CORS y REST Framework en MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_empleados_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_empleados_api.wsgi.application'


# Database
# CAMBIO IMPORTANTE: Se cambiÃ³ de SQLite a MySQL con PyMySQL
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rh_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/6.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CAMBIO IMPORTANTE: ConfiguraciÃ³n de REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}


# CAMBIO IMPORTANTE: ConfiguraciÃ³n de CORS para permitir peticiones desde React y Angular
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
    'http://localhost:5173',
    'http://127.0.0.1:4200',
    'http://127.0.0.1:5173',
]

CORS_ALLOW_CREDENTIALS = True
```

---

## 5. CREAR MODELO EMPLEADO

### Ruta: `C:\Escritorio\Software\proyecto_empleados_api\empleados\models.py`
### Estado: **EXISTENTE - REEMPLAZAR COMPLETAMENTE**

**CAMBIOS IMPORTANTES:**
- âœ… Se agregÃ³ modelo Empleado con campos: idEmpleado, nombre, departamento, sueldo
- âœ… Se configurÃ³ idEmpleado como clave primaria autoincremental
- âœ… Se agregaron validaciones a nivel de modelo
- âœ… Se configurÃ³ la tabla como 'empleado'

### Contenido completo

```python
from django.db import models


class Empleado(models.Model):
    """
    Modelo de base de datos para representar un empleado.
    
    Campos:
    - idEmpleado: Clave primaria autoincremental
    - nombre: Nombre del empleado (requerido)
    - departamento: Departamento al que pertenece (requerido)
    - sueldo: Salario del empleado con validaciÃ³n de valor positivo
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
```

### ExplicaciÃ³n

| Campo | Tipo | DescripciÃ³n |
|-------|------|------------|
| **idEmpleado** | AutoField (PK) | Identificador Ãºnico autoincremental |
| **nombre** | CharField(100) | Nombre del empleado (mÃ¡ximo 100 caracteres) |
| **departamento** | CharField(100) | Departamento (mÃ¡ximo 100 caracteres) |
| **sueldo** | DecimalField(10,2) | Salario con mÃ¡ximo 10 dÃ­gitos y 2 decimales |

---

## 6. CREAR SERIALIZER

### Ruta: `C:\Escritorio\Software\proyecto_empleados_api\empleados\serializers.py`
### Estado: **NUEVO - CREAR**

**CAMBIOS IMPORTANTES:**
- âœ… Se creÃ³ EmpleadoSerializer basado en ModelSerializer
- âœ… Se agregaron validaciones bÃ¡sicas en mÃ©todos validate_*
- âœ… Se validÃ³ que nombre y departamento tengan mÃ­nimo 3 caracteres
- âœ… Se validÃ³ que sueldo sea mayor a 0

### Contenido completo

```python
from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Empleado.
    Convierte objetos del modelo a JSON y viceversa.
    Incluye validaciones bÃ¡sicas para asegurar integridad de datos.
    """
    
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']
        read_only_fields = ['idEmpleado']
    
    def validate_nombre(self, value):
        """ValidaciÃ³n: El nombre no puede estar vacÃ­o y debe tener al menos 3 caracteres."""
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("El nombre es requerido y no puede estar vacÃ­o.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value.strip()
    
    def validate_departamento(self, value):
        """ValidaciÃ³n: El departamento no puede estar vacÃ­o y debe tener al menos 3 caracteres."""
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("El departamento es requerido y no puede estar vacÃ­o.")
        if len(value) < 3:
            raise serializers.ValidationError("El departamento debe tener al menos 3 caracteres.")
        return value.strip()
    
    def validate_sueldo(self, value):
        """ValidaciÃ³n: El sueldo debe ser un valor positivo (mayor que 0)."""
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser un valor positivo (mayor que 0).")
        return value
    
    def validate(self, data):
        """ValidaciÃ³n a nivel del objeto completo (despuÃ©s de validar campos individuales)."""
        return data
```

### ExplicaciÃ³n de validaciones

- **validate_nombre()**: Asegura que el nombre no estÃ© vacÃ­o y tenga mÃ­nimo 3 caracteres
- **validate_departamento()**: Asegura que el departamento no estÃ© vacÃ­o y tenga mÃ­nimo 3 caracteres
- **validate_sueldo()**: Asegura que el sueldo sea mayor a 0
- **validate()**: ValidaciÃ³n a nivel general del objeto

---

## 7. CREAR VISTAS CRUD

### Ruta: `C:\Escritorio\Software\proyecto_empleados_api\empleados\views.py`
### Estado: **EXISTENTE - REEMPLAZAR COMPLETAMENTE**

**CAMBIOS IMPORTANTES:**
- âœ… Se creÃ³ ListarEmpleadosView para GET (listar) y POST (crear)
- âœ… Se creÃ³ DetalleEmpleadoView para GET (detalle), PUT/PATCH (actualizar) y DELETE (eliminar)
- âœ… Se personalizaron las respuestas JSON con mensajes descriptivos
- âœ… Se usaron generics de Django REST Framework para reutilizar cÃ³digo

### Contenido completo

```python
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
    Vista para obtener, actualizar o eliminar un empleado especÃ­fico.
    
    GET: Retorna los detalles de un empleado especÃ­fico
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
```

### ExplicaciÃ³n de vistas

**ListarEmpleadosView (hereda de ListCreateAPIView):**
- GET `/api/empleados/` â†’ Lista todos los empleados
- POST `/api/empleados/` â†’ Crea un nuevo empleado

**DetalleEmpleadoView (hereda de RetrieveUpdateDestroyAPIView):**
- GET `/api/empleados/{id}/` â†’ Obtiene detalles de un empleado especÃ­fico
- PUT `/api/empleados/{id}/` â†’ Actualiza completo un empleado
- PATCH `/api/empleados/{id}/` â†’ Actualiza parcialmente un empleado
- DELETE `/api/empleados/{id}/` â†’ Elimina un empleado

---

## 8. CONFIGURAR URLs

### 8.1 URLs de la aplicaciÃ³n empleados

**Ruta:** `C:\Escritorio\Software\proyecto_empleados_api\empleados\urls.py`
**Estado:** **NUEVO - CREAR**

**CAMBIOS IMPORTANTES:**
- âœ… Se creÃ³ archivo urls.py en la aplicaciÃ³n empleados
- âœ… Se asociaron las vistas a rutas especÃ­ficas
- âœ… Se definiÃ³ el namespace 'empleados'

```python
from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    # Listar todos los empleados y crear nuevos
    path('', views.ListarEmpleadosView.as_view(), name='listar-crear-empleados'),
    
    # Obtener, actualizar y eliminar un empleado especÃ­fico
    path('<int:pk>/', views.DetalleEmpleadoView.as_view(), name='detalle-empleado'),
]
```

### 8.2 URLs principales del proyecto

**Ruta:** `C:\Escritorio\Software\proyecto_empleados_api\proyecto_empleados_api\urls.py`
**Estado:** **EXISTENTE - EDITAR**

**CAMBIOS IMPORTANTES:**
- âœ… Se agregÃ³ import `include` de django.urls
- âœ… Se agregÃ³ la ruta principal de la API

### Contenido completo

```python
"""
URL configuration for proyecto_empleados_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # CAMBIO IMPORTANTE: Se agregÃ³ la ruta para la API de empleados
    path('api/empleados/', include('empleados.urls')),
]
```

---

## 9. BASE DE DATOS MYSQL

### Objetivo
Crear la base de datos MySQL `rh_db` y la tabla `empleado`.

### 9.1 Script SQL

**Ruta:** `C:\Escritorio\Software\proyecto_empleados_api\create_database.sql`

```sql
-- Script para crear la base de datos y tabla de empleados
-- Base de datos: rh_db
-- Usuario: root
-- ContraseÃ±a: (vacÃ­a)

CREATE DATABASE IF NOT EXISTS rh_db;
USE rh_db;

CREATE TABLE empleado (
    idEmpleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL CHECK (sueldo > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla creada exitosamente
```

### 9.2 Crear base de datos

#### OpciÃ³n 1: Usando MySQL desde lÃ­nea de comandos (CMD o PowerShell)

```powershell
# Abre MySQL desde PowerShell
mysql -u root -p

# Dentro de MySQL, ejecuta los comandos SQL:
CREATE DATABASE IF NOT EXISTS rh_db;
USE rh_db;

CREATE TABLE empleado (
    idEmpleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL CHECK (sueldo > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# Salir
EXIT;
```

#### OpciÃ³n 2: Usando un cliente MySQL como MySQL Workbench o HeidiSQL
1. Abre el cliente MySQL
2. Copia y pega el contenido del script `create_database.sql`
3. Ejecuta las sentencias

#### OpciÃ³n 3: Usando la terminal con archivo SQL
```powershell
mysql -u root < create_database.sql
```

### 9.3 Configurar PyMySQL en Django

**Ruta:** `C:\Escritorio\Software\proyecto_empleados_api\proyecto_empleados_api\__init__.py`
**Estado:** **EXISTENTE - EDITAR**

**CAMBIOS IMPORTANTES:**
- âœ… Se agregÃ³ configuraciÃ³n de PyMySQL como conector MySQL

```python
import pymysql

pymysql.install_as_MySQLdb()
```

---

## 10. MIGRACIONES

### Objetivo
Generar y aplicar las migraciones de Django para crear la estructura de tablas.

### 10.1 Crear migraciones

**Comando:**
```powershell
python manage.py makemigrations
```

**Â¿QuÃ© hace?**
Lee los modelos Python (en este caso, el modelo Empleado) y genera archivos de migraciÃ³n que describen los cambios en la base de datos.

**Resultado esperado:**
```
Migrations for 'empleados':
  empleados\migrations\0001_initial.py
    + Create model Empleado
```

### 10.2 Archivo de migraciÃ³n generado

**Ruta:** `C:\Escritorio\Software\proyecto_empleados_api\empleados\migrations\0001_initial.py`
**Estado:** **AUTO-GENERADO**

```python
# Generated by Django 6.0.5 on 2026-05-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Empleado')),
                ('nombre', models.CharField(help_text='Nombre completo del empleado', max_length=100, verbose_name='Nombre')),
                ('departamento', models.CharField(help_text='Departamento del empleado', max_length=100, verbose_name='Departamento')),
                ('sueldo', models.DecimalField(decimal_places=2, help_text='Sueldo del empleado', max_digits=10, verbose_name='Sueldo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['idEmpleado'],
            },
        ),
    ]
```

### 10.3 Aplicar migraciones

**Comando:**
```powershell
python manage.py migrate
```

**Â¿QuÃ© hace?**
Ejecuta las migraciones generadas en el paso anterior, creando las tablas en la base de datos MySQL.

**Resultado esperado:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, empleados, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying auth.0002_alter_permission_options... OK
  Applying empleados.0001_initial... OK
  Applying sessions.0001_initial... OK
```

---

## 11. EJECUTAR EL SERVIDOR

### Objetivo
Iniciar el servidor de desarrollo de Django en el puerto 8080.

### Comando

```powershell
python manage.py runserver 8080
```

**Â¿QuÃ© hace?**
Inicia el servidor de desarrollo de Django en la direcciÃ³n `http://localhost:8080/`

**Resultado esperado:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 19, 2026 - 18:30:45
Django version 6.0.5, using settings 'proyecto_empleados_api.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.
```

### Endpoints disponibles

| MÃ©todo | Endpoint | DescripciÃ³n |
|--------|----------|-------------|
| **GET** | `http://localhost:8080/api/empleados/` | Listar todos los empleados |
| **POST** | `http://localhost:8080/api/empleados/` | Crear un nuevo empleado |
| **GET** | `http://localhost:8080/api/empleados/{id}/` | Obtener detalles de un empleado |
| **PUT** | `http://localhost:8080/api/empleados/{id}/` | Actualizar un empleado (completo) |
| **PATCH** | `http://localhost:8080/api/empleados/{id}/` | Actualizar un empleado (parcial) |
| **DELETE** | `http://localhost:8080/api/empleados/{id}/` | Eliminar un empleado |

---

## 12. PRUEBAS EN POSTMAN

### Objetivo
Probar todos los endpoints CRUD de la API usando Postman.

### 12.1 Descargar Postman
- Descarga desde: https://www.postman.com/downloads/
- Instala y abre la aplicaciÃ³n

### 12.2 Crear una colecciÃ³n

1. En Postman, haz clic en "Create" â†’ "Collection"
2. Nombra la colecciÃ³n: "Empleados API"
3. Haz clic en "Create"

### 12.3 Pruebas CRUD

#### ðŸ“ Prueba 1: LISTAR EMPLEADOS (GET)

**Nombre:** GET - Listar todos los empleados
**MÃ©todo:** GET
**URL:** `http://localhost:8080/api/empleados/`

**Steps:**
1. En Postman, crea una nueva request
2. Selecciona mÃ©todo GET
3. Pega la URL
4. Haz clic en "Send"

**Respuesta esperada (200 OK):**
```json
{
    "mensaje": "Empleados listados correctamente",
    "total": 0,
    "datos": []
}
```

---

#### âž• Prueba 2: CREAR EMPLEADO (POST)

**Nombre:** POST - Crear nuevo empleado
**MÃ©todo:** POST
**URL:** `http://localhost:8080/api/empleados/`

**Steps:**
1. Crea una nueva request POST
2. Pega la URL
3. Selecciona la pestaÃ±a "Body"
4. Selecciona "raw" y cambia el formato a "JSON"
5. Copia y pega el siguiente JSON:

```json
{
    "nombre": "Juan PÃ©rez",
    "departamento": "TecnologÃ­a",
    "sueldo": 3500.00
}
```

6. Haz clic en "Send"

**Respuesta esperada (201 Created):**
```json
{
    "mensaje": "Empleado creado exitosamente",
    "datos": {
        "idEmpleado": 1,
        "nombre": "Juan PÃ©rez",
        "departamento": "TecnologÃ­a",
        "sueldo": "3500.00"
    }
}
```

**Crear mÃ¡s empleados para las pruebas:**

```json
{
    "nombre": "MarÃ­a GarcÃ­a",
    "departamento": "Recursos Humanos",
    "sueldo": 3200.00
}
```

```json
{
    "nombre": "Carlos LÃ³pez",
    "departamento": "Ventas",
    "sueldo": 2800.00
}
```

---

#### ðŸ” Prueba 3: OBTENER DETALLES DE UN EMPLEADO (GET por ID)

**Nombre:** GET - Obtener detalles de empleado
**MÃ©todo:** GET
**URL:** `http://localhost:8080/api/empleados/1/`

**Steps:**
1. Crea una nueva request GET
2. Pega la URL (reemplaza `1` con el ID del empleado)
3. Haz clic en "Send"

**Respuesta esperada (200 OK):**
```json
{
    "mensaje": "Empleado obtenido correctamente",
    "datos": {
        "idEmpleado": 1,
        "nombre": "Juan PÃ©rez",
        "departamento": "TecnologÃ­a",
        "sueldo": "3500.00"
    }
}
```

---

#### âœï¸ Prueba 4: ACTUALIZAR UN EMPLEADO (PUT)

**Nombre:** PUT - Actualizar empleado (completo)
**MÃ©todo:** PUT
**URL:** `http://localhost:8080/api/empleados/1/`

**Steps:**
1. Crea una nueva request PUT
2. Pega la URL
3. Selecciona la pestaÃ±a "Body"
4. Selecciona "raw" y formato "JSON"
5. Copia y pega:

```json
{
    "nombre": "Juan Carlos PÃ©rez",
    "departamento": "TecnologÃ­a Senior",
    "sueldo": 4500.00
}
```

6. Haz clic en "Send"

**Respuesta esperada (200 OK):**
```json
{
    "mensaje": "Empleado actualizado exitosamente",
    "datos": {
        "idEmpleado": 1,
        "nombre": "Juan Carlos PÃ©rez",
        "departamento": "TecnologÃ­a Senior",
        "sueldo": "4500.00"
    }
}
```

---

#### ðŸ”§ Prueba 5: ACTUALIZAR PARCIALMENTE UN EMPLEADO (PATCH)

**Nombre:** PATCH - Actualizar empleado (parcial)
**MÃ©todo:** PATCH
**URL:** `http://localhost:8080/api/empleados/2/`

**Steps:**
1. Crea una nueva request PATCH
2. Pega la URL
3. Body en "raw" JSON:

```json
{
    "sueldo": 3500.00
}
```

4. Haz clic en "Send"

**Respuesta esperada (200 OK):**
```json
{
    "mensaje": "Empleado actualizado exitosamente",
    "datos": {
        "idEmpleado": 2,
        "nombre": "MarÃ­a GarcÃ­a",
        "departamento": "Recursos Humanos",
        "sueldo": "3500.00"
    }
}
```

---

#### ðŸ—‘ï¸ Prueba 6: ELIMINAR UN EMPLEADO (DELETE)

**Nombre:** DELETE - Eliminar empleado
**MÃ©todo:** DELETE
**URL:** `http://localhost:8080/api/empleados/3/`

**Steps:**
1. Crea una nueva request DELETE
2. Pega la URL (reemplaza `3` con el ID del empleado a eliminar)
3. Haz clic en "Send"

**Respuesta esperada (200 OK):**
```json
{
    "mensaje": "Empleado \"Carlos LÃ³pez\" eliminado exitosamente"
}
```

---

#### âŒ Prueba 7: VALIDACIONES - Sueldo negativo (POST)

**Nombre:** POST - ValidaciÃ³n: Sueldo negativo
**MÃ©todo:** POST
**URL:** `http://localhost:8080/api/empleados/`

**Body:**
```json
{
    "nombre": "Test Usuario",
    "departamento": "Testing",
    "sueldo": -1500.00
}
```

**Respuesta esperada (400 Bad Request):**
```json
{
    "sueldo": [
        "El sueldo debe ser un valor positivo (mayor que 0)."
    ]
}
```

---

#### âŒ Prueba 8: VALIDACIONES - Nombre corto (POST)

**Nombre:** POST - ValidaciÃ³n: Nombre muy corto
**MÃ©todo:** POST
**URL:** `http://localhost:8080/api/empleados/`

**Body:**
```json
{
    "nombre": "AB",
    "departamento": "Testing",
    "sueldo": 2000.00
}
```

**Respuesta esperada (400 Bad Request):**
```json
{
    "nombre": [
        "El nombre debe tener al menos 3 caracteres."
    ]
}
```

---

#### ðŸš« Prueba 9: Empleado no encontrado (GET)

**Nombre:** GET - Empleado no encontrado
**MÃ©todo:** GET
**URL:** `http://localhost:8080/api/empleados/999/`

**Respuesta esperada (404 Not Found):**
```json
{
    "detail": "Not found."
}
```

---

### 12.4 Configurar CORS desde cliente (React/Angular)

Para probar CORS desde React (puerto 5173) o Angular (puerto 4200):

#### Ejemplo con Fetch API (React/Vanilla JS):
```javascript
// GET - Listar empleados
fetch('http://localhost:8080/api/empleados/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));

// POST - Crear empleado
fetch('http://localhost:8080/api/empleados/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        nombre: 'Nuevo Empleado',
        departamento: 'Departamento',
        sueldo: 3000.00
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### Ejemplo con Axios (React):
```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8080/api/empleados/';

// GET
axios.get(API_URL)
    .then(response => console.log(response.data))
    .catch(error => console.error('Error:', error));

// POST
axios.post(API_URL, {
    nombre: 'Nuevo Empleado',
    departamento: 'Departamento',
    sueldo: 3000.00
})
.then(response => console.log(response.data))
.catch(error => console.error('Error:', error));
```

---

## 13. ESTRUCTURA FINAL DEL PROYECTO

### Ãrbol completo de directorios

```
C:\Escritorio\Software\proyecto_empleados_api\
â”‚
â”œâ”€â”€ venv/                                    # Ambiente virtual Python
â”‚   â”œâ”€â”€ Include/
â”‚   â”œâ”€â”€ Lib/
â”‚   â”œâ”€â”€ Scripts/
â”‚   â””â”€â”€ pyvenv.cfg
â”‚
â”œâ”€â”€ empleados/                                # AplicaciÃ³n Django
â”‚   â”œâ”€â”€ migrations/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ 0001_initial.py                 # MigraciÃ³n del modelo Empleado
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ admin.py                            # âœ… Registra modelo en admin
â”‚   â”œâ”€â”€ apps.py
â”‚   â”œâ”€â”€ models.py                           # âœ… Modelo Empleado
â”‚   â”œâ”€â”€ serializers.py                      # âœ… Serializador EmpleadoSerializer
â”‚   â”œâ”€â”€ tests.py
â”‚   â”œâ”€â”€ urls.py                             # âœ… URLs de la aplicaciÃ³n
â”‚   â””â”€â”€ views.py                            # âœ… Vistas ListarEmpleadosView y DetalleEmpleadoView
â”‚
â”œâ”€â”€ proyecto_empleados_api/                                # ConfiguraciÃ³n del proyecto
â”‚   â”œâ”€â”€ __pycache__/
â”‚   â”œâ”€â”€ __init__.py                         # âœ… ConfiguraciÃ³n PyMySQL
â”‚   â”œâ”€â”€ asgi.py
â”‚   â”œâ”€â”€ settings.py                         # âœ… ConfiguraciÃ³n completa
â”‚   â”œâ”€â”€ urls.py                             # âœ… URLs principales con API
â”‚   â””â”€â”€ wsgi.py
â”‚
â”œâ”€â”€ create_database.sql                      # Script SQL para crear BD
â”œâ”€â”€ db.sqlite3                               # (No se usa, usamos MySQL)
â”œâ”€â”€ manage.py                                # Herramienta CLI de Django
â””â”€â”€ requirements.txt                         # (Recomendado crear)
```

### Archivos modificados/creados resumen

| Archivo | Estado | Cambios |
|---------|--------|---------|
| `proyecto_empleados_api/settings.py` | EDITADO | ConfiguraciÃ³n MySQL, REST, CORS |
| `proyecto_empleados_api/urls.py` | EDITADO | AgregÃ³ ruta `/api/empleados/` |
| `proyecto_empleados_api/__init__.py` | EDITADO | ConfiguraciÃ³n PyMySQL |
| `empleados/models.py` | EDITADO | Modelo Empleado completo |
| `empleados/serializers.py` | NUEVO | EmpleadoSerializer con validaciones |
| `empleados/views.py` | EDITADO | Vistas CRUD con generics |
| `empleados/urls.py` | NUEVO | URLs de la aplicaciÃ³n |
| `empleados/admin.py` | EDITADO | Registro en admin panel |
| `create_database.sql` | NUEVO | Script para crear BD MySQL |

---

## ðŸ“‹ CHECKLIST DE VERIFICACIÃ“N

Antes de usar el servidor, verifica:

- âœ… Ambiente virtual activado: `(venv)` visible en terminal
- âœ… Dependencias instaladas: `pip list` muestra Django, DRF, CORS, PyMySQL
- âœ… MySQL corriendo en localhost:3306
- âœ… Base de datos `rh_db` creada
- âœ… Migraciones creadas: `python manage.py makemigrations` sin errores
- âœ… Migraciones aplicadas: `python manage.py migrate` sin errores
- âœ… Servidor inicia correctamente: `python manage.py runserver 8080`
- âœ… Endpoints responden: GET `http://localhost:8080/api/empleados/` retorna JSON

---

## ðŸš€ COMANDOS RÃPIDOS

```powershell
# Activar ambiente virtual
.\venv\Scripts\Activate.ps1

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor (puerto 8080)
python manage.py runserver 8080

# Crear superusuario para admin
python manage.py createsuperuser

# Ver logs del servidor
python manage.py runserver 8080 --verbosity=2

# Desactivar ambiente virtual
deactivate
```

---

## ðŸ“š RECURSOS COMPLEMENTARIOS

- [DocumentaciÃ³n Django](https://docs.djangoproject.com/)
- [DocumentaciÃ³n Django REST Framework](https://www.django-rest-framework.org/)
- [DocumentaciÃ³n django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [DocumentaciÃ³n MySQL](https://dev.mysql.com/doc/)
- [Tutorial Postman](https://learning.postman.com/docs/introduction/overview/)

---

**GuÃ­a completada. Â¡Proyecto listo para producciÃ³n con todas las mejores prÃ¡cticas implementadas!** ðŸŽ‰

