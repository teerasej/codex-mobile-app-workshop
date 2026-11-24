---
title: "Day 4 · Exercise 3 — ตรวจรุ่น API ที่เปิดบน Azure"
prev: {"text": "Exercise 2", "link": "/exercises/day-04-azure/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-04-azure/exercise-04"}
---

# Exercise 3 — ตรวจรุ่น API ที่เปิดบน Azure

> **Day 4 · Azure · 13:00–14:30**
>
> เตรียม HTTPS URL, ACR image/tag, revision และ UUID จาก [Exercise 2](/exercises/day-04-azure/exercise-02) บทหลักใช้ Azure โดยตรง ให้เก็บหลักฐานจากรุ่นที่เปิดอยู่ แล้วนำ URL เดิมไปใช้ใน Exercise 4

## Practice 1 — ตรวจ release บน Azure

<PracticeIllustration asset="d04-e03-p02" eager />

**Primary target:** ชี้ได้ว่า Application URL กำลังให้บริการจาก ACR image และ revision ใด พร้อมหลักฐานว่า API อ่านข้อมูลเดิมได้

### Steps

1. เปิด Container App ของ lab เดิมใน Azure portal → ดู `Overview` สำหรับ Application URL และ `Revisions and replicas` เพื่อตรวจ revision ที่พร้อมและรับ traffic จริง เทียบ image/tag เต็มกับ ACR ใน Exercise 2 หากอยากให้ Codex ช่วยตรวจ ให้ส่ง prompt นี้

   ~~~text
   ช่วยตรวจ release ของ Container App เดิมจาก Exercise 2 แบบอ่านอย่างเดียว
   เทียบชื่อ image และ tag ของ revision ที่พร้อมและรับ traffic กับ ACR ของ lab
   ขอ ACR digest ที่ตรวจได้ ชื่อ revision และ HTTPS Application URL
   ไม่เปลี่ยน configuration ไม่ restart และไม่เปิดค่า secrets
   ~~~

2. เปิด Application URL แล้วเติม path นี้ ผลที่คาดคือ HTTP 200, `status` เป็น `ok` และ `version` เป็นค่าที่ตั้งใน Exercise 2 ซึ่งปกติคือ `v1` ถ้าเห็นหน้า Quickstart หรือรุ่นไม่ตรง ให้ย้อนตรวจ traffic, image tag และ target port

   ~~~text
   /health
   ~~~

3. เปิด API docs จาก URL เดิมแล้วลงชื่อเข้าใช้ด้วย app user ของตนเอง เรียก `GET /requests/{id}` ด้วย UUID ที่สร้างใน Exercise 2 ตรวจว่าได้ HTTP 200 และเป็นรายการเดิม การตรวจนี้ใช้ฐานข้อมูลเดิมและอ่านข้อมูลโดยไม่สร้างรายการซ้ำ

   ~~~text
   /docs
   ~~~

4. จด **HTTPS URL, ACR image/tag, digest เท่าที่ตรวจได้, ชื่อ revision, ผล health และผลอ่าน UUID** ลงใน review log ถ้าทราบ commit ที่ใช้ build จริงให้บันทึกเพิ่ม หากยังยืนยัน commit ไม่ได้ให้บันทึกหลักฐาน image/tag ตามที่พบ

**Checkpoint:** ระบุ revision ที่รับ traffic ได้ และใช้ HTTPS URL เดิมตรวจทั้ง health และ authenticated read ผ่าน ใช้ URL นี้ต่อใน [Exercise 4](/exercises/day-04-azure/exercise-04)

## Practice 2 — ปล่อยรุ่นผ่าน GitHub (Optional · GitHub Actions)

<PracticeIllustration asset="d04-e03-p01" />

**Primary target:** สำหรับชุด lab ที่ผู้สอนเตรียม OIDC พร้อมแล้ว สั่งปล่อย API จาก `main` และตามรอย full commit SHA ถึง revision ที่ Azure ให้บริการ

### Steps

1. ทำส่วนนี้เมื่อผู้สอนแจ้งว่า private repo และ pipeline identity พร้อมแล้ว ผู้สอนเป็นผู้ตรวจ exact OIDC subject ของ `main` และจัดการ **Preview deployment access** → **Prepare deployment access** ตาม [Azure readiness](/resources/readiness#optional-github-actions-readiness) หากยังไม่พร้อม ให้จบที่ Practice 1 และไป Exercise 4 ได้เลย
2. ตรวจว่า repo มี `api/requirements.lock.txt`, workflow บน `main` และ API รองรับการรายงาน `APP_VERSION` ที่ `/health` ถ้ายังไม่มี workflow ให้ขอแผนจาก Codex ตาม prompt นี้ แล้วใช้ขั้นตอน branch/PR ของ Day 1 หลังตรวจ diff และผล tests

   ~~~text
   สำหรับแบบฝึกเสริม ช่วยเตรียม .github/workflows/deploy-api.yml จาก docs/deploy-api.yml.example
   ให้ workflow_dispatch ทำงานเฉพาะ main ใช้ pipeline identity ที่ผู้สอนเตรียมแล้ว
   รัน API tests ด้วย lockfile และ test doubles โดยไม่อ่าน .env หรือต่อฐานข้อมูล lab
   ให้ ACR Tasks build linux/amd64 ใส่ full commit SHA เป็น tag แล้วอัปเดต Container App เดิม
   ขอให้รอ /health ตอบ version ตรง SHA และขอดู diff ก่อน commit, push, merge หรือรัน
   ~~~

3. เมื่อ workflow อยู่บน `main` และผู้สอนยืนยันให้ทำ ให้เปิด `Actions` → เลือก workflow ด้านล่าง → `Run workflow` → เลือก `main` → `Run workflow` ขั้นนี้ใช้ ACR Tasks และเปลี่ยน revision ของแอป lab

   ~~~text
   Deploy training API
   ~~~

4. ตรวจผล test, Azure Login, build, app update และ health จาก run นั้น เทียบ commit SHA กับ ACR tag และ `version` ที่ `/health` ตอบ จากนั้นทำการตรวจ revision และ authenticated read ใน Practice 1 ซ้ำกับรุ่นใหม่ หาก Azure Login หรือสิทธิ์ไม่ผ่าน ให้ส่งข้อความผิดพลาดที่ตัด token ออกให้ผู้สอนตรวจ

**Checkpoint:** workflow run ผ่าน และ commit SHA ตรงกับ ACR image tag และ health version ของ revision ที่รับ traffic
