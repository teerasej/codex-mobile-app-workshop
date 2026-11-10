---
title: "Day 1 · Exercise 4 — กำหนดวิธีร่วมงานกับ Codex"
prev: {"text": "Exercise 3", "link": "/exercises/day-01-git/exercise-03"}
next: {"text": "สรุปท้ายวัน", "link": "/exercises/day-01-git/summary"}
---

# Exercise 4 — กำหนดวิธีร่วมงานกับ Codex


> **Day 1 · Git · 14:45–16:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-01-git/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

พรุ่งนี้เราจะเริ่มสร้าง API. เราต้องการผู้ช่วยที่ทำทีละเรื่องและรายงานผลลัพธ์ในแต่ละขั้นตอนให้เราตรวจสอบ ไม่ใช่ส่งไฟล์จำนวนมากจนตรวจไม่ทัน

## Practice 1 — ตั้ง core instructions

<PracticeIllustration asset="d01-e04-p01" eager />

**Primary target:** ใช้ AGENTS.md กำหนดขอบเขตการทำงานของ Codex ได้

### Steps

1. จาก main สร้าง branch `docs/codex-working-agreement`

   ```text
   ตรวจ git status ว่า working tree สะอาดและอยู่บน main
   จากนั้นสร้างและสลับไป branch docs/codex-working-agreement
   แล้วรายงานผล
   ```
2. ให้เราเปิด `docs/agents-template.md` ใน starter แล้วอ่าน Instruction ทั้งหมด
3. ขอ Codex คัดลอกเป็น `AGENTS.md` ที่ root ของ **โปรเจคผู้เรียน** (เช่น `service-desk-lite`) แล้วเพิ่มชื่อ project และวิธีตรวจ API/Flutter ที่เราจะใช้. ยังไม่สร้าง code และไม่เพิ่มเงื่อนไขที่เราไม่ได้ตกลง

   ```text
   คัดลอก docs/agents-template.md เป็น AGENTS.md ที่ root ของโปรเจค service-desk-lite
   แล้วเพิ่มเฉพาะ 2 ส่วนนี้:
   1) ชื่อ project: service-desk-lite
   2) วิธีตรวจงาน: API ตรวจด้วย curl ตาม docs/api-contract.md และ Flutter ตรวจด้วย flutter analyze และ flutter test
   ห้ามสร้าง code และห้ามเพิ่มเงื่อนไขอื่นที่ฉันไม่ได้ระบุ
   เมื่อเสร็จให้แสดง git diff ให้ฉันตรวจก่อน commit
   ```
4. เปิด chat ใหม่ใน local project เดิม แล้วส่งทีละ prompt:

   ```text
   อ่าน AGENTS.md แล้วสรุป Instruction ที่ใช้กับงานนี้ 4 ข้อ
   ```

   ```text
   สมมติฉันขอ “ทำแอปทั้งระบบแล้ว deploy เลย” นายจะไม่ทำอะไรบ้าง และจะถามอะไรกลับ?
   ```

5. ตรวจว่ามีการทำทีละ Practice, review diff, test จริง และไม่เปิดเผย secrets
   - ถ้าไม่มีข้อไหน ให้บอก codex เพิ่มและตรวจสอบ instruction จุดนี้สามารถนั่งแลกเปลี่ยนผลลัพธ์ของนักเรียนแต่ละคนได้

**Checkpoint:** task ใหม่อ่าน Instructionจ ากไฟล์ได้ และสามารถบอกได้ว่า AGENTS.md ไม่ใช่การรับประกันว่า AI จะทำถูกทุกครั้ง เรายังตรวจผลเอง

## Practice 2 — เตรียม backlog และส่งต่อ Day 2

<PracticeIllustration asset="d01-e04-p02" />

**Primary target:** แบ่งงาน API เป็นลำดับที่ตรวจทีละส่วนได้

### Steps

1. ส่ง:

   ```text
   อ่าน docs/api-contract.md แล้วสร้าง docs/day2-plan.md
   แบ่งงานเป็น Python bridge, routes/validation, PostgreSQL persistence,
   authentication และ tests โดยระบุผลตรวจได้ของแต่ละช่วง
   อย่าเพิ่ม frontend, deploy, extra routes หรือ implementation code วันนี้
   ```
2. ตรวจว่าตรงกับ Day 2 guide; ให้ Codex แก้เฉพาะแผนที่ขาด ไม่ขยาย scope
3. กลับ main, pull และตรวจ `git status`. จด main commit ล่าสุดไว้เป็นจุดเริ่มวันถัดไป

**Checkpoint:** มี working agreement และ Day 2 plan ใน repo พร้อมประวัติที่อธิบายได้
