"use client"
import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"

export default function Dashboard() {
  const router = useRouter()
  const [usuario, setUsuario] = useState(null)

  useEffect(() => {
    const u = localStorage.getItem("usuario")
    if (!u) {
      router.push("/")
    } else {
      setUsuario(JSON.parse(u))
    }
  }, [])

  function entrarPartida(id) {
    router.push(`/partida/${id}`)
  }

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">
        Hola, {usuario?.nombre || "..."}. Tus partidas:
      </h1>

      <div className="space-y-4">
        {/* Simulamos dos partidas */}
        <button
          onClick={() => entrarPartida("sabbat-13")}
          className="bg-gray-800 text-white px-4 py-2 rounded"
        >
          Sabbat 13
        </button>
        <button
          onClick={() => entrarPartida("traditioneclipse")}
          className="bg-gray-800 text-white px-4 py-2 rounded"
        >
          Tradition Eclipse
        </button>
      </div>
    </main>
  )
}