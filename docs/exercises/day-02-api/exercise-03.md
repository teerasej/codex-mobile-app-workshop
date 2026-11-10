---
title: "Day 2 · Exercise 3 — เก็บข้อมูลลง PostgreSQL"
prev: {"text": "Exercise 2", "link": "/exercises/day-02-api/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-02-api/exercise-04"}
---

# Exercise 3 — เก็บข้อมูลลง PostgreSQL

> **Day 2 · Python API · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


ฐานข้อมูลฝึกที่ผู้สอนให้มีข้อมูลตัวอย่างพร้อมใช้แล้ว ใช้ runtime `.env` เดิมจาก [Exercise 1](/exercises/day-02-api/exercise-01#postgres-connection) ถ้า API ยังรันอยู่ ให้กด **Ctrl+C** ก่อนเริ่ม

## Practice 1 — แทน memory ด้วย PostgreSQL {#practice-2-—-แทน-memory-ด้วย-postgresql}

<PracticeIllustration asset="d02-e03-p02" eager />

**Primary target:** ปิดแล้วเปิด API ใหม่ และยังหา Request ที่เพิ่งสร้างเจอ

### Steps

1. **เตรียมค่าต่อฐานข้อมูล**

   ~~~text
   อยากให้ API ต่อฐานข้อมูล ช่วยเตรียม api/app/config.py ตาม docs/api-contract.md
   ใช้ runtime .env ตอนที่ต้องเชื่อมต่อ ขออ่านแผนก่อนลงมือ
   ~~~

2. **เตรียมที่เก็บ Request**

   ~~~text
   ช่วยวางแผนสร้างส่วนอ่านเขียน PostgreSQL ด้วย psycopg ตาม docs/api-contract.md
   ใช้ runtime config ขออ่านแผนก่อนลงมือ
   ~~~

3. **ต่อ API เข้าฐานข้อมูล**

   ~~~text
   ต่อ routes เดิมเข้ากับ repository โดยคง API contract, schema และ learner01
   ถ้าต่อ DB ไม่ได้ ให้ตอบ 503
   ~~~

4. **อ่านรายการเดิม**

   เปิด Swagger UI แล้วลอง `GET /requests` ต้องเห็นเฉพาะรายการของ `learner01` ฐานข้อมูลฝึกที่เพิ่งเตรียมจะเห็น 3 รายการ ถ้าเคยทำแบบฝึกหัดแล้วอาจเห็นมากกว่านี้

5. **สร้าง Request ใหม่**

   ใน Swagger UI ใช้ `POST /requests` กับข้อมูลตัวอย่างจาก Exercise 2 ตั้งชื่อที่จำได้ แล้วจดค่า `id` (UUID) จากผล HTTP 201

   ตัวอย่าง JSON (ปรับตาม schema ใน `docs/api-contract.md`):

   ~~~json
   {
     "title": "Persist test - แจ้งปัญหา VPN",
     "description": "ทดสอบว่าข้อมูลยังอยู่หลังเริ่ม API ใหม่",
     "category": "equipment"
   }
   ~~~

6. **ปิด และเปิด API ใหม่**


7. **หา Request เดิม**

   เปิด Swagger UI แล้วใส่ ID ที่จดไว้ใน `GET /requests/{id}` ต้องได้ HTTP 200 พร้อมข้อมูลเดิม


**Checkpoint:** เปิด API ใหม่แล้วยังหา Request เดิมด้วย ID เดิมได้ ส่วน `/health` ใช้เช็กว่า API ตอบได้
