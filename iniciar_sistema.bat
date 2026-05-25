@echo off
echo ========================================
echo   INICIANDO SISTEMA COMPLETO
echo   Backend Django + Frontend React
echo ========================================
echo.

REM Obtener rutas
set DJANGO_DIR=C:\Escritorio\Software\proyecto_empleados_api
set REACT_DIR=C:\Escritorio\Software\proyecto_empleados_api_frontend

REM Color para las ventanas
color 0B

echo [1/2] Iniciando Backend Django en puerto 8000...
echo.
start "Django Backend - Puerto 8000" cmd /k "cd /d %DJANGO_DIR% && %DJANGO_DIR%\venv\Scripts\python.exe manage.py runserver 8000"

echo Esperando 3 segundos...
timeout /t 3 /nobreak

echo.
echo [2/2] Iniciando Frontend React en puerto 5173...
echo.
start "React Frontend - Puerto 5173" cmd /k "cd /d %REACT_DIR% && npm run dev"

echo.
echo ========================================
echo   SISTEMA INICIADO
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo API: http://localhost:8000/api/empleados/
echo Admin: http://localhost:8000/admin/
echo.
pause
