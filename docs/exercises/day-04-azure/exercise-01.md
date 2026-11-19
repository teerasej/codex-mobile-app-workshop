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
   ตรวจ API จาก Day 2–3 โดยไม่อ่าน .env หรือแก้ไฟล์
   ชี้ว่า protected routes ใช้ auth, repository ใช้ PostgreSQL และข้อมูลคงอยู่หลัง restart
   ตรวจว่า /health อ่าน version จาก APP_VERSION ได้ และมี tests ที่ไม่ใช้ Azure DB
   ตรวจ api/Dockerfile, .dockerignore และ api/app/config.py
   อธิบาย 4 ส่วนสั้น ๆ: Python 3.12, ติดตั้ง lockfile, COPY app และรันด้วย non-root user
   ยืนยัน build context ที่ root, host 0.0.0.0 และ port 8000
   ตรวจว่าไม่มี secret ใน COPY หรือ startup output และทุกไฟล์ที่ COPY มีจริง
   ถ้าเป็น API แบบ memory หรือปิด auth ให้หยุดและบอกสิ่งที่ต้องแก้ก่อน build
   ~~~

2. อ่านผลตรวจพร้อมผู้สอน. `api/requirements.lock.txt` ต้องเป็น UTF-8 และไม่มี path เฉพาะเครื่อง; Docker และ workflow ต้องใช้ lockfile ชุดเดียวกันที่ตรวจบน Linux แล้ว หากติด dependency ต่าง platform ให้แก้กับผู้สอนก่อน build ไม่ลบแพ็กเกจเพียงเพื่อให้ผ่าน
3. ชี้บรรทัด `COPY` ว่านำเข้าเฉพาะ application. Schema/seed/sample JSON ใช้เตรียม database ก่อนหน้านี้ จึงไม่ต้องรัน seed หรืออ่านไฟล์ตัวอย่างขณะเริ่ม API ใน container
4. ตรวจผล auth/persistence ที่บันทึกจาก Day 3. หากยังไม่มีหลักฐาน ให้กลับไปตรวจ API กับผู้สอนก่อน; อย่าถือว่าการตรวจ code อย่างเดียวพิสูจน์ว่า database ใช้งานได้

**Checkpoint:** อธิบายได้ว่า image มีอะไร, secret เข้าตอนรันอย่างไร และ API/lockfile พร้อมสำหรับ container

## Practice 2 — รันกล่องเดียวกันในเครื่อง

<PracticeIllustration asset="d04-e01-p02" />

**Primary target:** เรียก API ที่รันใน Docker แล้วพบข้อมูลเดิมได้

### Steps

1. ให้ Codex หยุดเฉพาะ API เดิมและ build image จาก root โปรเจค

   ~~~text
   ตรวจว่า Docker engine พร้อม แล้วหยุดเฉพาะ uvicorn ของโปรเจคนี้เพื่อคืน port 8000
   ถ้าไม่แน่ใจว่า process ไหนเป็นของโปรเจค ให้ถามฉันก่อน ไม่หยุด process อื่น
   build จาก root ด้วย api/Dockerfile ตั้งชื่อ image service-desk-api:day4-v1
   ไม่เปิด .env และยังไม่ส่ง image ขึ้น Azure
   สรุปว่า build ผ่านหรือไม่ พร้อมจุดที่ต้องแก้ถ้ามี
   ~~~

   คำสั่งอ้างอิงสำหรับตรวจผลที่ Codex ใช้:

   ~~~shell
   docker build -f api/Dockerfile -t service-desk-api:day4-v1 .
   ~~~

2. ขอให้ Codex เริ่ม container โดยส่ง env file ให้ Docker อ่านโดยตรง

   ~~~text
   จาก root ของโปรเจค รัน image service-desk-api:day4-v1 เป็น container service-desk-api-local
   ใช้ --rm และ bind เฉพาะ 127.0.0.1:8000 ไปยัง port 8000 ของ container
   ให้ Docker อ่าน api/.env ด้วย --env-file โดยไม่ cat, เปิด หรือพิมพ์ค่าในไฟล์
   ไม่ตรวจ environment แบบแสดงค่าทั้งหมด และไม่ deploy
   เปิดค้างไว้ระหว่างทดสอบ แล้วบอกฉันเมื่อ API พร้อม
   ~~~

   ~~~shell
   docker run --rm --name service-desk-api-local -p 127.0.0.1:8000:8000 --env-file api/.env service-desk-api:day4-v1
   ~~~

   หากค่าใน env file มี quote ครอบ ให้ผู้เรียนตรวจและแก้เองตามรูปแบบ `--env-file`; Docker อาจรับ quote เป็นส่วนหนึ่งของค่า ไม่ส่งไฟล์กลับ chat

3. ใน Edge เปิด health endpoint แล้วตรวจ `status` เป็น `ok`

   ~~~text
   http://127.0.0.1:8000/health
   ~~~

4. เปิด API docs อีกแท็บ แล้วใช้ app user เดิมของ Day 2 ลงชื่อเข้าใช้ด้วยปุ่ม `Authorize`. ค้น UUID ที่บันทึกไว้จาก Day 3

   ~~~text
   http://127.0.0.1:8000/docs
   ~~~

5. ให้ Codex เตรียม API checker สำหรับ Terminal อีกหน้าต่าง แล้วผู้เรียนกรอกรหัสผ่านเองใน Terminal นั้น

   ~~~text
   เตรียมการรัน scripts/check_api.py จาก root ด้วย Python ของโปรเจค
   ใช้ base URL http://127.0.0.1:8000 เปิดใน Terminal ที่ฉันกรอก password แบบไม่แสดงตัวอักษรได้
   ถ้าเปิด Terminal แบบนั้นไม่ได้ ให้บอกคำสั่งที่ตรงกับ OS และ Python ของฉันเพื่อรันเอง
   ห้ามส่ง password/token ผ่าน arguments หรือ chat
   อธิบายว่า checker จะเพิ่มข้อมูลสมมติหนึ่งรายการ และให้ฉันเก็บ UUID เพื่อตรวจ persistence
   ~~~

   คำสั่งอ้างอิง; Codex ต้องเลือก Python ของโปรเจคให้ตรงเครื่อง:

   ~~~shell
   python scripts/check_api.py --base-url http://127.0.0.1:8000
   ~~~

6. ตรวจว่าเห็น request/status ใน container log และไม่มี password/token แล้วสั่งหยุดเฉพาะ container นี้

   ~~~text
   ตรวจเฉพาะ log ของ container service-desk-api-local ที่ใช้ทดสอบเมื่อครู่
   สรุป route/status โดยไม่คัดลอกข้อมูลลับ แล้วหยุด container นี้
   ยืนยันว่า port 8000 ไม่ได้มี API เก่าของโปรเจคทำงานแทน
   ~~~

**Checkpoint:** health, login และ authenticated read/create ผ่านจาก container และพบ UUID เดิมใน PostgreSQL

**ถ้าติดขัด:** Connection refused ให้ตรวจ bind host/port. ถ้า health ผ่านแต่ข้อมูลล้ม ให้ตรวจ database/config กับผู้สอน. Apple Silicon build สำหรับ local ได้; image ของ Azure จะ build บน ACR เป็น `linux/amd64` ใน Exercise 2
