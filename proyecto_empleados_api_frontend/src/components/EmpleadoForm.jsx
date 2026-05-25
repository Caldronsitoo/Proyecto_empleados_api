import React, { useState, useEffect } from 'react';
import '../styles/Form.css';

export default function EmpleadoForm({ empleado, onGuardar, onCancelar }) {
  const [formData, setFormData] = useState({
    nombre: '',
    departamento: '',
    sueldo: '',
  });

  const [errores, setErrores] = useState({});

  useEffect(() => {
    if (empleado) {
      setFormData({
        nombre: empleado.nombre,
        departamento: empleado.departamento,
        sueldo: empleado.sueldo,
      });
    } else {
      setFormData({
        nombre: '',
        departamento: '',
        sueldo: '',
      });
    }
  }, [empleado]);

  const validar = () => {
    const nuevosErrores = {};

    if (!formData.nombre.trim()) {
      nuevosErrores.nombre = 'El nombre es requerido';
    }

    if (!formData.departamento.trim()) {
      nuevosErrores.departamento = 'El departamento es requerido';
    }

    if (!formData.sueldo || parseFloat(formData.sueldo) <= 0) {
      nuevosErrores.sueldo = 'El sueldo debe ser mayor a 0';
    }

    setErrores(nuevosErrores);
    return Object.keys(nuevosErrores).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Limpiar error del campo cuando el usuario empieza a escribir
    if (errores[name]) {
      setErrores(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validar()) {
      onGuardar({
        nombre: formData.nombre,
        departamento: formData.departamento,
        sueldo: parseFloat(formData.sueldo),
      });
    }
  };

  return (
    <div className="form-container">
      <div className="form-card">
        <h2>{empleado ? '✏️ Editar Empleado' : '➕ Nuevo Empleado'}</h2>
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="nombre">Nombre</label>
            <input
              type="text"
              id="nombre"
              name="nombre"
              value={formData.nombre}
              onChange={handleChange}
              placeholder="Ej: Juan Pérez García"
              className={errores.nombre ? 'input-error' : ''}
            />
            {errores.nombre && <span className="error-text">{errores.nombre}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="departamento">Departamento</label>
            <select
              id="departamento"
              name="departamento"
              value={formData.departamento}
              onChange={handleChange}
              className={errores.departamento ? 'input-error' : ''}
            >
              <option value="">-- Selecciona un departamento --</option>
              <option value="Ventas">Ventas</option>
              <option value="Recursos Humanos">Recursos Humanos</option>
              <option value="Tecnología">Tecnología</option>
              <option value="Finanzas">Finanzas</option>
              <option value="Operaciones">Operaciones</option>
              <option value="Logística">Logística</option>
              <option value="Marketing">Marketing</option>
              <option value="Administración">Administración</option>
            </select>
            {errores.departamento && <span className="error-text">{errores.departamento}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="sueldo">Sueldo (COP)</label>
            <input
              type="number"
              id="sueldo"
              name="sueldo"
              value={formData.sueldo}
              onChange={handleChange}
              placeholder="Ej: 3500000.00"
              step="0.01"
              min="0"
              className={errores.sueldo ? 'input-error' : ''}
            />
            {errores.sueldo && <span className="error-text">{errores.sueldo}</span>}
          </div>

          <div className="form-actions">
            <button type="submit" className="btn btn-success">
              {empleado ? '💾 Actualizar' : '✅ Crear'}
            </button>
            <button type="button" onClick={onCancelar} className="btn btn-secondary">
              ❌ Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
