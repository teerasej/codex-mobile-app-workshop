<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <div class="markdown-preview" aria-label="ตัวอย่าง README หลังแสดงผล Markdown">
    <h4>Workshop notes</h4>
    <p><strong>Service Desk Lite</strong> คือโปรเจคฝึกของเรา</p>
    <h5>สิ่งที่เราจะฝึก</h5>
    <ul>
      <li>อ่าน <code>README.md</code></li>
      <li>ตรวจรูปแบบเอกสาร</li>
    </ul>
    <h5>ลำดับการทำงาน</h5>
    <ol>
      <li>แก้เอกสาร</li>
      <li>ตรวจผลก่อน commit</li>
    </ol>
    <p><a :href="withBase('/files/project-brief.md')">Project brief</a></p>
    <pre><code>git status</code></pre>
  </div>
</template>

<style scoped>
.markdown-preview { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 20px; overflow-wrap: anywhere; }
.markdown-preview h4 { margin: 0 0 16px; font-size: 23px; }
.markdown-preview h5 { margin: 20px 0 8px; font-size: 18px; font-weight: 600; }
.markdown-preview pre { margin-top: 16px; padding: 12px; background: var(--vp-code-block-bg); border-radius: 6px; }
</style>
