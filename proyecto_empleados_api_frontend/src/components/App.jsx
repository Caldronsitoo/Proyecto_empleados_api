import React, { useState, useEffect } from 'react';
import { empleadosAPI } from '../services/api';
import EmpleadoForm from './EmpleadoForm';
import EmpleadoList from './EmpleadoList';
import '../styles/App.css';

export default function App() {
  const [empleados, setEmpleados] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [editingId, setEditingId] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  // Cargar empleados al montar el componente
  useEffect(() => {
    cargarEmpleados();
  }, []);

  const cargarEmpleados = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await empleadosAPI.getAll();
      setEmpleados(Array.isArray(data) ? data : []);
    } catch (err) {
      setError('Error al cargar empleados: ' + err.message);
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleGuardar = async (formData) => {
    try {
      if (editingId) {
        // Actualizar
        const empleadoActualizado = await empleadosAPI.update(editingId, formData);
        setEmpleados(empleados.map(emp => emp.idEmpleado === editingId ? empleadoActualizado : emp));
        setEditingId(null);
      } else {
        // Crear
        const nuevoEmpleado = await empleadosAPI.create(formData);
        setEmpleados([...empleados, nuevoEmpleado]);
      }
      setShowForm(false);
      setError(null);
    } catch (err) {
      setError('Error al guardar empleado: ' + err.message);
    }
  };

  const handleEditar = (id) => {
    setEditingId(id);
    setShowForm(true);
  };

  const handleEliminar = async (id) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este empleado?')) {
      try {
        await empleadosAPI.delete(id);
        setEmpleados(empleados.filter(emp => emp.idEmpleado !== id));
        setError(null);
      } catch (err) {
        setError('Error al eliminar empleado: ' + err.message);
      }
    }
  };

  const handleCancelar = () => {
    setShowForm(false);
    setEditingId(null);
  };

  const empleadoSeleccionado = editingId ? empleados.find(emp => emp.idEmpleado === editingId) : null;

  const empleadosFiltrados = empleados.filter(emp =>
    emp.nombre.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.departamento.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🏢 Gestión de Empleados</h1>
        <p className="subtitle">Sistema de Recursos Humanos</p>
      </header>

      <main className="app-main">
        {error && <div className="alert alert-error">{error}</div>}

        <div className="controls">
          <div className="search-box">
            <input
              type="text"
              placeholder="🔍 Buscar por nombre o departamento..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
          </div>
          <button
            onClick={() => setShowForm(!showForm)}
            className="btn btn-primary"
          >
            {showForm ? '❌ Cancelar' : '➕ Nuevo Empleado'}
          </button>
        </div>

        {showForm && (
          <EmpleadoForm
            empleado={empleadoSeleccionado}
            onGuardar={handleGuardar}
            onCancelar={handleCancelar}
          />
        )}

        {loading && <div className="loading">⏳ Cargando empleados...</div>}

        {!loading && empleadosFiltrados.length === 0 ? (
          <div className="empty-state">
            <p>📭 No hay empleados para mostrar</p>
          </div>
        ) : (
          <EmpleadoList
            empleados={empleadosFiltrados}
            onEditar={handleEditar}
            onEliminar={handleEliminar}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>© 2026 Sistema de Recursos Humanos | Total de empleados: {empleados.length}</p>
      </footer>
    </div>
  );
}
