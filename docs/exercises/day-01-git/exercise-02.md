---
title: "Day 1 · Exercise 2 — เปลี่ยนข้อความผ่าน branch และ PR"
prev: {"text": "Exercise 1", "link": "/exercises/day-01-git/exercise-01"}
next: {"text": "Exercise 3", "link": "/exercises/day-01-git/exercise-03"}
---

# Exercise 2 — เปลี่ยนข้อความผ่าน branch และ PR


> **Day 1 · Git · 10:45–12:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-01-git/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## เวลาในช่วงนี้

| เวลา | กิจกรรม |
| --- | --- |
| 10:45–11:00 | สร้าง private repository และเชื่อม origin |
| 11:00–11:15 | Push และตรวจไฟล์บน GitHub |
| 11:15–11:35 | สร้างการเปลี่ยนแปลงบน branch |
| 11:35–12:00 | ตรวจ Pull Request และ merge |

## Scenario

เราอยากให้เนื้อหาขั้นตอนการรับเรื่องสุภาพขึ้น แต่ยังไม่อยากเปลี่ยนฉบับหลักทันที

## Practice 1 — เชื่อม local กับ remote

<PracticeIllustration asset="d01-e02-p01" eager />

**Primary target:** ให้ Codex สร้าง private repository ใต้บัญชี GitHub ของตนและเชื่อมกับ local project ได้

### Steps

1. เปิด GitHub ใน browser และลงชื่อเข้าใช้บัญชีสำหรับฝึก ตรวจชื่อบัญชีจากเมนูรูปโปรไฟล์ก่อนเริ่ม ใช้ local project `service-desk-lite` จาก Exercise 1 ต่อไป
2. ใน task เดิม ส่ง prompt เพื่อตรวจบัญชีและปลายทางก่อนสร้าง:

   ```text
   ตรวจ GitHub account ที่ใช้งานอยู่
   ```
   ```text
   ตรวจว่าบัญชีนี้มี repository ชื่อ service-desk-lite อยู่แล้วหรือไม่
   ```
   ```text
   ถ้าเชื่อม GitHub ไม่ได้หรือยังไม่ได้ลงชื่อเข้าใช้ ให้บอกสิ่งที่ต้องทำก่อน ไม่เดาว่าเชื่อมแล้ว
   ```

3. เทียบชื่อบัญชีที่ Codex แสดงกับบัญชีใน browser หากไม่ตรง ให้หยุดและลงชื่อเข้าใช้บัญชีที่ถูกต้องก่อน
4. เมื่อชื่อบัญชีถูกต้องและยังไม่มี repository ชื่อนี้ ส่ง prompt:

   ```text
   สร้าง repository ใหม่ชื่อ service-desk-lite เป็น Private โดยเป็น repository ว่างๆ
   ```

5. ขอให้ Codex ช่วยพาไปดู repository ด้วย prompt:

   ```text
   แสดงลิงก์หน้าเว็บ repository service-desk-lite ที่เพิ่งสร้าง
   ```

6. ใน browser เปิดเมนูรูปโปรไฟล์ → **Your repositories** แล้วค้นหาชื่อ repository และเปิด ตรวจชื่อเจ้าของและป้าย **Private** ให้ตรงกับ URL จาก Codex ตอนนี้ยังไม่ควรเห็นไฟล์จากเครื่อง หากชื่อซ้ำ ให้ตกลงชื่อใหม่กับผู้สอนและใช้ชื่อนั้นต่อเนื่องทุก prompt

7. เมื่อยืนยัน URL แล้ว ให้ Codex ตั้งชื่อ branch หลักเป็น `main` และเพิ่ม remote `origin` หากมี `main` หรือ `origin` อยู่แล้ว ให้ตรวจของเดิมก่อนแก้ไข:

   ```text
   ตรวจ branch ปัจจุบันและ remote ของ service-desk-lite
   ถ้า branch ปัจจุบันมีชื่ออื่นและยังไม่มี main ให้เปลี่ยนชื่อ branch นี้เป็น main
   ถ้ายังไม่มี origin ให้เพิ่ม origin ด้วย URL ของ private repository ที่ฉันยืนยันแล้ว
   ถ้ามี main แยกอยู่แล้ว หรือ origin ชี้ไปที่ URL อื่น ให้หยุดและแจ้งฉัน
   แสดงชื่อ branch และ URL ของ origin ให้ตรวจ ยังไม่ต้อง push
   ```

**Checkpoint:** เปิด repository จากบัญชีของตนได้ เห็นว่าเป็น Private และ `origin` ชี้ไป repository เดียวกัน โดยยังไม่มีการ push ไฟล์

> **ถ้าติดขัด:** หากสร้างไม่ได้ ให้ตรวจบัญชี สิทธิ์ และการเชื่อมต่อกับผู้สอน ไม่เปลี่ยนเป็น Public เพื่อแก้ปัญหา การสร้าง remote เหมือนเตรียมตู้เก็บงานที่ยังว่าง; Practice ถัดไปจึงนำฉบับที่บันทึกไว้ไปใส่

## Practice 2 — ส่ง local commits ไปเก็บไว้ใน remote

<PracticeIllustration asset="d01-e02-push-verify" />

**Primary target:** ให้ Codex push งานจากเครื่อง แล้วตรวจว่า remote มี commit และไฟล์ตรงกันกับในเครื่องได้

### Steps

1. ใน local project เดิม ขอให้ Codex ตรวจงานก่อนส่ง:

   ```text
   แสดงรายการไฟล์ที่ยังไม่ commit และ diff ของไฟล์ที่เปลี่ยน
   ```

2. หากมีไฟล์ฝึกที่แก้ค้าง ตรวจ diff ก่อน แล้วสั่งให้ codex commit การเปลี่ยนแปลงเหล่านั้น
   - หากไม่มีก็ข้ามขั้นตอนนี้ได้เลย

3. สั่งให้ Codex push local project นี้ไปที่ remote

   ```text
   ตรวจว่าอยู่บน main และ origin ตรงกับ private repository ที่ยืนยันแล้ว
   ถ้าตรง ให้รัน git push -u origin main
   ถ้าไม่ตรง ให้หยุดและแจ้งฉัน
   ```

4. หากระบบขอลงชื่อเข้าใช้ ให้ทำผ่าน browser หรือ credential manager ด้วยตนเอง จากนั้นให้ Codex ลอง push อีกครั้ง ไม่คัดลอก token ลง chat
5. เปิด repository URL จาก Codex ใน browser หรือไปที่ **Your repositories** แล้วเปิด repository เดิม เลือก branch **main** และเปิด commit ล่าสุด เทียบ commit ID กับผลในเครื่อง
6. เปิด root `README.md` ตรวจ Workshop notes และผลลัพธ์ที่แก้ใน Exercise 1 Practice 4 ให้ตรงกับฉบับที่ commit

**Checkpoint:** commit ล่าสุดบน GitHub branch `main` มี ID ตรงกับในเครื่อง และ root `README.md` มี Workshop notes ฉบับที่ commit แล้ว

อ่านเพิ่ม: [GitHub CLI: create a repository](https://cli.github.com/manual/gh_repo_create) · [GitHub repository quickstart](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)

## Practice 3 — สร้างการเปลี่ยนแปลง

<PracticeIllustration asset="d01-e02-p02" />

**Primary target:** ตรวจและ commit การแก้ข้อความบน branch ได้

### Steps

1. ให้ Codex สร้าง branch `feature/receipt-message` จาก `main`
   ส่ง:

   ```text
   สร้าง branch `feature/receipt-message` ใหม่ก่อนแก้ไข
   แก้เฉพาะบรรทัดข้อความยืนยันใน docs/project-brief.md
   จาก “ข้อความยืนยัน: รับคำขอแล้ว” เป็น “ข้อความยืนยัน: รับคำขอแล้ว ขอบคุณครับ”
   ```
2. เปิด diff และตรวจว่ามีการแก้ไขหนึ่งบรรทัดตามที่ขอ
3. ให้ commit ด้วย
   ```text
   docs: clarify request receipt
   ```
4. แล้วสั่งให้ Codex push branch นี้
5. สั่งให้ Codex สลับ branch เพื่อเทียบไฟล์เดียวกันในแต่ละ branch

   ```text
   สลับไป branch `main`
   แล้วแสดงบรรทัดข้อความยืนยันใน docs/project-brief.md
   จากนั้นสลับไป branch `feature/receipt-message` แล้วแสดงบรรทัดเดิมอีกครั้ง
   สุดท้ายสรุปความต่างของสอง branch และบอก branch ที่ใช้อยู่ตอนนี้
   ```


6. ตรวจผลที่ Codex แสดง:
   - บน `main` ต้องเป็น “ข้อความยืนยัน: รับคำขอแล้ว”
   - บน `feature/receipt-message` ต้องเป็น “ข้อความยืนยัน: รับคำขอแล้ว ขอบคุณครับ”
7. (ไม่บังคับ) เปิดไฟล์ `docs/project-brief.md` ในโปรแกรมแก้ไขของตน สลับ branch ผ่าน Codex อีกครั้ง แล้วสังเกตว่าเนื้อหาไฟล์เปลี่ยนตาม branch

**Checkpoint:** main ยังไม่เปลี่ยน และ branch มี diff เฉพาะเรื่องที่ตั้งใจ

## Practice 4 — ตรวจ Pull Request และ merge

<PracticeIllustration asset="d01-e02-p03" />

**Primary target:** รวมการเปลี่ยนแปลงที่ผ่านการตรวจเข้าฉบับหลักได้

### Steps

1. บน GitHub เปิด **Pull requests → New pull request** เลือก base `main`, compare `feature/receipt-message`
2. ตั้งชื่อ `Clarify request receipt` และเขียน: เปลี่ยนอะไร / เพราะอะไร / ตรวจอย่างไร
3. เปิด **Files changed** อ่าน diff กับเพื่อนหนึ่งคน ถาม “มีอะไรเกินที่ขอไหม?”.
      - ถ้าทำคนเดียวให้บันทึก self-review
4. ถ้ามีจุดผิด ให้กลับไปแก้บน branch เดิม, commit และ push แล้วตรวจใหม่
5. เมื่อผ่าน ให้ merge ตามสิทธิ์ repo. กลับเครื่องให้ Codex
   ```text
   เช็คว่า branch `main` มีอัพเดตใหม่จาก remote ไหม
   ```
   ถ้ามีให้ทำการ pull commit ล่าสุดจาก remote มาโดยสั่ง prompt ผ่าน codex
   ```text
   pull อัพเดตใหม่จาก remote สำหรับ branch main
   ```

**Checkpoint:** PR เป็น Merged และข้อความใหม่อยู่บน local main หลัง pull.

**ถ้าติดขัด:** ไม่พบปุ่ม merge ให้ตรวจสิทธิ์/branch rule กับผู้ดูแล. ใช้ local branch/diff ฝึกต่อได้ แต่บันทึกว่า remote PR checkpoint ยังไม่ผ่าน
