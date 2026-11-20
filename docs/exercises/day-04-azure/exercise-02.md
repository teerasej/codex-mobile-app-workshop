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

เราจะย้าย API ไปยังพื้นที่ lab ที่ได้รับมอบหมาย โดยใช้ database เดิม
ACR เป็นคลังที่เก็บ image และ pull identity เป็นกุญแจที่ Container App ใช้เข้าคลัง

> ทำขั้นสร้าง/แก้ resource เฉพาะ lab ที่เจ้าของอนุมัติ. ถ้าได้รับสิทธิ์ให้อ่านอย่างเดียว ให้ตรวจหน้าจอและบันทึกขั้น deploy ว่ายังไม่ได้ทดลอง ไม่กดสร้างหรือแก้สิทธิ์เพื่อทำตามตัวอย่าง

## Practice 1 — เตรียม registry และ image

<PracticeIllustration asset="d04-e02-p01" eager />

**Primary target:** Build และระบุ image ที่เก็บอยู่ใน ACR ของตนได้

### Steps

1. เปิด Edge แล้วเข้า Azure portal ด้วยบัญชีฝึกของตน ตรวจ Directory และ Subscription กับ `deployment.txt` ที่ได้รับ จากนั้นส่ง prompt นี้

   ใช้อีเมลและ **Temporary Access Pass (TAP)** จากหัวข้อ **Microsoft Entra sign-in** ใน `README.md` ภายใน ZIP ส่วนตัวที่ผู้สอนส่งให้

   ![หน้า Directories + subscriptions ใน Azure portal สำหรับตรวจ Directory และตัวกรอง Subscription](https://learn.microsoft.com/en-us/azure/azure-portal/media/set-preferences/settings-directories-subscriptions-default-filter.png)

   [ภาพจาก Microsoft Learn · Azure portal settings](https://learn.microsoft.com/en-us/azure/azure-portal/set-preferences#directories--subscriptions)

   ~~~text
   ช่วยเปิดขั้นตอน Sign in ของ Azure CLI ให้หน่อย
   ~~~
   หลังจาก login เข้า Azure CLI แล้ว
   ~~~text
   ขอดู subscription, region, resource group และ pull identity ที่ฉันยืนยันไว้ จะเอาไปเทียบกับ deployment.txt
   ~~~

2. จดชื่อ resource ที่จะใช้ตลอดวันร่วมกับผู้สอน: resource group เดิม, ACR, environment และ app. ACR ใช้ตัวอักษร/ตัวเลขไม่ใส่ hyphen; ชื่อ ACR ต้องไม่ซ้ำทั้ง Azure. ใช้ pull/pipeline identities ที่ได้รับ ไม่สร้างซ้ำ

   > **ใช้ subscription ของตนเอง:** ให้เจ้าของอนุมัติงบและให้ผู้ดูแลเตรียม resource group/identities/roles ก่อนเริ่ม. Private PostgreSQL ต้องใช้ environment/network ที่ IT เตรียมไว้ ไม่แก้ shared firewall จากแบบฝึกหัดนี้

3. ขอให้ Codex เสนอแผนสร้าง registry/environment ตาม lab โดยยังไม่ลงมือ

   ~~~text
   ช่วยวางแผนเตรียมที่เก็บ image กับที่รันแอป โดยใช้ subscription, region และชื่อที่ฉันยืนยันไว้
   ใช้ resource group กับ pull และ pipeline identities เดิม

   ตามแผน lab ขอ ACR Basic ที่ปิด admin และ Container Apps แบบ Consumption-only
   ใช้แบบไม่มี Log Analytics, dedicated profile หรือ private endpoint ถ้าใช้เครือข่ายส่วนตัว ให้ใช้ environment ที่ IT เตรียมไว้
   ขอเห็นคำสั่ง เป้าหมาย และจุดที่อาจมีค่าใช้จ่ายก่อน แล้วรอฉันยืนยัน เก็บ PostgreSQL กับ resources ส่วนกลางไว้ตามเดิม
   ~~~

4. ตรวจแผนกับผู้สอน เมื่อได้รับอนุมัติแล้วจึงส่ง prompt ให้สร้างทีละ resource

   ~~~text
   ทำตามแผน ACR กับ environment ที่ฉันเพิ่งอนุมัติได้เลยทีละขั้น
   เช็กว่า Azure CLI ใช้ containerapp extension ได้ก่อน ถ้าติดสิทธิ์, provider, quota หรือชื่อ ให้หยุดแล้วบอกว่าติดตรงไหน
   ใช้ subscription และ resource group ที่ตกลงไว้ เสร็จแล้วช่วยยืนยันว่าเป็น Consumption-only และ logs destination เป็น none
   ~~~

   คำสั่งสร้าง environment อ้างอิงสำหรับแผนนี้; ให้ Codex เติมค่าจริงที่ยืนยันแล้ว:

   ~~~shell
   az containerapp env create --name <ENV_NAME> --resource-group <LAB_RG> --location <REGION> --enable-workload-profiles false --logs-destination none
   ~~~

   Consumption-only เป็นแบบ legacy ที่ lab นี้เลือกไว้ ไม่ใช่ค่าเริ่มต้นของทุกหน้า Create. หากหน้า Portal แสดงค่าต่างจากแผน อย่ากดสร้างซ้ำ ให้ผู้สอนช่วยตรวจ

5. ให้ Codex build image บน ACR จาก root โปรเจค

   ~~~text
   ช่วย build image service-desk-api:day4-v1 ด้วย ACR Tasks ใน registry ที่เราเพิ่งตรวจ
   ทำจาก root ตามตัวอย่าง ใช้ api/Dockerfile กับ linux/amd64 และกัน .env กับ secrets ออกจากไฟล์ที่ส่งไป build
   ขอผล build, loginServer และ tag ที่ได้จริง เดี๋ยวค่อยสร้าง Container App ในขั้นถัดไป
   ถ้า Tasks ใช้ไม่ได้ ให้หยุดแล้วบอกสิ่งที่ต้องแจ้ง
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

   ใช้ชื่อ registry ของตนเอง แล้วตรวจว่า `service-desk-api` มี tag `day4-v1` ชื่อและ tag ในภาพเป็นตัวอย่างของ Microsoft Learn

   ![หน้า Repositories ของ Azure Container Registry แสดงรายการ repository และ tags](https://learn.microsoft.com/en-us/azure/container-registry/media/container-registry-repositories/container-registry-repositories.png)

   [ภาพจาก Microsoft Learn · Repositories and tags](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repositories)

   ![หน้า Overview ของ Azure Container Registry แสดงค่า Login server](https://learn.microsoft.com/en-us/azure/container-registry/media/container-registry-get-started-portal/container-registry-overview.png)

   [ภาพจาก Microsoft Learn · Container registry quickstart](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal#create-a-container-registry)

**Checkpoint:** ACR build ผ่านและเห็น repository/tag ที่ตรงกันใน Portal

## Practice 2 — สร้าง Container App และสิทธิ์ดึง image

<PracticeIllustration asset="d04-e02-p02" />

**Primary target:** ให้ Container App เข้าถึง private image ด้วย managed identity ได้

### Steps

1. แจ้งผู้สอนรหัสผู้เรียน, GitHub owner/repository/main และชื่อ ACR. รอผู้สอนยืนยันสิทธิ์ pull identity, pipeline identity และ OIDC ก่อน deploy private image. GitHub subject ต้องตรง repository จริง รวม immutable owner/repository IDs เมื่อ repository ใช้รูปแบบนั้น; ไม่คาดเดาจากชื่อ
2. ให้ Codex ตรวจ prerequisite ของ ACR แบบอ่านอย่างเดียว แล้วส่งผลที่ไม่มี secret ให้ผู้สอน

   ~~~text
   ช่วยดูว่า Container App จะดึง image จาก ACR ของ lab ด้วย pull identity ได้ไหม
   ขอชื่อกับ resource ID ของ identity และ registry
   รอบนี้ขอตรวจอย่างเดียว
   ~~~

   คำสั่งตรวจอ้างอิง:

   ~~~shell
   az acr config authentication-as-arm show --registry <ACR_NAME>
   ~~~

   ผู้ดูแลเตรียม `AcrPull` หรือ role ที่ตรง registry policy. Contributor ไม่ได้ให้สิทธิ์สร้าง role assignments; ไม่เปิด ACR admin หรือแก้ ABAC เพื่อข้ามปัญหา

3. เมื่อผู้สอนยืนยันว่าสิทธิ์พร้อม ให้ Codex แสดงแผน app ชั่วคราวจาก public quickstart image. ตรวจเป้าหมายและอนุมัติก่อนให้ทำ

   ~~~text
   อยากเปิดหน้า quickstart ชั่วคราวบน Container App ที่เราจะใช้ต่อในขั้นถัดไป
   ช่ววางแผนโดยใช้ชื่อที่ฉันยืนยันใน resource group และ environment เดิม
   ใช้ mcr.microsoft.com/k8se/quickstart:latest ที่พอร์ต 80 เปิดให้เข้าผ่าน HTTPS จากภายนอก
   ขอฉันดูแผนและยืนยันก่อนลงมือ
   ~~~

4. หลังยืนยันแผน ให้ Codex ดำเนินการเฉพาะขั้นที่แสดง แล้วตรวจผล

   ~~~text
   สร้าง app และผูก registry ตามแผนได้เลย
   ถ้า resource หรือสิทธิ์ไม่ตรงกับแผน ให้หยุดแล้วบอกว่าติดตรงไหน
   ขอแค่ Application URL สำหรับเปิดหน้า quickstart กับชื่อ pull identity
   ~~~

5. ใน Portal ค้นชื่อ Container App → เปิด `Identity` → `User assigned`. ตรวจชื่อ identity กับที่ได้รับ. เปิดหน้ารายละเอียด container/revision แล้วตรวจ registry และการใช้ managed identity ตามผลของ Codex หากหาเมนูไม่พบ ให้ค้นชื่อเมนูในแถบซ้ายหรือให้ผู้สอนชี้จากหน้าจอจริง

   ![หน้า Identity ของ Container App เปิดแท็บ User assigned เพื่อดูรายการ managed identities](https://learn.microsoft.com/en-us/azure/container-apps/media/managed-identity/screenshot-user-assigned-identity.png)

   [ภาพจาก Microsoft Learn · Managed identities](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity#configure-managed-identities)

6. กลับ `Overview` → เปิด `Application URL`. ตอนนี้ควรเป็นหน้า quickstart; เก็บ URL นี้ไว้ แต่ยังไม่ถือว่า Service Desk API ใช้งานได้

   ![หน้า Hello World ที่ควรเห็นในเบราว์เซอร์หลังเปิด Application URL ของ Container App ชั่วคราว](https://learn.microsoft.com/en-us/azure/container-apps/media/get-started/azure-container-apps-quickstart.png)

   [ภาพจาก Microsoft Learn · Container Apps portal quickstart](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-portal#create-a-container-app)

**Checkpoint:** app ชั่วคราวผูก pull identity และ registry ถูกต้อง โดยไม่มี ACR admin password; การดึง private image จะพิสูจน์ใน Practice ถัดไป

## Practice 3 — ตั้ง secrets และเปิด API จริง

<PracticeIllustration asset="d04-e02-p03" />

**Primary target:** รัน API บน HTTPS พร้อมเชื่อม PostgreSQL ด้วย runtime configuration ได้

### Steps

1. ใน Container App เปิด `Secrets` → `Add`. กรอก **Name** ตาม block นี้, เลือก **Type: Container Apps Secret**, ใส่ **Value** เป็น DATABASE_URL ของ runtime login เดิมด้วยตนเอง แล้วกด `Add`

   ~~~text
   database-url
   ~~~

   [วิธีเปิดหน้า Add secret ใน Azure portal · Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets?tabs=azure-portal#defining-secrets)

2. ทำซ้ำสำหรับ JWT_SECRET จาก `.env` ส่วนตัวชุดเดิม โดยใช้ชื่อด้านล่าง. ตรวจว่าเห็นชื่อ secret ทั้งสองก่อนทำต่อ ไม่เปิดแสดงค่า ไม่ใช้ setup login และไม่สร้าง key ใหม่เพื่อให้ deployment ผ่าน

   ~~~text
   jwt-secret
   ~~~

3. ส่ง prompt ให้ Codex เตรียมการเปลี่ยน image และอ้าง secret ด้วยชื่อ ตรวจเป้าหมายแล้วจึงยืนยันให้ทำ

   ~~~text
   อยากให้ URL เดิมเปิด Service Desk API แทนหน้า quickstart ช่วยวางแผนเปลี่ยนไปใช้ ACR image service-desk-api:day4-v1
   ใช้ฐานข้อมูลเดิมโดยไม่ seed และอ้าง secret ด้วยชื่อ DATABASE_URL=secretref:database-url และ JWT_SECRET=secretref:jwt-secret โดยไม่อ่านค่า
   ตั้ง CORS_ORIGINS=http://localhost:3000 ให้ preview ต่อได้ และ APP_VERSION=v1 ให้เช็กจาก /health ได้

   คงขนาด 0.25 vCPU, 0.5Gi และ 0–1 replicas ให้ HTTPS เข้าถึง API ที่พอร์ต 8000 และปิด insecure HTTP
   ถ้ามี probe ให้ใช้พอร์ต API เดียวกัน และใส่ขั้นรอให้ revision พร้อมหลังเปลี่ยนครบ
   ขอรายการที่จะเปลี่ยนก่อน แล้วรอฉันยืนยัน
   ~~~

4. หลังตรวจแผน ส่งข้อความให้ทำเฉพาะรายการที่อนุมัติ

   ~~~text
   เปลี่ยน image, การตั้งค่า และ ingress ตามที่ฉันเพิ่งอนุมัติได้เลย
   พอ revision พร้อม ขอชื่อ revision, image, HTTPS URL และผล /health โดยไม่เปิดค่า secrets หรือแสดง environment ทั้งชุด
   บอกฉันเมื่อพร้อมให้ลองล็อกอินและอ่านข้อมูลจริงตามขั้นถัดไป
   ~~~

5. ใน Portal เปิด `Ingress` ตรวจ **Target port: 8000** และปิด **Insecure connections**.

   [วิธีตรวจ Target port และการตั้งค่า HTTPS ใน Ingress · Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/ingress-how-to?tabs=azure-portal#enable-ingress)

6. เปิดรายละเอียด revision ตรวจ image/tag และ environment variables ว่าอ้างชื่อ secret ถูกต้อง. API ใช้ port 8000 ภายใน ส่วน URL ของผู้ใช้เป็น HTTPS port 443

   ![หน้า Environment variables ใน Container App แสดงการเลือก Reference a secret และชื่อ secret ที่อ้างอิง](https://learn.microsoft.com/en-us/azure/container-apps/media/environment-variables/secret-env-var.png)

   [ภาพจาก Microsoft Learn · Environment variables](https://learn.microsoft.com/en-us/azure/container-apps/environment-variables#add-environment-variables-on-existing-container-apps)

7. ใน Microsoft Edge เปิด Application URL แล้วเติม `/health` เพื่อทดสอบการทำงานต้องได้ status `ok` และ version `v1`.
8. จากนั้นเติม `/docs` เพื่อเข้าใช้งาน Swagger
9. กด `Authorize` และกรอก app user/password เดิมเอง.
10. เรียก GET ของ UUID เดิมจาก Day 3
11. จากนั้นลอง POST ข้อมูลนี้

   ~~~json
   {
     "title": "ทดสอบจาก Azure",
     "description": "ตรวจว่าระบบบน Azure บันทึกคำขอบริการได้",
     "category": "it"
   }
   ~~~

12. จด UUID จาก response, API URL, image tag และ revision. หาก health ผ่านแต่ database ไม่ทำงานอย่างที่ควรจะเป็น ให้ผู้สอนตรวจ runtime login, TLS และ network จาก environment

**Checkpoint:** HTTPS health=200, login/read/create ผ่าน และ private image ถูก pull ได้จริง ไม่ใช่หน้า quickstart

**ถ้าติดขัด:** ImagePull error → identity/registry/tag; startup error → module/lockfile/config; 502/503 → revision/port/probe/network. ตรวจทีละชั้นกับผู้สอน
