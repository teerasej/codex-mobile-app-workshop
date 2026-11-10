---
title: "ไฟล์ฝึกและดาวน์โหลด"
prev: false
next: false
---

# ไฟล์สำหรับ Service Desk Lite

[กลับสารบัญ](/)

ดาวน์โหลด service-desk-starter.zip แล้วแตกไฟล์ก่อนเริ่ม Day 1. มีโฟลเดอร์ service-desk-lite ชั้นเดียว ไม่มี Git history, application source, passwords หรือข้อมูลบริษัทจริง

| ไฟล์ต้นทาง | ตำแหน่งในโปรเจคหลังแตก ZIP | ใช้เมื่อ |
| --- | --- | --- |
| [project-brief.md](/resources/project-brief) | docs/project-brief.md และ README.md | ทุกวัน |
| [api-contract.md](/resources/api-contract) | docs/api-contract.md | ทุกวัน |
| service-requests.json | data/service-requests.json | Day 2–3 |
| schema.sql | api/schema.sql | Day 2 seed |
| requirements.txt | api/requirements.txt | Day 2 install |
| api.env.example | api/.env.example | Day 2 configuration |
| [agents-template.md](/resources/agents-template) | docs/agents-template.md | Day 1 คัดลอกเป็น AGENTS.md |
| [review-log.md](/resources/review-log) | docs/review-log.md | ทุก Practice |
| gitignore.template | .gitignore | Day 1 |
| dockerignore.template | .dockerignore | Day 4 |
| Dockerfile | api/Dockerfile | Day 4 |
| deploy-api.yml.example | docs/deploy-api.yml.example | Day 4 คัดลอกเป็น workflow |
| check_api.py | scripts/check_api.py | Day 2 และ Day 4 |
| [change-request.md](/resources/change-request) | docs/change-request.md | หลัง core checkpoints |

## สิ่งที่ Codex กับผู้เรียนสร้างระหว่างฝึก

Day 1 สร้าง Git history และ AGENTS.md. Day 2 สร้าง api/app, tests และ requirements.lock.txt. Day 3 สร้าง client. Day 4 จึงคัดลอก workflow เข้า .github/workflows และ deploy ตามสิทธิ์ของตน. ไม่ใช่ไฟล์ที่หายจาก ZIP

requirements.txt เป็นรายการ dependencies เริ่มต้น ไม่ใช่ชุด versions ที่ซ้อมครบแล้ว. ผู้จัดต้องซ้อมบน Python 3.12/Windows และ Linux build แล้วบันทึก lockfile ที่ใช้จริงก่อนนำหลักสูตรไปสอนซ้ำ

## ข้อมูลสมมติ

มี Request 4 รายการ: learner01 จำนวน 3 รายการ และ learner02 จำนวน 1 รายการ. Password ไม่รวมใน public starter. ถ้าใช้ database ที่ผู้สอนเตรียม ข้อมูลชุดนี้มีอยู่แล้วพร้อม app passwords ใน **Student ZIP ส่วนตัว**; คง passwords/hash เดิมเมื่อ seed ซ้ำ. ถ้าใช้ database ใหม่ของตน seed จะรับ password ผ่าน getpass เฉพาะ user ที่ยังไม่มีและเก็บเฉพาะ hash. ใช้ database แยกกันเพื่อไม่ให้ข้อมูลคนอื่นรบกวนผลตรวจ

Student ZIP เป็นคนละไฟล์กับ public starter: คัดลอกเฉพาะ `api/.env` ของตนเมื่อยังไม่มีไฟล์ และใช้ค่าที่ไม่เป็นความลับใน `deployment.txt` สำหรับ Day 4. อย่าแตกทับทั้งโปรเจคหรือแทน `.gitignore` ของ starter ด้วยไฟล์จาก Student ZIP; อย่าวาง private ZIP/README, `.env`, XLSX หรือ passwords ใน Git/chat

ก่อน Day 4 ให้ผู้สอนตรวจ **GitHub OIDC subject ของ repository/main จริง** รวม immutable owner/repository IDs แล้ว Preview/Prepare deployment access. Template ไม่คำนวณ subject จากชื่อ และไม่เปลี่ยน GitHub settings เพื่อให้ trust แบบเก่าผ่าน. อ่าน [Azure readiness](/resources/readiness) ก่อนคัดลอก workflow

## API check script

รันด้วย Python standard library ไม่ต้องลง package เพิ่ม. Script เรียก API จริง ตรวจ auth/validation/ownership และสร้าง Request สมมติ 1 รายการต่อรอบเพื่อใช้ตรวจ persistence ต่อ. ไม่ลบข้อมูลหลังตรวจและไม่ทดแทน unit tests, expired-token test หรือ mobile/cloud rehearsal. ใส่ password เฉพาะ interactive terminal ของตนเอง

ตัวอย่างจาก root โปรเจคผู้เรียน:

~~~shell
python scripts/check_api.py --base-url http://127.0.0.1:8000
~~~

เปลี่ยนเป็น HTTPS origin ของ Azure เมื่อทำ Day 4. ไม่ส่ง token/password ใน arguments. Run ที่ fail ให้ดู route/status ในเครื่อง ไม่แนบค่าลับกลับ chat


## ดาวน์โหลดไฟล์ต้นฉบับ

<DownloadList />
