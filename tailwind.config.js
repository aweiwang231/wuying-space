/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'warm-black': '#141210',
        'warm-dark': '#1c1916',
        'warm-gray': '#262220',
        'warm-card': '#2e2a26',
        'warm-border': '#3d352c',
        accent: '#d4a04a',
        'accent-light': '#e8b86a',
        'accent-dim': '#b8862e',
        'text-main': '#e8dcc8',
        'text-muted': '#9a8b78',
        'text-soft': '#bfb098',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
