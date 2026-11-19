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
- Flutter ใช้ Dio ติดต่อ API ผ่าน HTTP/JSON; login ส่ง form-urlencoded ส่วน create/update ส่ง JSON โดย browser และ Android มีเงื่อนไขเครือข่ายต่างกัน
- DioException ช่วยแยก HTTP error จาก connection/timeout ที่อาจไม่มี response; timeout ของแต่ละช่วงไม่ใช่เวลารวมของคำขอ
- Plugin เพิ่มความสามารถของอุปกรณ์ และ debug APK เป็นหลักฐานการ build สำหรับฝึก
- หากทำ Practice เสริมบน Mac: Dart project เดิมรันบน iPhone Simulator ได้ โดย `.app` ที่ build ใช้สำหรับ Simulator ไม่ใช่ไฟล์ติดตั้งบน iPhone จริง

## ก่อนจบวัน ตรวจหลักฐาน

- ☐ ช่วง fixture: list/detail ทำงาน ทั้งหมดมี 3 รายการและแต่ละสถานะมี 1 รายการ
- ☐ ช่วง API จริง: Sign in ผิดแล้วลองใหม่ได้ เปลี่ยนผู้ใช้แล้วไม่มีข้อมูลเก่าค้าง
- ☐ สร้าง/เปลี่ยน status ผ่าน Dio/ApiService และเทียบ UUID กับ API ได้
- ☐ tests ครบ loading/empty/error/success และหยุด API → error → เปิด API → Retry ในแอปจริงได้
- ☐ flutter analyze และ flutter test ผ่าน พร้อมบันทึกกรณีที่ใช้ fake adapter แยกจาก UI จริง
- ☐ ทดลอง plugin และเปิด browser preview ใน Edge ได้
- ☐ มี Android debug app/APK และตรวจ UUID จากหน้าจอเทียบกับ API

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ

ส่ง prompt ให้ช่วยจัดหลักฐาน โดยตรวจผลที่เราเห็นจริงประกอบด้วย

~~~text
ช่วยเติม docs/review-log.md จากผลที่เราตรวจใน Day 3
แยก fixture, API จริง, tests, Edge, Android และ iOS optional
ระบุ passed/pending ตามหลักฐานจริง พร้อม UUID, test result และ build path ที่เกี่ยวข้อง
อย่าใส่ password/token/connection string และอย่าระบุว่า Android ผ่านจากผล web อย่างเดียว
ตรวจสถานะ PR/main ตาม workflow Day 1 ถ้ายังไม่ merge ให้บอกสิ่งที่ค้าง ไม่ merge เองจาก prompt นี้
~~~

**หลักฐานเสริม iOS (Optional):** ถ้าได้ทำ ให้เก็บผล Sign in/สร้าง Request /ปุ่มคู่มือบน iPhone Simulator, UUID ที่ตรวจเทียบกับ API และ `.app` path. ถ้าข้ามหรือเครื่องไม่พร้อม ให้บันทึก optional pending โดยไม่กระทบ checkpoint หลักและไม่ใช้แทน Android

## สิ่งที่เก็บไว้ใช้ต่อ

- client พร้อม model/service/screens, ApiService ที่รับ Dio และ API project เดิม
- pubspec.yaml และ pubspec.lock ที่เก็บรุ่น package ตามผล resolve จริง
- Android debug APK path, API origin และ UUID ที่ลองจริง (APK วันนี้ยังต้องใช้ local API/adb reverse)
- docs/review-log.md และ main commit หลังจบวัน
- ถ้าทำ iOS เสริม: เก็บ iOS source/config ที่ตรวจแล้วและ `.app` path ใน review log; ไม่ commit build outputs หรือ signing ส่วนตัว

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## Day 4 — ย้ายบริการไปเปิดบน Cloud

หน้าจอและเคาน์เตอร์ทำงานร่วมกันแล้ว พรุ่งนี้เราจะแพ็ก API แล้วย้ายสถานที่เปิดบริการไป Azure โดยใช้ Flutter project เดิมเปลี่ยนไปเชื่อม HTTPS

ก่อนเริ่ม ตรวจ Docker, Azure subscription/network/roles/OIDC และ lab cost ownership ตาม [readiness](/resources/readiness) เก็บ main และ lockfile ที่ตรวจแล้ว API ต้องคง auth/ownership/PostgreSQL และอ่าน `APP_VERSION` ก่อนนำไปใช้กับ revision ใน Day 4

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

วันนี้เรานำ API มาอยู่ในมือผู้ใช้ และแยก “หน้าจอดูดี” ออกจาก “ทำงานกับข้อมูลจริงได้”. ไป [Day 4](/exercises/day-04-azure/) เพื่อย้าย API ไป Azure โดยใช้ Flutter project เดิม

อ่านเพิ่ม: [Dio](https://pub.dev/packages/dio), [Flutter networking](https://docs.flutter.dev/cookbook/networking/fetch-data), [Flutter packages](https://docs.flutter.dev/packages-and-plugins/using-packages), [Android build](https://docs.flutter.dev/deployment/android), [iOS setup](https://docs.flutter.dev/platform-integration/ios/setup), [url_launcher](https://pub.dev/packages/url_launcher)
