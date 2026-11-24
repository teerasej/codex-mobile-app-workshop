---
title: "Day 4 — ย้ายเคาน์เตอร์ไปเปิดบน Cloud"
prev: {"text": "สรุป Day 3", "link": "/exercises/day-03-flutter/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-04-azure/exercise-01"}
---

# Day 4 — ย้ายเคาน์เตอร์ไปเปิดบน Cloud

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-03-flutter/)

## Overview theme

วันนี้เราจะแพ็ก API ใส่ Docker container แล้วเปิดบริการผ่าน Azure Container Apps.

**ผลท้ายวัน:** API ที่มี auth/persistence เปิดผ่าน HTTPS, deploy จาก GitHub ได้, Android เชื่อม API นี้ และตามรอย commit → image → revision ได้

**ก่อนเริ่ม:** ใช้โปรเจคเดิมจาก Day 3 บน branch main พร้อม API tests และ requirements.lock.txt. API ต้อง login ได้ ใช้ PostgreSQL จริง ข้อมูลอยู่หลัง restart และอ่าน version จาก APP_VERSION ได้. ถ้ายังเป็น API แบบเก็บข้อมูลใน memory หรือปิด auth ให้แจ้งผู้สอนก่อนแพ็ก container

Docker engine, Azure CLI และ [Azure readiness](/resources/readiness) ต้องพร้อมแล้ว. ใช้ subscription, student resource group, PostgreSQL และ pull/pipeline identities ที่ได้รับมอบหมาย; ทางเลือกใช้ทรัพยากรของตนต้องให้เจ้าของอนุมัติ. ผู้สอนเตรียมสิทธิ์และเครือข่ายก่อนช่วงที่ใช้งาน

> **License / ค่าใช้จ่าย** — Azure Container Apps, ACR, database และ build อาจมีค่าใช้จ่าย แผน lab ใช้ Environment แบบ Workload profiles (v2) ที่มีเฉพาะโปรไฟล์ Consumption แอปใช้ 0.25 vCPU, memory 0.5 GiB และ 0–1 replicas โดยไม่สร้าง Log Analytics การใช้ Docker Desktop และ GitHub Actions ต้องอยู่ในขอบเขตที่องค์กรอนุญาต

| เวลา | Exercise | อธิบาย / ลงมือ / ตรวจและแก้ |
| --- | --- | --- |
| 09:30–10:30 | 1. แพ็กและทดสอบ container | 10 / 35 / 15 นาที |
| 10:45–12:00 | 2. เปิด API บน Azure | 10 / 50 / 15 นาที |
| 13:00–14:30 | 3. Deploy จาก GitHub | 15 / 55 / 20 นาที |
| 14:45–16:00 | 4. เชื่อม Android และดูแลรุ่นที่ใช้งาน | 10 / 45 / 20 นาที |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00. การรอ provision ใช้เวลาช่วงตรวจ/ทบทวน; ถ้ารอนานให้เรียนอ่าน config/log จากผู้สอน แล้วกลับมาตรวจของตน ไม่ข้าม checkpoint เงียบ ๆ

## วิธีทำงานวันนี้

1. เปิด local project เดิมใน Codex แล้วส่ง prompt นี้

   ~~~text
   ตรวจ branch และไฟล์ที่ยังไม่ได้บันทึกใน Git ของโปรเจคนี้ก่อน
   ถ้า main มีงาน Day 3 ครบแล้ว ให้สร้างหรือสลับไป chore/container-deployment
   เก็บงานเดิมไว้ ถ้ามีงานค้างหรือ branch ชื่อนี้มีอยู่แล้วให้อธิบายก่อนทำต่อ
   ยังไม่ push, merge หรือเปลี่ยน Azure
   ~~~

2. ใช้ Microsoft Edge อ่านบทเรียน เปิด GitHub, API docs และ Azure portal ด้วยบัญชีของตน. ให้ Codex ช่วยรันงานในเครื่องจาก prompt ทีละขั้น; คำสั่งที่แสดงเป็นตัวอย่างสำหรับอ่านตรวจ ไม่ต้องจำหรือคัดลอก placeholder ไปใช้
3. ก่อนสร้างหรือแก้ Azure ให้ตรวจ subscription, resource group, resource ที่จะเปลี่ยน และค่าใช้จ่าย แล้วจึงยืนยันเฉพาะขั้นนั้น. ถ้าบัญชีนี้ได้รับอนุญาตให้อ่านอย่างเดียว ให้ดูค่าตามบทเรียนและบันทึก deployment ว่า **ยังไม่ได้ทดลอง**
4. Secret กรอกเองในช่องส่วนตัว. ให้ Docker อ่าน env file โดยตรงได้ แต่ไม่ให้ Codex เปิดหรือพิมพ์ค่าใน `.env`. ไม่รัน seed บน Cloud และไม่แก้ shared PostgreSQL หรือ resources ส่วนกลาง
5. เปิด ACR ที่ผู้สอนระบุใน `deployment.txt` แล้วให้ผู้สอนยืนยัน `AcrPull` ของ pull identity ก่อน deploy private image ตรวจ GitHub OIDC ของ repository/branch `main` แยกใน Exercise 3 เมื่อ deploy แล้วจึงส่ง API URL และผลทดสอบที่ไม่มี secret ให้ผู้สอน

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. แพ็กและทดสอบ container](/exercises/day-04-azure/exercise-01)
- [10:45–12:00 · 2. เปิด API บน Azure](/exercises/day-04-azure/exercise-02)
- [13:00–14:30 · 3. Deploy จาก GitHub](/exercises/day-04-azure/exercise-03)
- [14:45–16:00 · 4. เชื่อม Android และดูแลรุ่นที่ใช้งาน](/exercises/day-04-azure/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-04-azure/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ
