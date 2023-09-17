/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./core/templates/**/*.html",
    "./core/static/**/*.js",
    "./puddle/**/*.html", // Agrega cualquier otra ubicación de tus archivos HTML
    "./puddle/static/**/*.js", // Agrega cualquier otra ubicación de tus archivos JS

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

