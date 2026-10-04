/// <reference types="vitest/config" />
import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { readdirSync, rmSync, statSync } from 'node:fs'
import { join } from 'node:path'

/**
 * public/lessons also holds WAV masters and markdown previews that the app never loads.
 * They are removed from dist so a GitHub Pages deploy stays far below the 1 GB limit.
 */
function stripLessonMasters(): Plugin {
  const unwanted = /\.(wav|md)$/i
  let outDir = 'dist'
  return {
    name: 'strip-lesson-masters',
    apply: 'build',
    configResolved(config) {
      outDir = config.build.outDir
    },
    closeBundle() {
      const walk = (dir: string) => {
        for (const name of readdirSync(dir)) {
          const path = join(dir, name)
          if (statSync(path).isDirectory()) walk(path)
          else if (unwanted.test(name)) rmSync(path)
        }
      }
      try {
        walk(join(outDir, 'lessons'))
      } catch {
        // no lessons folder in this build
      }
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  // GitHub Pages serves the site from /<repo>/; the deploy workflow sets VITE_BASE.
  base: process.env.VITE_BASE ?? '/',
  plugins: [react(), tailwindcss(), stripLessonMasters()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test-setup.ts',
  },
})
