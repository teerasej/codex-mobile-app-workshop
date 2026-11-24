---
title: "Day 4 · Exercise 4 — เชื่อม Android และดูแลรุ่นที่ใช้งาน"
prev: {"text": "Exercise 3", "link": "/exercises/day-04-azure/exercise-03"}
next: {"text": "สรุปท้ายวัน", "link": "/exercises/day-04-azure/summary"}
---

# Exercise 4 — เชื่อม Android และดูแลรุ่นที่ใช้งาน

> **Day 4 · Azure · 14:45–16:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-04-azure/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

## Scenario

API เปิดแล้ว เราจะลองจากมุมผู้ใช้ และหาหลักฐานเมื่อมีปัญหา. Log เหมือนสมุดรับงาน ส่วน revision บอกว่าร้านกำลังใช้สูตรรุ่นไหน

## Practice 1 — ใช้ Android กับ HTTPS API

<PracticeIllustration asset="d04-e04-p01" eager />

**Primary target:** ส่ง Request จาก Android ไปถึง API บน Azure ได้

### Steps

1. ส่ง API URL จาก Exercise 3 ที่ไม่มี secret ให้ Codex แล้วขอเปิด browser preview ใหม่

   ~~~text
   อยากลองแอปกับ API บน Azure จาก browser ก่อน ช่วยปิดเฉพาะ API หรือ container ในเครื่องกับ Flutter preview เดิมของเรา
   เช็กว่า URL ที่ฉันให้เป็น HTTPS ของ lab จริง และไม่ใช่ localhost หรือ 127.0.0.1
   จาก client/ ส่ง URL นี้เป็น API_BASE_URL ผ่าน dart-define แล้วเปิด preview ที่ http://localhost:3000
   บน Windows ใช้ Edge บน Mac ใช้ web-server แล้วส่งลิงก์ให้ฉันเปิดใน Edge
   รอบนี้ปรับแค่การเปิดแอปในเครื่อง เก็บ Azure กับ CORS ไว้ตามเดิม
   ~~~

2. ใน Edge เปิด preview ตาม URL ที่ Codex แจ้ง. Login ด้วย app user ของตนแล้วสร้าง Request สมมติหนึ่งรายการ. ถ้า CORS ล้ม ให้เทียบ **frontend origin** กับ CORS ของ API

   ~~~text
   http://localhost:3000
   ~~~

   CORS_ORIGINS ต้องมี frontend origin นี้ ไม่ใช่ Application URL ของ API. ให้ผู้สอนตรวจแผนก่อนแก้ Cloud config

3. ขอให้ Codex สลับไป Android ที่เตรียมไว้แล้ว โดยใช้ HTTPS origin เดิม

   ~~~text
   ทีนี้อยากลองบน Android กับ API บน Azure ตัวเดิม ช่วยปิด browser preview ของเราแล้วดูว่ามีเครื่องไหนพร้อม
   ถ้ามีหลายเครื่อง ขอชื่อกับ device ID ให้ฉันเลือกก่อน
   รันจาก client/ แล้วส่ง HTTPS URL เดิมเป็น API_BASE_URL ผ่าน dart-define
   ให้ API ในเครื่องปิดต่อ ใช้ HTTPS ตรงโดยไม่พึ่ง adb reverse และไม่ใส่ password หรือ token ในคำสั่งหรือ log
   ~~~

4. ใน Android กรอก password เอง แล้วสร้าง Request นี้. จด UUID; ใน Edge เปิด HTTPS API `/docs` และ `Authorize` ด้วย user เดียวกัน เรียก GET UUID นี้ต้องพบ title/status ตรงกัน. Logout/login ใหม่ใน Android แล้วค้นรายการเดิม

   - **Title**

     ~~~text
     Request จาก Android บน Cloud
     ~~~

   - **Description**

     ~~~text
     ตรวจว่ามือถือส่งคำขอบริการถึง API บน Azure ได้
     ~~~

   - **Category:** เลือก

     ~~~text
     it
     ~~~

5. เมื่อรันทดสอบเสร็จ ให้ Codex หยุด Flutter run แล้ว build debug APK ด้วยค่า API เดิม

   ~~~text
   ขอไฟล์ติดตั้ง Android สำหรับทดสอบกับ API บน Azure ตัวที่เพิ่งลอง
   ช่วยหยุด Flutter รอบนี้ แล้ว build debug APK จาก client/ โดยส่ง HTTPS URL เดิมเป็น API_BASE_URL ผ่าน dart-define
   บอกผล build, ที่อยู่ไฟล์ APK และ API host ที่ใช้ รอบนี้ขอแค่ไฟล์ debug ในเครื่อง
   ~~~

   บันทึก APK path และ API host ใน review log. `dart-define` ต้องใส่ตอน build ใหม่ด้วย; APK เก่าจะไม่เปลี่ยน URL ตามการรันครั้งล่าสุดเอง

**Checkpoint:** local API ปิดอยู่ แต่ Android ยังสร้าง/อ่าน Request ผ่าน HTTPS ได้ และ APK ใช้ API host ที่ตรวจแล้ว

## Practice 2 — อ่าน Log และ Revision เพื่อตรวจปัญหา

<PracticeIllustration asset="d04-e04-p02" />

**Primary target:** ใช้หลักฐานของ revision ที่กำลังทำงานอธิบายอาการ API ได้

### Steps

1. ใน Edge เปิด Container App ของตน → หน้ารายการ revision (`Revisions and replicas` หรือ `Revision management` ตามหน้าจอ) → เลือก revision ที่พร้อมและรับ traffic. ตรวจชื่อ revision กับ image แล้วขอ Codex ยืนยันแบบอ่านอย่างเดียว

   ![หน้า Revision management ของ Container App แสดงรายการ revision สถานะ และสัดส่วน traffic](https://learn.microsoft.com/en-us/azure/container-apps/media/revisions/screen-shot-revision-mgmt-labels.png)

   [ภาพจาก Microsoft Learn · Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions#labels)

   ~~~text
   ช่วยดูว่า Container App ของ lab นี้กำลังให้ผู้ใช้เจอ API รุ่นไหน
   ขอดู revision ที่พร้อมและรับ traffic จริง พร้อมชื่อ image กับ tag เต็ม
   ถ้า revision ล่าสุดเป็นคนละตัว ช่วยชี้ให้เห็นด้วย รอบนี้แค่ดูใน Azure
   ~~~

2. เปิด `Monitoring` → `Log stream` ของ app → เลือก `Console` → เลือก revision/replica/container ที่กำลังใช้. เปิด stream ค้างไว้ แล้วเปิด `/docs` ใน Edge อีกแท็บ. หากใช้ Codex ดู log แทน ให้ส่ง prompt นี้

   ~~~text
   ฉันกำลังจะลองเรียก API ช่วยเปิด Console log สดของ revision, replica และ container ที่เราเพิ่งตรวจ
   เริ่มจากไม่เกิน 30 บรรทัดล่าสุด และอย่าแสดงค่า environment หรือ secrets
   เปิดค้างไว้ให้ฉันเทียบกับผลที่เห็น แล้วรอฉันบอกให้หยุด
   ~~~

   คำสั่งอ้างอิง; ถ้ามีหลาย revision ให้ Codex ระบุ revision/replica/container ที่ตรงกันเพิ่ม:

   ~~~shell
   az containerapp logs show --name <APP_NAME> --resource-group <LAB_RG> --type console --tail 30 --follow
   ~~~

   [วิธีเปิด Log stream และเลือก Console ใน Azure portal · Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/log-streaming#view-log-streams-via-the-azure-portal)

3. ใน `/docs` กด `Authorize` ด้วย user เดิม เลือก `GET /requests/{id}` → `Try it out`. ใช้ UUID ที่ไม่มีในข้อมูลของตน เช่นค่าด้านล่าง → `Execute`. ต้องได้ 404 แล้วกลับไป stream เทียบเวลา, path และ status โดยไม่คัดลอก token

   ~~~text
   00000000-0000-4000-8000-000000000000
   ~~~

4. ตรวจว่าแอปใช้โปรไฟล์ `Consumption`, CPU 0.25 vCPU, memory 0.5 GiB, min replicas 0 และ max replicas 1 หากแอปลดเหลือ 0 replicas ให้เรียก `/health` เพื่อเริ่ม replica แล้วเลือก replica นั้นใน Log stream อาจต้องรอช่วง cold start ดู logs สดระหว่างทดสอบ เพราะ Environment ของ lab ไม่ส่ง logs ไปเก็บใน Log Analytics ใช้ขนาดตามแผนตลอดขั้นนี้

   ภาพแสดงตำแหน่งของตัวเลือกจำนวน replicas ในแท็บ `Scale` ให้เทียบค่าของ lab กับตัวเลขในขั้นตอนนี้

   ![แท็บ Scale ของ Container App แสดงตัวเลือกจำนวน replicas ขั้นต่ำและขั้นสูง](https://learn.microsoft.com/en-us/azure/container-apps/media/scale-app/azure-container-apps-scale-slide.png)

   [ภาพจาก Microsoft Learn · Scaling](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)

5. หยุด stream เมื่อพบหลักฐานแล้ว. ถ้า Codex เปิดให้ ให้ส่งข้อความนี้

   ~~~text
   ได้ผลที่ต้องการแล้ว ช่วยปิดเฉพาะหน้าติดตาม log ที่เปิดเมื่อกี้
   ขอเวลา, เส้นทาง, status 404 และชื่อ revision สำหรับจดหลักฐาน โดยไม่คัดลอก token
   ~~~

6. จด UUID ที่สร้างใน Practice 1 แล้วขอแผน restart **เฉพาะ revision ของ app ฝึก**. Restart เป็นการเปลี่ยน Cloud runtime ให้ทำเมื่อเจ้าของอนุมัติ; บัญชีอ่านอย่างเดียวให้บันทึกว่ายังไม่ได้ทดลอง

   ~~~text
   อยากเช็กว่าข้อมูลยังอยู่ไหมหลังเปิด API ใหม่ ช่วยวางแผน restart เฉพาะ revision ของ app ฝึกที่กำลังให้บริการอยู่
   บอก subscription, resource group, app, revision และสิ่งที่ผู้ใช้อาจเจอระหว่างรอ
   ใช้ image, traffic, secrets และฐานข้อมูลชุดเดิม ขอให้ฉันยืนยันก่อนลงมือ
   ~~~

7. เมื่อตรวจเป้าหมายและอนุมัติแล้ว ส่ง prompt ให้ทำและตรวจข้อมูลเดิม

   ~~~text
   เปิดใหม่เฉพาะ revision ตามแผนที่ฉันเพิ่งอนุมัติได้เลย
   พอพร้อมและเช็ก /health แล้วบอกผลโดยไม่แสดง secrets ฉันจะล็อกอินไปค้น UUID เดิมเอง
   ถ้าฉันหารายการไม่เจอ ให้จดผลตามจริงและเก็บฐานข้อมูลไว้ตามเดิม
   ช่วยเล่าสั้น ๆ ด้วยว่าการเปิดรุ่นเดิมใหม่ต่างจาก rollback ยังไง
   ~~~

8. Login ใหม่ใน Android หรือ `/docs` แล้วอ่าน UUID ที่จดไว้. อภิปรายกับผู้สอน: หากต้องกลับรุ่นเดิมต้องเลือก image tag ที่รู้ว่าทำงานได้, deploy revision และตรวจอีกครั้ง; secret ที่แก้ต้อง restart revision หรือสร้าง revision ใหม่จึงนำไปใช้ ไม่ทดลอง rollback/traffic switching ในขั้นนี้

**Checkpoint:** ชี้ 404 ใน log พร้อม revision/image และอ่านข้อมูลเดิมหลัง restart ได้; ขั้นใดไม่ได้ทดลองให้ระบุสถานะตามจริง

## Practice 3 — ส่งมอบหลักฐานและวางแผนปิด lab

<PracticeIllustration asset="d04-e04-p03" />

**Primary target:** สรุปความพร้อมของต้นแบบและการจัดการ resources หลังเรียนได้

### Steps

1. เปิด `docs/review-log.md` เติมหลักฐาน 4 วัน: PR, tests, persistence UUID, Android, image SHA/revision. ช่องที่ยังไม่ผ่านให้คงสถานะจริง
2. ส่ง prompt ให้ Codex ช่วยสรุปจากหลักฐาน

   ~~~text
   ช่วยสรุปต้นแบบให้เพื่อนอ่านแล้วรู้ว่าเราลองอะไรแล้ว ผลเป็นยังไง อะไรยังไม่ได้ลอง และต้องทำอะไรเพิ่มก่อนใช้ในบริษัท
   ใช้หลักฐานจาก docs/review-log.md และ docs/project-brief.md เท่านั้น ถ้าขาดหลักฐานให้บอกตามจริง
   ระบุว่าเป็นสถานะต้นแบบในห้องเรียน และใส่เฉพาะข้อมูลที่แชร์ได้
   ~~~

3. ให้ Codex อ่านรายการ resources เพื่อทำแผนค่าใช้จ่าย/cleanup แล้วบันทึกเจ้าของและวันที่ตั้งใจปิด lab

   ~~~text
   ก่อนจบ lab ช่วยดูว่ามีทรัพยากรอะไรบ้างใน resource group ที่ฉันยืนยัน ให้เจ้าของใช้ทบทวนก่อนปิด
   ชี้ว่าตัวไหนยังอาจมีค่าใช้จ่าย เช่น ACR หรือ database แม้แอปตั้ง min replicas เป็น 0
   ใช้ข้อมูลที่ตรวจได้โดยไม่เดายอด รอบนี้ขอแค่รายการสำหรับทบทวน
   ~~~

4. ถ้าเจ้าของต้องการลบ ให้ตรวจรายการและยืนยันแยกครั้งนั้น. ไม่ลบ PostgreSQL/server/database เดิมหรือ resource group ที่มีงานจริง และไม่ใส่ cleanup อัตโนมัติใน workflow
5. เล่าให้เพื่อนฟังหนึ่งอย่างที่ Codex ช่วยเร็วขึ้น และหนึ่งอย่างที่ต้องตรวจด้วยตนเอง ถ้า core ครบและยังมีเวลา เปิด [change request](/resources/change-request) เป็นโจทย์ต่อยอดภายหลัง

**Checkpoint:** มีหลักฐานที่อ่านตามได้, งานค้าง และเจ้าของค่าใช้จ่าย/cleanup ชัดเจน
