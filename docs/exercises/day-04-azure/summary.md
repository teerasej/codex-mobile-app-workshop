---
title: "สรุป Day 4 — Azure"
prev: {"text": "Exercise 4", "link": "/exercises/day-04-azure/exercise-04"}
next: {"text": "โจทย์ต่อยอด", "link": "/resources/change-request"}
---

# สรุป Day 4 — Azure

> ใช้ช่วงสรุปในเวลา 14:45–16:00 ของวันนี้ ไม่เพิ่มเวลาเรียนหรือการบ้านบังคับ

## ใจความสำคัญ

- Container แพ็ก API พร้อมสิ่งที่ต้องใช้รัน; local verification ต้องมาก่อนส่งขึ้น Cloud
- API ที่ส่งต่อจาก Day 3 ต้องมี auth และ PostgreSQL persistence; API แบบ memory ยังไม่ผ่านจุดนี้
- ACR เก็บ image; Container Apps รัน image โดยใช้ configuration และ runtime secrets
- การ deploy ผ่าน Azure ใช้สิทธิ์บัญชี lab ของผู้เรียน ส่วน Container App ใช้ pull identity ดึง image จาก ACR
- จด ACR image tag, revision และ health version เพื่อชี้รุ่นที่เปิดบริการ เพิ่ม commit SHA เมื่อยืนยันได้ว่าใช้ build image รุ่นนั้น
- HTTPS, auth, database และ Android ต้องตรวจร่วมกัน; /health อย่างเดียวไม่พิสูจน์งานทั้งหมด

## ก่อนจบวัน ตรวจหลักฐาน

- ☐ HTTPS API เชื่อม PostgreSQL ได้ พร้อม read/create ที่ authenticated
- ☐ private ACR image เป็น linux/amd64 และ Container App ดึงด้วย identity ที่ได้รับ
- ☐ ชี้ ACR tag, health version และ ready revision ที่รับ traffic ได้
- ☐ ปิด local API แล้ว Android ยังอ่าน/สร้าง Request ผ่าน HTTPS ได้
- ☐ ชี้ 404 log และข้อมูลที่ยังอยู่หลัง restart
- ☐ มี review log, งานค้าง และเจ้าของค่าใช้จ่าย/แผน cleanup ของ lab

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ. ถ้าตรวจ Portal แบบอ่านอย่างเดียว ให้เขียนว่า deploy, cloud create/read และ restart **ยังไม่ได้ทดลอง**; การเห็นค่าในหน้าจอไม่แทนผลเหล่านี้

ถ้าทำ GitHub Actions แบบเสริม ให้แนบลิงก์ workflow run และผลตรวจว่า commit SHA ตรงกับ tag และ health version

## สิ่งที่เก็บไว้ใช้ต่อ

- Source repository, tests และ requirements.lock.txt
- Dockerfile และชื่อ configuration/secrets (เก็บเฉพาะชื่อ)
- APK path, image SHA, revision, UUID และ docs/review-log.md

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## หลังหลักสูตร — เลือกโจทย์จริงและวางแผนต่อยอด

เรามีต้นแบบที่เชื่อมหน้าจอ บริการข้อมูล ฐานข้อมูล และประวัติการปล่อยรุ่น เหมือนเคาน์เตอร์ที่เปิดให้ทดลองใช้งานพร้อมทะเบียนตรวจย้อนหลัง

ก่อนใช้กับบริษัท ให้ทีมที่รับผิดชอบตรวจ identity, authorization, data protection, operational ownership และ release process จากหลักฐานจริง; ทำ change request หลัง core checkpoints ครบ

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

เมื่อผ่าน checkpoints เราจะต่อเส้นทางจากแฟ้ม Request ในวันแรกถึงแอป Android ที่เรียกบริการบน Azure พร้อมประวัติการเปลี่ยนแปลงที่ตรวจย้อนกลับได้. ก่อนนำไปใช้งานในบริษัท ให้ทีมที่เกี่ยวข้องตรวจ identity, authorization, data protection, operational ownership และ release process จากหลักฐานจริง

อ่านเพิ่ม: [Image pull with managed identity](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity-image-pull), [GitHub OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect), [Ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-how-to), [Revision](https://learn.microsoft.com/en-us/azure/container-apps/revisions-manage), [Scaling](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)
