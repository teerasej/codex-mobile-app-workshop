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

API ทำงานบน laptop แล้ว เราต้องพิสูจน์ว่าเครื่องอื่นที่มี container runtime ก็รันได้จากกล่องเดียวกัน

## Practice 1 — อ่าน Dockerfile ก่อน build

<PracticeIllustration asset="d04-e01-p01" eager />

**Primary target:** อธิบายสิ่งที่นำเข้า image และสิ่งที่ต้องอยู่นอก image ได้

### Steps

1. ตรวจ api/Dockerfile และ .dockerignore จาก starter. Dockerfile ใช้ Python 3.12, ติดตั้ง lockfile, copy เฉพาะ app และรันด้วย non-root user
2. ส่ง prompt:

   ~~~text
   ตรวจ api/Dockerfile, .dockerignore และ app/config.py
   ยืนยันว่า build context คือ root, runtime port 8000, host 0.0.0.0
   ไม่มี .env/password/token ใน COPY, image layers หรือ startup output
   ตรวจ requirements.lock.txt จาก Day 2 ว่าเป็น UTF-8 และไม่มี local absolute paths
   ยังไม่ build หรือ deploy; อธิบาย 4 บรรทัดสำคัญของ Dockerfile
   ~~~
3. ถ้า lockfile ใช้ไม่ได้บน Linux ให้ Codex แยกเฉพาะ dependency ที่เป็น platform-specific อย่างมีเหตุผล แล้วบันทึกไฟล์ Linux lock ที่ซ้อมได้. อย่าลบแพ็กเกจที่ application ต้องใช้เพื่อให้ build ผ่าน
4. ตรวจว่าการ start API ไม่ต้องมี schema.sql/sample JSON ใน image เพราะ seed ทำไปแล้วบน database ฝึก

**Checkpoint:** ชี้ได้ว่า secret เข้า runtime ภายหลัง ไม่ถูก pack ไปกับ code และทุกไฟล์ COPY มีอยู่จริง

## Practice 2 — รันกล่องเดียวกันในเครื่อง

<PracticeIllustration asset="d04-e01-p02" />

**Primary target:** เรียก API ที่รันใน Docker แล้วพบข้อมูลเดิมได้

### Steps

1. หยุด uvicorn เดิมเพื่อคืน port 8000. จาก root ให้ Codex build:

   ~~~shell
   docker build -f api/Dockerfile -t service-desk-api:day4-v1 .
   ~~~
2. ผู้เรียนรัน container เองโดยไม่แสดงเนื้อหา .env:

   ~~~shell
   docker run --rm --name service-desk-api-local -p 127.0.0.1:8000:8000 --env-file api/.env service-desk-api:day4-v1
   ~~~

   Docker อ่าน env file โดยตรง; ให้ค่าทั้งสามใน .env ไม่มี quote ครอบที่กลายเป็นส่วนหนึ่งของค่า
3. เปิด /health และ /docs ผ่าน port เดิม. Login และค้น UUID ที่สร้างเมื่อวาน
4. รัน API check script จาก terminal อีกหน้าต่างด้วยรหัสผ่านทดลองของตน
5. ดู container log ว่ามี request/status แต่ไม่มี token/password. จบแล้ว Ctrl+C หรือ **docker stop service-desk-api-local**

**Checkpoint:** /health และ authenticated DB operations ผ่านใน container ไม่ใช่เผลอเรียก uvicorn ตัวเก่า

**ถ้าติดขัด:** Connection refused ให้ตรวจ bind host/port. Docker build บน Apple Silicon ใช้ทดสอบ local ได้; image สำหรับ Azure จะ build บน ACR ใน Exercise 2 จึงไม่เอา image arm64 ในเครื่องไปใช้โดยไม่ตรวจ architecture
