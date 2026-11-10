---
title: "Day 1 · Exercise 3 — รวมงานที่แก้บรรทัดเดียวกัน"
prev: {"text": "Exercise 2", "link": "/exercises/day-01-git/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-01-git/exercise-04"}
---

# Exercise 3 — รวมงานที่แก้บรรทัดเดียวกัน


> **Day 1 · Git · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-01-git/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

คนสองคนปรับข้อความคนละแบบ Git ไม่ควรตัดสินแทนว่าแบบไหนตรงกับความต้องการของทีม

## Practice 1 — สร้าง conflict แบบควบคุมได้

<PracticeIllustration asset="d01-e03-p01" eager />

**Primary target:** ทำให้เห็นว่า conflict เกิดจากการแก้ไฟล์ที่จุดเดียวกันอย่างไร

### Steps

1. ตรวจว่าอยู่ local `main` ที่ pull แล้วและไม่มีไฟล์แก้ค้าง. บันทึก review log ที่ค้างด้วย commit ก่อนเริ่ม
2. ให้ Codex ทำทีละ prompt โดยแสดงคำสั่งก่อนรัน และรอให้เสร็จก่อนส่ง prompt ถัดไป:

   **2.1 สร้าง `practice/message-a`**

   ```text
   แก้เฉพาะ docs/project-brief.md:
   จาก main สร้าง practice/message-a เปลี่ยนบรรทัดข้อความยืนยันเป็น
   “ข้อความยืนยัน: ทีมได้รับคำขอของคุณแล้ว” แล้ว commit
   ไม่ push ไม่ force ไม่ reset
   ```

   **2.2 สร้าง `practice/message-b`**

   ```text
   กลับ main เดิม สร้าง practice/message-b เปลี่ยนบรรทัดเดียวกันใน docs/project-brief.md เป็น
   “ข้อความยืนยัน: รับเรื่องแล้ว ติดตามได้ใน My requests” แล้ว commit
   ไม่ push ไม่ force ไม่ reset และไม่เปลี่ยน main
   ```

   **2.3 Merge เพื่อให้เกิด conflict**

   ```text
   ขณะอยู่ practice/message-b ให้ git merge practice/message-a
   ถ้าเกิด conflict ให้หยุดทันที ห้ามแก้ให้อัตโนมัติ
   ไม่ push ไม่ force ไม่ reset และไม่เปลี่ยน main
   ```
3. อ่าน output ของ merge แล้วเปิดไฟล์ที่มี `<<<<<<<`, `=======`, `>>>>>>>`
4. ให้ Codex อธิบาย conflict โดยยังไม่แก้

**Checkpoint:** เห็น conflict หนึ่งไฟล์และระบุข้อความทั้งสองเวอร์ชันได้. ไม่ถือว่า error นี้เป็นงานพัง; พวกเราตั้งใจสร้าง conflict นี้เพื่อทำความรู้จัก และอยู่กับมันได้อย่างสบายใจครับ

## Practice 2 — ตัดสินใจและแก้ conflict

<PracticeIllustration asset="d01-e03-p02" />

**Primary target:** รวมเนื้อหาที่ถูกต้องโดยไม่ทิ้ง conflict markers

### Steps

1. เลือกข้อความสุดท้ายร่วมกัน เช่น `ข้อความยืนยัน: ทีมได้รับคำขอของคุณแล้ว ติดตามได้ใน My requests`
2. ส่ง:

   ```text
   แก้ conflict เฉพาะข้อความยืนยันให้เป็น:
   “ข้อความยืนยัน: ทีมได้รับคำขอของคุณแล้ว ติดตามได้ใน My requests”
   ยังไม่ commit
   ```
3. ตรวจข้อความสุดท้ายและค้นหา markers ทั้งหมดว่าถูกลบออกไปแล้ว
4. ให้ git commit ด้วยข้อความด้านล่าง "docs: resolve receipt message conflict"`
5. Push `practice/message-b` เปิด PR ไป `main`
6. ตรวจ/merge เหมือน Exercise 2.
   - ไม่จำเป็นต้อง push `practice/message-a`
7. กลับ local main และ pull
8. ขอ Codex แสดงรายการเพื่อตรวจว่ามีการ merge เกิดขึ้นกับ branch main

**Checkpoint:** ไฟล์อ่านได้ตามปกติ ไม่มี markers; PR ถูก merge; main ตรงกับข้อความที่ทีมเลือก

**ถ้าติดขัด:** ถ้าไม่มี conflict ให้ตรวจว่าทั้งสอง branch เริ่มจาก main เดียวกันและแก้บรรทัดเดียวกัน.
