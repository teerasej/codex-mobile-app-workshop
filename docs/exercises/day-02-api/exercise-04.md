---
title: "Day 2 · Exercise 4 — Login, ownership และ tests"
prev: {"text": "Exercise 3", "link": "/exercises/day-02-api/exercise-03"}
next: {"text": "สรุปท้ายวัน", "link": "/exercises/day-02-api/summary"}
---

# Exercise 4 — Login, ownership และ tests


> **Day 2 · Python API · 14:45–16:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Practice 1 — ป้องกัน routes ด้วย token

<PracticeIllustration asset="d02-e04-p01" eager />

**Primary target:** ให้ผู้ใช้เข้าถึงได้เฉพาะ Request ของตนตาม token ที่ตรวจสอบแล้ว

### Steps

1. **เพิ่ม Login**

   ~~~text
   อยากให้ผู้ใช้ Login แล้วได้ token ช่วยเสนอแผนทำ POST /auth/token ตาม docs/api-contract.md
   โดยให้รับ username/password จาก form
   ~~~

2. **ล็อก Request routes**

   ~~~text
   ให้แต่ละคนเปิดได้เฉพาะ Request ของตัวเอง กำหนด owner จาก token และกรองทุก Request route ตาม owner
   ใช้ 401 เมื่อ token หายหรือใช้ไม่ได้ และ 404 เมื่อ GET/PATCH UUID ของคนอื่น ตาม contract
   ~~~

3. **Restart API**

   เปิด `/docs` ใหม่หลัง server พร้อม

4. **ลองก่อน Login**

   เรียก `GET /requests` โดยยังไม่ **Authorize** ต้องได้ `401`

5. **เข้าเป็น learner01**

   กด **Authorize** แล้วกรอกบัญชี `learner01` กับรหัสผ่านที่ได้รับ (อยู่ใน Student ZIP ไฟล์ README.md)

6. **สร้าง Request**

   ลอง `POST /requests` แล้วจด UUID ของรายการที่มี owner เป็น `learner01`

   ตัวอย่าง JSON (ปรับตาม schema ใน `docs/api-contract.md`):

   ~~~json
   {
     "title": "Ownership test - ขอเปลี่ยนเมาส์ใหม่",
     "description": "เมาส์ประจำโต๊ะใช้งานไม่ได้ ต้องการเปลี่ยนและตรวจว่ารายการอยู่หลังเริ่ม API ใหม่",
     "category": "equipment"
   }
   ~~~

7. **เปลี่ยนเป็น learner02**

   เลือก **Logout** ในหน้าต่าง **Authorize** แล้วเข้าเป็น `learner02`

8. **ลอง Request ของคนอื่น**

   ลอง GET และ PATCH สถานะที่ถูกต้องกับ UUID เดิม ทั้งสองครั้งต้องได้ `404`

9. **กลับเป็น learner01**

   เลือก **Logout** แล้วเข้าเป็น `learner01` อีกครั้ง

10. **เปิด Request ของตัวเอง**

    เรียก GET ด้วย UUID เดิม ต้องได้ `200`

เก็บ password และ token ไว้ในเครื่อง หากผลต่างจากที่คาด ให้บอก Codex เฉพาะ route และ HTTP status

**Checkpoint:** ไม่มี token ได้ 401, ผู้ใช้อื่นได้ 404, เจ้าของได้ 200

## Practice 2 — สร้าง test ที่จับความผิดพลาดได้

<PracticeIllustration asset="d02-e04-p02" />

**Primary target:** รัน automated tests ที่ตรวจพฤติกรรม API โดยไม่แตะ Azure database ได้

### Steps

1. **เตรียม test แบบ offline**

   ~~~text
   ช่วยเสนอแผนตั้ง pytest ใน api/tests
   ใช้ FastAPI TestClient
   ~~~

2. **เพิ่มกรณี route และ validation**

   ~~~text
   ช่วยเขียน test ที่ตรวจ status และ response จริง
   เริ่มจาก health,
   create ที่ถูกต้องได้ 201
   title มีแต่ช่องว่างได้ 422
   เพิ่ม enum ที่ผิดและ owner ที่ client ส่งมาเอง ทั้งสองกรณีต้องได้ 422
   ~~~

3. **เพิ่มกรณี Login และ ownership**

   ~~~text
   เพิ่ม test ทดสอบ password ผิด และ token ที่หาย ใช้ไม่ได้ หรือหมดอายุ ได้ 401
   เพิ่ม test สำหรับ GET/PATCH ของคนอื่นได้ 404 ส่วนเจ้าของสร้าง อ่าน และเปลี่ยนสถานะได้สำเร็จ
   ~~~

4. **รัน pytest**

   รันจาก root แล้วดูจำนวน passed/failed ที่ได้จริง

   ~~~shell
   python -m pytest api/tests -q
   ~~~

5. **เก็บเวอร์ชันแพ็กเกจ**

   ~~~text
   ใช้ Python ใน .venv รัน python -m pip check แล้วบันทึกเวอร์ชันแพ็กเกจที่ใช้จริงลง api/requirements.lock.txt เป็น UTF-8 สำหรับ Docker ใน Day 4
   หยุดและแจ้งผลถ้า pip check ไม่ผ่าน และเช็กว่า lockfile ไม่มี path จากเครื่องนี้
   ~~~

6. **ส่งงานเข้า main**

   ตรวจ diff แล้ว commit, push และเปิด PR จาก `feature/request-api` ตามขั้นตอน Day 1 เมื่อ merge แล้ว จด commit ล่าสุดใน review log

**Checkpoint:** pytest ผ่านและมี `api/requirements.lock.txt` สำหรับ Day 4
