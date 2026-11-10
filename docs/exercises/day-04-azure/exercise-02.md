---
title: "Day 4 · Exercise 2 — เปิด API บน Azure"
prev: {"text": "Exercise 1", "link": "/exercises/day-04-azure/exercise-01"}
next: {"text": "Exercise 3", "link": "/exercises/day-04-azure/exercise-03"}
---

# Exercise 2 — เปิด API บน Azure


> **Day 4 · Azure · 10:45–12:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-04-azure/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

เราจะย้าย API ไปยังพื้นที่ lab ที่ได้รับมอบหมาย โดยใช้ database เดิมและ managed identities ของตน. เตรียมสิทธิ์ดึง image ก่อนเปิด API เหมือนให้กุญแจคลังสินค้าก่อนส่งรถไปรับของ

## Practice 1 — เตรียม registry และ image

<PracticeIllustration asset="d04-e02-p01" eager />

**Primary target:** Build และระบุ image ที่เก็บอยู่ใน ACR ของตนได้

### Steps

1. ผู้เรียนรัน **az login** เอง เลือก tenant/subscription ที่ได้รับ และตรวจ subscription ID กับ `deployment.txt` ของ Student ZIP. ให้ Codex อ่านเฉพาะค่า deployment ที่ไม่เป็นความลับ; ไม่อ่าน README ส่วนตัวหรือ `.env`
2. ใช้ **RESOURCE_GROUP**, **PULL_IDENTITY_RESOURCE_ID** และ pipeline **AZURE_CLIENT_ID** ที่ได้รับ. ให้ Codex ตรวจ resource group/identity IDs ว่าอยู่ใน scope ของตนและใช้ identity เดิม. ตั้งชื่อ environment, app และ ACR ที่ไม่ซ้ำ; ACR ใช้ตัวอักษร/ตัวเลข ไม่ใส่ hyphen

   > **ใช้ subscription ของตนเอง:** ถ้าไม่มีพื้นที่ที่ผู้สอนเตรียม ให้เจ้าของอนุมัติ resource group ใหม่และให้ผู้ดูแลเตรียม pull/pipeline identities กับสิทธิ์ก่อนเริ่ม. เฉพาะทางเลือกนี้จึงสร้าง group/identities ใหม่; ไม่ใช้คำสั่งนี้แทนกลุ่มที่ได้รับมอบหมาย

3. ส่ง prompt:

   ~~~text
   เตรียมแผน Azure lab จาก subscription/region/resource IDs ที่ฉันยืนยัน
   ใช้ resource group และ pull/pipeline identities ที่ได้รับแล้ว ไม่สร้างชุดใหม่
   แสดงคำสั่งสร้าง ACR Basic (admin disabled) และ Container Apps environment แบบ Consumption-only ไม่สร้าง Log Analytics
   สร้างเฉพาะใน lab resource group ของฉัน ไม่แก้ shared PostgreSQL/control resources
   ถ้ามี resource เดิมให้ตรวจเจ้าของก่อนใช้ต่อ ไม่ยึด resource จากชื่ออย่างเดียว
   ถ้าใช้ private PostgreSQL ให้ใช้ environment ที่ IT เตรียมไว้
   ยังไม่รันจนฉันตรวจเป้าหมายและยืนยันค่าใช้จ่าย
   ~~~
4. ตัวอย่างคำสั่งสำหรับพื้นที่ที่ผู้สอนเตรียมและ public lab environment:

   ~~~shell
   az extension add --name containerapp --upgrade
   az group show --name <LAB_RG> --query id --output tsv
   az identity show --ids <PULL_IDENTITY_RESOURCE_ID> --query principalId --output tsv
   az acr create --resource-group <LAB_RG> --name <ACR_NAME> --sku Basic --admin-enabled false
   az containerapp env create --name <ENV_NAME> --resource-group <LAB_RG> --location <REGION> --enable-workload-profiles false --logs-destination none
   ~~~

   ตรวจว่า environment เป็น Consumption-only และ logs destination เป็น none; ไม่สร้าง dedicated profile, Log Analytics หรือ private endpoint ในแผนนี้. หากสิทธิ์หรือ provider ไม่พร้อมให้ผู้สอนช่วย ไม่เปลี่ยน subscription หรือสร้าง group ใหม่เพื่อข้ามปัญหา
5. หลังอนุมัติให้ทำทีละคำสั่ง แล้ว build จาก root:

   ~~~shell
   az acr build --registry <ACR_NAME> --image service-desk-api:day4-v1 --file api/Dockerfile .
   ~~~
6. เปิด ACR ใน Azure portal ดู repository service-desk-api และ tag day4-v1. จด loginServer/tag ใน review log โดยไม่บันทึกรหัสผ่าน

**Checkpoint:** ACR build สำเร็จและเห็น image tag จริง. หาก account ไม่มี ACR Tasks สิทธิ์ ให้ผู้ดูแลแก้ตาม readiness ไม่เปลี่ยนไปใช้ admin password ใน chat

## Practice 2 — สร้าง Container App และสิทธิ์ดึง image

<PracticeIllustration asset="d04-e02-p02" />

**Primary target:** ให้ Container App เข้าถึง private image ด้วย managed identity ได้

### Steps

1. ให้ Codex ตรวจ resource ID/principalId ของ **pull identity ที่ได้รับ** และ resource ID ของ ACR; ใช้ private GitHub repository จาก Day 1 และ main branch เดิม
2. แจ้งผู้สอนเฉพาะรหัสผู้เรียนและ GitHub owner/repository. ให้ผู้สอนตรวจ **full GitHub OIDC subject ของ main** จาก OIDC settings/API ของ repository จริง รวม owner/repository IDs; อย่าเดารูปแบบจากชื่อ. Repository ใหม่ใช้ immutable IDs ตาม [Azure readiness](/resources/readiness)
3. หลัง ACR พร้อม ให้ผู้สอนยืนยัน exact **GitHub OIDC subject** สำหรับ repository/main และเตรียม OIDC ของ pipeline identity กับ **AcrPull** ของ pull identity เดิม. รอผู้สอนยืนยันว่า access พร้อมก่อน deploy private image. ขั้นนี้ยังไม่ต้องมี app หรือ `/health`

   > ถ้าใช้ subscription ของตนเอง ให้ผู้ดูแลเตรียม GitHub OIDC ของ pipeline identity และกำหนด **AcrPull** ให้ pull identity ที่ ACR ของ lab โดยตรง. Contributor ของผู้เรียนไม่ได้รวมสิทธิ์สร้าง role assignments. Registry ที่ใช้ ABAC ต้องให้ผู้ดูแลใช้ role ตาม policy ไม่เปลี่ยน registry mode เพื่อข้ามปัญหา
4. สร้าง app ด้วย public quickstart image ชั่วคราว เพื่อให้เข้า portal ตั้ง secrets ได้ก่อน API runtime. ใช้ชื่อเดิมต่อไป ไม่สร้าง app ที่สอง:

   ~~~shell
   az containerapp create --name <APP_NAME> --resource-group <LAB_RG> --environment <ENV_NAME> --image mcr.microsoft.com/k8se/quickstart:latest --target-port 80 --ingress external --min-replicas 0 --max-replicas 1 --cpu 0.25 --memory 0.5Gi --user-assigned <PULL_IDENTITY_RESOURCE_ID>
   az containerapp registry set --name <APP_NAME> --resource-group <LAB_RG> --server <ACR_LOGIN_SERVER> --identity <PULL_IDENTITY_RESOURCE_ID>
   ~~~
5. เปิด Azure portal ตรวจ app → Identity และ registry configuration ให้ตรง identity/ACR ที่เลือก. รอ role assignment มีผลถ้าระบบยังปฏิเสธ
6. จด Application URL ของ app. ตอนนี้เป็นหน้า quickstart ไม่ใช่ Service Desk API; ยังไม่ถือว่า deploy API สำเร็จ

**Checkpoint:** app shell และ registry identity ตั้งค่าแล้ว ไม่มี ACR admin password. จะพิสูจน์ image pull จริงเมื่อเปลี่ยน image ใน Practice ถัดไป

## Practice 3 — ตั้ง secrets และเปิด API จริง

<PracticeIllustration asset="d04-e02-p03" />

**Primary target:** รัน API บน HTTPS พร้อมเชื่อม PostgreSQL ด้วย runtime configuration ได้

### Steps

1. ใน Azure portal เปิด Container App → **Secrets** เพิ่มชื่อ database-url และ jwt-secret. ผู้เรียนกรอกค่าจริงเอง ไม่แชร์หน้าจอตอนค่าปรากฏ
2. DATABASE_URL ใช้ **runtime login** ของ database ฝึกเดียวกับ Day 2 พร้อม TLS. ใช้ JWT_SECRET จาก `.env` ส่วนตัวชุดเดิม; ไม่คัดลอก setup credentials หรือสร้าง key ใหม่เพื่อให้ deployment ผ่าน. หากเจ้าของตั้งใจเปลี่ยน key ต้อง login ใหม่และปรับข้อมูลส่งมอบให้ตรงกัน
3. ให้ Codex เตรียมคำสั่งที่อ้าง **ชื่อ secret** เท่านั้น:

   ~~~shell
   az containerapp update --name <APP_NAME> --resource-group <LAB_RG> --image <ACR_LOGIN_SERVER>/service-desk-api:day4-v1 --cpu 0.25 --memory 0.5Gi --min-replicas 0 --max-replicas 1 --set-env-vars DATABASE_URL=secretref:database-url JWT_SECRET=secretref:jwt-secret CORS_ORIGINS=http://localhost:3000 APP_VERSION=v1
   az containerapp ingress enable --name <APP_NAME> --resource-group <LAB_RG> --type external --target-port 8000 --transport auto
   ~~~
4. ตรวจ Ingress ใช้ port **8000** และ **Allow insecure connections ปิด**. รอ revision พร้อม; ระหว่างเปลี่ยนจาก port 80 อาจยังเข้าไม่ได้ ให้ตรวจเมื่อ update ทั้งสองส่วนเสร็จ
5. เปิด `https://<APP_FQDN>/health` แล้ว /docs. Login และ GET UUID เดิม; สร้างคำขอใหม่ชื่อ **ทดสอบจาก Azure** ผ่าน /docs
6. ถ้า /health ผ่านแต่ DB ล้ม ให้ตรวจ runtime login, database, TLS และ network จาก environment. ให้ผู้สอนตรวจ network access ของ shared server ผ่านช่องทางส่วนตัว. คง TLS และตรวจเฉพาะชื่อ/reference ของตัวแปร environment
7. เมื่อ API ใช้งานจริงแล้ว ให้ผู้สอนกด **Check Day 4 resources** สำหรับผู้เรียนเดิม เพื่อยืนยัน app/registry/identity/HTTPS health และบันทึก API URL. ปุ่มนี้เป็นการตรวจภายหลัง ไม่ใช่ปุ่มเตรียมสิทธิ์ และ `/health` ไม่แทน login/create/read ของขั้นก่อน
8. บันทึก image tag, revision, API URL และ UUID ที่ query ได้จริง

**Checkpoint:** HTTPS /health=200, authenticated read/create ผ่าน และ private ACR image ถูก pull ได้จริง. หน้า quickstart ต้องไม่ใช่สิ่งที่เห็นแล้ว

**ถ้าติดขัด:** ImagePull error → role/identity/registry/tag; startup error → module/lockfile/config; 502/503 → revision/port/probe/network. อย่าแก้ทุกชั้นพร้อมกัน
