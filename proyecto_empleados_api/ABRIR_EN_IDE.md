# ðŸ”§ ABRIR PROYECTO EN IDE

## IDE RECOMENDADO: PyCharm

PyCharm es el IDE mÃ¡s completo para Django. Si lo prefieres, tambiÃ©n puedes usar VS Code.

---

## ðŸ“˜ OPCIÃ“N 1: PyCharm PROFESSIONAL (Recomendado)

### 1. Abrir el proyecto

1. Abre PyCharm
2. **File** â†’ **Open**
3. Selecciona: `C:\Escritorio\Software\proyecto_empleados_api`
4. Haz clic en "Open as Project"
5. PyCharm analizarÃ¡ el proyecto (~1 minuto)

### 2. Configurar intÃ©rprete Python

1. **File** â†’ **Settings** (o **PyCharm** â†’ **Preferences** en Mac)
2. Busca: **Project: proyecto_empleados_api** â†’ **Python Interpreter**
3. Haz clic en el âš™ï¸ (gear icon)
4. **Add**
5. **Existing Environment**
6. Busca: `C:\Escritorio\Software\proyecto_empleados_api\venv\Scripts\python.exe`
7. Haz clic en **OK**

**Resultado**: VerÃ¡s todos los paquetes instalados (Django, DRF, etc.)

### 3. Configurar Django en PyCharm

1. **File** â†’ **Settings**
2. Busca: **Django**
3. Marca: **Enable Django Support**
4. Project root: `C:\Escritorio\Software\proyecto_empleados_api`
5. Settings file: `proyecto_empleados_api/settings.py`
6. Manage script: `manage.py`
7. Haz clic en **OK**

### 4. Ejecutar servidor desde PyCharm

1. **Run** â†’ **Edit Configurations**
2. Haz clic en **+** (Add new)
3. Selecciona: **Django Server**
4. Name: `Django Dev Server`
5. Port: `8080`
6. Haz clic en **OK**
7. Presiona â–¶ï¸ (Play) o **Run** â†’ **Run 'Django Dev Server'**

**Resultado**: Servidor corriendo en `http://localhost:8080`

### 5. Usar la consola Django

En PyCharm:
- **Tools** â†’ **Run manage.py Task**
- O presiona: **Ctrl + Alt + R**

Luego escribe comandos como:
```
makemigrations
migrate
createsuperuser
```

### 6. Atajos Ãºtiles en PyCharm

| Atajo | AcciÃ³n |
|-------|--------|
| **Ctrl + Shift + P** | Encontrar archivo |
| **Ctrl + F** | Buscar en archivo |
| **Ctrl + H** | Buscar y reemplazar |
| **Ctrl + /** | Comentar lÃ­nea |
| **Shift + Alt + F** | Formatear cÃ³digo |
| **F2** | Ir a siguiente error |
| **Ctrl + B** | Ir a definiciÃ³n |

---

## ðŸŽ¨ OPCIÃ“N 2: Visual Studio Code

### 1. Abrir el proyecto

1. Abre VS Code
2. **File** â†’ **Open Folder**
3. Selecciona: `C:\Escritorio\Software\proyecto_empleados_api`
4. Haz clic en **Select Folder**

### 2. Instalar extensiones recomendadas

Extensiones necesarias:
- **Python** (Microsoft)
- **Pylance** (Microsoft)
- **Django** (Baptiste Darthenay)
- **Thunder Client** o **REST Client** (para pruebas)
- **Rainbow Brackets** (opcional, para mejor legibilidad)

Para instalar:
1. **Ctrl + Shift + X** (Extensions)
2. Busca extensiÃ³n
3. Haz clic en **Install**

### 3. Configurar intÃ©rprete Python

1. **Ctrl + Shift + P**
2. Escribe: `Python: Select Interpreter`
3. Elige: `./venv/Scripts/python.exe`

VS Code mostrarÃ¡ âœ… cuando estÃ© correcto.

### 4. Crear terminal integrada

1. **Ctrl + Ã±** (o **View** â†’ **Terminal**)
2. Escribe: `.\venv\Scripts\Activate.ps1`
3. VerÃ¡s: `(venv)` en la terminal

### 5. Ejecutar servidor

En la terminal:
```powershell
python manage.py runserver 8080
```

### 6. Pruebas REST en VS Code

Con **Thunder Client**:
1. Abre Thunder Client (icono en sidebar izquierdo)
2. New Request
3. URL: `http://localhost:8080/api/empleados/`
4. MÃ©todo: GET
5. Send

---

## ðŸ—‚ï¸ ESTRUCTURA EN EL IDE

En el explorador de archivos del IDE, verÃ¡s:

```
proyecto_empleados_api/
â”œâ”€â”€ ðŸ“ empleados/
â”‚   â”œâ”€â”€ ðŸ“ migrations/
â”‚   â”œâ”€â”€ admin.py           â† Edita aquÃ­ para personalizar admin
â”‚   â”œâ”€â”€ models.py          â† Define modelos aquÃ­
â”‚   â”œâ”€â”€ serializers.py     â† Validaciones aquÃ­
â”‚   â”œâ”€â”€ urls.py            â† URLs de la app aquÃ­
â”‚   â””â”€â”€ views.py           â† LÃ³gica CRUD aquÃ­
â”‚
â”œâ”€â”€ ðŸ“ proyecto_empleados_api/
â”‚   â”œâ”€â”€ settings.py        â† ConfiguraciÃ³n principal
â”‚   â”œâ”€â”€ urls.py            â† URLs del proyecto
â”‚   â””â”€â”€ __init__.py        â† PyMySQL config
â”‚
â”œâ”€â”€ ðŸ“„ manage.py           â† CLI de Django
â””â”€â”€ ðŸ“„ requirements.txt    â† Dependencias
```

---

## ðŸ” EXPLORAR CÃ“DIGO EN EL IDE

### Navegar entre archivos

**PyCharm**:
- **Ctrl + Shift + P**: BÃºsqueda rÃ¡pida de archivos
- **Ctrl + P**: Ir a definiciÃ³n

**VS Code**:
- **Ctrl + P**: BÃºsqueda rÃ¡pida de archivos
- **Ctrl + F**: Buscar dentro del archivo
- **F12**: Ir a definiciÃ³n

### Ver documentaciÃ³n

Coloca el cursor en una clase/funciÃ³n y:
- **PyCharm**: Presiona **Ctrl + Q**
- **VS Code**: Presiona **Hover** o **Ctrl + K, Ctrl + I**

---

## ðŸ› DEBUG EN EL IDE

### PyCharm

1. Haz clic en el nÃºmero de lÃ­nea para poner un **breakpoint** (aparece un punto rojo)
2. **Run** â†’ **Debug 'Django Dev Server'**
3. Abre Postman e haz una peticiÃ³n
4. El cÃ³digo se pausarÃ¡ en el breakpoint
5. Inspeciona variables en el panel inferior

### VS Code

1. Instala: **Python Debugger** (Microsoft)
2. Crea archivo `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver", "8080"],
            "django": true
        }
    ]
}
```

3. Haz clic en el nÃºmero de lÃ­nea para breakpoint
4. **F5** (Run â†’ Start Debugging)

---

## ðŸ“ EDITAR ARCHIVOS

### Modelo Empleado

Archivo: `empleados/models.py`

Para agregar un campo:
```python
class Empleado(models.Model):
    # ... campos existentes ...
    fecha_contratacion = models.DateField()  # â† NUEVO
```

Luego:
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Vistas (CRUD)

Archivo: `empleados/views.py`

Puedes personalizar respuestas, agregar filtros, etc.

### Serializer (Validaciones)

Archivo: `empleados/serializers.py`

Agregar validaciÃ³n personalizada:
```python
def validate_nombre(self, value):
    if "123" in value:
        raise serializers.ValidationError("No se permiten nÃºmeros")
    return value
```

---

## ðŸŽ¯ ATAJOS ÃšTILES

### PyCharm

| Atajo | FunciÃ³n |
|-------|---------|
| **Alt + Enter** | Quick fixes y sugerencias |
| **Ctrl + Alt + O** | Optimizar imports |
| **Ctrl + Alt + L** | Formatear cÃ³digo |
| **Ctrl + D** | Duplicar lÃ­nea |
| **Ctrl + X** | Cortar lÃ­nea |
| **Shift + F6** | Renombrar sÃ­mbolo |

### VS Code

| Atajo | FunciÃ³n |
|-------|---------|
| **Ctrl + .** | Quick fixes |
| **Alt + Shift + F** | Formatear documento |
| **Ctrl + Shift + K** | Eliminar lÃ­nea |
| **Alt + Up/Down** | Mover lÃ­nea |
| **Ctrl + Shift + L** | Seleccionar todas las instancias |

---

## ðŸ–¥ï¸ TERMINAL EN EL IDE

### Comandos Ãºtiles

```powershell
# Hacer migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell de Django (para testear cÃ³digo)
python manage.py shell

# Ver todas las rutas
python manage.py show_urls

# Ejecutar pruebas
python manage.py test

# Limpiar migraciones
python manage.py migrate empleados zero
```

---

## ðŸ“¦ INSTALAR NUEVOS PAQUETES

### En PyCharm

1. **File** â†’ **Settings**
2. **Project: proyecto_empleados_api** â†’ **Python Interpreter**
3. Haz clic en **+** (Add)
4. Busca y selecciona el paquete
5. Haz clic en **Install Package**

### En VS Code / Terminal

```powershell
pip install nombre-paquete
```

Luego actualiza `requirements.txt`:
```powershell
pip freeze > requirements.txt
```

---

## ðŸ”— RECURSOS EN EL IDE

### DocumentaciÃ³n dentro del cÃ³digo

En PyCharm, coloca el cursor en:
- `models.Model` â†’ **Ctrl + Q** â†’ Ve documentaciÃ³n de Django
- `serializers.Serializer` â†’ **Ctrl + Q** â†’ Ve documentaciÃ³n de DRF

---

## âœ… CHECKLIST

- âœ… Proyecto abierto en IDE
- âœ… IntÃ©rprete Python configurado
- âœ… Terminal activa con `(venv)`
- âœ… Servidor corriendo (`python manage.py runserver 8080`)
- âœ… Postman importado y listo
- âœ… Puedes ver cÃ³digo con colores

Â¡Listo para desarrollar! ðŸš€

---

**IDE Recomendado: PyCharm Professional**
**Alternativa: VS Code + Extensiones**
**Python: 3.8+**
**Django: 6.0.5**

