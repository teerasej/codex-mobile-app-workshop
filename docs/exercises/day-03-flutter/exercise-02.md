---
title: "Day 3 · Exercise 2 — Navigation และ State"
prev: {"text": "Exercise 1", "link": "/exercises/day-03-flutter/exercise-01"}
next: {"text": "Exercise 3", "link": "/exercises/day-03-flutter/exercise-03"}
---

# Exercise 2 — Navigation และ State


> **Day 3 · Flutter · 10:45–12:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-03-flutter/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

คนใช้ต้องแตะใบงานเพื่อดูรายละเอียด แล้วกลับมารายการเดิมโดยไม่หลงทาง

## Practice 1 — เปิดรายละเอียดใบงานที่เลือก

<PracticeIllustration asset="d03-e02-p01" eager />

**Primary target:** เดินทางจาก list ไป detail ของรายการที่แตะและกลับได้

### Steps

1. ส่ง:

   ~~~text
   เพิ่ม RequestDetailScreen และ navigation จาก My requests
   ใช้ Navigator push/pop แบบง่าย ส่ง ServiceRequest ของรายการที่แตะ
   Detail แสดง id/title/description/category/status
   ยังใช้ fixture และยังไม่เชื่อม API
   เพิ่ม widget test แตะรายการที่สองแล้วเห็น description ของรายการที่สอง
   ~~~
2. เปิด preview แตะรายการที่สอง. เทียบ description/id กับ sample
3. กด Back แล้วเปิดรายการแรก. ตรวจว่าไม่ค้างข้อมูลรายการก่อนหน้า
4. ให้ Codex อธิบาย master-detail เทียบกับสารบัญและหน้ารายละเอียดในแฟ้มใบงาน

**Checkpoint:** แตะรายการไหนได้รายละเอียดของรายการนั้น และ Back ทำงาน

## Practice 2 — เปลี่ยนตัวกรองด้วย State

<PracticeIllustration asset="d03-e02-p02" />

**Primary target:** เปลี่ยน UI ตามค่าที่ผู้ใช้เลือกโดยไม่แก้ source data ได้

### Steps

1. ส่ง:

   ~~~text
   เพิ่ม filter บน My requests: ทั้งหมด/new/in_progress/done
   เก็บ selectedStatus ใน State และคำนวณรายการจากข้อมูลเดิม
   อย่า mutate fixture; แสดงจำนวนรายการหลังกรอง
   เพิ่ม empty widget เมื่อไม่มีผล และ reset filter กลับทั้งหมดได้
   แยก loading/empty/error/data เป็น state ที่ API service จะใช้ใน Exercise 3
   ~~~
2. เลือกแต่ละสถานะ; sample ของ learner01 ควรได้สถานะละ 1 รายการ
3. เลือกทั้งหมดแล้วกลับเป็น 3 รายการ. อย่าใช้ expected counts นี้หลังเริ่มเพิ่มข้อมูลจริง
4. ให้ Codex รัน widget test สำหรับ filter และ empty list โดยส่ง list ว่างผ่าน test fixture

**Checkpoint:** filter เปลี่ยนเฉพาะสิ่งที่แสดง ไม่เปลี่ยน status ของข้อมูล และ empty list ไม่ทำให้หน้าจอว่างแบบไม่มีคำอธิบาย
