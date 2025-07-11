// Funciones para interactuar con el backend de FastAPI

const BASE_URL = 'http://127.0.0.1:8000';

// --- Funciones para la API de Cripta (Usuarios) ---

/**
 * Registra un nuevo usuario.
 * @param {object} userData - Datos del usuario para registro (email, password, username, etc.)
 * @returns {Promise<object>} - Datos del usuario registrado
 */
export const registerUser = async (userData) => {
  try {
    const response = await fetch(`${BASE_URL}/cripta/registro`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al registrar usuario.');
    }
    return data;
  } catch (error) {
    console.error('Error en registerUser:', error);
    throw error;
  }
};

/**
 * Inicia sesión de un usuario.
 * @param {object} credentials - Credenciales del usuario (email, password)
 * @returns {Promise<object>} - Datos del usuario autenticado
 */
export const loginUser = async (credentials) => {
  try {
    const response = await fetch(`${BASE_URL}/cripta/inicio`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al iniciar sesión.');
    }
    return data;
  } catch (error) {
    console.error('Error en loginUser:', error);
    throw error;
  }
};

/**
 * Actualiza los datos de un usuario.
 * @param {string} userId - ID del usuario a actualizar.
 * @param {object} updateData - Datos a actualizar (username, password, bio, etc.)
 * @returns {Promise<object>} - Datos del usuario actualizados
 */
export const updateUser = async (userId, updateData) => {
  try {
    const response = await fetch(`${BASE_URL}/cripta/${userId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updateData),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al actualizar usuario.');
    }
    return data;
  } catch (error) {
    console.error('Error en updateUser:', error);
    throw error;
  }
};

/**
 * Elimina un usuario.
 * @param {string} userId - ID del usuario a eliminar.
 * @returns {Promise<void>}
 */
export const deleteUser = async (userId) => {
  try {
    const response = await fetch(`${BASE_URL}/cripta/${userId}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Error al eliminar usuario.');
    }
  } catch (error) {
    console.error('Error en deleteUser:', error);
    throw error;
  }
};

// --- Funciones para la API de RitualAPI (Dados) ---

/**
 * Realiza una tirada de dado numérico.
 * @param {number} caras - Número de caras del dado.
 * @returns {Promise<object>} - Resultado de la tirada.
 */
export const rollDadoNumerico = async (caras) => {
  try {
    const response = await fetch(`${BASE_URL}/RitualRoll/dadoNumerico/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ caras }),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al tirar dado numérico.');
    }
    return data;
  } catch (error) {
    console.error('Error en rollDadoNumerico:', error);
    throw error;
  }
};

/**
 * Realiza una tirada múltiple.
 * @param {object} input - Objeto con dados, caras, dificultad, bonus, modoDificultad.
 * @returns {Promise<object>} - Resultado de la tirada múltiple.
 */
export const rollTiradaMultiple = async (input) => {
  try {
    const response = await fetch(`${BASE_URL}/RitualRoll/tiradaMultiple/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(input),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al realizar tirada múltiple.');
    }
    return data;
  } catch (error) {
    console.error('Error en rollTiradaMultiple:', error);
    throw error;
  }
};

/**
 * Realiza una tirada de CWoD 20.
 * @param {object} input - Objeto con dados y dificultad.
 * @returns {Promise<object>} - Resultado de la tirada CWoD 20.
 */
export const rollCWoD20 = async (input) => {
  try {
    const response = await fetch(`${BASE_URL}/RitualRoll/CWoD20/tirada/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(input),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al realizar tirada CWoD 20.');
    }
    return data;
  } catch (error) {
    console.error('Error en rollCWoD20:', error);
    throw error;
  }
};

/**
 * Aplica la regla del 10 a una tirada CWoD 20 guardada.
 * @param {string} tiradaId - ID de la tirada a la que aplicar la regla.
 * @returns {Promise<object>} - Resultado actualizado de la tirada.
 */
export const applyReglaDelDiez = async (tiradaId) => {
  try {
    const response = await fetch(`${BASE_URL}/RitualRoll/CWoD20/tirada/regla10/${tiradaId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'Error al aplicar la Regla del 10.');
    }
    return data;
  } catch (error) {
    console.error('Error en applyReglaDelDiez:', error);
    throw error;
  }
};
