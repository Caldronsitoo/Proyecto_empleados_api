import axios from 'axios';

const API_URL = 'http://localhost:8000/api/empleados/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

const parseResponseData = (response) => {
  if (response?.data?.datos !== undefined) {
    return response.data.datos;
  }
  return response?.data;
};

export const empleadosAPI = {
  // Obtener todos los empleados
  getAll: async () => {
    try {
      const response = await api.get('');
      return parseResponseData(response);
    } catch (error) {
      console.error('Error al obtener empleados:', error);
      throw error;
    }
  },

  // Obtener un empleado por ID
  getById: async (id) => {
    try {
      const response = await api.get(`${id}/`);
      return parseResponseData(response);
    } catch (error) {
      console.error('Error al obtener empleado:', error);
      throw error;
    }
  },

  // Crear un nuevo empleado
  create: async (datos) => {
    try {
      const response = await api.post('', datos);
      return parseResponseData(response);
    } catch (error) {
      console.error('Error al crear empleado:', error);
      throw error;
    }
  },

  // Actualizar un empleado
  update: async (id, datos) => {
    try {
      const response = await api.put(`${id}/`, datos);
      return parseResponseData(response);
    } catch (error) {
      console.error('Error al actualizar empleado:', error);
      throw error;
    }
  },

  // Eliminar un empleado
  delete: async (id) => {
    try {
      const response = await api.delete(`${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al eliminar empleado:', error);
      throw error;
    }
  },
};

export default api;
