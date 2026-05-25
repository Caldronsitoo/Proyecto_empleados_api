# 🚀 Frontend React - Proyecto empleados API

Sistema de frontend desarrollado con React + Vite para gestión de empleados conectado a backend Django REST API.

## 🔍 Características

âœ… **CRUD Completo**
- Crear nuevos empleados
- Listar todos los empleados
- Editar empleados existentes
- Eliminar empleados

âœ… **Funcionalidades Adicionales**
- ðŸ” BÃºsqueda en tiempo real por nombre o departamento
- ðŸ“± DiseÃ±o responsivo (funciona en mÃ³viles y tablets)
- ðŸŽ¨ Interfaz moderna con gradientes y animaciones
- âš¡ ValidaciÃ³n de formularios en cliente
- ðŸ”Œ IntegraciÃ³n directa con API REST Django

## ðŸš€ Inicio RÃ¡pido

### OpciÃ³n 1: Iniciar todo automÃ¡ticamente

```powershell
# Desde PowerShell
C:\Escritorio\Software\iniciar_sistema.ps1
```

O hacer doble clic en: `C:\Escritorio\Software\iniciar_sistema.bat`

### OpciÃ³n 2: Iniciar manualmente

```bash
# Terminal 1: Backend Django
cd C:\Escritorio\Software\proyecto_empleados_api
venv\Scripts\Activate.ps1
python manage.py runserver 8000

# Terminal 2: Frontend React
cd C:\Escritorio\Software\proyecto_empleados_api_frontend
npm run dev
```

## ðŸ“± URLs Disponibles

- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API REST**: http://localhost:8000/api/empleados/
- **Admin Django**: http://localhost:8000/admin/

## ðŸŽ¯ Uso

### Crear Empleado
1. Haz clic en "âž• Nuevo Empleado"
2. Completa los campos (nombre, departamento, sueldo)
3. Haz clic en "âœ… Crear"

### Editar Empleado
1. Haz clic en "âœï¸ Editar" en la fila del empleado
2. Modifica los datos
3. Haz clic en "ðŸ’¾ Actualizar"

### Buscar
Usa la barra de bÃºsqueda para filtrar por nombre o departamento en tiempo real.

### Eliminar
Haz clic en "ðŸ—‘ï¸ Eliminar" (pedirÃ¡ confirmaciÃ³n)

## ðŸ—ï¸ Estructura

```
src/
â”œâ”€â”€ components/
â”‚   â”œâ”€â”€ App.jsx           # Componente principal
â”‚   â”œâ”€â”€ EmpleadoForm.jsx  # Formulario
â”‚   â””â”€â”€ EmpleadoList.jsx  # Tabla de empleados
â”œâ”€â”€ services/
â”‚   â””â”€â”€ api.js            # Cliente HTTP (Axios)
â”œâ”€â”€ styles/
â”‚   â”œâ”€â”€ App.css           # Estilos generales
â”‚   â”œâ”€â”€ Form.css          # Estilos del formulario
â”‚   â””â”€â”€ Table.css         # Estilos de la tabla
â””â”€â”€ main.jsx              # Punto de entrada
```

## ðŸ“¦ Dependencias

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "axios": "^1.x"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "@vitejs/plugin-react": "^4.0.0"
  }
}
```

## ðŸŽ¨ CaracterÃ­sticas de DiseÃ±o

- âœ¨ Gradiente morado moderno
- ðŸŽ­ Animaciones suaves
- ðŸ“Š Tabla responsiva
- ðŸ”” Validaciones en tiempo real
- ðŸŽ¯ UI intuitiva

## ðŸ” BÃºsqueda en Tiempo Real

Filtra empleados mientras escribes:
- Busca por nombre completo
- Busca por departamento
- Case-insensitive

## ðŸ“± Responsivo

- âœ… Desktop (1920px+)
- âœ… Laptop (1024px+)
- âœ… Tablet (768px+)
- âœ… Mobile (320px+)

## ðŸ› SoluciÃ³n de Problemas

**Error de conexiÃ³n a API**
```
â†’ Verifica que Django estÃ© corriendo en puerto 8000
â†’ Verifica CORS en Django settings.py
```

**Los estilos no se ven**
```
â†’ Recarga con Ctrl+Shift+Del (cachÃ©)
â†’ Recarga con Ctrl+F5 (hard refresh)
```

**Puerto 5173 ya en uso**
```
â†’ npm run dev -- --port 5174
```

## ðŸš€ Build para ProducciÃ³n

```bash
npm run build
```

Genera carpeta `dist/` lista para deployment.

## ðŸ“š Ver TambiÃ©n

- [Backend Django](../proyecto_empleados_api/README.md)
- [API Documentation](../proyecto_empleados_api/GUIA_COMPLETA_API_EMPLEADOS.md)
- [SQL Server Config](../proyecto_empleados_api/CONEXION_SQL_SERVER.md)

