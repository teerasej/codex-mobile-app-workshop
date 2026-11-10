---
title: "สรุป Day 1 — Git"
prev: {"text": "Exercise 4", "link": "/exercises/day-01-git/exercise-04"}
next: {"text": "ไป Day 2", "link": "/exercises/day-02-api/"}
---

# สรุป Day 1 — Git


## ใจความสำคัญ

- Markdown ใช้เครื่องหมายในข้อความธรรมดาเพื่อจัดรูปแบบเอกสาร เช่น หัวข้อ รายการ ลิงก์ และ code block; Preview ช่วยตรวจรูปแบบ ส่วน Git เก็บประวัติของไฟล์

- Git เก็บประวัติของไฟล์; commit คือภาพงานหนึ่งช่วงที่ย้อนดูเหตุผลได้
- Branch แยกงานหนึ่งเรื่อง ส่วน PR ช่วยให้ทีมตรวจ diff ก่อนรวมงาน
- Merge conflict ต้องตัดสินใจจากความหมายของงาน ไม่ใช่ลบข้อความเพื่อให้ error หาย
- AGENTS.md และ prompt ที่มีขอบเขตช่วยให้ Codex ทำทีละส่วน; ผู้เรียนยังเป็นคนตรวจและตัดสินใจ

## ก่อนจบวัน

- ☐ มี Workshop notes ใน README ที่แก้เอง แสดงผลและเปิดลิงก์ Project brief บน GitHub ได้ พร้อมอธิบาย syntax หนึ่งอย่าง

- ☐ ชี้ initial commit และอธิบาย diff ของการเปลี่ยนแปลงหนึ่งเรื่องได้
- ☐ มี PR ที่ review/merge และ main ที่ pull แล้ว
- ☐ แก้ conflict ด้วยข้อความที่ตกลงกันและไม่มี conflict markers
- ☐ มี AGENTS.md, docs/day2-plan.md และ review log ที่บันทึกผลจริง

ช่องที่ยังไม่ผ่านให้บันทึกตามจริง พร้อมสาเหตุและสิ่งที่ต้องทำต่อ ไม่เปลี่ยนเป็น “ผ่าน” เพียงเพราะ Codex รายงานว่างานเสร็จ

## สิ่งที่เก็บไว้ใช้ต่อ

- โฟลเดอร์ service-desk-lite และ private repository เดิม
- docs/project-brief.md, docs/api-contract.md, AGENTS.md
- docs/day2-plan.md, docs/review-log.md และ main commit ล่าสุด

เก็บ password/token/connection string ในช่องทางส่วนตัว ไม่ใส่ใน review log หรือ repository

## Day 2 — เปลี่ยน Instruction เป็นบริการข้อมูล

เหมือนจัดแฟ้มและInstructionที่เคาน์เตอร์พร้อมแล้ว พรุ่งนี้เราจะเพิ่มพนักงานรับเรื่อง: FastAPI ใช้ API contract เดิม ตรวจข้อมูล และเก็บลง PostgreSQL

ก่อนเริ่ม ให้ main ไม่มีงานค้าง ตรวจ Python 3.12 และ Azure PostgreSQL readiness; เปิด local project เดิม ไม่เริ่ม repository ใหม่

## ทบทวนกับเพื่อน

อธิบายหนึ่งสิ่งที่ Codex ช่วย และหนึ่งจุดที่คุณตรวจด้วยตนเอง ชี้หลักฐานจากผลงานวันนี้ประกอบคำอธิบาย

วันนี้เราไม่ได้แข่งกันพิมพ์คำสั่ง Git แต่ฝึกตัดสินใจว่า **จะเปลี่ยนอะไร ตรวจอย่างไร และเมื่อไรจึงรวมงานได้**. เก็บโฟลเดอร์เดิมและบัญชี GitHub ไว้ แล้วไป [Day 2](/exercises/day-02-api/)

แหล่งอ่านเพิ่มเติม: [Codex และ AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)
