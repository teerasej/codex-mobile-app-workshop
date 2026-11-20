---
title: "Day 4 · Exercise 1 — แพ็กและทดสอบ container"
prev: {"text": "ภาพรวมวัน", "link": "/exercises/day-04-azure/"}
next: {"text": "Exercise 2", "link": "/exercises/day-04-azure/exercise-02"}
---

# Exercise 1 — แพ็กและทดสอบ container

> **Day 4 · Azure · 09:30–10:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-04-azure/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

## Scenario

API ทำงานบน laptop แล้ว เราจะใส่ code และ dependencies ไว้ใน image เหมือนจัดกล่องสูตรอาหารให้เครื่องอื่นเปิดใช้ได้ โดยเก็บรหัสผ่านไว้นอกกล่อง

## Practice 1 — อ่าน Dockerfile ก่อน build

<PracticeIllustration asset="d04-e01-p01" eager />

**Primary target:** อธิบายสิ่งที่นำเข้า image และสิ่งที่ต้องอยู่นอก image ได้

### Steps

1. เปิด `api/Dockerfile` และ `.dockerignore` ในโปรเจค แล้วส่ง prompt นี้ให้ Codex ตรวจความพร้อม

   ~~~text
   ก่อนแพ็ก API ช่วยดูว่าพร้อมเอาไปเปิดใน Docker หรือยัง
   ชี้ให้ดูว่าส่วนที่ต้องล็อกอินมีการตรวจสิทธิ์ ข้อมูลเก็บใน PostgreSQL และมีหลักฐานว่าข้อมูลยังอยู่หลังเปิด API ใหม่
   ขอเช็กด้วยว่า /health อ่าน APP_VERSION และรัน tests ได้โดยไม่ต่อ Azure DB

   ดู api/Dockerfile, .dockerignore และ api/app/config.py
   ช่วยเช็กว่า build จาก root ของโปรเจกต์ เปิดที่ 0.0.0.0:8000
   ถ้ายังเก็บข้อมูลใน memory หรือยังขาดการล็อกอิน ให้บอกสิ่งที่ต้องแก้ก่อน build
   ~~~

2. อ่านผลตรวจพร้อมผู้สอน. Docker และ workflow ต้องใช้ lockfile ชุดเดียวกัน


**Checkpoint:** อธิบายได้ว่า image มีอะไร, secret เข้าตอนรันอย่างไร และ API/lockfile พร้อมสำหรับ container

## Practice 2 — รัน Image

<PracticeIllustration asset="d04-e01-p02" />

**Primary target:** เรียก API ที่รันใน Docker แล้วพบข้อมูลเดิมได้

### Steps

1. ให้ Codex หยุดเฉพาะ API เดิมและ build image จาก root โปรเจค

   ~~~text
   ช่วยแพ็ก API เป็น image ชื่อ service-desk-api:day4-v1 จาก root ของโปรเจกต์

   คำสั่งอ้างอิงสำหรับตรวจผลที่ Codex ใช้:

   ~~~

2. ขอให้ Codex เริ่มการทำงานของ container โดยส่ง env file ให้ Docker อ่านโดยตรง

   ~~~text
   ทำสอบ API ที่อยู่ใน Image ที่เพิ่ง build เสร็จ ช่วยเปิดเป็น container ชื่อ service-desk-api-local

   ทำจาก root ตามตัวอย่าง เปิดพอร์ต 8000 ให้เข้าถึงได้จากเครื่องนี้ที่ 127.0.0.1 เท่านั้น
   ให้ Docker รับ api/.env โดยตรงผ่าน --env-file
   เปิดไว้ในเครื่องระหว่างที่ฉันทดสอบ แล้วบอกเมื่อ API พร้อม
   ~~~

   ~~~shell
   docker run --rm --name service-desk-api-local -p 127.0.0.1:8000:8000 --env-file api/.env service-desk-api:day4-v1
   ~~~

   หากค่าใน env file มี quote ครอบ ให้ผู้เรียนตรวจและแก้เองตามรูปแบบ `--env-file`

3. ใน Edge เปิด health endpoint แล้วตรวจ `status` เป็น `ok`

   ~~~text
   http://127.0.0.1:8000/health
   ~~~

4. เปิด API docs อีกแท็บ แล้วใช้ app user เดิมของ Day 2 ลงชื่อเข้าใช้ด้วยปุ่ม `Authorize`. ค้น UUID ที่บันทึกไว้จาก Day 3

   ~~~text
   http://127.0.0.1:8000/docs
   ~~~



**Checkpoint:** health, login และ authenticated read/create ผ่านจาก container และพบ UUID เดิมใน PostgreSQL

**ถ้าติดขัด:** Connection refused ให้ตรวจ bind host/port. ถ้า health ผ่านแต่ข้อมูลล้ม ให้ตรวจ database/config กับผู้สอน. Apple Silicon build สำหรับ local ได้; image ของ Azure จะ build บน ACR เป็น `linux/amd64` ใน Exercise 2
