"use client"

import React, { useState } from 'react';
import { rollDadoNumerico } from '../api'; // Importa la función de la API

const DadoRoleroBoton = () => {
  const [caras, setCaras] = useState(6); // Por defecto un d6
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState(null);
  const [tiradaId, setTiradaId] = useState(null);

  const handleRoll = async () => {
    setError(null);
    setResultado(null);
    setTiradaId(null);
    try {
      const data = await rollDadoNumerico(caras);
      setResultado(data.resultado);
      setTiradaId(data.tirada_id);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="card p-4 flex flex-col items-center space-y-3">
      <h3 className="text-xl font-bold text-dark-gothic-text">Tirada de Dado Numérico</h3>
      <input
        type="number"
        value={caras}
        onChange={(e) => setCaras(Math.max(1, parseInt(e.target.value) || 1))}
        className="input-field w-24 text-center"
        min="1"
        aria-label="Número de caras del dado"
      />
      <button onClick={handleRoll} className="btn-primary">
        Tirar 1D{caras}
      </button>
      {resultado !== null && (
        <div className="text-lg text-dark-gothic-accent font-semibold">
          Resultado: {resultado}
        </div>
      )}
      {tiradaId && (
        <p className="text-sm text-gray-400">ID de Tirada: {tiradaId.substring(0, 8)}...</p>
      )}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default DadoRoleroBoton;
