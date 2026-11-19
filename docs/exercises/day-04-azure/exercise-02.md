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

เราจะย้าย API ไปยังพื้นที่ lab ที่ได้รับมอบหมาย โดยใช้ database เดิม. ACR เป็นคลังเก็บ image และ pull identity เป็นกุญแจที่ Container App ใช้เข้าคลัง; ผู้สอนเตรียมสิทธิ์ให้ก่อนเราเปิด API

> ทำขั้นสร้าง/แก้ resource เฉพาะ lab ที่เจ้าของอนุมัติ. ถ้าได้รับสิทธิ์ให้อ่านอย่างเดียว ให้ตรวจหน้าจอและบันทึกขั้น deploy ว่ายังไม่ได้ทดลอง ไม่กดสร้างหรือแก้สิทธิ์เพื่อทำตามตัวอย่าง

## Practice 1 — เตรียม registry และ image

<PracticeIllustration asset="d04-e02-p01" eager />

**Primary target:** Build และระบุ image ที่เก็บอยู่ใน ACR ของตนได้

### Steps

1. เปิด Edge แล้วเข้า Azure portal ด้วยบัญชีฝึกของตน ตรวจ Directory และ Subscription กับ `deployment.txt` ที่ได้รับ จากนั้นส่ง prompt นี้

   ~~~text
   ช่วยเริ่มขั้นตอนลงชื่อเข้าใช้ Azure CLI แล้วรอฉันลงชื่อเข้าใช้ด้วยตนเองใน Edge
   ตรวจเฉพาะ subscription/region/resource group และ pull identity ที่ฉันยืนยัน
   อ่านได้เฉพาะข้อมูล deployment ที่ไม่เป็นความลับ ไม่เปิด private README หรือ .env
   สรุปเป้าหมายให้ฉันเทียบกับ deployment.txt ยังไม่สร้างหรือแก้ resource
   ถ้า tenant/subscription ไม่ตรง ให้หยุดและบอกฉัน
   ~~~

2. จดชื่อ resource ที่จะใช้ตลอดวันร่วมกับผู้สอน: resource group เดิม, ACR, environment และ app. ACR ใช้ตัวอักษร/ตัวเลขไม่ใส่ hyphen; ชื่อ ACR ต้องไม่ซ้ำทั้ง Azure. ใช้ pull/pipeline identities ที่ได้รับ ไม่สร้างซ้ำ

   > **ใช้ subscription ของตนเอง:** ให้เจ้าของอนุมัติงบและให้ผู้ดูแลเตรียม resource group/identities/roles ก่อนเริ่ม. Private PostgreSQL ต้องใช้ environment/network ที่ IT เตรียมไว้ ไม่แก้ shared firewall จากแบบฝึกหัดนี้

3. ขอให้ Codex เสนอแผนสร้าง registry/environment ตาม lab โดยยังไม่ลงมือ

   ~~~text
   เตรียมแผนจาก subscription, region และชื่อ resource ที่ฉันยืนยัน
   ใช้ resource group และ pull/pipeline identities เดิม ไม่สร้างชุดใหม่
   ใช้ ACR Basic, admin disabled และ Container Apps environment แบบ Consumption-only
   ไม่สร้าง Log Analytics, dedicated profile หรือ private endpoint
   ถ้ามี resource เดิมให้ตรวจเจ้าของก่อนใช้ ถ้า private network ให้ใช้ environment ที่ IT เตรียม
   แสดงคำสั่ง เป้าหมาย และค่าใช้จ่ายที่อาจเกิด แล้วรอฉันยืนยันเฉพาะขั้นนี้
   ไม่แก้ PostgreSQL หรือ resources ส่วนกลาง
   ~~~

4. ตรวจแผนกับผู้สอน เมื่อได้รับอนุมัติแล้วจึงส่ง prompt ให้สร้างทีละ resource

   ~~~text
   ทำเฉพาะแผน registry/environment ที่ฉันเพิ่งอนุมัติทีละขั้น
   ตรวจว่า Azure CLI มี containerapp extension ที่ใช้ได้ก่อน
   ถ้าสิทธิ์, provider, quota หรือชื่อไม่พร้อม ให้หยุดพร้อมสาเหตุ ไม่เปลี่ยน subscription หรือสร้าง group ใหม่
   หลังสร้าง ตรวจ Consumption-only และ logs destination none ให้ตรงแผน
   ~~~

   คำสั่งสร้าง environment อ้างอิงสำหรับแผนนี้; ให้ Codex เติมค่าจริงที่ยืนยันแล้ว:

   ~~~shell
   az containerapp env create --name <ENV_NAME> --resource-group <LAB_RG> --location <REGION> --enable-workload-profiles false --logs-destination none
   ~~~

   Consumption-only เป็นแบบ legacy ที่ lab นี้เลือกไว้ ไม่ใช่ค่าเริ่มต้นของทุกหน้า Create. หากหน้า Portal แสดงค่าต่างจากแผน อย่ากดสร้างซ้ำ ให้ผู้สอนช่วยตรวจ

5. ให้ Codex build image บน ACR จาก root โปรเจค

   ~~~text
   build API ด้วย ACR Tasks ใน registry ที่เราเพิ่งตรวจ
   ใช้ root build context, api/Dockerfile และ platform linux/amd64
   ตั้ง image เป็น service-desk-api:day4-v1 ไม่ส่ง .env หรือ secrets เข้า build context
   แสดงผล build และ loginServer/tag ที่ใช้จริง ยังไม่สร้าง Container App
   ถ้า Tasks ใช้ไม่ได้ ให้หยุดและแจ้งผู้สอน ไม่ใช้ admin password แทน
   ~~~

   ~~~shell
   az acr build --registry <ACR_NAME> --image service-desk-api:day4-v1 --file api/Dockerfile --platform linux/amd64 .
   ~~~

6. ใน Edge เปิด Azure portal → ค้นชื่อ ACR → `Repositories` → เลือก image ต่อไปนี้ แล้วตรวจ tag จากผล build

   ~~~text
   service-desk-api
   ~~~

   ~~~text
   day4-v1
   ~~~

   จด `Login server` จากหน้า Overview และ image tag ใน review log โดยไม่บันทึกรหัสผ่าน

**Checkpoint:** ACR build ผ่านและเห็น repository/tag ที่ตรงกันใน Portal

## Practice 2 — สร้าง Container App และสิทธิ์ดึง image

<PracticeIllustration asset="d04-e02-p02" />

**Primary target:** ให้ Container App เข้าถึง private image ด้วย managed identity ได้

### Steps

1. แจ้งผู้สอนรหัสผู้เรียน, GitHub owner/repository/main และชื่อ ACR. รอผู้สอนยืนยันสิทธิ์ pull identity, pipeline identity และ OIDC ก่อน deploy private image. GitHub subject ต้องตรง repository จริง รวม immutable owner/repository IDs เมื่อ repository ใช้รูปแบบนั้น; ไม่คาดเดาจากชื่อ
2. ให้ Codex ตรวจ prerequisite ของ ACR แบบอ่านอย่างเดียว แล้วส่งผลที่ไม่มี secret ให้ผู้สอน

   ~~~text
   ตรวจ ACR ของ lab แบบอ่านอย่างเดียวว่าอนุญาต ARM audience tokens สำหรับ managed-identity image pull หรือไม่
   ตรวจชื่อ/resource ID ของ pull identity และ registry ที่จะใช้
   ถ้า authentication-as-arm ไม่ enabled หรือ role ยังไม่พร้อม ให้หยุดและแจ้งผู้สอน
   ไม่เปลี่ยน registry mode, role assignments หรือ authentication settings
   ~~~

   คำสั่งตรวจอ้างอิง:

   ~~~shell
   az acr config authentication-as-arm show --registry <ACR_NAME>
   ~~~

   ผู้ดูแลเตรียม `AcrPull` หรือ role ที่ตรง registry policy. Contributor ไม่ได้ให้สิทธิ์สร้าง role assignments; ไม่เปิด ACR admin หรือแก้ ABAC เพื่อข้ามปัญหา

3. เมื่อผู้สอนยืนยันว่าสิทธิ์พร้อม ให้ Codex แสดงแผน app ชั่วคราวจาก public quickstart image. ตรวจเป้าหมายและอนุมัติก่อนให้ทำ

   ~~~text
   เตรียม app ชื่อที่ฉันยืนยันใน resource group/environment เดิม
   ใช้ image mcr.microsoft.com/k8se/quickstart:latest ชั่วคราว port 80, external HTTPS ingress
   CPU 0.25, memory 0.5Gi, min replicas 0 และ max 1
   แนบ pull identity เดิม และตั้ง private registry ให้ใช้ identity นี้ ไม่ใช้ username/password
   แสดงแผนและรอฉันยืนยันก่อนสร้างหรือแก้ resource
   ใช้ app นี้ต่อใน Practice ถัดไป ไม่สร้าง app ที่สอง
   ~~~

4. หลังยืนยันแผน ให้ Codex ดำเนินการเฉพาะขั้นที่แสดง แล้วตรวจผล

   ~~~text
   ทำเฉพาะแผน app และ registry identity ที่ฉันอนุมัติเมื่อครู่
   ถ้า resource หรือสิทธิ์ไม่ตรงให้หยุด ไม่สร้างของทดแทน
   รายงาน Application URL และชื่อ pull identity โดยไม่แสดง secrets
   ~~~

5. ใน Portal ค้นชื่อ Container App → เปิด `Identity` → `User assigned`. ตรวจชื่อ identity กับที่ได้รับ. เปิดหน้ารายละเอียด container/revision แล้วตรวจ registry และการใช้ managed identity ตามผลของ Codex หากหาเมนูไม่พบ ให้ค้นชื่อเมนูในแถบซ้ายหรือให้ผู้สอนชี้จากหน้าจอจริง
6. กลับ `Overview` → เปิด `Application URL`. ตอนนี้ควรเป็นหน้า quickstart; เก็บ URL นี้ไว้ แต่ยังไม่ถือว่า Service Desk API ใช้งานได้

**Checkpoint:** app ชั่วคราวผูก pull identity และ registry ถูกต้อง โดยไม่มี ACR admin password; การดึง private image จะพิสูจน์ใน Practice ถัดไป

## Practice 3 — ตั้ง secrets และเปิด API จริง

<PracticeIllustration asset="d04-e02-p03" />

**Primary target:** รัน API บน HTTPS พร้อมเชื่อม PostgreSQL ด้วย runtime configuration ได้

### Steps

1. ใน Container App เปิด `Secrets` → `Add`. กรอก **Name** ตาม block นี้, เลือก **Type: Container Apps Secret**, ใส่ **Value** เป็น DATABASE_URL ของ runtime login เดิมด้วยตนเอง แล้วกด `Add`

   ~~~text
   database-url
   ~~~

2. ทำซ้ำสำหรับ JWT_SECRET จาก `.env` ส่วนตัวชุดเดิม โดยใช้ชื่อด้านล่าง. ตรวจว่าเห็นชื่อ secret ทั้งสองก่อนทำต่อ ไม่เปิดแสดงค่า ไม่ใช้ setup login และไม่สร้าง key ใหม่เพื่อให้ deployment ผ่าน

   ~~~text
   jwt-secret
   ~~~

3. ส่ง prompt ให้ Codex เตรียมการเปลี่ยน image และอ้าง secret ด้วยชื่อ ตรวจเป้าหมายแล้วจึงยืนยันให้ทำ

   ~~~text
   เตรียมการเปลี่ยน app เดิมจาก quickstart เป็น ACR image service-desk-api:day4-v1 ที่ build แล้ว
   ใช้ DATABASE_URL=secretref:database-url และ JWT_SECRET=secretref:jwt-secret ไม่อ่านค่า secret
   ตั้ง CORS_ORIGINS=http://localhost:3000 และ APP_VERSION=v1
   คง CPU 0.25/memory 0.5Gi/min 0/max 1 เปลี่ยน ingress target port เป็น 8000 และปิด insecure HTTP
   ตรวจ probe port ถ้ามีให้ตรง API port รอ revision พร้อมหลัง image/config/ingress เปลี่ยนครบ
   แสดงรายการเปลี่ยนก่อน แล้วรอฉันยืนยันเฉพาะขั้นนี้ ไม่ seed database
   ~~~

4. หลังตรวจแผน ส่งข้อความให้ทำเฉพาะรายการที่อนุมัติ

   ~~~text
   ทำเฉพาะการเปลี่ยน image/configuration/ingress ที่ฉันเพิ่งอนุมัติ
   รอ revision พร้อม แล้วสรุปชื่อ revision, image, HTTPS URL และผล health
   ไม่พิมพ์ค่า environment ทั้งหมดหรืออ่าน secrets และไม่ถือว่า health ผ่านแทน DB/auth
   ~~~

5. ใน Portal เปิด `Ingress` ตรวจ **Target port: 8000** และปิด **Insecure connections**. เปิดรายละเอียด revision ตรวจ image/tag และ environment variables ว่าอ้างชื่อ secret ถูกต้อง. API ใช้ port 8000 ภายใน ส่วน URL ของผู้ใช้เป็น HTTPS port 443
6. ใน Edge เปิด Application URL แล้วเติม `/health` ต้องได้ status `ok` และ version `v1`. จากนั้นเติม `/docs`, กด `Authorize` และกรอก app user/password เดิมเอง. เรียก GET ของ UUID เดิมจาก Day 3 แล้วลอง POST ข้อมูลนี้

   ~~~json
   {
     "title": "ทดสอบจาก Azure",
     "description": "ตรวจว่าระบบบน Azure บันทึกคำขอบริการได้",
     "category": "it"
   }
   ~~~

7. จด UUID จาก response, API URL, image tag และ revision. ส่งเฉพาะผลที่ไม่มี secret ให้ผู้สอนตรวจ หาก health ผ่านแต่ DB ล้ม ให้ผู้สอนตรวจ runtime login, TLS และ network จาก environment; ไม่ลด TLS หรือแก้ shared firewall เอง

**Checkpoint:** HTTPS health=200, login/read/create ผ่าน และ private image ถูก pull ได้จริง ไม่ใช่หน้า quickstart

**ถ้าติดขัด:** ImagePull error → identity/registry/tag; startup error → module/lockfile/config; 502/503 → revision/port/probe/network. ตรวจทีละชั้นกับผู้สอน
