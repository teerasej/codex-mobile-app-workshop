---
title: "Day 2 · Exercise 2 — Route, model และ validation"
prev: {"text": "Exercise 1", "link": "/exercises/day-02-api/exercise-01"}
next: {"text": "Exercise 3", "link": "/exercises/day-02-api/exercise-03"}
---

# Exercise 2 — Route, model และ validation


> **Day 2 · Python API · 10:45–12:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Practice 1 — สร้างและอ่าน Request ผ่าน routes

<PracticeIllustration asset="d02-e02-p01" eager />

**Primary target:** ส่ง JSON สร้าง Request และอ่านรายการที่เพิ่งสร้างได้

### Steps

1. **อ่าน API contract**

   ~~~text
   อ่าน data model กับ endpoints ใน docs/api-contract.md แล้วสรุปเราจะสร้าง route API สำหรับการทำงานกับข้อมูล Request ยังไงบ้าง แสดง route ที่จำเป็น และ field ใน request และส่ง response อะไรบ้าง
   ~~~

2. **ทำ routes สำหรับสร้างและอ่าน**

   ~~~text
   สร้าง route ตามที่ออกแบบ
   เก็บข้อมูลตอนนี้ใน memory ชั่วคราว ใส่ comment ว่าเป็น development-only
   ~~~

3. **สร้าง Request ใน Swagger UI**

   เปิด swagger UI
   แล้วเลือก **POST /requests → Try it out**. แทนที่ JSON ใน **Request body** ทั้งหมดด้วยตัวอย่างนี้ แล้วกด **Execute**. จด UUID จาก response 201

   ~~~json
   {
     "title": "ขอจอภาพสำหรับห้องอบรม",
     "description": "ขอจอภาพหนึ่งเครื่องสำหรับใช้ฝึกในห้องตัวอย่าง",
     "category": "equipment"
   }
   ~~~

4. **อ่าน Request เดิม**

   เรียก `GET /requests/{id}` ด้วย UUID ที่จดไว้ เช็กชื่อและสถานะ `new`

5. **เปลี่ยนสถานะ**

   เรียก `PATCH /requests/{id}/status` ด้วย UUID เดิม

   ~~~json
   {"status": "in_progress"}
   ~~~

6. **เช็กสถานะใหม่**

   เรียก `GET /requests/{id}` อีกครั้ง เช็กว่า UUID เดิมมีสถานะ `in_progress`

**Checkpoint:** POST ได้ 201, GET/PATCH ได้ 200 และแสดง id เดียวกัน. ขณะนี้ข้อมูลยังหายเมื่อ restart ได้ จึงยังไม่ผ่าน persistence

## Practice 2 — ปฏิเสธข้อมูลที่ไม่เข้าเกณฑ์

<PracticeIllustration asset="d02-e02-p02" />

**Primary target:** ตรวจว่า API รับเฉพาะข้อมูลที่ contract อนุญาตได้

### Steps

1. **หากฎที่ขาด**

   ~~~text
   เทียบ Pydantic models ที่มี กับ docs/api-contract.md สรุปว่ากฎเรื่อง trim, ความยาว, category, status และ field ที่ client ส่งได้ยังขาดตรงไหน
   ~~~

2. **เติม validation**

   ~~~text
   เติม validation rule ที่ขาดตาม contract ที่กำหนดไว้
   ~~~

3. **ลองส่ง title ว่าง**

   ใช้ JSON จาก Practice 1 แล้วแก้เฉพาะ `title` ให้เป็นช่องว่าง ส่ง POST และหา `title` ในรายละเอียดของ 422

   ~~~json
   {
     "title": "   ",
     "description": "ขอจอภาพหนึ่งเครื่องสำหรับใช้ฝึกในห้องตัวอย่าง",
     "category": "equipment"
   }
   ~~~

4. **ลองส่ง owner เอง**

   ใช้ JSON เดิมที่ถูกต้อง แล้วเพิ่ม field `owner_username` ส่ง POST และหา `owner_username` ในรายละเอียดของ 422

   ~~~json
   {
     "title": "ขอจอภาพสำหรับห้องอบรม",
     "description": "ขอจอภาพหนึ่งเครื่องสำหรับใช้ฝึกในห้องตัวอย่าง",
     "category": "equipment",
     "owner_username": "learner02"
   }
   ~~~

5. **สร้าง Request สำหรับทดสอบ**

   ส่ง POST ด้วย JSON ที่ถูกต้องจาก Practice 1 เช็ก 201 และจด UUID ใหม่

   ~~~json
   {
     "title": "ขอจอภาพสำหรับห้องอบรม",
     "description": "ขอจอภาพหนึ่งเครื่องสำหรับใช้ฝึกในห้องตัวอย่าง",
     "category": "equipment"
   }
   ~~~

6. **ลองส่งสถานะผิด**

   ใช้ UUID ใหม่ส่ง PATCH แล้วหา `status` ในรายละเอียดของ 422

   ~~~json
   {"status": "closed"}
   ~~~

7. **ลองส่งสถานะที่ถูกต้อง**

   ใช้ UUID เดิมส่ง PATCH แล้วเช็ก 200

   ~~~json
   {"status": "done"}
   ~~~

8. **ดู schema ใน OpenAPI**

   เปิด `/openapi.json` ค้น `CreateRequest` หรือชื่อ model ที่ Codex ใช้ แล้วเทียบ field กับ **Request body** ใน `/docs`

**Checkpoint:** valid input ผ่าน แต่สามกรณีผิดถูกปฏิเสธพร้อมตำแหน่ง field. ไม่แก้ field ใน Flutter ในอนาคตเพื่อหลบ contract ที่ไม่ตรง

**ถ้าติดขัด:** ถ้าไม่ได้ 422 ให้ส่งเฉพาะ JSON ตัวอย่างและ HTTP status ที่เห็น แล้วถาม Codex

~~~text
กรณีนี้ควรได้ 422 ช่วยตามให้ดูว่า route นี้ใช้ Pydantic model ไหน และกฎที่ขาดอยู่ตรงไหน ยังไม่ต้องแก้ไฟล์
~~~
