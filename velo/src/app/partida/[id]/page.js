"use client"
import { useParams } from "next/navigation"
import { useEffect, useState } from "react"

export default function PartidaPage() {
  const { id } = useParams()
  const [usuario, setUsuario] = useState(null)

  useEffect(() => {
    const u = localStorage.getItem("usuario")
    if (!u) window.location.href = "/"
    else setUsuario(JSON.parse(u))
  }, [])

  return (
    <main className="p-6">
      <h1 className="text-3xl font-bold mb-4">Partida: {id}</h1>
      <p>Bienvenido {usuario?.nombre || "..."}</p>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-8">
        <div className="p-4 border rounded">📜 Fichas de personaje (próximamente)</div>
        <div className="p-4 border rounded">💬 Chat (próximamente)</div>
        <div className="p-4 border rounded">🎲 Tiradas (próximamente)</div>
      </div>
    </main>
  )
}
