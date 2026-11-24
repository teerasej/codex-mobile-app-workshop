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

   - ใช้ค่า `ACR_NAME` จาก `deployment.txt` ในช่อง Value ส่วน `ACR_LOGIN_SERVER` ใช้เมื่ออ้างถึง image เต็ม

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
   อยากกดปล่อย API รุ่นที่ตรวจแล้วจาก GitHub ได้ ช่วยใช้ docs/deploy-api.yml.example ทำไฟล์ .github/workflows/deploy-api.yml
   ขอให้เริ่มจากใช้ requirements.lock.txt ที่ตรวจบน Linux แล้วรัน test โดยจำลองการคุยกับฐานข้อมูล ไม่อ่าน .env หรือต่อ Azure DB
   จากนั้นให้ ACR Tasks build จาก root ด้วย api/Dockerfile สำหรับ linux/amd64 ติด tag เป็น full commit SHA
   ใช้ OIDC ของ pipeline identity เดิมและปรับเฉพาะ app เดิม โดยไม่สร้าง resource หรือ seed ฐานข้อมูล

   ช่วยเช็กว่า workflow_dispatch ต้องกดเองและทำงานเฉพาะ main โดยมีสิทธิ์ contents:read กับ id-token:write ตามตัวอย่าง
   ขอดู diff และคำอธิบายสั้น ๆ ตั้งแต่ test, Azure login, build, update จนถึงรอ /health ตอบ version ตรงกับ commit ใหม่
   รอบนี้แค่เตรียมไฟล์ให้ตรวจ ยังไม่ push, merge หรือรัน workflow
   ~~~

6. อ่านผลตรวจ: workflow ต้องรอ health ที่มี **version ตรง SHA ใหม่**; การเห็น HTTP 200 ของ revision เก่ายังไม่ถือว่ารุ่นใหม่พร้อม

**Checkpoint:** workflow ใช้ชื่อ Secrets/Variables ถูกต้อง, ไม่มีค่าลับใน code และผู้สอนยืนยัน OIDC พร้อมแล้ว

## Practice 2 — ส่ง commit ที่ตรวจแล้วขึ้น Azure

<PracticeIllustration asset="d04-e03-p02" />

**Primary target:** ตามรอย release จาก GitHub commit ไปถึง revision ที่ให้บริการได้

### Steps

1. ให้ Codex รัน tests และเตรียมรายการไฟล์สำหรับ commit ก่อน

   ~~~text
   ก่อนส่งงาน ช่วยลองรัน API tests ด้วย Python ของโปรเจกต์ โดยไม่ใช้ .env หรือต่อ Azure DB
   ถ้า test ไม่ผ่าน ขอให้บอกว่าติดอะไรและเก็บเงื่อนไขของ test ไว้ตามเดิม
   ขอดูผลกับ diff ของ chore/container-deployment พร้อมรายชื่อไฟล์ที่จะ commit
   กัน .env, .local, ไฟล์ build และ credentials ออกจากรายการ แล้วรอให้ฉันตรวจในเครื่องก่อน
   ~~~

2. เมื่อตรวจผ่าน ให้สั่ง Codex ส่งงานตาม workflow Git ที่ฝึก Day 1

   ~~~text
   ไฟล์ที่ฉันตรวจแล้วบน chore/container-deployment ส่งได้เลย
   ช่วย commit เฉพาะไฟล์ชุดนั้น แล้ว push branch ไปยัง private repository เดิมและเปิด PR เข้า main
   ส่งลิงก์ PR มาให้ฉันตรวจเอง หยุดก่อน merge หรือเริ่ม deploy
   ~~~

   เปิด PR ใน Edge ตรวจ `Files changed` และผล checks แล้วจึงกด `Merge pull request` → `Confirm merge` ตามสิทธิ์ของตน. ถ้าองค์กรบังคับ reviewer ให้รอ reviewer ก่อน

3. หลัง merge เปิด `Actions` → เลือก workflow ชื่อต่อไปนี้ → `Run workflow` → เลือก branch `main` → กด `Run workflow`. ขั้นนี้เริ่ม build/deploy จริงและใช้ทรัพยากรของ lab; ทำเมื่อเจ้าของอนุมัติแล้วเท่านั้น

   ~~~text
   Deploy training API
   ~~~

4. เปิด run ล่าสุด → job `deploy`. ดูผลตามลำดับ **Test API without Azure database access → azure/login@v2 → Build immutable image and update existing app**. ขั้นสุดท้ายมี health/version check รวมอยู่ด้วย. ถ้า tests fail ให้แก้ผ่าน branch/PR ใหม่ก่อนรันอีกครั้ง
5. เมื่อ run ผ่าน ให้ Codex ตรวจ release แบบอ่านอย่างเดียว

   ~~~text
   ช่วยดูว่าตอนนี้ Azure ให้บริการ API รุ่นที่ workflow เพิ่งปล่อยจริงไหม รอบนี้ขอตรวจอย่างเดียว
   เทียบ full commit SHA ของรอบนี้กับ tag ใน ACR, image ของ revision ที่ให้บริการ และ version ที่ /health ตอบกลับ
   ขอ SHA, image, revision และ HTTPS URL พร้อมบอกว่า revision พร้อมและรับ traffic อยู่ไหม
   ใช้ผลจากรุ่นที่เพิ่งปล่อย และใส่เฉพาะข้อมูลที่แชร์ได้
   ~~~

6. เปิด HTTPS API `/docs` ใน Edge, `Authorize` ใหม่ แล้วอ่าน UUID เดิมและสร้างข้อมูลสมมติหนึ่งรายการ. เก็บ UUID และส่งผลที่ไม่มี secret ให้ผู้สอนตรวจ. Health ใน workflow ไม่แทนการตรวจ DB/auth นี้

**Checkpoint:** commit SHA = ACR image tag = app version, revision ที่ให้บริการตรงรุ่น และ authenticated read/create ผ่านหลัง deployment

**ถ้าติดขัด:** ไม่เห็น `Run workflow` ให้ตรวจว่า YAML อยู่บน main. ถ้า Azure Login แจ้ง AADSTS700213 หรือมี 403 ให้ส่งข้อความ error ที่ไม่มี token ให้ผู้สอนตรวจ subject/role scope; ไม่เปลี่ยน GitHub OIDC settings หรือลดรูปแบบ immutable IDs เพื่อให้ผ่าน ไม่ใช้ password credential หรือ token ของเพื่อน. ดู [GitHub OIDC reference](https://docs.github.com/en/actions/reference/security/oidc#immutable-subject-claims)
