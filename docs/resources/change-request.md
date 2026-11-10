---
title: "คำขอเปลี่ยนแปลงท้ายหลักสูตร"
prev: false
next: false
---

<DownloadFile file="change-request.md" />

# คำขอเปลี่ยนแปลงท้ายหลักสูตร

ผู้ใช้ขอให้รายการ Request แสดงสถานะเป็นภาษาไทย โดยเก็บค่า API เดิม: new → รับเรื่องแล้ว, in_progress → กำลังดำเนินการ, done → เสร็จแล้ว

เกณฑ์ตรวจ: ทั้ง list/detail แสดงคำเดียวกัน, filter ยังทำงาน, JSON/DB ยังคงใช้ค่า enum ภาษาอังกฤษ, automated test เดิมผ่าน. ให้ทำเฉพาะเมื่อ core checkpoint ครบ; ไม่เพิ่ม fourth status หรือแก้ข้อมูลต้นฉบับ.
