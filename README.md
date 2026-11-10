# Nextflow · Service Desk Lite

Thai-first participant website for a connected four-day Codex mobile application workshop. One fictional service-request project grows through Git, FastAPI/PostgreSQL, Flutter and Azure Container Apps.

## Read and maintain

- Website: https://teerasej.github.io/codex-mobile-app-workshop/
- Canonical learner source: `docs/`; exercises, day overviews and daily summaries live under `docs/exercises/`.
- Approved downloadable files: `docs/public/files/`. Keep downloadable templates aligned with the starter ZIP.
- All 40 core Practices and the optional iOS Simulator Practice have a distinct illustration below their heading (41 illustrations). Reviewed WebP copies live in `docs/public/images/practices/`; the theme's `practice-images.json` contains only public URLs, dimensions and Thai alternative text.
- Use the shared `PracticeIllustration` component with a stable practice asset ID. Preserve the complete scene and aspect ratio when exporting replacement sizes. Keep original artwork, generation prompts and review records outside this repository.
- This repository contains participant material only. Instructor notes, source PDFs, credentials and rehearsal records belong outside this repository.

## Local preview

Use Node.js 24 and npm. Run `npm ci` once, then `npm start` (or `npm run docs:dev`) while editing. Open http://127.0.0.1:4173/codex-mobile-app-workshop/. Keep the server running: saving Markdown, theme components, or styles under `docs/` updates the browser automatically. Port 4173 is fixed so the review link stays the same; stop an existing preview before starting this server.

For a production check, run `npm run check:content`, `npm run docs:build`, then `npm run docs:preview -- --host 127.0.0.1 --port 4173`. Production preview serves the last build and does not update on save. The project base path is `/codex-mobile-app-workshop/`.

## Publication

The Pages workflow publishes only `docs/.vitepress/dist` from `main`. The repository uses GitHub Actions as its Pages source. A local build is not a public deployment; verify the completed deployment and actual routes/downloads before sharing the live URL.

## Learning evidence

The website packages authored instructions and synthetic samples. It does not establish account entitlement, Windows/Android or iOS Simulator execution, database access, Azure roles or full classroom rehearsal. Record these separately before teaching. The iOS Simulator extension in Day 3 Exercise 4 is optional for a prepared Mac; Android remains the core mobile checkpoint.
