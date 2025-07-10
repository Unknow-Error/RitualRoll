// postcss.config.js
// Configuración de PostCSS para Tailwind CSS y Autoprefixer

module.exports = {
  plugins: {
    // El plugin de Tailwind CSS para PostCSS
    // Asegúrate de que '@tailwindcss/postcss' esté instalado
    '@tailwindcss/postcss': {},
    // Autoprefixer añade prefijos de proveedor a las propiedades CSS
    // para compatibilidad con diferentes navegadores
    autoprefixer: {},
  },
};
