
"use client"
import { useEffect } from "react"
import { useRouter } from "next/navigation"

export default function Home() {
  const router = useRouter()

  useEffect(() => {
    const usuario = localStorage.getItem("Usuario")
    if (usuario) {
      router.push("/dashboard")
    }
  }, [])

  function simularLogin() {
    localStorage.setItem("usuario", JSON.stringify({ nombre: "Nephelim" }))
    router.push("/dashboard")
  }

  return (
    <>
    <main className="min-h-screen flex items-center justify-center">
      <div className="text-center space-y-4">
        <h1 className="text-3xl font-bold">Bienvenido a RitualRoll</h1>
        <p>Por favor, inicia sesión para continuar</p>
        <button
          onClick={simularLogin}
          className="bg-indigo-600 text-white px-4 py-2 rounded"
        >
          Ingresar (simulado)
        </button>
      </div>
    </main>
    <footer className="w-full text-center py-4 text-sm text-gray-400">
          RitualRoll © {new Date().getFullYear()}
          Nicolas Salvatore © Licencia MIT
    </footer>
    </>
  )
}

