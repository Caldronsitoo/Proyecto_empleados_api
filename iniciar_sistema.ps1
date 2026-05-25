# Script para iniciar el sistema completo
# Backend Django + Frontend React

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   INICIANDO SISTEMA COMPLETO" -ForegroundColor Cyan
Write-Host "   Backend Django + Frontend React" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Rutas
$DJANGO_DIR = "C:\Escritorio\Software\proyecto_empleados_api"
$REACT_DIR = "C:\Escritorio\Software\proyecto_empleados_api_frontend"
$PYTHON_EXE = "$DJANGO_DIR\venv\Scripts\python.exe"

# Función para iniciar procesos
function Start-Service {
    param(
        [string]$Name,
        [string]$Path,
        [string]$Command
    )
    
    Write-Host "[*] Iniciando $Name..." -ForegroundColor Yellow
    Start-Process -FilePath "cmd.exe" -ArgumentList "/k", "cd /d $Path && $Command" -WindowStyle Normal
    Write-Host "[$Name] iniciado en nueva ventana" -ForegroundColor Green
    Start-Sleep -Seconds 2
}

# Iniciar Django Backend
Write-Host ""
Write-Host "[1/2] Backend Django" -ForegroundColor Cyan
Start-Service -Name "Django Backend" -Path $DJANGO_DIR -Command "$PYTHON_EXE manage.py runserver 8000"

# Esperar un poco
Write-Host "Esperando a que Django inicie..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# Iniciar React Frontend
Write-Host ""
Write-Host "[2/2] Frontend React" -ForegroundColor Cyan
Start-Service -Name "React Frontend" -Path $REACT_DIR -Command "npm run dev"

# Información final
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   SISTEMA INICIADO" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "URLs disponibles:" -ForegroundColor Cyan
Write-Host "  • Frontend React:  http://localhost:5173" -ForegroundColor White
Write-Host "  • Backend Django:  http://localhost:8000" -ForegroundColor White
Write-Host "  • API REST:        http://localhost:8000/api/empleados/" -ForegroundColor White
Write-Host "  • Admin Django:    http://localhost:8000/admin/" -ForegroundColor White
Write-Host ""
Write-Host "✓ Presiona cualquier tecla para cerrar este script (los servidores seguirán ejecutándose)" -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
