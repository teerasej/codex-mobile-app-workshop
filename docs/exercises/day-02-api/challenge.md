---
title: "Day 2 Challenge — สร้างและทดสอบ Requests API"
prev: false
next: false
---

# Day 2 Challenge — สร้างและทดสอบ Requests API

**โจทย์เสริม · 30–45 นาที** ลองสร้าง API รับเรื่องจากไฟล์ JSON ด้วย FastAPI แล้วใช้ test ยืนยันว่าเพิ่ม ดูรายการ และลบ Request ได้ตามที่กำหนด

**[ดูแนวทางเฉลย](/exercises/day-02-api/challenge-solution)**

## เตรียมก่อนเริ่ม

- ทำ Exercise 4 จนรัน `pytest` ได้แล้ว เปิดโฟลเดอร์ใหม่แยกจากโปรเจกต์ Service Desk Lite ใน Codex
- สร้างและเปิดใช้ `.venv` ด้วย Python 3.12 ในโฟลเดอร์นี้ตาม [วิธีเตรียม Python ใน Exercise 1](/exercises/day-02-api/exercise-01) แล้วติดตั้ง FastAPI, Pydantic 2, HTTPX และ pytest

  ```shell
  python -m pip install fastapi "pydantic>=2,<3" httpx pytest
  ```

- ดาวน์โหลดไฟล์ด้านล่างแล้ววางไว้ที่โฟลเดอร์หลักของโจทย์ ข้าง `main.py` ที่จะสร้างใน Practice 2

<DownloadFile file="service-requests-challenge.json" />

Python และแพ็กเกจที่ใช้ในโจทย์นี้ใช้ฟรี ใช้สิทธิ์ Codex ที่เตรียมไว้สำหรับ workshop และเก็บข้อมูลของ API นี้ใน memory บนเครื่อง

## Practice 1 — สร้าง data models

สร้าง Pydantic models เพื่อกำหนดข้อมูลที่ API รับและข้อมูลที่ API ส่งกลับ

### Steps

1. เปิดไฟล์ JSON แล้วสังเกตว่ามี Request สมมติสามรายการ แต่ละรายการมี UUID ที่กำหนดไว้แล้ว
2. สร้าง `schemas.py` ให้มี `CreateRequest` และ `ServiceRequest` ใช้กฎด้านล่างเป็นโจทย์ให้ Codex

   | Field | กฎ |
   | --- | --- |
   | `title` | ข้อความ 5–100 ตัวอักษรหลังตัดช่องว่างหัวท้าย |
   | `description` | ข้อความ 10–500 ตัวอักษรหลังตัดช่องว่างหัวท้าย |
   | `category` | `it`, `facility` หรือ `equipment` |
   | `id` | UUID ใน `ServiceRequest` โดย API สร้างให้เมื่อเพิ่มรายการ |
   | `status` | `new`, `in_progress` หรือ `done` ใน `ServiceRequest` โดยรายการที่สร้างใหม่เริ่มที่ `new` |

   ```text
   อ่าน service-requests-challenge.json แล้วเสนอแผนสั้น ๆ สำหรับสร้าง schemas.py ด้วย Pydantic 2 ให้ CreateRequest รับเฉพาะ title, description และ category และปฏิเสธ field อื่นทั้งหมด ตัดช่องว่างหัวท้ายก่อนตรวจความยาว title 5–100 และ description 10–500 ตัวอักษร category รับ it, facility หรือ equipment ส่วน ServiceRequest เพิ่ม id ชนิด UUID และ status ที่รับ new, in_progress หรือ done เมื่ออธิบายแผนแล้วให้สร้างเฉพาะ schemas.py
   ```

**Checkpoint** ตรวจว่า `ServiceRequest` อ่านข้อมูลตัวอย่างได้ครบสามรายการ และ `CreateRequest` ปฏิเสธ `title` ที่มีแต่ช่องว่างหรือ body ที่ส่ง `id` หรือ `status` มาด้วย

## Practice 2 — สร้างสาม routes

ให้ FastAPI โหลด Request จาก JSON มาไว้ใน memory และจัดการรายการผ่านสาม routes

### Steps

1. ให้ Codex สร้าง `main.py` ตามตาราง เมื่อแอปเริ่มใหม่ให้โหลดสามรายการเดิมจากไฟล์ ข้อมูลที่เพิ่มหรือลบระหว่างรันอยู่ใน memory เท่านั้น

   | Route | ผลที่ต้องได้ |
   | --- | --- |
   | `GET /requests` | `200` พร้อม JSON array ของรายการปัจจุบัน |
   | `POST /requests` | `201` พร้อมรายการใหม่ที่มี UUID และ `status` เป็น `new` หรือ `422` เมื่อ body ผิดกฎ |
   | `DELETE /requests/{id}` | `204` พร้อม body ว่าง, `404` เมื่อหา UUID ไม่เจอ หรือ `422` เมื่อ `id` ผิดรูปแบบ UUID |

   ```text
   ใช้ schemas.py สร้าง FastAPI app ใน main.py เมื่อแอปเริ่มทำงานให้อ่านไฟล์ service-requests-challenge.json ที่อยู่ข้าง main.py และโหลดข้อมูลเข้า memory โดยใช้ ServiceRequest สร้าง GET /requests ให้คืนรายการปัจจุบันด้วย 200 สร้าง POST /requests ให้รับ CreateRequest สร้าง UUID และตั้ง status เป็น new แล้วคืนรายการใหม่ด้วย 201 ถ้า body ผิดกฎให้ได้ 422 สร้าง DELETE /requests/{id} ที่รับ UUID และลบเฉพาะรายการนั้น ให้ได้ 204 พร้อม body ว่าง หรือ 404 ถ้าไม่พบ UUID ส่วน id ที่ไม่ใช่ UUID ให้ได้ 422 เก็บการเพิ่มและลบไว้ใน memory
   ```

**Checkpoint** ชี้ให้เห็นใน `main.py` ว่าแต่ละ route คืนอะไร และอธิบายได้ว่าทำไมสามรายการเดิมจึงกลับมาเมื่อเริ่มแอปใหม่

## Practice 3 — เขียนและรัน automated tests

ใช้ `pytest` และ FastAPI `TestClient` ตรวจพฤติกรรม API จาก HTTP status และ response body

### Steps

1. สร้าง `tests/test_requests.py` ให้แต่ละ test เริ่มจากข้อมูลตัวอย่างชุดใหม่ ใช้กรณีทดสอบด้านล่างเป็นโจทย์ให้ Codex

   ```text
   เขียน tests/test_requests.py ด้วย pytest และ FastAPI TestClient ให้แต่ละ test เปิด TestClient ใน with block เพื่อเริ่มจากข้อมูลตัวอย่างชุดใหม่ ตรวจว่า GET ได้ 200 และคืน UUID ทั้งสามตัวจากไฟล์ ตรวจว่า POST ได้ 201 คืน UUID ใหม่และ status เป็น new และ GET เห็นรายการนั้น ตรวจว่า DELETE ได้ 204 กับ body ว่าง และ GET ไม่พบรายการที่ลบแล้ว ลบ UUID เดิมอีกครั้งต้องได้ 404 ทดสอบ POST ด้วย title ที่มีแต่ช่องว่าง, category ผิด, และ field เกิน แยกเป็นกรณีที่ต้องได้ 422 รวมถึง DELETE ด้วย id ที่ไม่ใช่ UUID ต้องได้ 422
   ```

2. รันจากโฟลเดอร์เดียวกับ `main.py` ด้วย Python ใน virtual environment ของโจทย์

   ```shell
   python -m pytest -q
   ```

3. ถ้ามี test ไม่ผ่าน ให้อ่านว่าค่าที่คาดต่างจาก response จริงตรงไหน แล้วให้ Codex ช่วยไล่จาก test ไปหา route หรือ model ที่เกี่ยวข้อง แก้ตามกติกาของโจทย์แล้วรันทั้งชุดอีกครั้ง

**Checkpoint** แสดงผลจาก Terminal ที่ยืนยันว่ารันครบทุกกรณีและผ่านทั้งหมด เปิด test สักหนึ่งกรณีแล้วอธิบายได้ว่าตรวจอะไรใน response

[กลับไปสรุป Day 2](/exercises/day-02-api/summary)
