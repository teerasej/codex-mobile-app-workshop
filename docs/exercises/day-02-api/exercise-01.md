---
title: "Day 2 · Exercise 1 — Python bridge และ API แรก"
prev: {"text": "ภาพรวมวัน", "link": "/exercises/day-02-api/"}
next: {"text": "Exercise 2", "link": "/exercises/day-02-api/exercise-02"}
---

# Exercise 1 — Python bridge และ API แรก


> **Day 2 · Python API · 09:30–10:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

## Scenario

เริ่มจากเช็กว่าเครื่องเราเข้าถึงฐานข้อมูลฝึกได้ เหมือนลองกุญแจก่อนเปิดร้าน จากนั้นใช้ JSON ตัวอย่างเพื่อฝึก Python แล้วเปิด API แรกบนเครื่องของเรา


## เตรียม Python · 10 นาที

เปิดโฟลเดอร์ `service-desk-lite` ใน Codex แบบ local แล้วส่งทีละ prompt รอให้แต่ละขั้นเสร็จก่อนส่งขั้นถัดไป

1. **สร้าง `.venv`**

   ~~~text
   ช่วยสร้าง .venv ที่ root ด้วย Python 3.12 ถ้ามี .venv รุ่นนี้แล้วให้ใช้ต่อ ถ้าไม่พบ 3.12 หรือ .venv เดิมใช้คนละรุ่น ให้บอกรุ่นที่พบแล้วหยุด
   ~~~

   ถ้าไม่มี Python 3.12 ให้ส่งข้อความนี้โดยใส่รุ่นที่ผู้สอนอนุมัติ แล้วทำต่อเมื่อขั้นติดตั้งและ import ผ่าน

   ~~~text
   ผู้สอนอนุมัติ Python รุ่น [รุ่นที่อนุมัติ] ช่วยใช้รุ่นนี้กับ .venv ถ้าต้องแทน .venv เดิม ให้บอกแผนก่อน
   ~~~

2. **เปิดใช้ `.venv`**

   ~~~text
   เปิดใช้ .venv ตามระบบของเครื่อง แล้วเช็กว่า sys.executable ชี้เข้า .venv ถ้าเปิดใช้ไม่ได้ ให้บอกวิธีเรียก Python ใน .venv โดยตรง
   ~~~

   ถ้า PowerShell บล็อกการเปิดใช้ ให้เรียก `.\.venv\Scripts\python.exe` โดยตรงโดยไม่แก้ policy ส่วน macOS ใช้ `.venv/bin/python`

3. **ติดตั้งแพ็กเกจ**

   ~~~text
   ใช้ Python ใน .venv ติดตั้งจาก api/requirements.txt แล้วเช็กว่า import fastapi, uvicorn, psycopg และ dotenv ได้
   ~~~

## Practice 1 — ตรวจการเชื่อมต่อ PostgreSQL {#postgres-connection}

<PracticeIllustration asset="d02-e01-postgres-check" eager />

**Primary target:** ยืนยันว่าเครื่องของเราใช้ runtime login ที่ได้รับเชื่อม PostgreSQL ฝึกผ่าน TLS และรันคำสั่งอ่านอย่างง่ายได้

### Steps

1. **เตรียม `.env`**

   แตก Student ZIP ไว้นอก Git repository แล้วลากโฟลเดอร์ที่แตกไว้ มาใส่ลงกับ prompt นี้

   ~~~text
   copy api/.env จากโฟลเดอร์ไปที่ api/.env ของโปรเจคนี้
   ~~~

2. **ตั้ง Git ให้ข้าม `.env`**

   เปิดไฟล์ `.gitignore` เพื่อตรวจสอบว่ามี `api/.env` หรือไม่

   ~~~text
   เพิ่มไฟล์นี้เข้า .gitignore
   ~~~


3. **ดูแผนเชื่อมต่อ**

   ~~~text
   ช่วยวางแผนเช็ก PostgreSQL ด้วย psycopg รันแค่ SELECT 1 แล้วปิด connection
   ~~~

4. **ทดสอบการเชื่อมต่อ**

   ~~~text
   รันตามแผนที่ตรวจแล้ว ถ้าผ่านให้ตอบ 1 ถ้าไม่ผ่านให้บอกเฉพาะหมวดปัญหาที่ระบุได้
   ~~~

**Checkpoint:** ได้ `1` จึงผ่าน ถ้าติดขัดให้บันทึกว่า PostgreSQL ยังไม่ผ่าน แจ้งผู้สอนเป็นการส่วนตัว แล้วทำ Practices 2–3 ต่อได้ ขั้นนี้ไม่มีไฟล์ให้ commit

## Practice 2 — อ่านข้อมูลด้วย function, class และ module {#practice-1-—-อ่านข้อมูลด้วย-function-class-และ-module}

<PracticeIllustration asset="d02-e01-p01" />

**Primary target:** ตามรอยจาก JSON หนึ่งรายการไปเป็น Python object และข้อความผลลัพธ์ได้

### Steps

1. **สร้าง Python bridge**

   ~~~text
   อ่านตัวอย่าง Request จาก data/service-requests.json
   สร้างไฟล์ที่จำเป็นให้น้อยที่สุดใน api/bridge
   แสดงจำนวนรายการกับ title และ status
   ~~~

2. **รันตัวอย่าง**

   รันจาก root แล้วเทียบ title แรกกับข้อมูลใน JSON

   ~~~shell
   ทดสอบการทำงานของไฟล์ แสดงผลลัพธ์ที่ได้
   ~~~

3. **ปรับข้อความ**

   ~~~text
   ชี้จุดที่อ่าน JSON สร้าง object และเรียก function ให้ดูหน่อย
   ~~~

**Checkpoint:** เห็น 4 รายการข้อมูลและ title แรกตรงกับ JSON

## Practice 3 — เปิด API ที่ตอบได้ {#practice-2-—-เปิด-api-ที่ตอบได้}

<PracticeIllustration asset="d02-e01-p02" />

**Primary target:** เรียก endpoint แรกและอ่าน HTTP status กับ response body ได้

### Steps

1. **สร้าง FastAPI app**

   ~~~text
   อยากเปิด FastAPI app บนเครื่องนี้
   ~~~

2. **เพิ่ม `/health`**

   ~~~text
   อยากเช็กว่า API สามารถทำงานได้ ช่วยเพิ่ม GET /health ตาม docs/api-contract.md
   ~~~

3. **รัน API**

   ถ้า server ยังไม่พร้อมใช้งานให้ ใช้คำสั่งด้านล่างรันเพื่อเริ่ม server ใหม่

   ~~~text
   ใช้ uvicorn ทดสอบการทำงานของ API โดยเปิด server ค้างไว้
   ~~~

4. **เปิด `/health`**

   เปิด URL นี้แล้วดู response body

   ~~~text
   http://127.0.0.1:8000/health
   ~~~

5. **ตรวจผลใน Swagger UI**

   เปิด URL นี้ ขยาย **GET /health** แล้วเลือก **Try it out → Execute** ดู HTTP status และ response body

   ~~~text
   http://127.0.0.1:8000/docs
   ~~~

**Checkpoint:** เห็น HTTP 200 และ response ตรงกับตัวอย่างเมื่อใช้ version เริ่มต้น

~~~json
{"status":"ok","version":"v1"}
~~~

ถ้าเจอ `ModuleNotFoundError` ให้ตรวจ interpreter และ working folder ถ้า port ถูกใช้โดย server ฝึกเดิม ให้หยุด server เดิมด้วย Ctrl+C แล้วเริ่มใหม่
