---
title: "Day 2 — บริการข้อมูลแอพผ่าน internet"
prev: {"text": "สรุป Day 1", "link": "/exercises/day-01-git/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-02-api/exercise-01"}
---

<script setup>
import { withBase } from 'vitepress'

const studentPackages = ['student-01.zip', 'student-02.zip', 'student-03.zip']
</script>

# Day 2 — บริการข้อมูลแอพผ่าน internet

<section class="day-two-downloads" aria-label="ดาวน์โหลดไฟล์สำหรับ Day 2">
  <p class="day-two-downloads-title">ดาวน์โหลดไฟล์สำหรับ Day 2</p>
  <div class="day-two-download-buttons">
    <a v-for="file in studentPackages" :key="file" :href="withBase('/files/' + file)" :download="file">
      ดาวน์โหลด {{ file }}
    </a>
  </div>
</section>

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-01-git/) · [วันถัดไป](/exercises/day-03-flutter/)

## Overview theme

วันนี้ Service Desk Lite จะรับ Request จริงผ่าน Python Web API. ถ้าเคยใช้ Power Apps กับ connector ลองนึกว่าเรากำลังสร้างจุดรับข้อมูลที่ connector เรียกใช้เอง: มีช่องที่ต้องกรอก ตรวจข้อมูลก่อนบันทึก และตอบผลที่หน้าจอนำไปใช้ได้

**ผลท้ายวัน:** FastAPI อ่าน/สร้าง/แก้สถานะ Request ใน Azure PostgreSQL ได้ พร้อม login, ownership check และ automated tests

**Prerequisites:** Day 1 main ที่อัปเดตแล้ว, [Azure PostgreSQL readiness](/resources/readiness), Python 3.12, [API contract](/resources/api-contract) และ [sample JSON](/files/service-requests.json) ใน starter. เปิด Codex local project เดิม

> **License / ค่าใช้จ่าย:** Python/FastAPI ไม่ต้องซื้อ paid license; บัญชี Codex ต้องมีสิทธิ์และ usage. ใช้ database ฝึกที่ผู้สอนเตรียมให้แต่ละคน หรือ database ใหม่ที่เจ้าของอนุมัติ ซึ่งมีค่าใช้จ่าย. ไม่เชื่อม database ใช้งานจริง

| เวลา | Exercise |
| --- | --- |
| 09:30–10:30 | 1. Python bridge และ API แรก |
| 10:45–12:00 | 2. Route, model และ validation |
| 13:00–14:30 | 3. เก็บข้อมูลลง PostgreSQL |
| 14:45–16:00 | 4. Login, ownership และ tests |

## วิธีทำงานวันนี้

**บอกสิ่งที่อยากได้ → ดูแผน → ลอง → เช็กผล**

ให้ Codex เสนอแผนสั้น ๆ ก่อนแก้โค้ด แล้วทำทีละส่วน ลองตาม checkpoint ด้วยตัวเอง ถ้าผลต่างจากที่คาด ให้บอก Codex ว่าคาดอะไรและเห็นอะไร ขอให้ช่วยดูทีละจุด

- ก่อน Exercise 1 ให้สร้าง `feature/request-api` จาก `main` ที่ไม่มีงานค้าง ถ้าอยู่ branch นี้แล้วให้ใช้ต่อ
- ใช้ Python ใน `.venv` ทุกครั้ง ตรวจ interpreter เมื่อเปิด terminal ใหม่
- เก็บ Student ZIP, `.env`, passwords และ tokens ไว้ส่วนตัว ส่งเฉพาะผลทดสอบที่ไม่มีค่าลับ
- Commit เฉพาะไฟล์ที่ตรวจแล้ว ถ้าไม่มีไฟล์เปลี่ยนให้ข้าม commit และค่อย merge ตอนจบวัน

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. Python bridge และ API แรก](/exercises/day-02-api/exercise-01)
- [10:45–12:00 · 2. Route, model และ validation](/exercises/day-02-api/exercise-02)
- [13:00–14:30 · 3. เก็บข้อมูลลง PostgreSQL](/exercises/day-02-api/exercise-03)
- [14:45–16:00 · 4. Login, ownership และ tests](/exercises/day-02-api/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-02-api/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ

<style scoped>
.day-two-downloads {
  margin: 24px 0;
  padding: 20px;
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 12px;
  background: var(--vp-c-brand-soft);
}

.day-two-downloads-title {
  margin: 0 0 12px;
  font-weight: 600;
}

.day-two-download-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.day-two-download-buttons a {
  display: flex;
  flex: 1 1 210px;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 10px 16px;
  border-radius: 999px;
  background: var(--vp-button-brand-bg);
  color: var(--vp-button-brand-text);
  font-size: 14px;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
}

.day-two-download-buttons a:hover {
  background: var(--vp-button-brand-hover-bg);
  color: var(--vp-button-brand-hover-text);
}

.day-two-download-buttons a:focus-visible {
  outline: 3px solid var(--vp-c-brand-1);
  outline-offset: 4px;
}

@media (max-width: 639px) {
  .day-two-download-buttons a {
    flex-basis: 100%;
  }
}
</style>
