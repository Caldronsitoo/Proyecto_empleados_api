-- Script de datos de prueba para la tabla empleado
-- Ejecuta esto después de crear la tabla

USE rh_db;

-- Insertar empleados de ejemplo
INSERT INTO empleado (nombre, departamento, sueldo) VALUES
('Juan Pérez', 'Tecnología', 3500.00),
('María García', 'Recursos Humanos', 3200.00),
('Carlos López', 'Ventas', 2800.00),
('Ana Martínez', 'Marketing', 3000.00),
('Roberto Rodríguez', 'Finanzas', 3800.00),
('Laura Sánchez', 'Tecnología', 4000.00),
('Miguel Fernández', 'Operaciones', 2900.00),
('Patricia Gómez', 'Dirección', 5000.00);

-- Verificar datos insertados
SELECT * FROM empleado;

-- Ver cantidad de empleados
SELECT COUNT(*) as total_empleados FROM empleado;

-- Ver empleados agrupados por departamento
SELECT departamento, COUNT(*) as cantidad, AVG(sueldo) as sueldo_promedio 
FROM empleado 
GROUP BY departamento;
