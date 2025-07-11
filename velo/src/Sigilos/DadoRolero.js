"use client"

import { useState } from 'react'

export default function DadoRolero() {
  const [resultado, setResultado] = useState(null)

  const tirarDado = () => {
    setResultado(10)  // Resultado fijo
  }

  return (
    <div className="p-4 bg-gray-800 rounded shadow text-white text-center">
      <h2 className="text-xl mb-4 font-bold">Tirada de prueba</h2>
      <button
        onClick={tirarDado}
        className="bg-indigo-600 hover:bg-indigo-500 px-4 py-2 rounded"
      >
        Tirar d10
      </button>
      {resultado !== null && (
        <p className="mt-4 text-lg">
          Resultado: <span className="font-bold">{resultado}</span>
        </p>
      )}
    </div>
  )
}