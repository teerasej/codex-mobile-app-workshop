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

**Primary target:** ใช้ Dart class และ null safety อ่านคำขอหนึ่งรายการได้

### Steps

1. จาก root ให้ Codex ตรวจว่าไม่มี client เดิม แล้วรัน:

   ~~~shell
   flutter create --platforms=web,android --project-name service_desk_lite client
   ~~~

   ถ้ามี client อยู่แล้ว ให้ตรวจและใช้ต่อ ไม่สร้างทับ
2. ส่ง:

   ~~~text
   อ่าน docs/api-contract.md และ data/service-requests.json จาก root
   สร้าง client/lib/models/service_request.dart มี class ServiceRequest
   สร้าง fromJson ให้ใช้ชนิดข้อมูล/null safety ตรง contract
   required fields ห้ามกลบข้อมูลที่ขาดด้วย empty string หรือค่าปลอม
   เพิ่ม Dart unit test อ่าน sample ที่ถูกต้องและ reject JSON ที่ไม่มี id
   ยังไม่เชื่อม API และยังไม่ทำ UI
   ~~~
3. ให้ Codex ชี้ความต่างระหว่าง String กับ String? และอธิบายว่า data ที่จำเป็นหายควรแสดง error แทนแต่งค่าเอง
4. ให้รัน test ของ model จาก client. ตรวจหนึ่งชื่อ/สถานะกับ JSON จริง

**Checkpoint:** sample ที่ถูกแปลงได้ ส่วน required id ที่หายทำให้ test ตรวจพบ

## Practice 2 — ประกอบ My requests ด้วย Widgets

<PracticeIllustration asset="d03-e01-p02" />

**Primary target:** แสดงข้อมูลตัวอย่างเป็นรายการที่อ่านง่ายได้

### Steps

1. ส่ง:

   ~~~text
   สร้างหน้าจอ My requests สำหรับ Service Desk Lite ด้วย Material widgets
   ใช้ sample เฉพาะ owner learner01 จาก data/service-requests.json
   คัดลอก fixture ไป client/assets และประกาศ asset ใน pubspec.yaml
   ใช้ ServiceRequest model ที่มีอยู่ แสดง title/category/status
   ข้อความ UI ภาษาไทย; ใส่ป้าย “ข้อมูลตัวอย่าง” ให้ชัด
   แยก widget สำหรับหนึ่งรายการ; ไม่เรียก API และไม่ hardcode secret
   ~~~
2. ให้รัน:

   ~~~shell
   flutter run -d chrome --web-hostname localhost --web-port 3000
   ~~~
3. ตรวจว่ามี 3 รายการ และชื่อแรกตรง sample. ปรับขนาด browser ให้แคบใกล้มือถือ
4. ถ้าเกิด overflow ส่งภาพเฉพาะหน้าจอทดลองให้ Codex แก้ layout จุดนั้น. อย่าให้เขียนแอปใหม่ทั้งหมด

**Checkpoint:** เห็น title/category/status ครบโดยไม่ล้นหน้าจอ และรู้ว่ายังเป็นข้อมูลตัวอย่าง
