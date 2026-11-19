---
title: "แนวทางเฉลย Day 2 Challenge — Requests API"
prev: false
next: false
---

# แนวทางเฉลย Day 2 Challenge — Requests API

[กลับไปหน้าโจทย์ Day 2 Challenge](/exercises/day-02-api/challenge)

## จัดไฟล์ในโฟลเดอร์โจทย์

```text
day2-requests-challenge/
├── service-requests-challenge.json
├── schemas.py
├── main.py
└── tests/
    └── test_requests.py
```

## 1. ให้ `schemas.py` ตรวจข้อมูล

คิดเหมือนแบบฟอร์มแจ้งซ่อม ผู้แจ้งกรอกหัวข้อ รายละเอียด และประเภท ส่วนเจ้าหน้าที่ออกเลขรับเรื่องและกำหนดสถานะเริ่มต้น `CreateRequest` คือแบบฟอร์มที่ผู้แจ้งส่งมา ส่วน `ServiceRequest` คือใบรับเรื่องที่มีข้อมูลครบแล้ว

- ใช้ `ConfigDict(extra="forbid")` ใน `CreateRequest` เพื่อปฏิเสธ field ที่อยู่นอกแบบฟอร์ม
- ใช้ `StringConstraints` ตัดช่องว่างและกำหนดความยาว เช่น `title` ด้านล่าง แล้วใช้หลักเดียวกันกับ `description` โดยตั้งช่วง 10–500 ตัวอักษร
- ใช้ `Literal` กำหนดค่าที่รับได้ของ `category` ให้ `ServiceRequest` ใช้ fields เดิมและเพิ่ม `id` ชนิด `UUID` กับ `status` ที่มีสามค่าตามโจทย์

```python
from typing import Annotated

from pydantic import StringConstraints

Title = Annotated[str, StringConstraints(strip_whitespace=True, min_length=5, max_length=100)]
```

## 2. โหลดข้อมูลและต่อ routes ใน `main.py`

ใน FastAPI `lifespan` ให้อ่านไฟล์ที่อยู่ข้าง `main.py` ด้วย `Path(__file__).with_name("service-requests-challenge.json")` และ `read_text(encoding="utf-8")` แปลง JSON เป็นรายการ แล้วตรวจแต่ละ record ด้วย `ServiceRequest.model_validate()` ใส่ผลใน dictionary ใหม่บน `app.state` โดยใช้ UUID เป็น key ทำขั้นตอนนี้ก่อน `yield` เพื่อให้ข้อมูลพร้อมเมื่อรับ request แรก [FastAPI Lifespan และ TestClient](https://fastapi.tiangolo.com/advanced/testing-events/)

| Route | วิธีทำและผลที่คาด |
| --- | --- |
| GET | คืนค่าจาก dictionary เป็น list โดยใช้ `list[ServiceRequest]` เป็น response model ครั้งแรกต้องได้ `200` พร้อมสามรายการ |
| POST | รับ `CreateRequest` สร้าง `ServiceRequest` ด้วย `uuid4()` และ `status="new"` เก็บก่อนคืน response `201` ถ้า body ผิดกฎ FastAPI ตอบ `422` |
| DELETE | ให้ `id` ใน path มี type `UUID` แล้วลบด้วย UUID นั้น ถ้าหาไม่เจอให้ใช้ `HTTPException(status_code=404, detail="Request not found")` ถ้าลบได้ให้คืน `Response(status_code=204)` ที่มี body ว่าง ถ้า `id` ผิดรูปแบบ FastAPI ตอบ `422` |

## 3. ทดสอบหนึ่งรอบตั้งแต่สร้างจนลบ

สร้าง fixture ของ `pytest` ชื่อ `client` ใน `tests/test_requests.py` ใช้ `from main import app` แล้ว `yield` client จากใน `with TestClient(app) as client:` ให้ fixture ใช้ scope เริ่มต้นของ pytest เพื่อเปิด client ใหม่และรัน `lifespan` สำหรับแต่ละ test

ตัวอย่างนี้ตรวจรายการเดียวตั้งแต่สร้างจนลบ โดยใช้ `id` จาก response `201` เพื่อเช็กว่าเป็นรายการเดียวกันตลอด

```python
def test_create_then_delete_request(client):
    created = client.post("/requests", json={
        "title": "ขอจอภาพสำหรับห้องอบรม",
        "description": "ขอจอภาพหนึ่งเครื่องสำหรับห้องฝึกอบรมสมมติ",
        "category": "equipment",
    })
    assert created.status_code == 201
    record = created.json()
    assert record["status"] == "new"
    request_id = record["id"]

    listed = client.get("/requests")
    assert listed.status_code == 200
    assert record in listed.json()

    deleted = client.delete(f"/requests/{request_id}")
    assert deleted.status_code == 204
    assert deleted.content == b""
    listed = client.get("/requests")
    assert listed.status_code == 200
    assert request_id not in {item["id"] for item in listed.json()}
```

เติม test ที่ตรวจ UUID ทั้งสามตัวจากไฟล์ กรณีลบ UUID เดิมซ้ำแล้วได้ `404` และกรณีที่ต้องได้ `422` ตามโจทย์ แล้วรันจากโฟลเดอร์หลัก

```shell
python -m pytest -q
```

## ถ้าผลต่างจากที่คาด

| อาการ | จุดที่ให้ตรวจ |
| --- | --- |
| POST รับ `title` ที่เป็นช่องว่าง หรือรับ field เกิน | ดูว่า route ใช้ `CreateRequest` หรือยัง เช็ก `strip_whitespace` และ `extra="forbid"` ใน model ถ้า response เป็น `422` อยู่แล้ว ให้ดู `detail` ว่า error ชี้ไปที่ field ที่ส่งผิดหรือไม่ |
| ลบสำเร็จแต่ได้ `200` หรือมี body | ตรวจ `status_code` ของ route และค่าที่คืน กรณีสำเร็จให้ตั้ง `204` และคืน `Response` ว่าง |
| ลบด้วย `id` ผิดรูปแบบแล้วได้ `404` | ตรวจ type ของ path parameter ว่าเป็น `UUID` เพื่อให้ FastAPI ตรวจรูปแบบก่อนค้นหารายการ |
| GET ครั้งแรกไม่มีข้อมูล หรือ test ผ่านเฉพาะเมื่อรันแยก | ตรวจว่า fixture เปิด `TestClient` ด้วย `with` ทุกครั้ง และ `lifespan` สร้าง dictionary ใหม่จาก JSON |

กลับไปเช็ก [เกณฑ์ผ่านในหน้าโจทย์](/exercises/day-02-api/challenge) แล้วเก็บผล `pytest` จาก Terminal ของตัวเอง
