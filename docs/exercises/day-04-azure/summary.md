---
title: "สรุป Day 4 — Azure"
prev: {"text": "Exercise 4", "link": "/exercises/day-04-azure/exercise-04"}
next: {"text": "โจทย์ต่อยอด", "link": "/resources/change-request"}
---

# สรุป Day 4 — Azure

> ใช้ช่วงสรุปในเวลา 14:45–16:00 ของวันนี้ ไม่เพิ่มเวลาเรียนหรือการบ้านบังคับ

## ใจความสำคัญ

- Container แพ็ก API พร้อมสิ่งที่ต้องใช้รัน; local verification ต้องมาก่อนส่งขึ้น Cloud
- ACR เก็บ image; Container Apps รัน image โดยใช้ configuration และ runtime secrets
- Pipeline identity ใช้ deploy ส่วน image-pull identity ใช้ดึง image; หน้าที่และสิทธิ์ต่างกัน
- Commit SHA, image tag, app version และ revision ช่วยตามรอยรุ่นที่เปิดบริการ
- HTTPS, auth, database และ Android ต้องตรวจร่วมกัน; /health อย่างเดียวไม่พิสูจน์งานทั้งหมด

## ก่อนจบวัน ตรวจหลักฐาน

- ☐ HTTPS API เชื่อม PostgreSQL ได้ พร้อม read/create ที่ authenticated
- ☐ ชี้ commit SHA, ACR tag, version และ ready revision ที่สัมพันธ์กัน
- ☐ ปิด local API แล้ว Android ยังอ่าน/สร้างคำขอผ่าน HTTPS ได้
- ☐ ชี้ 404 log และข้อมูลที่ยังอยู่หลัง restart
- ☐ มี review log, งานค้าง และเจ้าของค่าใช้จ่าย/แผน cleanup ของ lab

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ

## สิ่งที่เก็บไว้ใช้ต่อ

- Source repository, tests และ requirements.lock.txt
- Dockerfile, workflow และชื่อ configuration/secrets (เก็บเฉพาะชื่อ)
- APK path, image SHA, revision, UUID และ docs/review-log.md

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## หลังหลักสูตร — เลือกโจทย์จริงและวางแผนต่อยอด

เรามีต้นแบบที่เชื่อมหน้าจอ บริการข้อมูล ฐานข้อมูล และประวัติการปล่อยรุ่น เหมือนเคาน์เตอร์ที่เปิดให้ทดลองใช้งานพร้อมทะเบียนตรวจย้อนหลัง

ก่อนใช้กับบริษัท ให้ทีมที่รับผิดชอบตรวจ identity, authorization, data protection, operational ownership และ release process จากหลักฐานจริง; ทำ change request หลัง core checkpoints ครบ

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

จากแฟ้มคำขอในวันแรก เรามาถึงแอป Android ที่เรียกบริการบน Azure และมีประวัติการเปลี่ยนแปลงให้ตรวจย้อนกลับได้. ขั้นต่อไปสำหรับบริษัทคือเลือก use case จริง แล้วให้ทีมที่เกี่ยวข้องตรวจ identity, authorization, data protection, operational ownership และ release process ก่อนนำไปใช้งาน

อ่านเพิ่ม: [Image pull with managed identity](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity-image-pull), [GitHub OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect), [Ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-how-to), [Revision](https://learn.microsoft.com/en-us/azure/container-apps/revisions-manage), [Scaling](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)
