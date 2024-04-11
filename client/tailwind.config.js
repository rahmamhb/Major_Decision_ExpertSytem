/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  mode: "jit",
  theme: {
    extend: {
      colors: {
        primaryBlue: "#9DC0C4",
        primaryGreen: "#C6C491",
        primaryPink: "#DAB2DF",
        primaryPurple: "#6B7594",
        secondaryPurple: "#DBCABF",
      },
      backgroundImage: {
        "landing-pattern": "url('/src/assets/1Bg.png')",
        "result-pattern": "url('/src/assets/lastBg.png')",
        "back-pattern": "url('/src/assets/bigBg.png')",
      },
    },
  },
  plugins: [],
}

