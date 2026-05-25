#!/usr/bin/env python
"""
Script de inicialización del proyecto Django API de Empleados.
Ejecuta automáticamente los pasos iniciales: makemigrations y migrate.

Uso: python init_project.py
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """
    Ejecuta un comando en terminal y muestra el resultado.
    
    Args:
        command (str): Comando a ejecutar
        description (str): Descripción del comando
    
    Returns:
        bool: True si fue exitoso, False si falló
    """
    print(f"\n{'='*60}")
    print(f"▶ {description}")
    print(f"{'='*60}")
    print(f"Comando: {command}\n")
    
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"\n✅ {description} - EXITOSO\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {description} - FALLÓ")
        print(f"Error: {e}\n")
        return False


def print_banner():
    """Imprime el banner inicial."""
    print(f"\n{'='*60}")
    print("🚀 INICIALIZADOR - API REST DE EMPLEADOS")
    print("   Django + DRF + MySQL + CORS")
    print(f"{'='*60}\n")


def print_info():
    """Imprime información del sistema."""
    print(f"\nℹ️ Información del sistema:")
    print(f"   Sistema Operativo: {platform.system()}")
    print(f"   Versión: {platform.release()}")
    print(f"   Directorio actual: {os.getcwd()}\n")


def main():
    """Función principal."""
    print_banner()
    print_info()
    
    # Paso 1: Verificar que estemos en el directorio correcto
    if not os.path.exists('manage.py'):
        print("❌ ERROR: No se encontró manage.py")
        print("Por favor, ejecuta este script desde la raíz del proyecto.")
        sys.exit(1)
    
    print("✅ manage.py encontrado - Estamos en el directorio correcto\n")
    
    # Paso 2: Crear migraciones
    success = run_command(
        'python manage.py makemigrations',
        'Crear migraciones (makemigrations)'
    )
    if not success:
        print("⚠️ Advertencia: makemigrations pudo haber fallado")
    
    # Paso 3: Aplicar migraciones
    success = run_command(
        'python manage.py migrate',
        'Aplicar migraciones (migrate)'
    )
    if not success:
        print("❌ ERROR: Falló la aplicación de migraciones")
        print("Verifica que MySQL esté corriendo y la base de datos rh_db exista.")
        sys.exit(1)
    
    # Paso 4: Crear superusuario
    print(f"\n{'='*60}")
    print("Crear superusuario (administrador)")
    print(f"{'='*60}")
    print("\nNota: Puedes saltarte este paso presionando Ctrl+C")
    print("      o crearlo después con: python manage.py createsuperuser\n")
    
    try:
        os.system('python manage.py createsuperuser')
    except KeyboardInterrupt:
        print("\n⏭️ Salto de creación de superusuario")
    
    # Paso 5: Mostrar resumen final
    print(f"\n{'='*60}")
    print("✅ INICIALIZACIÓN COMPLETADA")
    print(f"{'='*60}\n")
    
    print("📋 Próximos pasos:")
    print("\n1. Inicia el servidor de desarrollo:")
    print("   python manage.py runserver 8080")
    print("\n2. La API estará disponible en:")
    print("   http://localhost:8080/api/empleados/")
    print("\n3. Panel de administración:")
    print("   http://localhost:8080/admin/")
    print("\n4. Abre Postman e importa: PostmanCollection.json")
    print("\n5. Ejecuta las pruebas CRUD")
    print(f"\n{'='*60}\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Script interrumpido por el usuario")
        sys.exit(0)
