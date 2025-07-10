
import Header from "../componentes/Header";
import DadoRolero from '../componentes/DadoRolero'

export default function Home() {
  return (
    <>
      <Header />
      <main className="p-8 flex flex-col items-center gap-8">
        <h1 className="text-4xl font-bold">¡Bienvenido a RitualRoll!</h1>
        {/* Aquí puedes seguir colocando más componentes */}
        <DadoRolero />
      </main>
      <footer className="w-full text-center py-4 text-sm text-gray-400">
        RitualRoll © {new Date().getFullYear()}
        Nicolas Salvatore © Licencia MIT
      </footer>
    </>
  );
}
