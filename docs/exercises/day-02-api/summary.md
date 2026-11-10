---
title: "สรุป Day 2 — Python API"
prev: {"text": "Exercise 4", "link": "/exercises/day-02-api/exercise-04"}
next: {"text": "ไป Day 3", "link": "/exercises/day-03-flutter/"}
---

# สรุป Day 2 — Python API


## ใจความสำคัญ

- Function, class และ module ช่วยแบ่งงาน Python ให้ตรวจและแก้ทีละส่วนได้
- API contract กำหนด route และรูปแบบข้อมูลให้ FastAPI กับ Flutter พูดภาษาเดียวกัน
- Validation ตรวจข้อมูลก่อนบันทึก; PostgreSQL ทำให้ข้อมูลอยู่ต่อเมื่อ process เริ่มใหม่
- Login/token บอกว่าใครกำลังเรียก API และ ownership จำกัดว่าเห็น Request ใดได้; test ต้องตรวจกรณีปฏิเสธด้วย

## ก่อนจบวัน ตรวจหลักฐาน

- ☐ /health และ /docs ใช้งานได้; route/model ตรงกับ contract
- ☐ Invalid input ถูกปฏิเสธ และข้อมูลที่สร้างยังอยู่หลัง restart
- ☐ Login ได้และผู้ใช้คนอื่นอ่าน Request ของเราไม่ได้
- ☐ มี automated tests และผล live checker ตามที่ทำจริง; บันทึกสิ่งที่ยังไม่ผ่าน

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ

## สิ่งที่เก็บไว้ใช้ต่อ

- api/app, API tests และ requirements.lock.txt ที่สร้างและตรวจแล้ว
- API contract เดิม และ UUID ตัวอย่างที่สร้างในฐานข้อมูลฝึก
- docs/review-log.md, main commit และข้อมูลเข้าใช้ lab ในช่องทางส่วนตัว

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## Day 3 — นำ API มาอยู่ในมือผู้ใช้

วันนี้เคาน์เตอร์รับเรื่องทำงานแล้ว พรุ่งนี้ Flutter จะเป็นแบบฟอร์มที่ผู้ใช้ถืออยู่ ทุก field และ route จึงต้องตรง API contract เดิม

ก่อนเริ่ม ตรวจ API/auth/persistence ที่ผ่านจริง และเตรียม Flutter/Android toolchain; เก็บ database password ไว้ฝั่ง API เท่านั้น

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

เราเปลี่ยนข้อมูลจาก JSON เป็น API ที่มี validation, persistence และผู้ใช้ที่ตรวจสอบได้ ไป [Day 3](/exercises/day-03-flutter/) เพื่อให้คนใช้งานผ่านหน้าจอ

อ่านเพิ่ม: [FastAPI authentication](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/), [CORS](https://fastapi.tiangolo.com/tutorial/cors/), [Azure PostgreSQL TLS](https://learn.microsoft.com/en-us/azure/postgresql/security/security-tls)
