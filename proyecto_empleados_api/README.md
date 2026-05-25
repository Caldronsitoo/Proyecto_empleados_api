# ðŸš€ API REST de Empleados - Django REST Framework

**Un proyecto completo de API REST para gestiÃ³n de empleados con Django, Django REST Framework, MySQL y CORS.**

## ðŸ“¦ Requisitos

- Python 3.8+
- MySQL 5.7+
- Postman (para pruebas)
- Visual Studio Code o PyCharm

## âš¡ InstalaciÃ³n RÃ¡pida

### 1. Clonar y preparar el entorno

```powershell
cd C:\Escritorio\Software\proyecto_empleados_api
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Crear la base de datos MySQL

```sql
CREATE DATABASE IF NOT EXISTS rh_db;
USE rh_db;

CREATE TABLE empleado (
    idEmpleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL CHECK (sueldo > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 3. Ejecutar migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Iniciar el servidor

```powershell
python manage.py runserver 8080
```

**Servidor disponible en:** `http://localhost:8080`

---

## ðŸ“¡ Endpoints de la API

| MÃ©todo | Endpoint | DescripciÃ³n |
|--------|----------|-------------|
| GET | `/api/empleados/` | Listar todos los empleados |
| POST | `/api/empleados/` | Crear un nuevo empleado |
| GET | `/api/empleados/{id}/` | Obtener detalles de un empleado |
| PUT | `/api/empleados/{id}/` | Actualizar empleado (completo) |
| PATCH | `/api/empleados/{id}/` | Actualizar empleado (parcial) |
| DELETE | `/api/empleados/{id}/` | Eliminar un empleado |

---

## ðŸ§ª Ejemplos de Uso (cURL)

### Listar empleados
```bash
curl -X GET http://localhost:8080/api/empleados/
```

### Crear empleado
```bash
curl -X POST http://localhost:8080/api/empleados/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan PÃ©rez","departamento":"TecnologÃ­a","sueldo":3500.00}'
```

### Obtener empleado
```bash
curl -X GET http://localhost:8080/api/empleados/1/
```

### Actualizar empleado
```bash
curl -X PUT http://localhost:8080/api/empleados/1/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan Carlos","departamento":"Tech Lead","sueldo":4500.00}'
```

### Eliminar empleado
```bash
curl -X DELETE http://localhost:8080/api/empleados/1/
```

---

## ðŸ”Œ CORS Configurado

La API permite peticiones desde:

- `http://localhost:4200` (Angular)
- `http://localhost:5173` (React/Vite)
- `http://127.0.0.1:4200` (Angular - localhost)
- `http://127.0.0.1:5173` (React - localhost)

### Ejemplo de peticiÃ³n desde React

```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8080/api/empleados/';

// GET - Listar
axios.get(API_URL)
  .then(res => console.log(res.data))
  .catch(err => console.error(err));

// POST - Crear
axios.post(API_URL, {
  nombre: 'MarÃ­a GarcÃ­a',
  departamento: 'RRHH',
  sueldo: 3200.00
})
.then(res => console.log(res.data))
.catch(err => console.error(err));
```

---

## ðŸ“‹ Estructura del Proyecto

```
proyecto_empleados_api/
â”œâ”€â”€ empleados/
â”‚   â”œâ”€â”€ migrations/
â”‚   â”œâ”€â”€ admin.py
â”‚   â”œâ”€â”€ models.py         # Modelo Empleado
â”‚   â”œâ”€â”€ serializers.py    # Validaciones
â”‚   â”œâ”€â”€ views.py          # Vistas CRUD
â”‚   â”œâ”€â”€ urls.py           # Rutas de la app
â”‚   â””â”€â”€ ...
â”œâ”€â”€ proyecto_empleados_api/
â”‚   â”œâ”€â”€ settings.py       # ConfiguraciÃ³n Django
â”‚   â”œâ”€â”€ urls.py           # Rutas principales
â”‚   â””â”€â”€ __init__.py       # PyMySQL config
â”œâ”€â”€ manage.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ GUIA_COMPLETA_API_EMPLEADOS.md
```

---

## âœ… Validaciones

- **Nombre:** MÃ­nimo 3 caracteres, requerido
- **Departamento:** MÃ­nimo 3 caracteres, requerido
- **Sueldo:** Mayor a 0, mÃ¡ximo 10 dÃ­gitos con 2 decimales

---

## ðŸ”§ ConfiguraciÃ³n

### MySQL
- **Host:** localhost
- **Port:** 3306
- **Database:** rh_db
- **User:** root
- **Password:** (vacÃ­a)

### Django
- **DEBUG:** True (cambiar a False en producciÃ³n)
- **ALLOWED_HOSTS:** '*' (cambiar en producciÃ³n)
- **Database Engine:** django.db.backends.mysql

---

## ðŸ“š Para MÃ¡s InformaciÃ³n

Lee la guÃ­a completa: [GUIA_COMPLETA_API_EMPLEADOS.md](GUIA_COMPLETA_API_EMPLEADOS.md)

Contiene:
- âœ… InstalaciÃ³n paso a paso
- âœ… ExplicaciÃ³n de cada archivo
- âœ… Modelos y validaciones
- âœ… Pruebas completas en Postman
- âœ… Ejemplos de cÃ³digo
- âœ… Troubleshooting

---

## ðŸš€ PrÃ³ximos Pasos

1. **AutenticaciÃ³n:** Implementar JWT o Token Auth
2. **PaginaciÃ³n:** Agregar paginaciÃ³n a listados
3. **Filtros:** Agregar filtros avanzados
4. **DocumentaciÃ³n:** Generar Swagger/OpenAPI
5. **Tests:** Crear suite de tests unitarios
6. **Docker:** Containerizar la aplicaciÃ³n

---

## ðŸ“ Licencia

Este proyecto es de cÃ³digo abierto y estÃ¡ disponible bajo licencia MIT.

---

**Autor:** Generado como guÃ­a educativa
**Fecha:** Mayo 2026
**VersiÃ³n:** 1.0

