---
title: "Service Desk Lite — ข้อตกลง API สำหรับ workshop"
prev: false
next: false
---

<DownloadFile file="api-contract.md" />

# Service Desk Lite — ข้อตกลง API สำหรับ workshop

นี่คือข้อตกลงที่ออกแบบสำหรับแบบฝึกหัด ไม่ใช่ข้อความที่คัดมาจาก approved outline ใช้เหมือนแบบฟอร์มใบสั่งอาหาร: คนรับออร์เดอร์กับครัวต้องใช้ช่องข้อมูลเดียวกัน

## Data model

`ServiceRequest`: `id` (UUID string), `title` (trimmed 5–100 characters), `description` (trimmed 10–500 characters), `category` (`it`, `facility`, `equipment`), `status` (`new`, `in_progress`, `done`), `owner_username` (server assigns from token), `created_at` (UTC ISO 8601 string).

`CreateRequest` รับเฉพาะ title, description, category; ปฏิเสธ unknown fields และ client-supplied owner/status/id ด้วย 422. `UpdateStatus` รับเฉพาะ status ที่อยู่ในสามค่า. ตรวจความยาวหลัง trim. ไม่มี delete route หรือ pagination ในรุ่นฝึกนี้. `GET /requests` เรียง created_at ASC แล้ว id ASC เพื่อให้ตรวจผลซ้ำได้.

`User`: integer id, unique username, password_hash. ไม่ส่ง password/hash กลับ API. Seed users ก่อน seed requests. ไม่เปิด endpoint สมัครผู้ใช้สาธารณะ.

## Endpoints

| Method / path | Input | Successful response | Access / failure |
| --- | --- | --- | --- |
| GET /health | none | 200: `{ "status": "ok", "version": "v1" }` | public; ไม่แสดง config/secrets |
| POST /auth/token | form-urlencoded username, password | 200: `{ "access_token": "…", "token_type": "bearer" }` | wrong credentials → 401 |
| GET /requests | none | 200: JSON array of ServiceRequest | bearer required; current owner's rows only |
| GET /requests/{id} | UUID path | 200: ServiceRequest | missing/other owner's UUID → 404 |
| POST /requests | CreateRequest JSON | 201: ServiceRequest, status=new | bearer required |
| PATCH /requests/{id}/status | `{ "status": "done" }` | 200: updated ServiceRequest | bearer + owner required; wrong enum → 422 |

ทุก protected route: missing/invalid/expired token → 401 พร้อม `WWW-Authenticate: Bearer`; UUID ที่ไม่ถูกชนิด → 422. 404 มี body `{ "detail": "Request not found" }`. 401 มี `{ "detail": "Invalid credentials" }` หรือข้อความทั่วไปที่ไม่เผยว่ามีบัญชีนั้นหรือไม่. Validation ใช้ FastAPI 422 detail list; ไม่บังคับข้อความ error ทุกตัวอักษร. Database unavailable → 503 กับข้อความทั่วไป ไม่แสดง connection string.

## Authentication baseline

- ใช้ pwdlib Argon2 hash + PyJWT, HS256 และ key จาก JWT_SECRET; token มี sub=username และ exp (30 นาที)
- verify signature, exp, algorithm และผู้ใช้มีอยู่ทุกครั้ง; ไม่ใช้ decode แบบข้าม signature verification
- อ่าน env ด้วย python-dotenv จาก api/.env ในเครื่อง; production/container ใช้ environment variables
- การฝึก password/token นี้เป็น baseline เพื่อเรียนรู้; deployment ใช้เฉพาะบัญชีทดลอง ไม่ใช่ company SSO
- Day 2 Exercise 2 อนุญาต in-memory repository ชั่วคราวเพื่อเรียน route; ก่อนจบวันต้องเปลี่ยนเป็น PostgreSQL และปิด routes ด้วย auth

## Files / modules ที่ให้ Codex สร้างทีละช่วง

- `api/app/main.py`: FastAPI app และ routers; `/health`; CORS; ห้าม seed หรือ create tables เมื่อ import/start server
- `api/app/schemas.py`: Pydantic models; `api/app/repository.py`: database access ด้วย psycopg parameter binding `%s` + argument tuple ไม่ต่อ input เป็น SQL
- `api/app/config.py`: load api/.env using path relative to this file; ใช้ env ทับค่าไฟล์ได้; validate required config without logging secret
- `api/app/auth.py`: hashing/login/token/current user; `api/app/seed.py`: manual idempotent setup; `api/app/__init__.py`
- `api/tests/`: pytest ใช้ FastAPI TestClient และ dependency overrides กับ test doubles; ไม่ต่อ Azure DB หรือ seed production ใน unit tests
- ให้ settings/repository เป็น dependency ที่สร้างเมื่อใช้จริง ไม่โหลด `.env` หรือตรวจ required runtime secrets ตอน import app. Tests inject dummy settings/key และ test repository ก่อนส่ง request; ไม่มี test ใดต้องอ่าน `.env` ของผู้เรียน
- `pytest.ini` ที่ root กำหนด `pythonpath = api`

## Seed และ persistence

API ใช้ **runtime login** จาก `api/.env` เท่านั้น. Manual seed รับ host/database/setup username ผ่าน interactive prompts และ setup password ผ่าน getpass แยกจาก runtime `.env`; ไม่บันทึก setup credentials. ใช้ TLS และไม่แสดง connection string/password/hash

รันจากโฟลเดอร์ api: `python -m app.seed --check`, `python -m app.seed`, `python -m app.seed --check`. `--check` อ่านอย่างเดียว ไม่ apply schema/สร้าง users/hash; รายงานจำนวน users/requests และต่อ owner. ถ้า database ยังไม่มีตารางให้บอกว่า schema ยังไม่พร้อมโดยไม่สร้างให้

Seed ปกติอ่าน schema.sql และ ../data/service-requests.json; apply additive schema ใน transaction. เพิ่ม user ที่ขาดด้วย pwdlib Argon2 โดยรับ app password ผ่าน getpass **เฉพาะ user ที่ยังไม่มี**. ผู้ได้รับ Student ZIP ใช้ app passwords ที่ได้รับ; user ที่มีอยู่ต้องคง hash เดิมและไม่ขอ password ใหม่เพื่อแสร้งว่า reset แล้ว. INSERT requests เฉพาะ UUID ที่ยังไม่มี ไม่เขียนทับ status/เนื้อหา/เวลา/owner เดิม ไม่ DROP/TRUNCATE. Commit เมื่อสำเร็จและ rollback เมื่อผิดพลาด

**พื้นที่ที่ผู้สอนเตรียม:** มี users 2/requests 4 ก่อนเริ่มแล้ว. เก็บ `.env`, JWT_SECRET และ app passwords จาก Student ZIP เดิม ไม่คัดลอก `.env.example` ทับ. Seed rerun เป็นการตรวจว่าคงข้อมูลเดิม ไม่ใช่การล้างกลับจุดเริ่มต้น. ถ้าฝึกเพิ่มข้อมูลแล้วให้เทียบกับ baseline ก่อนรันแทน. **พื้นที่ของตนเอง:** ให้เจ้าของเตรียม setup/runtime logins และสิทธิ์ก่อน seed; ใช้ `.env.example` เฉพาะเมื่อยังไม่มี `.env`

## Local / cloud configuration

- API port 8000; local `127.0.0.1`, Docker bind `0.0.0.0`
- Flutter Web ใช้ `http://localhost:3000`; API allowed origins แยกด้วย comma จาก CORS_ORIGINS; allow_methods GET/POST/PATCH/OPTIONS, allow_headers Authorization/Content-Type, allow_credentials=false (bearer header; ไม่ใช้ cookies)
- Flutter `API_BASE_URL` รับจาก `--dart-define`, ไม่ hardcode host; เก็บ token ใน memory เท่านั้นและล้างเมื่อ logout/401
- Android local lab ใช้ `adb reverse tcp:8000 tcp:8000` แล้ว URL `http://127.0.0.1:8000`; HTTP exception เฉพาะ debug manifest. Day 4 ใช้ HTTPS จริง
- Cloud DATABASE_URL ต้องใช้ TLS (`sslmode=require` เป็น lab minimum; CA validation ให้เป็นไปตาม IT policy). ไม่ปิด TLS เพื่อแก้ปัญหา
- `GET /health` พิสูจน์ process ทำงานเท่านั้น; ต้อง login/create/read หลัง deployment เพื่อพิสูจน์ DB ด้วย

## Expected sample result

หลังเตรียม database ใหม่และก่อนเพิ่มข้อมูล: learner01 เห็น 3 requests (แต่ละ status อย่างละหนึ่ง), learner02 เห็น 1 request. GET ของ learner02 ไปยัง UUID ของ learner01 ต้องเป็น 404. หลังสร้างหนึ่งรายการด้วย learner01 จำนวนของเขาเพิ่มจาก 3 เป็น 4; ถ้าฝึกซ้ำให้นับจากค่าก่อนสร้างแทน.
