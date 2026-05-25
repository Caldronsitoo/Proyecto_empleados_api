# âš¡ QUICK START - GUÃA DE INICIO RÃPIDO

**Si vas apurado, este archivo tiene lo esencial en 5 minutos.**

---

## ðŸš€ EN 5 PASOS

### 1ï¸âƒ£ Activar Ambiente Virtual (1 min)

```powershell
cd C:\Escritorio\Software\proyecto_empleados_api
.\venv\Scripts\Activate.ps1
```

**VerÃ¡s**: `(venv)` antes de la ruta

### 2ï¸âƒ£ Instalar Dependencias (2 min)

```powershell
pip install -r requirements.txt
```

**Espera a que termine** (descarga ~30MB)

### 3ï¸âƒ£ Crear Base de Datos MySQL (1 min)

Abre MySQL y ejecuta:

```sql
CREATE DATABASE IF NOT EXISTS rh_db;
USE rh_db;
CREATE TABLE empleado (
    idEmpleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL CHECK (sueldo > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 4ï¸âƒ£ Hacer Migraciones (1 min)

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5ï¸âƒ£ Ejecutar Servidor (1 min)

```powershell
python manage.py runserver 8080
```

**VerÃ¡s**: `Starting development server at http://127.0.0.1:8080/`

---

## âœ… Â¡LISTO! LA API ESTÃ CORRIENDO

### Endpoints Disponibles

| AcciÃ³n | URL | MÃ©todo |
|--------|-----|--------|
| **Listar** | `/api/empleados/` | GET |
| **Crear** | `/api/empleados/` | POST |
| **Obtener** | `/api/empleados/{id}/` | GET |
| **Actualizar** | `/api/empleados/{id}/` | PUT |
| **Actualizar parcial** | `/api/empleados/{id}/` | PATCH |
| **Eliminar** | `/api/empleados/{id}/` | DELETE |

---

## ðŸ§ª PRUEBA RÃPIDA CON cURL

### Listar empleados (debe devolver vacÃ­o)

```bash
curl -X GET http://localhost:8080/api/empleados/
```

**Respuesta esperada**:
```json
{
    "mensaje": "Empleados listados correctamente",
    "total": 0,
    "datos": []
}
```

### Crear un empleado

```bash
curl -X POST http://localhost:8080/api/empleados/ \
  -H "Content-Type: application/json" \
  -d "{\"nombre\":\"Juan\",\"departamento\":\"TI\",\"sueldo\":3500.00}"
```

### Listar (ahora debe tener 1)

```bash
curl -X GET http://localhost:8080/api/empleados/
```

---

## ðŸ“± PROBAR CON POSTMAN

1. Abre Postman
2. File â†’ Import
3. Selecciona: `PostmanCollection.json`
4. Haz clic en "1. Listar Empleados"
5. Presiona Send

**Â¡Listo!** Tienes todas las pruebas CRUD preparadas

---

## ðŸ”— CORS CONFIGURADO PARA

- `http://localhost:4200` (Angular)
- `http://localhost:5173` (React)

**Ejemplo React**:

```javascript
fetch('http://localhost:8080/api/empleados/')
  .then(r => r.json())
  .then(data => console.log(data))
```

---

## ðŸ› ERRORES COMUNES

### âŒ "Connection refused to MySQL"

**SoluciÃ³n**: AsegÃºrate que MySQL estÃ© corriendo
```powershell
# Windows - verifica en Services o:
mysql -u root
```

### âŒ "CORS Error"

**SoluciÃ³n**: La API ya estÃ¡ configurada. Si aÃºn tienes error, verifica:
- Â¿EstÃ¡ el servidor corriendo en puerto 8080?
- Â¿Tu cliente estÃ¡ en puerto 4200 o 5173?

### âŒ "ModuleNotFoundError"

**SoluciÃ³n**: No tienes dependencias instaladas
```powershell
pip install -r requirements.txt
```

---

## ðŸ“š DOCUMENTACIÃ“N COMPLETA

- **GuÃ­a paso a paso**: `GUIA_COMPLETA_API_EMPLEADOS.md`
- **Arquitectura**: `ARQUITECTURA.md`
- **Referencia archivos**: `RESUMEN_ARCHIVOS.md`
- **Setup general**: `README.md`

---

## ðŸŽ¯ PRÃ“XIMOS PASOS

1. **Insertar datos ejemplo**:
   ```sql
   -- En MySQL
   USE rh_db;
   INSERT INTO empleado VALUES (NULL, 'MarÃ­a', 'RRHH', 3200);
   INSERT INTO empleado VALUES (NULL, 'Carlos', 'Ventas', 2800);
   ```

2. **Crear superusuario** (para admin):
   ```powershell
   python manage.py createsuperuser
   # Accede en: http://localhost:8080/admin/
   ```

3. **Conectar frontend**:
   - React: ver ejemplo en README.md
   - Angular: usar HttpClient con la URL base

---

**Â¡Ya estÃ¡ todo configurado! ðŸŽ‰**

PrÃ³ximo paso: Abre Postman e importa `PostmanCollection.json`

