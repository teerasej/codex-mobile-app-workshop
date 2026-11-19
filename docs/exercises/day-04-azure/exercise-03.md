---
title: "Day 4 · Exercise 3 — Deploy จาก GitHub"
prev: {"text": "Exercise 2", "link": "/exercises/day-04-azure/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-04-azure/exercise-04"}
---

# Exercise 3 — Deploy จาก GitHub

> **Day 4 · Azure · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-04-azure/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

## Scenario

เมื่อเปลี่ยน code เราจะให้ GitHub ทดสอบแล้วส่งรุ่นเดียวกับ commit ที่ตรวจแล้วไป Azure. หมายเลข commit เหมือนเลขพัสดุที่ตามได้ตั้งแต่ต้นทาง จนถึง image และ revision ที่เปิดให้ใช้

## Practice 1 — เตรียม workflow ที่ใช้ OIDC

<PracticeIllustration asset="d04-e03-p01" eager />

**Primary target:** เชื่อม GitHub workflow กับ Azure โดยไม่เก็บ Azure client secret ใน code ได้

### Steps

1. เปิด `docs/deploy-api.yml.example` ในโปรเจค. Workflow ใช้ `workflow_dispatch` คือผู้เรียนกดเริ่มเอง ไม่ deploy อัตโนมัติทุกครั้งที่ push
2. ขอคำยืนยันจากผู้สอนว่า OIDC ของ repository/main พร้อมแล้ว และ pipeline client ID ตรงกับที่ได้รับ. ใช้ **pipeline identity** สำหรับ GitHub deploy ส่วน **pull identity** ให้ Container App ดึง image. ถ้าเปลี่ยน repository/main หรือ subject ต้องให้ผู้สอนตรวจใหม่ รวม immutable owner/repository IDs ตาม [Azure readiness](/resources/readiness)
3. ใน Edge เปิด private GitHub repository → `Settings` → `Secrets and variables` → `Actions` → แท็บ `Secrets`. กด `New repository secret` ทีละรายการ กรอก **Name** จากแต่ละ block และ **Secret** จาก deployment ที่ได้รับ แล้วกด `Add secret`

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

   - ชื่อ ACR ไม่ใช่ login server ที่ลงท้าย azurecr.io

     ~~~text
     ACR_NAME
     ~~~

   - ชื่อ resource group ของ lab

     ~~~text
     RESOURCE_GROUP
     ~~~

   - ชื่อ Container App เดิม

     ~~~text
     CONTAINER_APP_NAME
     ~~~

   ตรวจว่ามี Secrets 3 ชื่อและ Variables 3 ชื่อ. ไม่ใส่ DATABASE_URL/JWT_SECRET ใน GitHub; ค่าทั้งสองอยู่ใน Container App แล้ว

5. ให้ Codex เตรียม workflow แล้วแสดง diff

   ~~~text
   คัดลอก docs/deploy-api.yml.example เป็น .github/workflows/deploy-api.yml
   ตรวจว่า test ใช้ doubles ไม่อ่าน .env และไม่ต่อ Azure DB
   ใช้ root build context, api/Dockerfile และ requirements.lock.txt ชุดที่ตรวจบน Linux แล้ว
   build ด้วย ACR Tasks เป็น linux/amd64 และใช้ full commit SHA เป็น image tag
   ใช้ OIDC ของ pipeline identity และ update app เดิมเท่านั้น
   workflow_dispatch รันเฉพาะ main ไม่สร้าง resources ใหม่หรือ seed DB
   ตรวจ permissions contents:read และ id-token:write
   แสดง diff และอธิบาย test → Azure login → build → update → ตรวจ health version
   ยังไม่ push, merge หรือ run workflow
   ~~~

6. อ่านผลตรวจ: workflow ต้องรอ health ที่มี **version ตรง SHA ใหม่**; การเห็น HTTP 200 ของ revision เก่ายังไม่ถือว่ารุ่นใหม่พร้อม

**Checkpoint:** workflow ใช้ชื่อ Secrets/Variables ถูกต้อง, ไม่มีค่าลับใน code และผู้สอนยืนยัน OIDC พร้อมแล้ว

## Practice 2 — ส่ง commit ที่ตรวจแล้วขึ้น Azure

<PracticeIllustration asset="d04-e03-p02" />

**Primary target:** ตามรอย release จาก GitHub commit ไปถึง revision ที่ให้บริการได้

### Steps

1. ให้ Codex รัน tests และเตรียมรายการไฟล์สำหรับ commit ก่อน

   ~~~text
   รัน API tests ในเครื่องด้วย Python ของโปรเจค โดยไม่ใช้ .env หรือ Azure DB
   ตรวจ diff และรายการไฟล์ที่จะ commit ของ branch chore/container-deployment
   ไม่รวม .env, .local, build output หรือ credentials
   ถ้า tests ล้มให้รายงานสาเหตุ ไม่ลบหรือผ่อน test เพื่อให้ผ่าน
   แสดงผล tests และสรุป diff ให้ฉันตรวจก่อน ยังไม่ส่งขึ้น GitHub
   ~~~

2. เมื่อตรวจผ่าน ให้สั่ง Codex ส่งงานตาม workflow Git ที่ฝึก Day 1

   ~~~text
   commit เฉพาะไฟล์ที่ฉันตรวจแล้วบน branch chore/container-deployment
   push branch นี้ไป private repository เดิม และเปิด PR เข้า main
   ส่ง PR URL ให้ฉันตรวจ ยังไม่ merge และไม่ run deployment
   ~~~

   เปิด PR ใน Edge ตรวจ `Files changed` และผล checks แล้วจึงกด `Merge pull request` → `Confirm merge` ตามสิทธิ์ของตน. ถ้าองค์กรบังคับ reviewer ให้รอ reviewer ก่อน

3. หลัง merge เปิด `Actions` → เลือก workflow ชื่อต่อไปนี้ → `Run workflow` → เลือก branch `main` → กด `Run workflow`. ขั้นนี้เริ่ม build/deploy จริงและใช้ทรัพยากรของ lab; ทำเมื่อเจ้าของอนุมัติแล้วเท่านั้น

   ~~~text
   Deploy training API
   ~~~

4. เปิด run ล่าสุด → job `deploy`. ดูผลตามลำดับ **Test API without Azure database access → azure/login@v2 → Build immutable image and update existing app**. ขั้นสุดท้ายมี health/version check รวมอยู่ด้วย. ถ้า tests fail ให้แก้ผ่าน branch/PR ใหม่ก่อนรันอีกครั้ง
5. เมื่อ run ผ่าน ให้ Codex ตรวจ release แบบอ่านอย่างเดียว

   ~~~text
   ตรวจ release ของ workflow run นี้โดยไม่เปลี่ยน Azure
   เทียบ full commit SHA ของ run กับ ACR image tag, image ของ revision ที่ให้บริการ และ /health.version
   ระบุว่า revision พร้อมและได้รับ traffic หรือไม่ ไม่ถือว่า health ของรุ่นเก่าผ่านแทน
   รายงานเฉพาะ SHA, image, revision และ HTTPS URL ไม่เปิด secrets
   ~~~

6. เปิด HTTPS API `/docs` ใน Edge, `Authorize` ใหม่ แล้วอ่าน UUID เดิมและสร้างข้อมูลสมมติหนึ่งรายการ. เก็บ UUID และส่งผลที่ไม่มี secret ให้ผู้สอนตรวจ. Health ใน workflow ไม่แทนการตรวจ DB/auth นี้

**Checkpoint:** commit SHA = ACR image tag = app version, revision ที่ให้บริการตรงรุ่น และ authenticated read/create ผ่านหลัง deployment

**ถ้าติดขัด:** ไม่เห็น `Run workflow` ให้ตรวจว่า YAML อยู่บน main. ถ้า Azure Login แจ้ง AADSTS700213 หรือมี 403 ให้ส่งข้อความ error ที่ไม่มี token ให้ผู้สอนตรวจ subject/role scope; ไม่เปลี่ยน GitHub OIDC settings หรือลดรูปแบบ immutable IDs เพื่อให้ผ่าน ไม่ใช้ password credential หรือ token ของเพื่อน. ดู [GitHub OIDC reference](https://docs.github.com/en/actions/reference/security/oidc#immutable-subject-claims)
