/** @type {import('tailwindcss').Config} */
export default {
  // 确保这里包含了你的所有文件路径
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // 背景色：比纯黑更有质感的深蓝灰
        'cyber-black': '#0f172a',
        'cyber-gray': '#1e293b',
        // 强调色：赛博朋克风格
        'neon-blue': '#00f3ff',
        'neon-purple': '#bc13fe',
        // 辅助色
        'text-main': '#e2e8f0',
        'text-muted': '#94a3b8',
      },
      fontFamily: {
        // 以后代码块用 mono 字体
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
