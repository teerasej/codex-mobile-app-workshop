---
title: "Day 3 · Exercise 3 — เชื่อม API กับงานของผู้ใช้"
prev: {"text": "Exercise 2", "link": "/exercises/day-03-flutter/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-03-flutter/exercise-04"}
---

# Exercise 3 — เชื่อม API กับงานของผู้ใช้


> **Day 3 · Flutter · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-03-flutter/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

ตอนนี้แบบฟอร์มต้องคุยกับทะเบียนงานจริง เราจะเอาข้อมูลตัวอย่างออกจากเส้นทางใช้งานหลัก และใช้ login ที่ทำเมื่อวาน

## Practice 1 — Sign in แล้วโหลดคำขอของตน

<PracticeIllustration asset="d03-e03-p01" eager />

**Primary target:** เปิดรายการของผู้ใช้จาก authenticated API ได้

### Steps

1. เปิด API ใน terminal ที่สองจาก root ด้วยคำสั่ง Day 2. ตรวจ /health และ login ใน /docs ว่ายังทำงาน
2. ให้ Codex เพิ่ม package http ด้วย **flutter pub add http** จาก client
3. ส่ง prompt:

   ~~~text
   เพิ่ม ApiService ที่รับ http.Client สำหรับทดสอบ และ API_BASE_URL จาก
   String.fromEnvironment ไม่มี default ชี้ไป cloud ที่ไม่ทราบ
   เพิ่ม Sign in screen ส่ง form username/password ไป POST /auth/token
   เก็บ bearer token ใน memory; ส่ง Authorization header เมื่อ GET /requests
   อย่า log token/password และล้าง token เมื่อ logout/401
   โหลดเฉพาะรายการที่ API ส่งกลับ ไม่ filter owner แทนการตรวจฝั่ง server
   เปลี่ยน runtime จาก fixture เป็น API; fixture ใช้เฉพาะ test
   ถ้าไม่ได้ตั้ง API_BASE_URL ให้แสดงข้อความแนะนำ ไม่ crash
   ฝั่ง FastAPI เพิ่ม CORS_ORIGINS ตาม contract สำหรับ http://localhost:3000
   ให้แสดง diff ของ client และ API แยกกัน
   ~~~
4. Restart API หลังแก้ CORS. หยุด Flutter run เดิมแล้วเปิดใหม่:

   ~~~shell
   flutter run -d chrome --web-hostname localhost --web-port 3000 --dart-define=API_BASE_URL=http://127.0.0.1:8000
   ~~~
5. ผู้เรียนใส่รหัสผ่านเองใน UI. Login learner01 แล้วเทียบรายการกับ /docs
6. Logout แล้ว login learner02. ต้องไม่เห็นคำขอที่ learner01 เพิ่งสร้าง

**Checkpoint:** ป้ายข้อมูลตัวอย่างหายจาก runtime, ใช้ข้อมูลจริงจาก API, เปลี่ยนผู้ใช้แล้วรายการเปลี่ยนตามเจ้าของ

## Practice 2 — ส่งคำขอและติดตามสถานะจากหน้าจอ

<PracticeIllustration asset="d03-e03-p02" />

**Primary target:** ทำวงจรสร้างคำขอถึงอัปเดตสถานะผ่าน API ได้

### Steps

1. ส่ง:

   ~~~text
   เพิ่ม CreateRequestScreen พร้อม title/description/category form
   Validate ตาม contract, POST JSON โดยไม่ส่ง owner/id/status
   ระหว่างส่ง disable submit กันกดซ้ำ; ไม่ retry POST อัตโนมัติ
   เมื่อสำเร็จกลับ list แล้ว refresh จาก API
   ใน detail เพิ่มเปลี่ยน status ตามสามค่าของ contractด้วย PATCH
   หลัง PATCH refresh ข้อมูลที่ API ยืนยัน ไม่แสดงสำเร็จก่อน response
   ใช้ ApiService เดิม ไม่เปลี่ยน field/route
   ~~~
2. สร้างคำขอชื่อ **ทดสอบส่งจาก Flutter** พร้อมรายละเอียดอย่างน้อย 10 ตัวอักษร
3. ไป list → detail จด UUID แล้วเปิด /docs ตรวจ UUID เดียวกันด้วยผู้ใช้คนเดียวกัน
4. เปลี่ยน status เป็น in_progress และ done. Refresh browser, login ใหม่ถ้าจำเป็น, ตรวจว่ายังเป็น done
5. ลอง title ว่าง ต้องเห็นข้อความใกล้ช่องกรอกและไม่สร้างรายการใหม่

**Checkpoint:** UI กับ API มี UUID/status เดียวกัน และหนึ่งการกดไม่เพิ่มรายการซ้ำ

## Practice 3 — บอกผู้ใช้เมื่อกำลังรอหรือเกิดปัญหา

<PracticeIllustration asset="d03-e03-p03" />

**Primary target:** แสดง UI states ที่สะท้อนผลการเรียก API จริงได้

### Steps

1. ส่ง:

   ~~~text
   ตรวจ states ของ ApiService/screens:
   loading ต้องเห็น progress, empty ต้องมีคำแนะนำ,
   error ต้องมีข้อความอ่านรู้เรื่องและปุ่ม Retry, success ต้องมีข้อมูล
   timeout 10 วินาที; 401 กลับ Sign in; 422 ผูกกับ field ถ้าระบุได้
   ไม่แสดง raw stack trace และไม่ log bearer token
   เพิ่ม tests ผ่าน injected http.Client/fake responses สำหรับ 200-empty, 401,
   422, 503 และ timeout. ห้ามเรียก network จริงใน tests
   ~~~
2. ระหว่าง login อยู่ ให้หยุด API แล้วกด Refresh ใน app. ต้องเห็น error/Retry แทนหน้าเงียบหรือโหลดไม่จบ
3. เปิด API ใหม่แล้ว Retry. ต้องได้ข้อมูลกลับมา; หาก token หมดอายุให้ Sign in ใหม่
4. ให้ Codex ใช้ test fixture เพื่อพิสูจน์ loading และ empty โดยไม่ลบข้อมูลใน DB. รัน tests แล้วบันทึกว่ากรณีไหนทดสอบด้วย UI จริง/กรณีไหนด้วย fake response

**Checkpoint:** มีหลักฐานทั้ง loading/empty/error/success และหลัง API กลับมาผู้ใช้ทำต่อได้

**ถ้าติดขัด:** Browser error แต่ /docs ทำงานให้ตรวจ origin/port และ CORS ก่อนแก้ auth. 401 ให้ตรวจ token lifecycle; 422 ให้ตรวจ schema. ไม่แก้ด้วย allow-all หรือใส่ database password ใน Flutter
