-- Script para crear la base de datos y tabla de empleados
-- Base de datos: rh_db
-- Usuario: root
-- Contraseña: (vacía)

CREATE DATABASE IF NOT EXISTS rh_db;
USE rh_db;

CREATE TABLE empleado (
    idEmpleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL CHECK (sueldo > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla creada exitosamente
