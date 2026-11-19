---
title: "Day 3 — นำบริการของเรา มาอยู่ในมือผู้ใช้ ด้วย Flutter"
prev: {"text": "สรุป Day 2", "link": "/exercises/day-02-api/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-03-flutter/exercise-01"}
---

# Day 3 — นำบริการของเรา มาอยู่ในมือผู้ใช้ ด้วย Flutter

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-02-api/) · [วันถัดไป](/exercises/day-04-azure/)

## Overview theme

วันนี้เรานำ API มาใส่หน้าจอแอป เริ่มจากข้อมูลตัวอย่างที่เห็นผลทันที แล้วค่อยเชื่อมบริการจริง เหมือนจัดหน้าร้านให้พร้อมก่อนเปิดรับงานจากเคาน์เตอร์


**ผลลัพธ์:** Flutter ใช้ Dio เชื่อม Sign in, list/detail, create/update และ UI states กับ API เดิม; มี browser preview และ Android debug app

**ทางเลือกสำหรับ Mac ที่พร้อม:** หลังผ่านกิจกรรมหลักและยังมีเวลา ลองรันและ build แอปเดิมสำหรับ iPhone Simulator ใน Exercise 4 · Practice 3. ข้ามได้โดยไม่เสีย checkpoint หลัก

**Prerequisites:** โฟลเดอร์ `service-desk-lite` เดิม, Flutter/Edge/Android toolchain ตาม [readiness](/resources/readiness), API ที่ผ่าน auth/ownership/PostgreSQL ใน Day 2 และรหัสผ่านทดลองสองบัญชี Flutter ไม่ต้องรู้ database password

> **License:** Flutter/Dart ไม่ต้องซื้อ paid license. ต้องมีสิทธิ์ Codex. ใช้ Android debug build ไม่ต้องมี Google Play developer account; iOS Simulator เสริมไม่ต้องสมัคร Apple Developer แบบเสียเงินหรือตั้งค่า signing. วันนี้ไม่เผยแพร่แอปขึ้น store

| เวลา | Exercise |
| --- | --- |
| 09:30–10:30 | 1. Dart และหน้าจอแรก |
| 10:45–12:00 | 2. Navigation และ State |
| 13:00–14:30 | 3. เชื่อม API กับงานของผู้ใช้ |
| 14:45–16:00 | 4. Native plugin และ mobile build |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00

Practice เสริม iOS ใช้เวลาที่เหลือหลังงานหลักในช่วงเดิม ประมาณ 10–15 นาทีเมื่อเครื่องพร้อม; เวลา build ขึ้นกับเครื่อง เตรียม [Xcode และ Simulator ก่อนเรียน](/resources/readiness#ios-simulator-optional); ถ้าไม่พร้อมให้ข้ามและเก็บเวลาสรุปท้ายวัน

## จุดเริ่มและโครงสร้างวันนี้

1. เปิดโฟลเดอร์ `service-desk-lite` เป็น local project ใน Codex แล้วส่ง prompt นี้ก่อนเริ่ม ไม่ต้องพิมพ์คำสั่ง Git เอง

   ~~~text
   อ่าน AGENTS.md แล้วตรวจแบบ read-only ว่านี่คือ root ของ service-desk-lite
   ตรวจ branch/working tree, docs/api-contract.md, data/service-requests.json และ api/ จาก Day 2
   ตรวจ flutter --version, flutter doctor -v และ flutter devices โดยไม่ติดตั้งเครื่องมือ
   สรุปสิ่งที่พร้อมและยังไม่พร้อม ห้าม reset, clean, stash หรือเขียนทับงานเดิม
   ถ้ามีงานค้างให้หยุดและบอกไฟล์ที่ต้องตรวจ ก่อน pull หรือเปลี่ยน branch
   ~~~

2. เมื่อยืนยันว่าไม่มีงานค้าง ส่ง prompt นี้ หากชื่อ branch มีอยู่แล้ว ให้ใช้ต่อหลังตรวจว่าเป็นงานวันนี้

   ~~~text
   ช่วยนำ main ล่าสุดมาใช้ตาม workflow Day 1 แล้วสร้าง feature/flutter-client
   ถ้ามี branch นี้แล้วให้ตรวจและใช้ต่อ ไม่ลบหรือสร้างทับ
   ถ้า pull/เปลี่ยน branch ไม่ได้ให้แจ้งเหตุผลและหยุด ไม่ force หรือ reset
   ~~~

3. ทำ Exercise 1–2 ด้วย **ไฟล์ตัวอย่าง (fixture)** จึงยังไม่ต้องเปิด API ก่อน Exercise 3 ตรวจ API ตามจุดเริ่มของหน้านั้น ถ้า auth หรือ PostgreSQL ยังไม่พร้อม ให้กลับไปทำ Day 2 ส่วนนั้นก่อน

| ส่วนของโปรเจกต์ | ใช้ทำอะไร |
| --- | --- |
| `api/` | API เดิมจาก Day 2 |
| `client/lib/models/` | รูปร่างข้อมูล Dart |
| `client/lib/services/` | `ApiService` กลางที่ใช้ Dio ตั้งแต่ Exercise 3 |
| `client/lib/screens/` | หน้าจอที่ใช้ model/service เดิมร่วมกัน |

ส่ง prompt ทีละก้อน รอดูผลและ diff ก่อนขั้นถัดไป ใช้ `StatefulWidget`/`setState` ตามจำเป็น ไม่เพิ่มหลาย framework คำสั่ง Flutter ทำใน `client/`; Codex จะบอกตำแหน่งก่อนรัน

> **Browser วันนี้:** ใช้ Edge ในโปรไฟล์ของตนเองที่ถูกต้อง Windows ใช้ target `edge`; macOS ใช้ `web-server` แล้วเปิด URL ใน Edge ด้วยตนเอง วิธีหลังมี debugging จำกัด ทั้งสองแบบใช้ `http://localhost:3000` เหมือนกัน ถ้าพอร์ตถูกใช้อยู่ ให้ตรวจว่าเป็นงานใดก่อน ไม่ปิด process ที่ไม่รู้จักหรือเปลี่ยนพอร์ตเอง

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. Dart และหน้าจอแรก](/exercises/day-03-flutter/exercise-01)
- [10:45–12:00 · 2. Navigation และ State](/exercises/day-03-flutter/exercise-02)
- [13:00–14:30 · 3. เชื่อม API กับงานของผู้ใช้](/exercises/day-03-flutter/exercise-03)
- [14:45–16:00 · 4. Native plugin และ mobile build](/exercises/day-03-flutter/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-03-flutter/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ
