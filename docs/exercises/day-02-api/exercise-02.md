---
title: "Day 2 · Exercise 2 — Route, model และ validation"
prev: {"text": "Exercise 1", "link": "/exercises/day-02-api/exercise-01"}
next: {"text": "Exercise 3", "link": "/exercises/day-02-api/exercise-03"}
---

# Exercise 2 — Route, model และ validation


> **Day 2 · Python API · 10:45–12:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

::: tip วิธีทำงานวันนี้
ก่อนเริ่ม Exercise 1 ให้ Codex สร้าง branch **feature/request-api** จาก main ที่ไม่มีงานค้างเพียงครั้งเดียว. ถ้าอยู่ branch นี้จาก Practice ก่อนแล้วให้ใช้ต่อ ไม่สร้างซ้ำและไม่กลับไปเริ่มจาก main ใหม่. ทุก Practice เริ่มด้วยตรวจ plan และจบด้วย checkpoint → commit เฉพาะไฟล์ที่ตรวจแล้ว. ยังไม่ merge จนจบวัน

คำสั่ง **python** ต่อจากสร้าง environment หมายถึง Python ใน **.venv** ของโปรเจคเท่านั้น. หาก Codex เปิด terminal ใหม่ ให้ยืนยัน interpreter นี้ก่อนรัน. ผู้เรียนไม่จำเป็นต้องจำคำสั่ง แต่ต้องรู้ว่าเป็นการติดตั้ง รัน server หรือรัน test
:::


## Scenario

คนกรอกแบบฟอร์มอาจลืมใส่รายละเอียด เราต้องให้ API บอกว่าอะไรไม่ถูก ก่อนเก็บลงทะเบียนงาน

## Practice 1 — สร้างและอ่านคำขอผ่าน routes

<PracticeIllustration asset="d02-e02-p01" eager />

**Primary target:** ส่ง JSON สร้างคำขอและอ่านรายการที่เพิ่งสร้างได้

### Steps

1. เปิด docs/api-contract.md และอ่านเฉพาะ data model กับ endpoints
2. ส่ง prompt:

   ~~~text
   สร้าง routes GET /requests, GET /requests/{id}, POST /requests
   และ PATCH /requests/{id}/status ตาม contract
   ใน Practice นี้ใช้ in-memory repository ชั่วคราวและ owner learner01 เท่านั้น
   ใส่ comment ว่า development-only และต้องแทนด้วย DB/auth วันนี้
   เก็บชื่อ route/field/status ให้ตรง contract; UUID กับ created_at ให้ server สร้าง
   ใช้ Pydantic request/response models. ยังไม่สร้าง UI หรือ Azure resources
   ~~~
3. ใน /docs ขยาย **POST /requests** แล้วเลือก **Try it out**. คลิกช่อง **Request body** แล้วเลือกข้อความทั้งหมดด้วย **Ctrl+A** บน Windows หรือ **Cmd+A** บน macOS ก่อนวาง JSON ด้านล่างเพื่อแทนตัวอย่างเดิมทั้งหมด จากนั้นเลือก **Execute**. อย่าวางต่อท้าย JSON เดิม:

   ~~~json
   {
     "title": "ขอจอภาพสำหรับห้องอบรม",
     "description": "ขอจอภาพหนึ่งเครื่องสำหรับใช้ฝึกในห้องตัวอย่าง",
     "category": "equipment"
   }
   ~~~
4. จด id ที่ server ตอบ. เรียก GET /requests/{id} ด้วย id นั้น แล้วดูชื่อ/สถานะ new
5. ทดลอง PATCH status เป็น in_progress แล้ว GET อีกครั้ง

**Checkpoint:** POST ได้ 201, GET/PATCH ได้ 200 และแสดง id เดียวกัน. ขณะนี้ข้อมูลยังหายเมื่อ restart ได้ จึงยังไม่ผ่าน persistence

## Practice 2 — ปฏิเสธข้อมูลที่ไม่เข้าเกณฑ์

<PracticeIllustration asset="d02-e02-p02" />

**Primary target:** ตรวจว่า API รับเฉพาะข้อมูลที่ contract อนุญาตได้

### Steps

1. ส่ง:

   ~~~text
   ตรวจและเติม validation ของ models ให้ตรง docs/api-contract.md
   trim ก่อนตรวจความยาว; reject unknown fields
   ทดสอบ title ว่าง/สั้น, category ผิด, status ผิด และ client-supplied owner_username
   แสดงกรณีที่พบว่าขาดก่อนแก้ และห้ามลด validation เพื่อให้ test ผ่าน
   ~~~
2. ลอง POST ที่ title เป็นช่องว่าง และรายละเอียดถูกต้อง ต้องได้ 422
3. ลอง POST ที่เพิ่ม "owner_username": "learner02" ต้องได้ 422
4. ลอง PATCH status เป็น closed ต้องได้ 422; ใช้ done จึงผ่าน
5. เปิด /openapi.json และค้น CreateRequest หรือชื่อ schema ที่ Codexใช้. ชี้ว่า /docs อ่านรูปแบบ API จาก schema นี้

**Checkpoint:** valid input ผ่าน แต่สามกรณีผิดถูกปฏิเสธพร้อมตำแหน่ง field. ไม่แก้ field ใน Flutter ในอนาคตเพื่อหลบ contract ที่ไม่ตรง

**ถ้าติดขัด:** ถ้า response ไม่มี 422 ให้ตรวจ Pydantic model และ route annotation กับ Codex. ส่งเฉพาะ request ตัวอย่างและ error ที่ไม่มี secret
