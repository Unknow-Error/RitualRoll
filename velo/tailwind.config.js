// tailwind.config.js
// Configuración opcional de Tailwind CSS para personalizaciones avanzadas

/** @type {import('tailwindcss').Config} */
module.exports = {
  // La sección 'content' es crucial. Le dice a Tailwind dónde buscar
  // las clases de utilidad para generar el CSS final.
  // Asegúrate de incluir todas las rutas donde usas clases de Tailwind.
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}', // Para el Pages Router de Next.js
    './components/**/*.{js,ts,jsx,tsx,mdx}', // Para componentes compartidos
    './app/**/*.{js,ts,jsx,tsx,mdx}',     // Para el App Router de Next.js
    // Puedes añadir más rutas si tienes archivos con clases de Tailwind
    // en otros directorios, por ejemplo: './src/**/*.{js,ts,jsx,tsx,mdx}'
  ],
  // La sección 'theme' es donde extiendes o sobrescribes el tema por defecto de Tailwind.
  // Por ejemplo, puedes añadir colores, tamaños de fuente, espaciado, etc.
  theme: {
    extend: {
      // Aquí puedes añadir tus personalizaciones, por ejemplo:
      // colors: {
      //   'custom-blue': '#3490dc',
      // },
      // spacing: {
      //   '128': '32rem',
      // },
    },
  },
  // La sección 'plugins' es para añadir plugins de Tailwind CSS.
  // Por ejemplo, @tailwindcss/typography, @tailwindcss/forms, etc.
  plugins: [],
};
