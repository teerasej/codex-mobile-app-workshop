<template>
  <footer class="course-credits" aria-label="Copyright and contact">
    <span>© 2026 Teerasej Jiraphatchandej. All rights reserved.</span>
    <nav aria-label="Contact links">
      <a href="mailto:teerasej@nextflow.in.th">Email me</a>
      <a href="https://www.facebook.com/teerasej">Facebook</a>
      <a href="https://www.youtube.com/teerasej">YouTube</a>
    </nav>
  </footer>
</template>

<style scoped>
.course-credits { padding: 24px; border-top: 1px solid var(--vp-c-divider); color: var(--vp-c-text-2); font-size: 13px; line-height: 1.9; text-align: center; }
.course-credits nav { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 20px; margin-top: 6px; }
.course-credits a { text-decoration: underline; text-underline-offset: 3px; }
.course-credits a:hover { color: var(--vp-c-brand-1); }
.course-credits a:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 4px; }
</style>
