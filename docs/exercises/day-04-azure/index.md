---
title: "Day 4 — ย้ายเคาน์เตอร์ไปเปิดบน Cloud"
prev: {"text": "สรุป Day 3", "link": "/exercises/day-03-flutter/summary"}
next: {"text": "Exercise 1", "link": "/exercises/day-04-azure/exercise-01"}
---

# Day 4 — ย้ายเคาน์เตอร์ไปเปิดบน Cloud

[กลับสารบัญ](/) · [วันก่อนหน้า](/exercises/day-03-flutter/)

## Overview theme

วันนี้เราแพ็ก API ใส่ Docker container แล้วเปิดบริการผ่าน Azure Container Apps. Image เหมือนกล่องสูตรพร้อมวัตถุดิบ, ACR คือชั้นเก็บกล่อง และ Revision คือป้ายรุ่นที่บอกว่าตอนนี้กำลังเสิร์ฟสูตรไหน

**ผลท้ายวัน:** API ที่มี auth/persistence เปิดผ่าน HTTPS, deploy จาก GitHub ได้, Android เชื่อม API นี้ และตามรอย commit → image → revision ได้

**Prerequisites:** main จาก Day 3, API unit tests/requirements.lock.txt, Docker engine, Azure CLI และ [Azure readiness](/resources/readiness) ผ่าน. ใช้ subscription, student resource group และ PostgreSQL ที่ได้รับมอบหมาย; ทางเลือกใช้ทรัพยากรของตนต้องได้รับอนุมัติจากเจ้าของ. ใช้ pull/pipeline identities ที่เตรียมไว้. OIDC/role/network ต้องพร้อมก่อนช่วงที่ใช้งาน

> **License / ค่าใช้จ่าย:** Azure Container Apps, ACR, database และ build อาจมีค่าใช้จ่าย. แผน lab ใช้ app ละ 0.25 vCPU/0.5Gi, min=0/max=1 บน Consumption-only; ไม่สร้าง Log Analytics. ใช้เฉพาะ lab ที่เจ้าของอนุมัติงบแล้ว. Docker Desktop และ GitHub Actions ต้องอยู่ในสิทธิ์ที่องค์กรอนุญาต; ไม่ถือว่าทั้งวันไม่มีค่าใช้จ่าย

| เวลา | Exercise | อธิบาย / ลงมือ / ตรวจและแก้ |
| --- | --- | --- |
| 09:30–10:30 | 1. แพ็กและทดสอบ container | 10 / 35 / 15 นาที |
| 10:45–12:00 | 2. เปิด API บน Azure | 10 / 50 / 15 นาที |
| 13:00–14:30 | 3. Deploy จาก GitHub | 15 / 55 / 20 นาที |
| 14:45–16:00 | 4. เชื่อม Android และดูแลรุ่นที่ใช้งาน | 10 / 45 / 20 นาที |

พัก 10:30–10:45 และ 14:30–14:45; กลางวัน 12:00–13:00. การรอ provision ใช้เวลาช่วงตรวจ/ทบทวน; ถ้ารอนานให้เรียนอ่าน config/log จากผู้สอน แล้วกลับมาตรวจของตน ไม่ข้าม checkpoint เงียบ ๆ

## Instructionของวันนี้

ทำ code บน branch **chore/container-deployment**. คำสั่ง Azure ที่มี <...> ต้องให้ Codex เติม **ค่าที่ผู้เรียนยืนยัน** ก่อนรัน; ห้ามคัดลอกทั้ง placeholder. Azure CLI ตัวอย่างเป็นบรรทัดเดียว ใช้ได้ทั้ง PowerShell และ macOS โดยไม่เปลี่ยน line-continuation

ทุก prompt ที่สร้าง/แก้ cloud resources ต้องแสดง subscription, resource group, รายการ resources และผลต่อค่าใช้จ่ายก่อน แล้วผู้เรียนจึงให้ทำเฉพาะขั้นนั้น. ไม่ให้ Codex อ่านไฟล์ .env หรือรัน seed ใน cloud. ไม่แก้หรือลบ shared PostgreSQL/control resources. หลังสร้าง ACR ให้ผู้สอนตรวจ exact GitHub OIDC subject แล้วกด **Preview deployment access → Prepare deployment access** ก่อน deploy private image; เมื่อ API ทำงานแล้วจึงกด **Check Day 4 resources**

## เปิดแบบฝึกหัด

- [09:30–10:30 · 1. แพ็กและทดสอบ container](/exercises/day-04-azure/exercise-01)
- [10:45–12:00 · 2. เปิด API บน Azure](/exercises/day-04-azure/exercise-02)
- [13:00–14:30 · 3. Deploy จาก GitHub](/exercises/day-04-azure/exercise-03)
- [14:45–16:00 · 4. เชื่อม Android และดูแลรุ่นที่ใช้งาน](/exercises/day-04-azure/exercise-04)

เมื่อจบ Exercise 4 ไปที่ [สรุปท้ายวัน](/exercises/day-04-azure/summary) เพื่อเช็กหลักฐานและเตรียมงานต่อ
