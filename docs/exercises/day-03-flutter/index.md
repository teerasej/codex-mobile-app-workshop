---
title: "Day 3 — นำบริการมาอยู่ในมือผู้ใช้"
prev: {"text": "สรุป Day 2", "link": "/exercises/day-02-api/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-03-flutter/exercise-01"}
---

# Day 3 — นำบริการมาอยู่ในมือผู้ใช้

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-02-api/) · [วันถัดไป](/exercises/day-04-azure/)

## Overview theme

วันนี้เรานำ API มาใส่หน้าจอที่ใช้งานได้จริง เริ่มจากมองเห็นใบงาน แล้วค่อยเชื่อมข้อมูล. Widget เปรียบเหมือนชิ้นส่วนเคาน์เตอร์ ส่วน State คือป้ายที่บอกว่ากำลังรอข้อมูล ว่าง มีปัญหา หรือพร้อมให้บริการ

**ผลท้ายวัน:** Flutter Sign in, list/detail, create/update และ UI states ทำงานกับ API เดิม; มี browser preview และ Android debug app

**ทางเลือกสำหรับ Mac ที่พร้อม:** หลังผ่านกิจกรรมหลักและยังมีเวลา ลองรันและ build แอปเดิมสำหรับ iPhone Simulator ใน Exercise 4 · Practice 3. ข้ามได้โดยไม่เสีย checkpoint หลัก

**Prerequisites:** ผ่าน API/auth/persistence Day 2, Flutter/Chrome/Android toolchain พร้อมตาม [readiness](/resources/readiness), รหัสผ่านทดลองสองบัญชี. Flutter ไม่ต้องรู้ database password

> **License:** Flutter/Dart ไม่ต้องซื้อ paid license. ต้องมีสิทธิ์ Codex. ใช้ Android debug build ไม่ต้องมี Google Play developer account; iOS Simulator เสริมไม่ต้องสมัคร Apple Developer แบบเสียเงินหรือตั้งค่า signing. วันนี้ไม่เผยแพร่แอปขึ้น store

| เวลา | Exercise | อธิบาย / ลงมือ / ตรวจและแก้ |
| --- | --- | --- |
| 09:30–10:30 | 1. Dart และหน้าจอแรก | 15 / 35 / 10 นาที |
| 10:45–12:00 | 2. Navigation และ State | 10 / 50 / 15 นาที |
| 13:00–14:30 | 3. เชื่อม API กับงานของผู้ใช้ | 10 / 60 / 20 นาที |
| 14:45–16:00 | 4. Native plugin และ mobile build | 10 / 45 / 20 นาที |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00

Practice เสริม iOS ใช้เวลาที่เหลือหลังงานหลักในช่วงเดิม ประมาณ 10–15 นาทีเมื่อเครื่องพร้อม; เวลา build ขึ้นกับเครื่อง เตรียม [Xcode และ Simulator ก่อนเรียน](/resources/readiness#ios-simulator-optional); ถ้าไม่พร้อมให้ข้ามและเก็บเวลาสรุปท้ายวัน

## จุดเริ่มและโครงสร้างวันนี้

ให้ Codex pull main แล้วสร้าง branch **feature/flutter-client**. โค้ด Flutter อยู่ **client/**; API เดิมอยู่ **api/**. ใช้ Dart model ใน client/lib/models, API service ใน client/lib/services และ screens ใน client/lib/screens. เริ่มด้วย StatefulWidget/setState ตามความจำเป็น ไม่เพิ่ม state-management framework หลายตัว

ก่อนทำแต่ละ prompt ให้ตรวจแผนและขอบเขตตาม AGENTS.md. คำสั่ง flutter ให้รันจาก **client/** เว้นแต่ระบุเป็นอย่างอื่น

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. Dart และหน้าจอแรก](/exercises/day-03-flutter/exercise-01)
- [10:45–12:00 · 2. Navigation และ State](/exercises/day-03-flutter/exercise-02)
- [13:00–14:30 · 3. เชื่อม API กับงานของผู้ใช้](/exercises/day-03-flutter/exercise-03)
- [14:45–16:00 · 4. Native plugin และ mobile build](/exercises/day-03-flutter/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-03-flutter/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ
