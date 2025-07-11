"use client"

import React, { useState } from 'react';
import { rollTiradaMultiple } from '../api';

const TiradaMultipleBoton = () => {
  const [dadosCount, setDadosCount] = useState(2);
  const [carasInput, setCarasInput] = useState('6,6'); // Ejemplo: 2 dados de 6 caras
  const [dificultad, setDificultad] = useState(0);
  const [bonus, setBonus] = useState(0);
  const [modoDificultad, setModoDificultad] = useState(true); // true para éxito, false para fallo
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState(null);
  const [tiradaId, setTiradaId] = useState(null);

  const handleRoll = async () => {
    setError(null);
    setResultado(null);
    setTiradaId(null);
    try {
      const carasArray = carasInput.split(',').map(Number).filter(n => !isNaN(n) && n > 0);
      
      if (carasArray.length !== dadosCount) {
        setError("La lista de caras debe coincidir con la cantidad de dados.");
        return;
      }

      const inputData = {
        dados: dadosCount,
        caras: carasArray,
        dificultad: dificultad,
        bonus: bonus,
        modoDificultad: modoDificultad,
      };
      const data = await rollTiradaMultiple(inputData);
      setResultado(data.resultado);
      setTiradaId(data.tirada_id);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="card p-4 flex flex-col items-center space-y-3">
      <h3 className="text-xl font-bold text-dark-gothic-text">Tirada Múltiple</h3>
      <div className="flex flex-col space-y-2 w-full">
        <label className="text-dark-gothic-text">
          Cantidad de Dados:
          <input
            type="number"
            value={dadosCount}
            onChange={(e) => setDadosCount(Math.max(1, parseInt(e.target.value) || 1))}
            className="input-field ml-2 w-20"
            min="1"
          />
        </label>
        <label className="text-dark-gothic-text">
          Caras por Dado (ej: 6,6,10):
          <input
            type="text"
            value={carasInput}
            onChange={(e) => setCarasInput(e.target.value)}
            className="input-field ml-2"
            placeholder="ej: 6,6,10"
          />
        </label>
        <label className="text-dark-gothic-text">
          Dificultad:
          <input
            type="number"
            value={dificultad}
            onChange={(e) => setDificultad(parseInt(e.target.value) || 0)}
            className="input-field ml-2 w-20"
          />
        </label>
        <label className="text-dark-gothic-text">
          Bonus:
          <input
            type="number"
            value={bonus}
            onChange={(e) => setBonus(parseInt(e.target.value) || 0)}
            className="input-field ml-2 w-20"
          />
        </label>
        <label className="text-dark-gothic-text flex items-center">
          Modo Dificultad (Éxito/Fallo):
          <input
            type="checkbox"
            checked={modoDificultad}
            onChange={(e) => setModoDificultad(e.target.checked)}
            className="ml-2 h-4 w-4 text-dark-gothic-accent rounded"
          />
        </label>
      </div>
      <button onClick={handleRoll} className="btn-primary w-full">
        Tirar Dados Múltiples
      </button>
      {resultado !== null && (
        <div className="text-lg text-dark-gothic-accent font-semibold text-center">
          <pre>{JSON.stringify(resultado, null, 2)}</pre>
        </div>
      )}
      {tiradaId && (
        <p className="text-sm text-gray-400">ID de Tirada: {tiradaId.substring(0, 8)}...</p>
      )}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default TiradaMultipleBoton;
