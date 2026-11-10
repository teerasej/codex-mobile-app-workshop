---
title: "สรุป Day 3 — Flutter"
prev: {"text": "Exercise 4", "link": "/exercises/day-03-flutter/exercise-04"}
next: {"text": "ไป Day 4", "link": "/exercises/day-04-azure/"}
---

# สรุป Day 3 — Flutter

> ใช้ช่วงสรุปในเวลา 14:45–16:00 ของวันนี้ ไม่เพิ่มเวลาเรียนหรือการบ้านบังคับ

## ใจความสำคัญ

- Dart model และ null safety ช่วยรับข้อมูลจาก API อย่างมีรูปแบบ
- Widget/layout, state และ master-detail navigation ทำให้คนใช้งานข้อมูลได้
- UI ต้องรับมือ loading, empty, error และ unauthorized ไม่ใช่ตรวจเฉพาะหน้าที่สำเร็จ
- Flutter ติดต่อ API ผ่าน HTTP/JSON; browser และ Android มีเงื่อนไขเครือข่ายต่างกัน
- Plugin เพิ่มความสามารถของอุปกรณ์ และ debug APK เป็นหลักฐานการ build สำหรับฝึก
- หากทำ Practice เสริมบน Mac: Dart project เดิมรันบน iPhone Simulator ได้ โดย `.app` ที่ build ใช้สำหรับ Simulator ไม่ใช่ไฟล์ติดตั้งบน iPhone จริง

## ก่อนจบวัน ตรวจหลักฐาน

- ☐ เปิด list/detail และสาธิต filter/empty state ได้
- ☐ Sign in แล้ว create/update ผ่าน API; แสดงผล loading/error ตาม checkpoint
- ☐ ทดลอง plugin และเปิด browser preview ได้
- ☐ มี Android debug app/APK และตรวจ UUID จากหน้าจอเทียบกับ API

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ

**หลักฐานเสริม iOS (Optional):** ถ้าได้ทำ ให้เก็บผล Sign in/สร้างคำขอ/ปุ่มคู่มือบน iPhone Simulator, UUID ที่ตรวจเทียบกับ API และ `.app` path. ถ้าข้ามหรือเครื่องไม่พร้อม ให้บันทึก optional pending โดยไม่กระทบ checkpoint หลักและไม่ใช้แทน Android

## สิ่งที่เก็บไว้ใช้ต่อ

- client พร้อม model/service/screens และ API project เดิม
- Android debug APK path, API origin และ UUID ที่ลองจริง
- docs/review-log.md และ main commit หลังจบวัน
- ถ้าทำ iOS เสริม: เก็บ iOS source/config ที่ตรวจแล้วและ `.app` path ใน review log; ไม่ commit build outputs หรือ signing ส่วนตัว

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## Day 4 — ย้ายบริการไปเปิดบน Cloud

หน้าจอและเคาน์เตอร์ทำงานร่วมกันแล้ว พรุ่งนี้เราจะแพ็ก API แล้วย้ายสถานที่เปิดบริการไป Azure โดยใช้ Flutter project เดิมเปลี่ยนไปเชื่อม HTTPS

ก่อนเริ่ม ตรวจ Docker, Azure subscription/network/roles/OIDC และ lab cost ownership; เก็บ main และ lockfile ที่ตรวจแล้ว

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

วันนี้เรานำ API มาอยู่ในมือผู้ใช้ และแยก “หน้าจอดูดี” ออกจาก “ทำงานกับข้อมูลจริงได้”. ไป [Day 4](/exercises/day-04-azure/) เพื่อย้าย API ไป Azure โดยใช้ Flutter project เดิม

อ่านเพิ่ม: [Flutter networking](https://docs.flutter.dev/cookbook/networking/fetch-data), [Android build](https://docs.flutter.dev/deployment/android), [iOS setup](https://docs.flutter.dev/platform-integration/ios/setup), [url_launcher](https://pub.dev/packages/url_launcher)
