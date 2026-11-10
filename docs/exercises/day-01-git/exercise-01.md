---
title: "Day 1 · Exercise 1 — เริ่มโปรเจค และเก็บตัวอย่างแรก"
prev: {"text": "ภาพรวมวันที่ 1", "link": "/exercises/day-01-git/"}
next: {"text": "Exercise 2", "link": "/exercises/day-01-git/exercise-02"}
---

# Exercise 1 — เริ่มโปรเจค และเก็บตัวอย่างแรก


> **Day 1 · Git · 09:30–10:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-01-git/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## เวลาในช่วงนี้

| เวลา | กิจกรรม |
| --- | --- |
| 09:30–09:45 | ให้ Codex รู้จักโปรเจค |
| 09:45–10:00 | Markdown: อธิบาย 4 / ลงมือ 8 / ตรวจ 3 นาที |
| 10:00–10:25 | ทำ initial commit |
| 10:25–10:30 | ทบทวนและแก้จุดติดขัด |

## Scenario

ทีมตกลงว่าจะรับ Request บริการในแอปเดียว เราต้องรู้ว่ากำลังทำงานในโฟลเดอร์ใด และเก็บไฟล์ตั้งต้นไว้เป็นจุดอ้างอิง

## Practice 1 — ให้ Codex รู้จักโปรเจค

<PracticeIllustration asset="d01-e01-p01" eager />

**Primary target:** ระบุขอบเขตแอปจากไฟล์จริงได้

### Steps

1. เปิด ChatGPT desktop app
2. เลือก **Codex** จากเมนู ChatGPT
3. แล้วเพิ่มโฟลเดอร์ `service-desk-lite` เป็น local project. เลือกทำงานกับโฟลเดอร์นี้โดยตรง (**Local** ถ้ามีตัวเลือก)
4. เปิด task ใน project นี้ แล้วส่ง:

   ```text
   จาก project-brief.md และ api-contract.md
   สรุปว่าให้หน่อยว่าโปรเจคนี้ทำอะไรได้ 4 ข้อ พร้อมสิ่งที่อยู่นอกขอบเขตการทำงาน 3 ข้อ และระบุไฟล์ต้นทางของคำตอบ
   ```
   ```text
   ระบุโฟลเดอร์ที่กำลังทำงาน
   ```
5. เปรียบเทียบคำตอบกับ brief
6. เมื่อเปรียบเทียบคำตอบกับ brief และตรวจแล้วว่าถูกต้อง ให้ส่ง prompt ต่อไปนี้ใน task เดิม เพื่อให้ Codex บันทึกผลลง `docs/review-log.md`:

   ```text
   อัปเดตเฉพาะ review-log.md โดยเก็บข้อความเดิมทั้งหมด
   เพิ่มบันทึก Day 1 / Exercise 1 / Practice 1 ตามแบบฟอร์มที่มีอยู่ ถ้ามีบันทึกนี้แล้วให้ปรับรายการเดิม ไม่เพิ่มซ้ำ
   บันทึกว่า “ระบุขอบเขตแอปจากไฟล์จริงได้” พร้อมข้อมูลสรุปด้านบน
   บันทึกไฟล์ แล้วแสดง diff พร้อมสรุปสิ่งที่เพิ่มหรือเปลี่ยนให้ฉันตรวจ
   ```

7. เปิด `docs/review-log.md` ผ่าน file preview แล้วตรวจว่าเป้าหมาย ขอบเขตแอป และไฟล์อ้างอิงตรงกับสิ่งที่เราตรวจแล้ว และข้อความเดิมยังอยู่ครบ หากไม่ตรง ให้บอก Codex แก้เฉพาะจุดนั้นก่อนทำ Checkpoint

**Checkpoint:** ชี้ได้ว่า local project อยู่ที่ไหน และอธิบาย Sign in → My requests → Detail/Create ได้โดยไม่อ่านตาม AI ทุกคำ

## Practice 2 — เขียน README ด้วย Markdown

<PracticeIllustration asset="d01-e01-markdown" />

**Primary target:** ใช้ Markdown จัดรูปแบบส่วน Workshop notes ใน README ให้ผู้อื่นอ่าน และเข้าใจการทำงานได้


> **License:** Markdown และ plain-text editor ไม่ต้องซื้อ paid license เพิ่ม ใช้สิทธิ์ Codex/GitHub ตามเงื่อนไขเดิมของวันนี้

### Markdown ใช้ทำอะไร

Markdown คือข้อความธรรมดาที่ใช้เครื่องหมายช่วยจัดรูปแบบ ลองนึกถึงสูตรอาหาร: หัวข้อบอกชื่อเมนู รายการบอกวัตถุดิบ และเลขลำดับบอกว่าทำอะไรก่อนหลัง เราอ่านต้นฉบับได้ และโปรแกรมที่รองรับจะแสดงเป็นไฟล์ที่อ่านง่าย

| Syntax | ใช้ทำอะไร |
| --- | --- |
| `#` / `##` / `###` ตามด้วยช่องว่าง | หัวข้อใหญ่และหัวข้อย่อย |
| `- ` และ `1. ` | รายการแบบจุดและแบบเรียงลำดับ |
| `**ข้อความ**` | เน้นข้อความเป็นตัวหนา |
| `[ชื่อที่อ่านได้](ปลายทาง)` | ลิงก์ไปไฟล์หรือเว็บไซต์ |
| backtick หนึ่งตัวครอบข้อความ | แสดงชื่อไฟล์หรือคำสั่งแบบ inline code |
| backtick สามตัวเปิดและปิดคนละบรรทัด | แสดง code block หลายบรรทัด |

> **สังเกต:** เครื่องหมายใน Markdown เป็นส่วนหนึ่งของไฟล์ ส่วน Preview แสดงรูปแบบที่อ่านง่าย การแสดงคำสั่งใน code block ไม่ได้รันคำสั่งนั้น

### Steps

1. เปิด `README.md` ที่ root ของโฟลเดอร์ผู้เรียน `service-desk-lite` ด้วย plain-text editor
   1. Windows ใช้ **Notepad**
   2. macOS ใช้ **TextEdit → Format → Make Plain Text** เมื่อจำเป็น
      - ตรวจว่าแก้ไฟล์ `.md` เดิม ไม่ใช่สร้างไฟล์ `.md.txt`
2. เพิ่มส่วนต่อไปนี้ไว้ที่ท้ายไฟล์

ตัวอย่างด้านขวาแสดงหน้าตาก่อนแก้ข้อความในขั้นถัดไป

<div class="markdown-comparison">
<div>

**ต้นฉบับที่คัดลอกไปเพิ่มท้าย README**

````markdown
## Workshop notes

**Service Desk Lite** คือโปรเจคฝึกของเรา

### สิ่งที่เราจะฝึก

- อ่าน `README.md`
- ตรวจรูปแบบไฟล์

### ลำดับการทำงาน

1. แก้ไฟล์
2. ตรวจผลก่อน commit

[Project brief](docs/project-brief.md)

```shell
git status
```
````

</div>
<div>

**ตัวอย่างหลังแสดงผล Markdown**

<MarkdownWorkshopPreview />

</div>
</div>

3. ลองแก้รายการข้อที่สองด้วยตนเองเป็นข้อความนี้ โดยคงเครื่องหมายรายการไว้ แล้วบันทึกไฟล์เป็น UTF-8

   ```markdown
   - ตรวจ Markdown ด้วยตนเอง
   ```

4. เทียบต้นฉบับกับตัวอย่าง Preview ด้านบน สังเกตหัวข้อ ตัวหนา รายการ ลิงก์ inline code และ code block ถ้า file preview ของเครื่องแสดง Markdown ได้ ให้เปิดตรวจด้วย

5. ถ้าพบข้อผิดพลาด ให้แก้ด้วยตนเองและตรวจซ้ำ

**Checkpoint:** README เดิมยังอยู่ มี Workshop notes เพียงหนึ่งส่วน

**ถ้าติดขัด:** ถ้าทั้งไฟล์ถูกแสดงเป็น code ให้ตรวจ backtick เปิด/ปิด ถ้าลิงก์เสีย ให้ตรวจว่าคิดตำแหน่งจาก root README ไม่ใช่จากหน้าเว็บไซต์คู่มือ ใช้บรรทัดว่างคั่นย่อหน้าและรายการ

อ่านเพิ่มเติม: [Basic writing and formatting syntax — GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Practice 3 — ทำ initial commit

<PracticeIllustration asset="d01-e01-p02" />

**Primary target:** เก็บสถานะเริ่มต้นเป็น commit ที่ตรวจสอบได้

### Steps

1. ให้ Codex ตรวจว่ามี Git repository อยู่แล้วหรือไม่.
2. ส่ง prompt เพื่อเตรียม Git:

   ```text
   เตรียม Git เฉพาะโฟลเดอร์ service-desk-lite นี้
   ```

3. ส่ง prompt เพื่อดูรายการไฟล์ที่จะ commit:

   ```text
   แสดงรายการไฟล์ที่จะ commit
   ```

4. ส่ง prompt เพื่อถามข้อความ commit:

   ```text
   ถ้า commit จะใช้ข้อความอะไร
   ```

5. ตรวจรายการไฟล์และข้อความ commit แล้วส่ง prompt เพื่อ commit:

   ```text
   commit ไฟล์ทั้งหมด โดยใช้ ข้อความ `docs: start service desk workshop`
   ```

**Checkpoint:** มี commit หนึ่งรายการที่รวม README พร้อม Workshop notes และ working tree ไม่มีการแก้ค้าง. บันทึก commit ID ใน review log แล้วบันทึก log เมื่อทำ Practice ถัดไป

> ⚠️: ไม่ต้องสร้าง commit ทุกครั้งที่พิมพ์หนึ่งบรรทัด

## Practice 4 — ให้ Codex แก้ README และ commit การเปลี่ยนแปลง

<PracticeIllustration asset="d01-e01-readme-commit" />

**Primary target:** ตรวจ working tree และ diff ก่อน commit การแก้ README

### Steps

1. ใน task เดิม ให้ Codex แก้ส่วน Workshop notes:

   ```text
   แก้เฉพาะส่วน Workshop notes ใน README.md ให้เพิ่มหัวข้อ "### ผลลัพธ์ที่คาดหวัง" พร้อมรายการ 2 ข้อ
   ```

2. ถามสถานะ working tree:

   ```text
   ตรวจ working tree ตอนนี้ มีไฟล์ใดถูกแก้ไขบ้าง
   ```

3. ให้ Codex แก้ส่วนเดิมอีกครั้ง:

   ```text
   แก้ส่วน Workshop notes ใน README.md อีกครั้ง ให้รายการใน "ผลลัพธ์ที่คาดหวัง" กระชับขึ้น แก้เฉพาะส่วนนี้
   ```

4. ให้แสดง diff:

   ```text
   แสดง diff ของ README.md พร้อมสรุปสิ่งที่เปลี่ยน
   ```

5. ตรวจ diff ว่ามีเฉพาะส่วน Workshop notes ที่เปลี่ยน แล้วสั่ง commit:

   ```text
   commit การแก้ README.md นี้ โดยใช้ข้อความ `docs: update workshop notes`
   ```


**Checkpoint:** diff เปลี่ยนเฉพาะส่วน Workshop notes มี commit ใหม่ และ working tree ไม่มีการแก้ค้าง

## Practice 5 — ดู Git history และผู้ commit

<PracticeIllustration asset="d01-e01-git-history" />

**Primary target:** อ่าน history และแยกความต่างของแต่ละ commit ได้

### Steps

1. ใน task เดิม ให้ Codex แสดง history:

   ```text
   แสดง git history 3 รายการล่าสุด
   ```

2. ถามความต่างของ commit และผู้ที่ commit:

   ```text
   บอกได้ไหมว่าทั้ง 2 commit ต่างกันยังไง และใครเป็นคน commit
   ```

3. เปรียบเทียบคำตอบกับ history ที่แสดง ตรวจ commit ID ข้อความ commit และชื่อผู้ commit

**Checkpoint:** อธิบายได้ว่า commit `docs: start service desk workshop` และ `docs: update workshop notes` ต่างกันอย่างไร และใครเป็นผู้ commit
