"use client"

import React, { useState } from 'react';
import { rollCWoD20, applyReglaDelDiez } from '../api';

const TiradaWodBoton = () => {
  const [dados, setDados] = useState(1);
  const [dificultad, setDificultad] = useState(6);
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState(null);
  const [tiradaId, setTiradaId] = useState(null);
  const [regla10Applied, setRegla10Applied] = useState(false);

  const handleRoll = async () => {
    setError(null);
    setResultado(null);
    setTiradaId(null);
    setRegla10Applied(false);
    try {
      const data = await rollCWoD20({ dados, dificultad });
      setResultado(data.resultado);
      setTiradaId(data.tirada_id);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleRegla10 = async () => {
    setError(null);
    if (!tiradaId) {
      setError("Primero debes realizar una tirada.");
      return;
    }
    try {
      const data = await applyReglaDelDiez(tiradaId);
      setResultado(data.resultado_actualizado);
      setRegla10Applied(true);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="card p-4 flex flex-col items-center space-y-3">
      <h3 className="text-xl font-bold text-dark-gothic-text">Tirada CWoD 20</h3>
      <div className="flex flex-col space-y-2 w-full">
        <label className="text-dark-gothic-text">
          Cantidad de Dados:
          <input
            type="number"
            value={dados}
            onChange={(e) => setDados(Math.max(1, parseInt(e.target.value) || 1))}
            className="input-field ml-2 w-20"
            min="1"
          />
        </label>
        <label className="text-dark-gothic-text">
          Dificultad:
          <input
            type="number"
            value={dificultad}
            onChange={(e) => setDificultad(Math.max(1, parseInt(e.target.value) || 1))}
            className="input-field ml-2 w-20"
            min="1"
          />
        </label>
      </div>
      <button onClick={handleRoll} className="btn-primary w-full">
        Tirar {dados}D10 (Dif. {dificultad})
      </button>
      {tiradaId && resultado !== null && (
        <div className="w-full text-center">
          <div className="text-lg text-dark-gothic-accent font-semibold">
            Resultado: {JSON.stringify(resultado)}
          </div>
          {!regla10Applied && (
            <button onClick={handleRegla10} className="btn-primary mt-2 text-sm">
              Aplicar Regla del 10
            </button>
          )}
        </div>
      )}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default TiradaWodBoton;
