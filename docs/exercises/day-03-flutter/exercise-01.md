---
title: "Day 3 · Exercise 1 — Dart และหน้าจอแรก"
prev: {"text": "ภาพรวมวัน", "link": "/exercises/day-03-flutter/"}
next: {"text": "Exercise 2", "link": "/exercises/day-03-flutter/exercise-02"}
---

# Exercise 1 — Dart และหน้าจอแรก


> **Day 3 · Flutter · 09:30–10:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-03-flutter/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

เราจะให้ทีมเห็นหน้าตา My requests ก่อนเชื่อมระบบจริง เพื่อดูว่าข้อมูลสำคัญอยู่ครบหรือยัง

## Practice 1 — แปลง JSON เป็น Dart object

<PracticeIllustration asset="d03-e01-p01" eager />

**Primary target:** ใช้ Dart class และ null safety อ่าน Request หนึ่งรายการได้

### Steps

1. หลังผ่านจุดเริ่มในภาพรวม Day 3 ส่งให้ Codex สร้างส่วนหน้าจอในโปรเจกต์เดิม

   ~~~text
   เช็คก่อนว่ามีโฟลเดอร์ client อยู่แล้วหรือยัง
   ถ้ายังไม่มี ให้สร้างแอป Flutter ชื่อ service_desk_lite ใน client ให้รองรับ web กับ Android
   ถ้ามีแล้ว อย่าสร้างทับ บอกฉันว่าใช้ต่อได้ไหม
   เสร็จแล้วสรุปสิ่งที่ทำและแสดง diff
   ~~~
2. สร้าง model ให้ข้อมูลมีช่องตรงกับ API เหมือนใช้แบบฟอร์มเดียวกันทั้งหน้าร้านและเคาน์เตอร์

   ~~~text
   ดู docs/api-contract.md กับ data/service-requests.json แล้วสร้าง ServiceRequest model ให้อ่านข้อมูลใบงานได้
   ถ้ามี model เดิมอยู่แล้วให้ใช้ต่อ ถ้าข้อมูลที่จำเป็นหายหรือผิดชนิด ให้ error อย่าแต่งค่าขึ้นมาเอง
   ~~~
3. ขอคำอธิบายสั้น ๆ จากไฟล์ที่เพิ่งได้

   ~~~text
   อธิบายสั้น ๆ ว่า String กับ String? ใน Dart ต่างกันยังไง โดยยกตัวอย่างจาก model ที่เพิ่งสร้าง
   ~~~
4. ส่ง prompt ให้สร้างและรันการตรวจข้อมูล

   ~~~text
   เขียน test ให้ ServiceRequest model 2 กรณี
   1) อ่านใบงานหนึ่งรายการจาก data/service-requests.json แล้ว title กับ status ต้องตรงกับไฟล์
   2) ข้อมูลที่ไม่มี id ต้อง error ห้ามสร้างค่าสมมติ
   รัน test แล้วสรุปว่าผ่านกี่อัน พร้อมบอก title/status ที่ตรวจจริง
   ~~~

**Checkpoint:** JSON ตัวอย่างแปลงเป็น Dart ได้โดย title/status ตรงกับไฟล์ และ test ที่ขาด `id` ตรวจพบ error

## Practice 2 — ประกอบ My requests ด้วย Widgets

<PracticeIllustration asset="d03-e01-p02" />

**Primary target:** แสดงข้อมูลตัวอย่างเป็นรายการที่อ่านง่ายได้

### Steps

1. ส่ง prompt นี้ให้ประกอบหน้ารายการ โดยยังใช้ข้อมูลตัวอย่าง

   ~~~text
   สร้างหน้า My requests ของ Service Desk Lite แสดงใบงาน 3 รายการของ learner01 จาก data/service-requests.json
   ~~~
   ~~~text
   โชว์ title, category และ status ในแต่ละการ์ด ข้อความเป็นภาษาไทย และมีป้าย “ข้อมูลตัวอย่าง” ให้เห็นชัด
   ~~~
   ~~~text
   ใช้ model เดิม แยกการ์ดหนึ่งใบเป็น widget ของมันเอง
   ยังไม่ต้องเรียก API (ข้อมูลตัวอย่างต้องอยู่ในโฟลเดอร์ client เพื่อให้ web อ่านได้)
   แก้ test เดิมของแอปตัวอย่างให้เช็คหน้านี้แทน แล้วรัน test สรุปผลให้ดู
   ~~~
2. ส่ง prompt ให้เปิด preview แล้วเก็บหน้าต่างรันนี้ไว้ เรายังไม่ต้องใช้ API ใน Practice นี้

   ~~~text
   รันแอปบน web ที่ localhost:3000 ให้ฉันเปิดดูใน Edge
   ถ้ารันบน Mac ให้บอก URL ที่ต้องเปิดเอง
   ถ้าพอร์ตถูกใช้อยู่ ให้หยุดเฉพาะแอปของเราที่รันค้างไว้ ห้ามปิดอย่างอื่นหรือเปลี่ยนพอร์ตเอง ถ้าไม่แน่ใจให้ถามก่อน
   เสร็จแล้วบอก URL และวิธีหยุดแอปนี้
   ~~~
3. เปิด URL ใน Edge ตรวจว่ามี **3 รายการของ learner01** ชื่อแรกตรงกับไฟล์ตัวอย่าง แล้วลดความกว้าง browser ใกล้หน้าจอมือถือ
4. ถ้าข้อความล้น ส่งภาพเฉพาะหน้าจอทดลองพร้อม prompt นี้

   ~~~text
   ในภาพมีข้อความล้นจอ ช่วยแก้ให้ title, category และ status อ่านได้แม้หน้าจอแคบ
   แก้เฉพาะส่วนที่เกี่ยวข้อง ไม่ต้องแตะข้อมูลเดิม แล้วแสดง diff
   ~~~

**Checkpoint:** เห็น title/category/status ครบโดยไม่ล้นหน้าจอ และรู้ว่ายังเป็นข้อมูลตัวอย่าง
