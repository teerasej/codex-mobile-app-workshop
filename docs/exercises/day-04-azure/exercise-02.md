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

ถ้าคุณมี ACR image หรือ Container App พร้อมจากขั้นที่ทำไปแล้ว ให้ตรวจค่าที่ใช้อยู่และทำต่อจาก checkpoint ล่าสุด

## Practice 1 — เตรียม registry และ image

<PracticeIllustration asset="d04-e02-p01" eager />

**Primary target:** นำ image ที่ทดสอบในเครื่องเข้า ACR ของ lab และระบุ tag ที่พร้อม deploy ได้

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

2. เปิด `deployment.txt` จาก Student ZIP แล้วจด `RESOURCE_GROUP`, `ACR_NAME`, `ACR_LOGIN_SERVER` และ `PULL_IDENTITY_RESOURCE_ID` สำหรับ lab ของตน ใช้ registry ที่ผู้สอนเตรียมไว้

   ถ้าไม่มีค่า ACR หรือเปิด registry แล้วเจอ `403` ให้แจ้งผู้สอนพร้อมรหัสผู้เรียน, Resource Group, ชื่อ ACR และข้อความผิดพลาดที่ตัด token ออก ผู้สอนตรวจสิทธิ์ของบัญชีที่ใช้ build และ `AcrPull` ของ pull identity แยกกัน

   > **ใช้ subscription ของตนเอง** ให้เจ้าของอนุมัติงบและให้ผู้ดูแลเตรียม resource group กับ identities ก่อน หากยังไม่มี ACR ที่กำหนดไว้ ให้ขอแผนสร้าง ACR Basic ใน group ของตน โดยปิด admin และ anonymous pull ใช้ RBAC Registry Permissions และให้ผู้ดูแล grant `AcrPull` ที่ ACR แก่ pull identity เดิม

3. ขอให้ Codex ตรวจ ACR ที่ได้รับ แล้ววางแผน Container Apps Environment

   ~~~text
   ใช้ subscription, region, resource group, ACR_NAME และ ACR_LOGIN_SERVER จาก deployment.txt ของฉัน
   รอบนี้ตรวจ ACR แบบอ่านอย่างเดียว ขอให้ยืนยันว่าเป็น Basic ปิด admin และ login server ตรงกับไฟล์
   วางแผน Container Apps Environment แบบ Workload profiles (v2) ที่มีเฉพาะโปรไฟล์ Consumption
   ใช้แบบไม่มี Log Analytics, Dedicated profile หรือ private endpoint หาก PostgreSQL ใช้เครือข่ายส่วนตัว ให้ใช้ Environment ที่ IT เตรียมไว้
   ขอเห็นคำสั่ง เป้าหมาย และจุดที่อาจมีค่าใช้จ่ายก่อน แล้วรอฉันยืนยัน
   ~~~

4. ตรวจแผนกับผู้สอน เมื่อได้รับอนุมัติแล้วให้ใช้ Environment เดิมที่ตรงกับแผน หรือสร้างตามคำสั่งที่ตรวจแล้ว

   ~~~text
   ทำตามแผน Environment ที่ฉันอนุมัติใน subscription และ resource group ที่ตกลงไว้
   ตรวจว่า az containerapp env create --help แสดง --enable-workload-profiles และ --logs-destination
   ถ้าติดสิทธิ์, provider, quota หรือชื่อ ให้หยุดแล้วบอกว่าติดตรงไหน
   ตรวจ Environment ว่าสร้างสำเร็จ มีเฉพาะโปรไฟล์ Consumption และไม่ได้ตั้งปลายทางส่ง logs
   ถ้า IT เตรียม Environment ไว้แล้ว ให้ตรวจตัวเดิมตามค่าที่ IT อนุมัติ
   ~~~

   ให้ Codex เติมค่าจริงที่ยืนยันแล้วในคำสั่งอ้างอิงด้านล่าง ใช้คำสั่งสร้างเฉพาะเมื่อยังไม่มี Environment ที่ได้รับอนุมัติ หากใช้เครือข่ายส่วนตัว ให้ใช้ Environment ที่ IT ระบุ

   ~~~shell
   az containerapp env create --subscription "<SUBSCRIPTION_ID>" --resource-group "<LAB_RG>" --name "<ENV_NAME>" --location "<REGION>" --enable-workload-profiles true --logs-destination none
   ~~~

   ตรวจ Environment ที่สร้างสำหรับ lab ด้วยคำสั่งแบบอ่านอย่างเดียว

   ~~~shell
   az containerapp env show --subscription "<SUBSCRIPTION_ID>" --resource-group "<LAB_RG>" --name "<ENV_NAME>" --query "{state:properties.provisioningState,profiles:properties.workloadProfiles[].name,logsDestination:properties.appLogsConfiguration.destination}" --output json
   ~~~

   ควรเห็น `state` เป็น `Succeeded` และ `profiles` มีรายการเดียวคือ `Consumption` ค่า `logsDestination` อาจแสดงเป็น `null` หรือ `none` ซึ่งหมายถึงไม่มีปลายทางส่ง logs หากผลต่างจากแผน ให้ผู้สอนตรวจ Environment ที่มีอยู่ก่อนสร้างหรือแก้ไข

5. เริ่มจาก image ที่ build และทดสอบแล้วใน Exercise 1 ให้ Codex ตรวจชื่อ tag และ platform ในเครื่องก่อน

   ~~~text
   ใช้ image ของ Service Desk API ที่ฉัน build แล้วจาก Exercise 1
   ตรวจชื่อ tag และ platform ของ image ใน Docker แล้วเทียบกับ ACR ของ lab ที่ฉันยืนยันไว้
   ขอแผนส่ง image เข้า ACR และรอให้ฉันอนุมัติก่อน push หรือเริ่ม ACR Tasks
   ถ้ามี image รุ่นเดียวกันใน ACR แล้ว ให้ตรวจ tag, digest และ platform แล้วใช้ต่อได้
   ถ้า local tag ของฉันต่างจากตัวอย่าง ให้ใช้ local tag ที่ตรวจพบ
   ~~~

   ~~~shell
   docker image inspect service-desk-api:day4-v1 --format '{{.Os}}/{{.Architecture}}'
   ~~~

   - **ถ้าได้ `linux/amd64` และมีสิทธิ์ push** ให้ sign in เข้า ACR ด้วย Azure CLI ของ lab, tag image เดิม แล้ว push ไปยัง Login server ที่ตรวจแล้ว ให้ Codex แทนค่าตัวอย่างในวงเล็บมุมก่อนรัน

     ~~~shell
     az acr login --name "<ACR_NAME>"
     docker tag service-desk-api:day4-v1 "<ACR_LOGIN_SERVER>/service-desk-api:day4-v1"
     docker push "<ACR_LOGIN_SERVER>/service-desk-api:day4-v1"
     ~~~

   - **ถ้าได้ `linux/arm64`** ให้ใช้ ACR Tasks จาก root ของโปรเจกต์เพื่อ build สำหรับ Azure โดยตรง ตรวจ `.dockerignore` ก่อนว่าไม่ส่ง `.env` หรือ credentials ขึ้นไป หากติดสิทธิ์ push หรือ ACR Tasks ให้ผู้สอนตรวจสิทธิ์ของ lab หรือเตรียม image `linux/amd64` ใน ACR ให้ใช้

     ~~~shell
     az acr build --registry "<ACR_NAME>" --image service-desk-api:day4-v1 --file api/Dockerfile --platform linux/amd64 .
     ~~~

   ใช้ tag นี้เมื่อยังว่างหรือเป็น image รุ่นที่ยืนยันแล้ว หาก tag ถูกใช้กับคนละรุ่น ให้ตกลงชื่อ tag ใหม่และใช้ชื่อเดียวกันในขั้นต่อไป [Docker push ไปยัง ACR](https://learn.microsoft.com/en-us/azure/container-apps/tutorial-code-to-cloud) · [Platform ที่ Container Apps รองรับ](https://learn.microsoft.com/en-us/azure/container-apps/containers)

6. ใน Edge เปิด [Resource groups ใน Azure portal](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups) แล้วเลือกกลุ่มที่ตรงกับ `RESOURCE_GROUP` ใน `deployment.txt` จากรายการ resources ในกลุ่ม ให้เปิด ACR ที่สร้างไว้ เลือก `Repositories` แล้วตรวจว่า repository และ tag ตรงกับผล build

   ~~~text
   service-desk-api
   ~~~

   ~~~text
   day4-v1
   ~~~

   ใช้ชื่อ registry ของตนเอง แล้วตรวจว่า `service-desk-api` มี tag ที่ตกลงไว้ ซึ่งในตัวอย่างคือ `day4-v1` ชื่อและ tag ในภาพเป็นตัวอย่างของ Microsoft Learn

   ![หน้า Repositories ของ Azure Container Registry แสดงรายการ repository และ tags](https://learn.microsoft.com/en-us/azure/container-registry/media/container-registry-repositories/container-registry-repositories.png)

   [ภาพจาก Microsoft Learn · Repositories and tags](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repositories)

7. กลับไปที่ `Overview` ของ ACR แล้ว **จด `Login server` และ image tag ที่ตรวจจาก Step 6 พร้อม digest ที่ระบบแสดง** ลงใน review log โดยไม่บันทึกรหัสผ่าน

   ![หน้า Overview ของ Azure Container Registry แสดงค่า Login server](https://learn.microsoft.com/en-us/azure/container-registry/media/container-registry-get-started-portal/container-registry-overview.png)

   [ภาพจาก Microsoft Learn · Container registry quickstart](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal#create-a-container-registry)

**Checkpoint:** เห็น image `linux/amd64` พร้อม repository/tag และ digest ที่ตรวจแล้วใน ACR ของ lab

## Practice 2 — สร้าง Container App และสิทธิ์ดึง image

<PracticeIllustration asset="d04-e02-p02" />

**Primary target:** ให้ Container App เข้าถึง private image ด้วย managed identity ได้

### Steps

1. แจ้งผู้สอนรหัสผู้เรียนและชื่อ ACR ที่ใช้ ให้ผู้สอนยืนยันว่า pull identity ใน `deployment.txt` มี `AcrPull` ที่ขอบเขตของ ACR นี้ หากยังไม่ได้รับสิทธิ์ ให้ผู้สอนตรวจใน Instructor Console ก่อนนำ private image ขึ้นแอป
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

3. เมื่อผู้สอนยืนยันว่าสิทธิ์พร้อม ให้ Codex แสดงแผน app ชั่วคราวจาก public quickstart image หากมี Container App ที่ lab อนุมัติแล้ว ให้ใช้ตัวเดิมและตรวจ registry binding กับ pull identity ตรวจเป้าหมายและอนุมัติก่อนให้ทำ

   ~~~text
   อยากเปิดหน้า quickstart ชั่วคราวบน Container App ที่เราจะใช้ต่อในขั้นถัดไป
   ช่วยวางแผนโดยใช้ชื่อที่ฉันยืนยันใน resource group และ environment เดิม เลือกโปรไฟล์ Consumption สำหรับ environment ของ lab
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

6. กลับ `Overview` → เปิด `Application URL` ถ้าเพิ่งสร้างแอป ควรเห็นหน้า Quickstart ถ้าแอปเดิมรัน Service Desk API อยู่แล้ว ให้ตรวจ `/health` และใช้ URL เดิมต่อ

   ![หน้า Hello World ที่ควรเห็นในเบราว์เซอร์หลังเปิด Application URL ของ Container App ชั่วคราว](https://learn.microsoft.com/en-us/azure/container-apps/media/get-started/azure-container-apps-quickstart.png)

   [ภาพจาก Microsoft Learn · Container Apps portal quickstart](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-portal#create-a-container-app)

**Checkpoint:** app ชั่วคราวผูก pull identity และ registry ถูกต้อง โดยไม่มี ACR admin password; การดึง private image จะพิสูจน์ใน Practice ถัดไป

## Practice 3 — ตั้ง secrets และเปิด API จริง

<PracticeIllustration asset="d04-e02-p03" />

**Primary target:** รัน API บน HTTPS พร้อมเชื่อม PostgreSQL ด้วย runtime configuration ได้

### Steps

1. ใน Container App เปิด `Secrets` → `Add` แล้วตั้ง **Name** เป็น `database-url` ตามบล็อกด้านล่าง เลือก **Type** เป็น `Container Apps Secret` จากนั้นเปิดไฟล์ `api/.env` ส่วนตัวของโปรเจกต์ แล้วคัดลอกเฉพาะค่าหลัง `DATABASE_URL=` ของ runtime login เดิมไปวางในช่อง **Value** ด้วยตนเอง แล้วกด `Add`

   ~~~text
   database-url
   ~~~

   [วิธีเปิดหน้า Add secret ใน Azure portal · Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets?tabs=azure-portal#defining-secrets)

2. ทำซ้ำสำหรับ JWT_SECRET จาก `.env` ส่วนตัวชุดเดิม โดยใช้ชื่อด้านล่าง. ตรวจว่าเห็นชื่อ secret ทั้งสองก่อนทำต่อ ไม่เปิดแสดงค่า ไม่ใช้ setup login และไม่สร้าง key ใหม่เพื่อให้ deployment ผ่าน

   ~~~text
   jwt-secret
   ~~~

3. ส่ง prompt ให้ Codex เตรียมการเปลี่ยน image และอ้าง secret ด้วยชื่อ ตรวจเป้าหมายแล้วจึงยืนยันให้ทำ หาก `AGENTS.md` ยังระบุให้รอ GitHub OIDC ก่อน deploy private image ให้แก้เฉพาะข้อ Day 4 ตาม [template ฉบับล่าสุด](/resources/agents-template) แล้วเริ่ม chat ใหม่ในโปรเจกต์เดิม ตรวจและยืนยันแผนใน chat นั้นก่อนทำ Step 4

   ~~~text
   อยากให้ URL เดิมเปิด Service Desk API แทนหน้า quickstart ช่วยวางแผนเปลี่ยนไปใช้ ACR image และ tag ที่ฉันตรวจแล้วใน Practice 1
   งานนี้ deploy โดยตรงผ่าน Azure ใน Exercise 2 ตรวจว่า Container App ตั้งค่าให้ใช้ pull identity จาก deployment.txt กับ ACR นี้ และ identity มีสิทธิ์ pull แล้ว
   ใช้ฐานข้อมูลเดิมโดยไม่ seed และอ้าง secret ด้วยชื่อ DATABASE_URL=secretref:database-url และ JWT_SECRET=secretref:jwt-secret โดยไม่อ่านค่า
   ตั้ง CORS_ORIGINS=http://localhost:3000 ให้ preview ต่อได้ และ APP_VERSION=v1 ให้เช็กจาก /health ได้

   คงขนาด 0.25 vCPU, 0.5Gi และ 0–1 replicas ให้ HTTPS เข้าถึง API ที่พอร์ต 8000 และปิด insecure HTTP
   ถ้ามี probe ให้ใช้พอร์ต API เดียวกัน และใส่ขั้นรอให้ revision พร้อมหลังเปลี่ยนครบ
   ขอรายการที่จะเปลี่ยนก่อน แล้วรอฉันยืนยัน
   ~~~

4. หลังตรวจแผน ส่งข้อความให้ทำเฉพาะรายการที่อนุมัติ

   ~~~text
   เปลี่ยน image, การตั้งค่า และ ingress ตามที่ฉันเพิ่งอนุมัติได้เลย
   ใช้การ deploy โดยตรงผ่าน Azure ของ Exercise 2 ถ้าสิทธิ์ pull หรือการผูก ACR กับ pull identity ยังไม่พร้อม ให้หยุดและบอกว่าติดตรงไหน
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

12. จด UUID จาก response, API URL, image tag และ revision เก็บ UUID นี้ไว้ตรวจซ้ำใน Exercise 3. หาก health ผ่านแต่ database ไม่ทำงานอย่างที่ควรจะเป็น ให้ผู้สอนตรวจ runtime login, TLS และ network จาก environment

**Checkpoint:** HTTPS health=200, login/read/create ผ่าน และ private image ถูก pull ได้จริง ไม่ใช่หน้า quickstart

**ถ้าติดขัด:** ImagePull error → identity/registry/tag; startup error → module/lockfile/config; 502/503 → revision/port/probe/network. ตรวจทีละชั้นกับผู้สอน
