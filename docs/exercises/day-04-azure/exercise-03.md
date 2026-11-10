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

เมื่อเปลี่ยน code เราอยากให้ระบบทดสอบและส่งรุ่นเดียวกับ commit ที่ตรวจแล้วไป Azure ได้

## Practice 1 — เตรียม workflow ที่ใช้ OIDC

<PracticeIllustration asset="d04-e03-p01" eager />

**Primary target:** เชื่อม GitHub workflow กับ Azure โดยไม่เก็บ Azure client secret ใน code ได้

### Steps

1. อ่าน docs/deploy-api.yml.example จาก starter. Workflow เป็น **manual workflow_dispatch** เพื่อลดการ deploy โดยเผลอในห้องเรียน
2. ตรวจผล **Preview deployment access → Prepare deployment access** จาก Exercise 2: exact **GitHub OIDC subject**, repository/main, audience และ pipeline AZURE_CLIENT_ID ต้องตรงกับค่าที่ตรวจจริง. ถ้า `deployment.txt` ชุดล่าสุดมี `GITHUB_OIDC_SUBJECT` ให้เทียบกับผล Preview/Prepare ด้วย; ZIP ที่ส่งก่อนเตรียม access อาจยังไม่มีค่านี้. Repository ใหม่ใช้ subject ที่มี owner/repository IDs; ไม่แทนด้วยรูปแบบชื่ออย่างเดียว. ใช้ pipeline identity เดิม ไม่ใช้ pull identity เป็น AZURE_CLIENT_ID. ถ้าเปลี่ยน repository หรือ subject ให้ผู้สอน Preview/Prepare ใหม่ก่อน; ทางเลือก subscription ของตนให้ผู้ดูแลยืนยัน federation ตาม [Azure readiness](/resources/readiness)
3. ใน private GitHub repository เปิด **Settings → Secrets and variables → Actions** ใส่ Secrets:
   - AZURE_CLIENT_ID
   - AZURE_TENANT_ID
   - AZURE_SUBSCRIPTION_ID
4. ใส่ Variables: ACR_NAME, RESOURCE_GROUP, CONTAINER_APP_NAME ตาม resources ที่มีจริง. ไม่ใส่ DATABASE_URL/JWT_SECRET ที่นี่
5. ส่ง prompt:

   ~~~text
   คัดลอก docs/deploy-api.yml.example เป็น .github/workflows/deploy-api.yml
   ตรวจว่า test ใช้ doubles ไม่ต้องมี .env/Azure DB
   ตรวจ root build context, Dockerfile, requirements.lock.txt และ ARM/Linux compatibility
   ใช้ OIDC; build image tag = commit SHA; update app เดิมเท่านั้น
   workflow_dispatch เฉพาะ main ไม่มีการสร้าง resource group ใหม่หรือ seed DB
   แสดง diff ให้ฉันตรวจ; ไม่ push/merge/run workflow จนกว่าฉันสั่ง
   ~~~
6. อ่าน permissions และขั้น test → Azure login → build → update. ให้ Codex อธิบายสั้น ๆ ว่า pipeline identity ต่างจาก image-pull identity อย่างไร

**Checkpoint:** workflow อ้างชื่อ secrets/variables ถูกต้องและไม่มีค่า secret; OIDC และ role ที่จำเป็นพร้อม

## Practice 2 — ส่ง commit ที่ตรวจแล้วขึ้น Azure

<PracticeIllustration asset="d04-e03-p02" />

**Primary target:** ตามรอย release จาก GitHub commit ไปถึง revision ที่ให้บริการได้

### Steps

1. รัน API tests ในเครื่องอีกครั้งและตรวจ diff. Commit/push/PR/merge branch deployment ไป main. ไม่ใส่ build files, .env หรือ .local ใน commit
2. GitHub → **Actions → Deploy training API → Run workflow** เลือก branch main แล้วเริ่ม
3. เปิด run ดูทีละ step: Tests, Azure Login, Build, Update และ health request
4. ถ้า tests fail ให้แก้ code/test อย่างมีเหตุผลผ่าน branch/PR ใหม่. ห้ามลบ test เพื่อให้ deployment ผ่าน
5. เมื่อ run สำเร็จ ให้เปิด /health แล้วเทียบ **version** กับ full commit SHA ของ run. ACR tag และ revision image ต้องเป็น SHA เดียวกัน; workflow ต้องรอ version นี้ ไม่ถือว่า health ของ revision เก่าผ่านแทนได้
6. Login และ GET/POST หนึ่งรายการหลัง deployment. Health request ใน workflow ไม่แทนการทดสอบ DB/auth ของขั้นนี้. ให้ผู้สอนกด **Check Day 4 resources** อีกครั้งหลัง release เพื่อบันทึกสถานะและ API URL ล่าสุด

**Checkpoint:** commit SHA = ACR image tag = app version และ data operations ผ่านหลัง deployment

**ถ้าติดขัด:** Run workflow ไม่ขึ้นให้ตรวจว่า YAML อยู่ main. ถ้า Azure Login แจ้ง AADSTS700213 ให้เทียบ subject ที่ GitHub แสดงใน log กับ exact subject ใน Preview รวม immutable IDs, ref, issuer และ audience; ส่งเฉพาะข้อความที่ไม่มี token ให้ผู้สอนทบทวน access ก่อนรันใหม่. 403 ให้ตรวจ role scope. ไม่เปลี่ยน GitHub settings เพื่อลดรูปแบบ subject, ไม่ขยาย trust และไม่เปลี่ยนเป็น password credential หรือ token ของเพื่อน. ดู [GitHub OIDC reference](https://docs.github.com/en/actions/reference/security/oidc#immutable-subject-claims)
