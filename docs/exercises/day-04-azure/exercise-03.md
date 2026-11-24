---
title: "Day 4 · Exercise 3 — ตรวจรุ่น API ที่เปิดบน Azure"
prev: {"text": "Exercise 2", "link": "/exercises/day-04-azure/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-04-azure/exercise-04"}
---

# Exercise 3 — ตรวจรุ่น API ที่เปิดบน Azure

> **Day 4 · Azure · 13:00–14:30**
>
> เตรียม HTTPS URL, ACR image/tag, revision และ UUID จาก [Exercise 2](/exercises/day-04-azure/exercise-02) ใน Practice 1 ให้ตรวจว่า API ที่เปิดอยู่บน Azure เป็นรุ่นที่คุณ deploy ไว้และยังอ่านรายการแจ้งปัญหาเดิมได้ เมื่อผ่านแล้วให้นำ URL เดิมไปใช้ใน Exercise 4

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

เมื่อแก้ API เสร็จ คุณสามารถกดให้ GitHub ทดสอบแล้วส่งรุ่นที่ผ่านการทดสอบขึ้น Azure ได้ ส่วนนี้เป็นแบบฝึกเสริม หากยังไม่ได้เตรียมสิทธิ์ ให้ไป [Exercise 4](/exercises/day-04-azure/exercise-04) หลังผ่าน Practice 1

**OIDC (OpenID Connect)** คือวิธีที่ GitHub Actions ใช้ยืนยันตัวตนกับ Azure คล้ายการแสดงบัตรผ่านชั่วคราว Azure ตรวจว่างานมาจากโปรเจกต์และ branch ที่ได้รับอนุญาต แล้วให้สิทธิ์เข้าถึงช่วงสั้น ๆ โดยไม่ต้องเก็บ Azure client secret ไว้ใน GitHub [GitHub Docs](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure)

### Steps

1. ใช้ private GitHub repository ที่เตรียมไว้สำหรับ lab กับ branch `main` เมื่อผู้สอนยืนยันว่าพร้อม หากจะใช้ repository หรือ branch อื่น ให้ผู้สอนตรวจสิทธิ์ใหม่ก่อนรัน [Azure readiness](/resources/readiness#optional-github-actions-readiness)

2. ใน Edge เปิด repository ของ lab แล้วไปที่ `Settings` → `Secrets and variables` → `Actions` → แท็บ `Secrets`
3. กด `New repository secret` ทีละรายการ ใส่ชื่อจากบล็อกด้านล่างในช่อง **Name** และค่าที่ตรงกันจาก `deployment.txt` ในช่อง **Secret** แล้วกด `Add secret`

   - Pipeline client ID

     ~~~text
     AZURE_CLIENT_ID
     ~~~

   - Tenant ID

     ~~~text
     AZURE_TENANT_ID
     ~~~

   - Subscription ID

     ~~~text
     AZURE_SUBSCRIPTION_ID
     ~~~

4. เลือกแท็บ `Variables` → `New repository variable`. เพิ่ม **Name** ต่อไปนี้ โดยใส่ **Value** ตรง resource จาก Exercise 2 แล้วกด `Add variable` ทีละรายการ

   - **ชื่อ ACR** — ใช้ค่า `ACR_NAME` จาก `deployment.txt` ถ้าไฟล์เดิมไม่มีช่องนี้ ให้เปิด resource group ของ lab ใน Azure Portal แล้วเลือก Container Registry ที่ใช้ build ใน Exercise 2 ใช้ชื่อ resource ที่หัวหน้า `Overview` ส่วน `Login server` ที่ลงท้ายด้วย `.azurecr.io` ใช้เมื่ออ้างถึง image เต็ม

     ~~~text
     ACR_NAME
     ~~~

     ตัวอย่างข้อมูลใน `deployment.txt`

     ~~~text
     ACR_NAME=sdldemoacr01
     ACR_LOGIN_SERVER=sdldemoacr01.azurecr.io
     ~~~

     **คัดลอกเฉพาะค่าหลัง `ACR_NAME=`** ในตัวอย่างคือ **`sdldemoacr01`** ให้ใช้ชื่อ ACR ของ lab คุณในช่อง **Value**

   - ชื่อ resource group ของ lab จาก `RESOURCE_GROUP` ใน `deployment.txt`

     ~~~text
     RESOURCE_GROUP
     ~~~

   - **ชื่อ Container App** — ใน Azure Portal เปิด resource group เดิม แล้วเลือก Container App ที่เปิด Service Desk API ใน Exercise 2 คัดลอกชื่อ resource ที่หัวหน้า `Overview` ส่วน `Application URL` ใช้สำหรับเปิด API

     ~~~text
     CONTAINER_APP_NAME
     ~~~

     ตัวอย่าง `Application URL`

     ~~~text
     https://sdl-api-demo.sampleenv-a1b2c3d4.southeastasia.azurecontainerapps.io
     ~~~

     **คัดลอกเฉพาะชื่อ resource ที่หัวหน้า `Overview`** ในตัวอย่างคือ **`sdl-api-demo`** ซึ่งอยู่หลัง `https://` และก่อนจุดแรกใน URL ให้ใช้ชื่อ Container App ของ lab คุณในช่อง **Value**

   ตรวจว่ามี Secrets 3 ชื่อและ Variables 3 ชื่อ เก็บ `DATABASE_URL` และ `JWT_SECRET` ไว้ใน Container App ตาม Exercise 2

5. ตรวจว่า repo มี `api/requirements.lock.txt`, workflow บน `main` และ API รองรับการรายงาน `APP_VERSION` ที่ `/health` ถ้ายังไม่มี workflow ให้ขอแผนจาก Codex ตาม prompt นี้ แล้วใช้ขั้นตอน branch/PR ของ Day 1 หลังตรวจ diff และผล tests

   ~~~text
   สำหรับแบบฝึกเสริม ช่วยเตรียม .github/workflows/deploy-api.yml จาก docs/deploy-api.yml.example
   ให้ workflow_dispatch ทำงานเฉพาะ main ใช้ pipeline identity ที่ผู้สอนเตรียมแล้ว
   รัน API tests ด้วย lockfile และ test doubles โดยไม่อ่าน .env หรือต่อฐานข้อมูล lab
   ให้ ACR Tasks build linux/amd64 ใส่ full commit SHA เป็น tag แล้วอัปเดต Container App เดิม
   ขอให้รอ /health ตอบ version ตรง SHA และขอดู diff ก่อน commit, push, merge หรือรัน
   ~~~

6. เมื่อ workflow อยู่บน `main` และผู้สอนยืนยันให้ทำ ให้เปิด `Actions` → เลือก workflow ด้านล่าง → `Run workflow` → เลือก `main` → `Run workflow` ขั้นนี้ใช้ ACR Tasks และเปลี่ยน revision ของแอป lab

   ~~~text
   Deploy training API
   ~~~

7. ตรวจผล test, Azure Login, build, app update และ health จาก run นั้น เทียบ commit SHA กับ ACR tag และ `version` ที่ `/health` ตอบ จากนั้นทำการตรวจ revision และ authenticated read ใน Practice 1 ซ้ำกับรุ่นใหม่ หาก Azure Login หรือสิทธิ์ไม่ผ่าน ให้ส่งข้อความผิดพลาดที่ตัด token ออกให้ผู้สอนตรวจ

**Checkpoint:** workflow run ผ่าน และ commit SHA ตรงกับ ACR image tag และ health version ของ revision ที่รับ traffic
