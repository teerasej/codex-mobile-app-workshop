---
title: "Service Desk Lite — ใบงานบริการที่ติดตามได้"
prev: false
next: false
---

<DownloadFile file="project-brief.md" />

# Service Desk Lite — ใบงานบริการที่ติดตามได้

บริษัทสมมติ BrightDesk มี Request ภายใน เช่น ขออุปกรณ์ ประสานการซ่อม และจัดเตรียมห้องประชุม พนักงานอยากทราบว่าเรื่องของตนอยู่ขั้นตอนไหน เราจะสร้างต้นแบบหนึ่งระบบตั้งแต่ Git จนถึง API บน Azure

## ผู้ใช้และขอบเขต

- ผู้ใช้ทดลอง `learner01` และ `learner02` ใช้รหัสผ่านส่วนตัวที่ผู้สอนส่งมอบ; ถ้าเป็น database ใหม่ของตนจึงกำหนดเมื่อสร้าง user ครั้งแรก. คงรหัสผ่านเดิมเมื่อ seed ซ้ำ และไม่มีรหัสผ่านใน public starter
- ผู้ใช้ Sign in, ดูเฉพาะ Request ของตน, ดูรายละเอียด, สร้าง Request และปรับสถานะของตนได้
- สถานะ `new`, `in_progress`, `done` เป็นวงจรทดลอง ผู้ส่งอัปเดตความคืบหน้าที่ได้รับแจ้งและยืนยันงานเสร็จเอง ยังไม่มีบทบาทเจ้าหน้าที่/ผู้อนุมัติ
- หน้าจอ: Sign in → My requests → Request detail และ Create request
- API เชื่อม Azure Database for PostgreSQL; Flutter เรียก API เท่านั้น ไม่ต่อฐานข้อมูลโดยตรง
- Day 3 ใช้ browser preview และ Android debug build; Day 4 เปลี่ยน API URL ไป HTTPS บน Azure
- Codex เป็นผู้ช่วยพัฒนา ไม่ใช่ฟีเจอร์ AI ในตัวแอป ไม่ต้องเพิ่ม OpenAI API หรือ chatbot

## ขอบเขตที่ยังไม่ทำ

ไม่มีข้อมูลบริษัทจริง, การเชื่อมระบบเฉพาะขององค์กร, SSO, admin console, push notification, offline sync, file upload หรือการขึ้น app store การต่อยอดใช้จริงต้องออกแบบสิทธิ์ บัญชีองค์กร การรักษาข้อมูล และการดูแลระบบเพิ่มเติม

## ข้อตกลงตัวอย่าง

ชื่อแอป: Service Desk Lite
สถานะเริ่มต้น: new
ข้อความยืนยัน: รับ Request แล้ว

## Done ของโปรเจค

1. อธิบาย commit และ review ของตนได้
2. API สร้าง อ่าน แก้สถานะข้อมูลใน PostgreSQL ได้ และปฏิเสธ input/token ที่ไม่ถูกต้อง
3. ผู้ใช้หนึ่งอ่านหรือแก้ Request ของอีกคนไม่ได้
4. Flutter ส่ง Request จริงและแสดง loading/empty/error/success ได้
5. Android debug app เรียก Azure API ผ่าน HTTPS และยังพบข้อมูลหลัง restart API
6. ชี้ commit → image tag → revision ที่กำลังใช้งานได้
