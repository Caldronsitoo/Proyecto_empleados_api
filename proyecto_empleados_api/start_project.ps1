# Script para iniciar el proyecto Django en Windows PowerShell
# Uso: .\start_project.ps1

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (Test-Path .\venv\Scripts\Activate.ps1) {
    Write-Host "Activando entorno virtual..."
    . .\venv\Scripts\Activate.ps1
} else {
    Write-Host "No se encontró venv\Scripts\Activate.ps1. Asegúrate de crear el entorno virtual primero." -ForegroundColor Yellow
}

Write-Host "Iniciando servidor de desarrollo Django..."
python .\manage.py runserver 8080
