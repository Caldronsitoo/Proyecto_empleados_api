import React from 'react';
import '../styles/Table.css';

export default function EmpleadoList({ empleados, onEditar, onEliminar }) {
  return (
    <div className="table-container">
      <table className="empleados-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Departamento</th>
            <th>Sueldo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {empleados.map((empleado) => (
            <tr key={empleado.idEmpleado}>
              <td className="id-cell">#{empleado.idEmpleado}</td>
              <td className="nombre-cell">{empleado.nombre}</td>
              <td className="departamento-cell">
                <span className="dept-badge">{empleado.departamento}</span>
              </td>
              <td className="sueldo-cell">
                COP {parseFloat(empleado.sueldo).toLocaleString('es-CO', {
                  minimumFractionDigits: 2,
                  maximumFractionDigits: 2,
                })}
              </td>
              <td className="acciones-cell">
                <button
                  onClick={() => onEditar(empleado.idEmpleado)}
                  className="btn btn-edit"
                  title="Editar empleado"
                >
                  ✏️ Editar
                </button>
                <button
                  onClick={() => onEliminar(empleado.idEmpleado)}
                  className="btn btn-delete"
                  title="Eliminar empleado"
                >
                  🗑️ Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
