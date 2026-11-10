---
title: "Day 1 — วาง Instructionก่อนสร้าง: ทำงานกับ AI อย่างตรวจสอบได้"
prev: {"text": "ก่อนวันแรก", "link": "/resources/readiness"}
next: {"text": "Exercise 1", "link": "/exercises/day-01-git/exercise-01"}
---

<script setup>
import { withBase } from 'vitepress'

const slidesFilename = 'Service-Desk-Lite-Day-01-English-Markdown-v2.pdf'
</script>

# Day 1 — วาง Instruction ก่อนสร้าง: ทำงานกับ AI อย่างตรวจสอบได้

<p>
  <a class="day-one-slides-download" :href="withBase('/files/' + slidesFilename)" :download="slidesFilename">
    Download Day 1 slides (PDF)
  </a>
</p>

[กลับสารบัญ](/) · [วันถัดไป: Python API](/exercises/day-02-api/)

## Overview theme

วันนี้เราเป็นทีมที่กำลังเริ่มต้นการสร้าง Service Desk Lite. ก่อนสร้างหน้าจอหรือแอพใช้งาน เราจะฝึกเก็บประวัติการทำงานของไฟล์ แยกพื้นที่ทดลอง ตรวจการเปลี่ยนแปลง และรวมงานที่แตกต่างกันด้วย Git ซึ่งเหมือนสมุดบันทึกสูตรอาหาร: เรารู้ว่าสูตรไหนเปลี่ยนอะไรและย้อนดูโน๊ตที่เขียนไว้ได้ โดยไม่ต้องจำทุกอย่างเอง

**ผลท้ายวัน:** มี README ที่จัดรูปแบบด้วย Markdown, private GitHub repository, PR ที่ merge แล้ว, และ Instruction ให้ Codex ทำงานเป็นช่วงสั้น ๆ

**Prerequisites:** ผ่าน [readiness](/resources/readiness), ลงชื่อเข้า GitHub, แตก [starter ZIP](/files/service-desk-starter.zip) แล้ว. ใช้ local folder `service-desk-lite` ตลอดวัน

> **License:** Git ไม่ต้องซื้อ paid license. ต้องมีสิทธิ์ Codex ใน ChatGPT desktop และสิทธิ์ใช้ GitHub ตาม policy/plan; ถ้ายังไม่ยืนยันให้ระบุ “ต้องตรวจสอบก่อนเริ่มอบรม”

| เวลา | Exercise |
| --- | --- |
| 09:30–10:30 | 1. เริ่มโปรเจค และเก็บตัวอย่างแรก |
| 10:45–12:00 | 2. เปลี่ยนข้อความผ่าน branch และ PR |
| 13:00–14:30 | 3. รวมงานที่แก้บรรทัดเดียวกัน |
| 14:45–16:00 | 4. กำหนดวิธีร่วมงานกับ Codex |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00

## Markdown สั้น ๆ ก่อน commit แรก

ใน Exercise 1 ใช้เวลา 09:45–10:00 ฝึกหัวข้อ รายการ ตัวหนา ลิงก์ inline code และ code block ผ่านส่วน Workshop notes ใน README เดิม แล้วนำเอกสารนี้เข้า initial commit เรียนในเวลาเดิม ไม่เพิ่มการบ้านบังคับ

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. เริ่มโปรเจค และเก็บตัวอย่างแรก](/exercises/day-01-git/exercise-01)
- [10:45–12:00 · 2. เปลี่ยนข้อความผ่าน branch และ PR](/exercises/day-01-git/exercise-02)
- [13:00–14:30 · 3. รวมงานที่แก้บรรทัดเดียวกัน](/exercises/day-01-git/exercise-03)
- [14:45–16:00 · 4. กำหนดวิธีร่วมงานกับ Codex](/exercises/day-01-git/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-01-git/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ

<style scoped>
a.day-one-slides-download {
  display: inline-block;
  padding: 8px 18px;
  border-radius: 999px;
  background: var(--vp-button-brand-bg);
  color: var(--vp-button-brand-text);
  font-weight: 600;
  text-decoration: none;
}

a.day-one-slides-download:hover {
  background: var(--vp-button-brand-hover-bg);
  color: var(--vp-button-brand-hover-text);
}
</style>
