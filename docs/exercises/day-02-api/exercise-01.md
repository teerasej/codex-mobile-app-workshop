---
title: "Day 2 · Exercise 1 — Python bridge และ API แรก"
prev: {"text": "ภาพรวมวัน", "link": "/exercises/day-02-api/"}
next: {"text": "Exercise 2", "link": "/exercises/day-02-api/exercise-02"}
---

# Exercise 1 — Python bridge และ API แรก


> **Day 2 · Python API · 09:30–10:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-02-api/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

::: tip วิธีทำงานวันนี้
ก่อนเริ่ม Exercise 1 ให้ Codex สร้าง branch **feature/request-api** จาก main ที่ไม่มีงานค้างเพียงครั้งเดียว. ถ้าอยู่ branch นี้จาก Practice ก่อนแล้วให้ใช้ต่อ ไม่สร้างซ้ำและไม่กลับไปเริ่มจาก main ใหม่. ทุก Practice เริ่มด้วยตรวจ plan และจบด้วย checkpoint → commit เฉพาะไฟล์ที่ตรวจแล้ว. ยังไม่ merge จนจบวัน

คำสั่ง **python** ต่อจากสร้าง environment หมายถึง Python ใน **.venv** ของโปรเจคเท่านั้น. หาก Codex เปิด terminal ใหม่ ให้ยืนยัน interpreter นี้ก่อนรัน. ผู้เรียนไม่จำเป็นต้องจำคำสั่ง แต่ต้องรู้ว่าเป็นการติดตั้ง รัน server หรือรัน test
:::


## Scenario

ก่อนต่อฐานข้อมูล เราจะอ่านคำขอสมมติและแยกหน้าที่ของ Python เพื่อให้คุยกับ Codex รู้เรื่อง

## Practice 1 — อ่านข้อมูลด้วย function, class และ module

<PracticeIllustration asset="d02-e01-p01" eager />

**Primary target:** ตามรอยจาก JSON หนึ่งรายการไปเป็น Python object และข้อความผลลัพธ์ได้

### Steps

1. เปิด Terminal ของ local project. ให้ Codex ตรวจ Python 3.12 และสร้าง environment ด้วยคำสั่งตาม OS:

   Windows PowerShell:

   ~~~powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r api/requirements.txt
   ~~~

   macOS:

   ~~~bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r api/requirements.txt
   ~~~

   หาก Windows ไม่อนุญาต activate ใช้ **.\.venv\Scripts\python.exe** แทน python ในคำสั่งถัดไป ไม่แก้ system policy
2. ส่ง prompt แล้วตรวจแผนก่อนให้ทำ:

   ~~~text
   สร้างเฉพาะ Python bridge สำหรับอ่าน data/service-requests.json
   ทำ api/bridge/request_model.py มี dataclass RequestSummary และ function format_summary
   ทำ api/bridge/demo.py import ทั้งสองอย่างแล้วอ่าน JSON ด้วย UTF-8
   แสดงจำนวนรายการทั้งหมด และ title/status ของรายการแรก
   ใช้ pathlib หาไฟล์จากตำแหน่ง script ไม่ผูกกับ path เครื่อง
   อธิบาย function, class, module เทียบกับสูตรย่อย แบบฟอร์ม และแฟ้มเอกสาร
   ไม่สร้าง FastAPI หรือ database ใน Practice นี้
   ~~~
3. ให้รัน **python api/bridge/demo.py**. ตรวจว่าได้ 4 รายการและ title แรกตรงไฟล์ JSON
4. ขอ Codex ชี้บรรทัดที่อ่าน JSON, สร้าง object และเรียก function. เปลี่ยน format ของข้อความหนึ่งจุดแล้วรันอีกครั้ง โดยไม่แก้ข้อมูลต้นฉบับ

**Checkpoint:** จำนวน 4 ตรง sample และอธิบายได้ว่าข้อมูลกับวิธีแสดงผลอยู่คนละส่วน

## Practice 2 — เปิด API ที่ตอบได้

<PracticeIllustration asset="d02-e01-p02" />

**Primary target:** เรียก endpoint แรกแล้วแยก HTTP response ออกจาก Python source ได้

### Steps

1. ส่ง:

   ~~~text
   สร้าง api/app/__init__.py และ api/app/main.py สำหรับ FastAPI
   เพิ่มเฉพาะ GET /health ตาม docs/api-contract.md
   อ่าน APP_VERSION จาก environment โดย default v1
   ยังไม่เชื่อม DB, ไม่เพิ่ม auth และไม่สร้างตารางตอน start
   แสดงวิธีรันจาก root และ URL /health กับ /docs
   ~~~
2. ให้รัน server จาก root ใน terminal ที่เปิดค้างได้:

   ~~~shell
   python -m uvicorn app.main:app --app-dir api --reload --host 127.0.0.1 --port 8000
   ~~~
3. เปิด browser ที่ **http://127.0.0.1:8000/health** แล้ว **http://127.0.0.1:8000/docs**
4. ใน /docs ขยาย GET /health เลือก **Try it out → Execute** และดู HTTP status กับ response body

**Checkpoint:** เห็น 200 และ status=ok, version=v1. รู้ว่า terminal ที่รัน server ต้องเปิดอยู่

**ถ้าติดขัด:** ModuleNotFoundError ให้ตรวจ interpreter/.venv และ working folder ก่อนลง package ซ้ำ. Port in use ให้หยุดเฉพาะ server ฝึกเดิมด้วย Ctrl+C แล้วเริ่มใหม่
