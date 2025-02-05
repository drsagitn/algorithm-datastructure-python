/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    colors: {
      primary: '#D73800',
      black: '#181818',
      white: '#ffffff',
      orange: '#FFB499',
      gray: '#363636',
      lightOrange: '#FFDDD1',
      green: '#84E686',
    },
    extend: {
      keyframes: {
        zoomIn: {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.3)' },
          '100%': { transform: 'scale(1)' },
        },
        zoomOut: {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(0.8)' },
          '100%': { transform: 'scale(1)' },
        },
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        slideInUp: {
          '0%': { transform: 'translateY(100px)', opacity: 0 },
          '100%': { transform: 'translateY(0)', opacity: 1 },
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-100px)', opacity: 0 },
          '100%': { transform: 'translateX(0)', opacity: 1 },
        },
        slideInRight: {
          '0%': { transform: 'translateX(100px)', opacity: 0 },
          '100%': { transform: 'translateX(0)', opacity: 1 },
        },
        spin: {
          to: { transform: 'rotate(360deg)' },
        },
      },
      animation: {
        zoomIn: 'zoomIn 15s ease-in-out infinite',
        zoomOut: 'zoomOut 15s ease-in-out infinite',
        fadeIn: 'fadeIn 1s ease-out',
        slideInUp: 'slideInUp 1s ease-out',
        slideInLeft: 'slideInLeft 1s ease-out',
        slideInRight: 'slideInRight 1s ease-out',
        spin: 'spin 15s linear infinite',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
