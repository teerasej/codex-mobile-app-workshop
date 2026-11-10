---
title: "Day 2 — เปลี่ยนแบบฟอร์มให้เป็นบริการข้อมูล"
prev: {"text": "สรุป Day 1", "link": "/exercises/day-01-git/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-02-api/exercise-01"}
---

# Day 2 — เปลี่ยนแบบฟอร์มให้เป็นบริการข้อมูล

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-01-git/) · [วันถัดไป](/exercises/day-03-flutter/)

## Overview theme

วันนี้ Service Desk Lite จะรับคำขอจริงผ่าน Python Web API. ถ้าเคยใช้ Power Apps กับ connector ลองนึกว่าเรากำลังสร้างจุดรับข้อมูลที่ connector เรียกใช้เอง: มีช่องที่ต้องกรอก ตรวจข้อมูลก่อนบันทึก และตอบผลที่หน้าจอนำไปใช้ได้

**ผลท้ายวัน:** FastAPI อ่าน/สร้าง/แก้สถานะคำขอใน Azure PostgreSQL ได้ พร้อม login, ownership check และ automated tests

**Prerequisites:** Day 1 main ที่อัปเดตแล้ว, [Azure PostgreSQL readiness](/resources/readiness), Python 3.12, [API contract](/resources/api-contract) และ [sample JSON](/files/service-requests.json) ใน starter. เปิด Codex local project เดิม

> **License / ค่าใช้จ่าย:** Python/FastAPI ไม่ต้องซื้อ paid license; บัญชี Codex ต้องมีสิทธิ์และ usage. ใช้ database ฝึกที่ผู้สอนเตรียมให้แต่ละคน หรือ database ใหม่ที่เจ้าของอนุมัติ ซึ่งมีค่าใช้จ่าย. ไม่เชื่อม database ใช้งานจริง

| เวลา | Exercise | อธิบาย / ลงมือ / ตรวจและแก้ |
| --- | --- | --- |
| 09:30–10:30 | 1. Python bridge และ API แรก | 15 / 35 / 10 นาที |
| 10:45–12:00 | 2. Route, model และ validation | 10 / 50 / 15 นาที |
| 13:00–14:30 | 3. เก็บข้อมูลลง PostgreSQL | 15 / 55 / 20 นาที |
| 14:45–16:00 | 4. Login, ownership และ tests | 10 / 45 / 20 นาที |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00

## Database ที่ได้รับก่อนเริ่ม

ถ้าได้รับ Student ZIP ส่วนตัว ให้เก็บ `.env` และ app passwords ชุดเดิม. Database มี users 2/requests 4 แล้ว; Exercise 3 จะตรวจและรัน seed ซ้ำอย่างปลอดภัย โดยใช้ setup login แยกจาก runtime ของ API. ห้ามส่ง Student ZIP หรือค่าลับเข้า chat

## วิธีทำงานวันนี้

ก่อนเริ่ม Exercise 1 ให้ Codex สร้าง branch **feature/request-api** จาก main ที่ไม่มีงานค้างเพียงครั้งเดียว. ถ้าอยู่ branch นี้จาก Practice ก่อนแล้วให้ใช้ต่อ ไม่สร้างซ้ำและไม่กลับไปเริ่มจาก main ใหม่. ทุก Practice เริ่มด้วยตรวจ plan และจบด้วย checkpoint → commit เฉพาะไฟล์ที่ตรวจแล้ว. ยังไม่ merge จนจบวัน

คำสั่ง **python** ต่อจากสร้าง environment หมายถึง Python ใน **.venv** ของโปรเจคเท่านั้น. หาก Codex เปิด terminal ใหม่ ให้ยืนยัน interpreter นี้ก่อนรัน. ผู้เรียนไม่จำเป็นต้องจำคำสั่ง แต่ต้องรู้ว่าเป็นการติดตั้ง รัน server หรือรัน test

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. Python bridge และ API แรก](/exercises/day-02-api/exercise-01)
- [10:45–12:00 · 2. Route, model และ validation](/exercises/day-02-api/exercise-02)
- [13:00–14:30 · 3. เก็บข้อมูลลง PostgreSQL](/exercises/day-02-api/exercise-03)
- [14:45–16:00 · 4. Login, ownership และ tests](/exercises/day-02-api/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-02-api/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ
