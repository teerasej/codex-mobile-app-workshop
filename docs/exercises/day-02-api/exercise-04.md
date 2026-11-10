---
title: "Day 2 · Exercise 4 — Login, ownership และ tests"
prev: {"text": "Exercise 3", "link": "/exercises/day-02-api/exercise-03"}
next: {"text": "สรุปท้ายวัน", "link": "/exercises/day-02-api/summary"}
---

# Exercise 4 — Login, ownership และ tests


> **Day 2 · Python API · 14:45–16:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

::: tip วิธีทำงานวันนี้
ก่อนเริ่ม Exercise 1 ให้ Codex สร้าง branch **feature/request-api** จาก main ที่ไม่มีงานค้างเพียงครั้งเดียว. ถ้าอยู่ branch นี้จาก Practice ก่อนแล้วให้ใช้ต่อ ไม่สร้างซ้ำและไม่กลับไปเริ่มจาก main ใหม่. ทุก Practice เริ่มด้วยตรวจ plan และจบด้วย checkpoint → commit เฉพาะไฟล์ที่ตรวจแล้ว. ยังไม่ merge จนจบวัน

คำสั่ง **python** ต่อจากสร้าง environment หมายถึง Python ใน **.venv** ของโปรเจคเท่านั้น. หาก Codex เปิด terminal ใหม่ ให้ยืนยัน interpreter นี้ก่อนรัน. ผู้เรียนไม่จำเป็นต้องจำคำสั่ง แต่ต้องรู้ว่าเป็นการติดตั้ง รัน server หรือรัน test
:::


## Scenario

ทะเบียนคำขอมีเจ้าของแต่ละคน เราต้องตรวจบัตรผู้ใช้ก่อนเปิดใบงาน และใช้ test ช่วยเฝ้าประตูซ้ำทุกครั้งที่เปลี่ยน code

## Practice 1 — ป้องกัน routes ด้วย token

<PracticeIllustration asset="d02-e04-p01" eager />

**Primary target:** ให้ผู้ใช้เข้าถึงได้เฉพาะคำขอของตนตาม token ที่ตรวจสอบแล้ว

### Steps

1. ส่ง:

   ~~~text
   สร้าง POST /auth/token ด้วย form username/password ตาม contract
   ใช้ pwdlib verify hash, PyJWT HS256 จาก JWT_SECRET, sub และ exp 30 นาที
   เพิ่ม dependency ตรวจ token signature/expiry/user และ owner filter ทุก request route
   เอา owner ชั่วคราว learner01 ออกทั้งหมด; ไม่รับ owner จาก request body
   GET/PATCH UUID ของคนอื่นต้อง 404; missing/invalid token ต้อง 401
   ห้าม log password/hash/token. ไม่เพิ่ม sign-up, refresh token, role system หรือ SSO
   ~~~
2. Restart API; เปิด /docs ใหม่. GET /requests โดยยังไม่ authorize ต้องได้ 401
3. กด **Authorize** ใน /docs, ใส่ username/password ทดลองเองแล้ว authorize. อย่าส่ง token ให้ Codexอ่าน
4. ใช้ learner01 สร้างหนึ่งคำขอ จดเฉพาะ UUID และตรวจว่า owner เป็น learner01
5. Logout ใน Authorize แล้ว login learner02. GET UUID นั้นและ PATCH UUID นั้นต้อง 404
6. กลับ login learner01 แล้ว GET UUID เดิมต้อง 200

**Checkpoint:** ไม่มี token เข้าไม่ได้, คนอื่นเข้าไม่ได้, เจ้าของเข้าได้. เรายังไม่ได้สร้าง enterprise identity system; นี่คือ baseline ที่ฝึกตรวจได้

## Practice 2 — สร้าง test ที่จับความผิดพลาดได้

<PracticeIllustration asset="d02-e04-p02" />

**Primary target:** รัน automated tests ที่ตรวจพฤติกรรม API โดยไม่แตะ Azure database ได้

### Steps

1. ส่ง:

   ~~~text
   สร้าง pytest tests ใน api/tests และ pytest.ini ที่ root (pythonpath=api)
   ใช้ FastAPI TestClient และ dependency overrides/test doubles ไม่ต่อ Azure DB
   อย่าโหลด .env ตอน import app; tests inject dummy settings/key ผ่าน dependency
   ตรวจ: health; valid create=201; whitespace title=422; invalid enum=422;
   forged owner=422; missing token=401; bad password=401;
   invalid/expired token=401; another owner's GET/PATCH=404;
   own create/read/status update สำเร็จ. ห้ามใช้ secrets จาก .env ใน tests
   tests ต้องตรวจ response/status จริง ไม่ assert True หรือ snapshot ทั้ง code
   ~~~
2. รัน **python -m pytest api/tests -q**. อ่านจำนวน passed/failed จริง; ถ้าล้ม ให้เลือกแก้หนึ่ง failure และรันใหม่
3. ให้ Codex ทำ demonstration test failure แบบย้อนคืนได้ใน **test fixture** เท่านั้น เช่นเปลี่ยน expected HTTP status ของหนึ่ง test ให้ผิด รันแล้วเห็น fail จาก assertion ก่อนคืนค่าเดิมและรันผ่าน. ไม่แตะ auth production เพื่อโชว์ failure
4. ผู้เรียนรัน [API check script](/files/check_api.py) ที่มากับ starter ด้วยตนเอง (จะสร้างข้อมูลทดลอง 1 รายการ):

   ~~~shell
   python scripts/check_api.py --base-url http://127.0.0.1:8000
   ~~~

   Script รับ password ผ่าน getpass, ไม่พิมพ์ token และตรวจ API/ownership จริง. ถ้า UI terminal ไม่รองรับ hidden input ให้ใช้ native PowerShell/Terminal
5. เมื่อ tests ผ่าน ให้ Codex บันทึก exact dependency versions จาก .venv เป็น **api/requirements.lock.txt** ด้วย UTF-8 และรัน **python -m pip check**. ห้ามใช้ output redirect แบบ UTF-16 บน Windows PowerShell
6. ตรวจ diff และ log; commit/push/PR/merge ไป main. บันทึก test result, UUID persistence และ commit ล่าสุด. ปิด server ถ้าจบการเรียนแล้ว

**Checkpoint:** unit tests ผ่านโดยไม่ใช้ Azure, API check ผ่านกับฐานข้อมูลจริง และมี lockfile สำหรับ build วันถัดไป. ไม่ถือว่าแค่ install packages สำเร็จคือ test ผ่าน

# ถ้าวันนี้ยังทำไม่ครบ

ใช้ review log บอก Practice ล่าสุดที่ผ่าน และส่ง prompt recovery นี้กับ Codex ก่อนวันถัดไป:

~~~text
อ่าน docs/api-contract.md และ docs/review-log.md
ตรวจไฟล์ API ที่มีอยู่และ test ที่รันได้โดยไม่อ่าน .env
ทำตาราง ผ่านแล้ว/ยังขาด/หลักฐานที่ต้องตรวจ สำหรับ Day 2
เสนอแก้ทีละจุด ห้ามแทน database ด้วย mock ใน runtime เพื่อรายงานว่าผ่าน
~~~

ถ้า DB/auth ยังไม่ผ่าน Day 3 ทำ static UI กับ JSON ได้ แต่ต้องกลับมาผ่าน live integration ก่อนถือว่าจบโปรเจค
