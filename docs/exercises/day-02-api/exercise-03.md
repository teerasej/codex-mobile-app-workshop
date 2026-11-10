---
title: "Day 2 · Exercise 3 — เก็บข้อมูลลง PostgreSQL"
prev: {"text": "Exercise 2", "link": "/exercises/day-02-api/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-02-api/exercise-04"}
---

# Exercise 3 — เก็บข้อมูลลง PostgreSQL


> **Day 2 · Python API · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

::: tip วิธีทำงานวันนี้
ก่อนเริ่ม Exercise 1 ให้ Codex สร้าง branch **feature/request-api** จาก main ที่ไม่มีงานค้างเพียงครั้งเดียว. ถ้าอยู่ branch นี้จาก Practice ก่อนแล้วให้ใช้ต่อ ไม่สร้างซ้ำและไม่กลับไปเริ่มจาก main ใหม่. ทุก Practice เริ่มด้วยตรวจ plan และจบด้วย checkpoint → commit เฉพาะไฟล์ที่ตรวจแล้ว. ยังไม่ merge จนจบวัน

คำสั่ง **python** ต่อจากสร้าง environment หมายถึง Python ใน **.venv** ของโปรเจคเท่านั้น. หาก Codex เปิด terminal ใหม่ ให้ยืนยัน interpreter นี้ก่อนรัน. ผู้เรียนไม่จำเป็นต้องจำคำสั่ง แต่ต้องรู้ว่าเป็นการติดตั้ง รัน server หรือรัน test
:::


## Scenario

ปิดเคาน์เตอร์แล้วเปิดใหม่ ใบงานต้องยังอยู่ เราจะเปลี่ยนจากรายการใน memory เป็นทะเบียน PostgreSQL ที่เตรียมไว้

## Practice 1 — เตรียมข้อมูลทดลองใน database ของตน

<PracticeIllustration asset="d02-e03-p01" eager />

**Primary target:** พิสูจน์ว่า seed เติมเฉพาะข้อมูลที่ขาดและคงข้อมูลกับ credentials ที่เตรียมไว้

### Steps

1. หยุด API ด้วย Ctrl+C. หากได้รับ Student ZIP ส่วนตัว ให้คัดลอกเฉพาะ `api/.env` ไปยังโปรเจคของตนเมื่อยังไม่มีไฟล์นี้ เก็บ `.gitignore` ของ starter เดิม และตรวจ **git check-ignore api/.env**. หากมี `.env` อยู่แล้ว ให้ผู้เรียนตรวจว่าเป็น database ที่ได้รับมอบหมายโดยไม่แสดงค่าใน chat; ห้ามเขียนทับหรือสร้าง JWT_SECRET ใหม่โดยอัตโนมัติ
2. แยกกุญแจสองชุด: API ใช้ **runtime login** จาก `.env` เพื่ออ่าน/เขียนข้อมูล ส่วน seed ใช้ **setup login** สำหรับ schema. เก็บ Student ZIP และรหัสผ่าน app users ในช่องทางส่วนตัว ไม่ส่ง README ส่วนตัวหรือ `.env` ให้ Codex อ่าน. Database ที่ผู้สอนเตรียมใหม่มี users 2/requests 4 อยู่แล้ว

   > **ใช้ database ของตนเอง:** ให้เจ้าของเตรียม setup/runtime logins แยกกันตาม [readiness](/resources/readiness). เมื่อยังไม่มี `.env` จึงคัดลอก `.env.example` แล้วกรอก runtime DATABASE_URL และสร้าง JWT_SECRET แบบสุ่มผ่าน script ที่เขียนลงไฟล์โดยไม่พิมพ์ค่า. ไม่ใช้ setup/admin login เป็น API runtime

3. ส่ง prompt ให้ Codex สร้างโค้ด แต่ยังไม่รัน:

   ~~~text
   อ่าน api/schema.sql, data/service-requests.json และ docs/api-contract.md
   สร้าง app/config.py และ app/seed.py โดยไม่อ่านหรือแสดง .env ของฉัน
   config ใช้ runtime .env; ไม่โหลด secrets/ต่อ DB ตอน import เพื่อให้ tests inject settings ได้
   seed รับ host/database/setup username ผ่าน interactive prompts และ setup password ผ่าน getpass
   ไม่อ่าน runtime DATABASE_URL สำหรับ seed และไม่บันทึก setup credentials
   --check ต้องอ่านอย่างเดียว ไม่สร้าง schema, users หรือ hash; รายงานจำนวน users/requests และต่อ owner
   seed ปกติใช้ parameter binding, transaction และ pwdlib Argon2; ไม่ DROP/TRUNCATE
   เพิ่มเฉพาะ users/UUID ที่ขาด คง password hash/status/ข้อมูลเดิมทุก field
   ขอ app password ผ่าน getpass เฉพาะ user ที่ยังไม่มี; ผู้ที่ได้รับ Student ZIP ใช้ password ที่ได้รับ
   ไม่ seed ตอน API start/import แสดง diff แล้วหยุดให้ตรวจ
   ~~~
4. ตรวจโค้ดว่า seed ต่อ database ฝึกของตนด้วย setup login, ใช้ TLS และไม่พิมพ์ secret/hash. รันเองจาก root ใน terminal ของ `.venv`:

   ~~~shell
   cd api
   python -m app.seed --check
   python -m app.seed
   python -m app.seed --check
   cd ..
   ~~~

   Windows ที่ไม่ activate ใช้ `..\.venv\Scripts\python.exe` แทน python เมื่ออยู่ใน api; macOS ใช้ `../.venv/bin/python`. Database ของตนที่ยังว่าง: `--check` ต้องบอกว่ายังไม่มี schema โดยไม่สร้างให้ แล้วจึงรัน seed ปกติ
5. เทียบจำนวนก่อน/หลัง. Database ที่ผู้สอนเตรียมและยังไม่เพิ่มข้อมูลต้องคง users 2/requests 4; หากฝึกไปแล้วให้ใช้ baseline ที่บันทึก ไม่คาดหวังให้กลับเป็น 4. รัน seed ซ้ำแล้วจำนวน/hash/status เดิมต้องไม่เปลี่ยน. ใช้ app passwords ที่ได้รับเดิม; password ที่กรอกใหม่ไม่ใช่การ reset user ที่มีอยู่
6. กลับ root และใช้ runtime `.env` เดิมสำหรับ Practice ถัดไป. เก็บ setup credentials แยกจาก runtime configuration และ commit เฉพาะโค้ดที่ตรวจแล้ว

**Checkpoint:** seed rerun ไม่เขียนทับข้อมูลหรือ credentials; `--check` ไม่แก้ database; `.env` ถูก ignore. ตรวจ app login และ ownership ต่อใน Exercise 4

## Practice 2 — แทน memory ด้วย persistence

<PracticeIllustration asset="d02-e03-p02" />

**Primary target:** ตรวจว่าคำขอที่สร้างใหม่ยังอยู่หลัง restart API

### Steps

1. ส่ง:

   ~~~text
   เปลี่ยน repository ของ routes เดิมให้ใช้ Azure PostgreSQL ผ่าน psycopg
   ทุก query ใช้ parameter binding; commit เมื่อเขียนสำเร็จและ rollback เมื่อผิดพลาด
   อ่าน connection string จาก config โดยไม่ log ค่า; connection failure ส่ง 503 ทั่วไป
   ตอนนี้ owner ชั่วคราวยังเป็น learner01 จนถึง Exercise 4
   ไม่เปลี่ยน schema/contract และไม่ seed ตอน start/import
   แสดง diff ว่าจุดไหนแทน in-memory จริง
   ~~~
2. เริ่ม API ด้วยคำสั่งจาก Exercise 1. GET /requests ต้องแสดงเฉพาะ learner01. Database ใหม่ที่ยังไม่เพิ่มข้อมูลมี 3 รายการของเขา; หากเคยฝึกหรือผู้สอนทดสอบไว้แล้ว ให้เทียบกับ baseline ต่อ owner จาก Practice 1 ไม่ล้างข้อมูลให้กลับเป็น 3
3. POST คำขอใหม่ชื่อที่จำได้ เช่น ทดสอบการเก็บข้อมูลหลังเปิดใหม่ แล้วจด UUID
4. หยุดและเริ่ม server ใหม่. GET UUID เดิม ต้องได้ข้อมูลเดิม
5. ถ้าต่อ database ไม่ได้ ตรวจ host/TLS/network กับผู้สอน. ห้ามเปลี่ยนกลับ memory แล้วรายงานว่า persistence ผ่าน

**Checkpoint:** UUID ที่สร้างเองยังอยู่หลัง restart. อธิบายได้ว่า /health ผ่านไม่ได้แปลว่า query database ผ่าน
