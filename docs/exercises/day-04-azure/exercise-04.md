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
   หยุดเฉพาะ local API/container และ Flutter preview เดิมของโปรเจคนี้
   ตรวจว่า HTTPS API URL ที่ฉันยืนยันไม่ใช่ localhost หรือ 127.0.0.1
   จาก client/ เปิด Flutter ด้วย API_BASE_URL เป็น HTTPS origin นี้ผ่าน dart-define
   Windows ใช้ Edge device; macOS ใช้ web-server แล้วให้ฉันเปิด Microsoft Edge เอง
   คง web-hostname localhost และ web-port 3000 บอก URL ที่ฉันต้องเปิด
   ไม่แก้ Azure หรือเพิ่ม API URL เข้า CORS origins
   ~~~

2. ใน Edge เปิด preview ตาม URL ที่ Codex แจ้ง. Login ด้วย app user ของตนแล้วสร้าง Request สมมติหนึ่งรายการ. ถ้า CORS ล้ม ให้เทียบ **frontend origin** กับ CORS ของ API

   ~~~text
   http://localhost:3000
   ~~~

   CORS_ORIGINS ต้องมี frontend origin นี้ ไม่ใช่ Application URL ของ API. ให้ผู้สอนตรวจแผนก่อนแก้ Cloud config

3. ขอให้ Codex สลับไป Android ที่เตรียมไว้แล้ว โดยใช้ HTTPS origin เดิม

   ~~~text
   หยุด Flutter browser preview ของโปรเจคนี้ แล้วตรวจ Android device ที่พร้อม
   ถ้ามีหลายเครื่องให้แสดงชื่อ/device ID เพื่อให้ฉันเลือก ไม่เดาอุปกรณ์
   จาก client/ รันแอปบน Android ด้วย API_BASE_URL เป็น HTTPS origin เดิมผ่าน dart-define
   local API ต้องยังปิดอยู่ เส้นทาง HTTPS นี้ไม่ต้องใช้ adb reverse
   ไม่ใส่ password/token ในคำสั่งหรือ log
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
   หยุด flutter run ของโปรเจคนี้ก่อน แล้ว build Android debug APK จาก client/
   ใช้ API_BASE_URL เป็น HTTPS origin เดิมผ่าน dart-define
   บอก APK path และ API host ที่ใช้ build พร้อมผลสำเร็จหรือ error
   ไม่ทำ signed release หรือส่งขึ้น store
   ~~~

   บันทึก APK path และ API host ใน review log. `dart-define` ต้องใส่ตอน build ใหม่ด้วย; APK เก่าจะไม่เปลี่ยน URL ตามการรันครั้งล่าสุดเอง

**Checkpoint:** local API ปิดอยู่ แต่ Android ยังสร้าง/อ่าน Request ผ่าน HTTPS ได้ และ APK ใช้ API host ที่ตรวจแล้ว

## Practice 2 — อ่าน Log และ Revision เพื่อตรวจปัญหา

<PracticeIllustration asset="d04-e04-p02" />

**Primary target:** ใช้หลักฐานของ revision ที่กำลังทำงานอธิบายอาการ API ได้

### Steps

1. ใน Edge เปิด Container App ของตน → หน้ารายการ revision (`Revisions and replicas` หรือ `Revision management` ตามหน้าจอ) → เลือก revision ที่พร้อมและรับ traffic. ตรวจชื่อ revision กับ image แล้วขอ Codex ยืนยันแบบอ่านอย่างเดียว

   ~~~text
   ตรวจเฉพาะ Container App ของ lab นี้แบบอ่านอย่างเดียว
   แสดง revision ที่พร้อมและกำลังรับ traffic พร้อมชื่อ image/full tag
   แยก latest revision ออกจาก revision ที่ให้บริการจริงถ้าไม่ใช่ตัวเดียวกัน
   ไม่ update, restart หรือเปลี่ยน traffic
   ~~~

2. เปิด `Monitoring` → `Log stream` ของ app → เลือก `Console` → เลือก revision/replica/container ที่กำลังใช้. เปิด stream ค้างไว้ แล้วเปิด `/docs` ใน Edge อีกแท็บ. หากใช้ Codex ดู log แทน ให้ส่ง prompt นี้

   ~~~text
   เปิด console log stream ของ revision/replica/container ที่เราเพิ่งตรวจ
   ใช้ follow และ tail ไม่เกิน 30 บรรทัด ไม่พิมพ์ environment หรือ secrets
   เปิดค้างไว้ระหว่างที่ฉันทดสอบ request แล้วรอฉันบอกให้หยุด
   ~~~

   คำสั่งอ้างอิง; ถ้ามีหลาย revision ให้ Codex ระบุ revision/replica/container ที่ตรงกันเพิ่ม:

   ~~~shell
   az containerapp logs show --name <APP_NAME> --resource-group <LAB_RG> --type console --tail 30 --follow
   ~~~

3. ใน `/docs` กด `Authorize` ด้วย user เดิม เลือก `GET /requests/{id}` → `Try it out`. ใช้ UUID ที่ไม่มีในข้อมูลของตน เช่นค่าด้านล่าง → `Execute`. ต้องได้ 404 แล้วกลับไป stream เทียบเวลา, path และ status โดยไม่คัดลอก token

   ~~~text
   00000000-0000-4000-8000-000000000000
   ~~~

4. ตรวจ resource settings ว่า CPU=0.25 vCPU, memory=0.5Gi, min replicas=0/max=1 ตรงแผน. Environment ของ lab ใช้ Consumption-only และไม่เก็บ Log Analytics; จึงดู stream ระหว่างทดสอบและอาจเจอ cold start หลังไม่มีคนเรียก ไม่เพิ่มขนาดหรือทำ load test ในขั้นนี้
5. หยุด stream เมื่อพบหลักฐานแล้ว. ถ้า Codex เปิดให้ ให้ส่งข้อความนี้

   ~~~text
   หยุดเฉพาะการติดตาม log ที่เปิดไว้เมื่อครู่
   เก็บสรุปเวลา/path/status ของ 404 และชื่อ revision โดยไม่คัดลอก token
   ~~~

6. จด UUID ที่สร้างใน Practice 1 แล้วขอแผน restart **เฉพาะ revision ของ app ฝึก**. Restart เป็นการเปลี่ยน Cloud runtime ให้ทำเมื่อเจ้าของอนุมัติ; บัญชีอ่านอย่างเดียวให้บันทึกว่ายังไม่ได้ทดลอง

   ~~~text
   แสดงแผน restart เฉพาะ active revision ที่เราเพิ่งตรวจของ app ฝึกนี้
   ระบุ subscription/resource group/app/revision และผลกระทบชั่วคราว
   ไม่เปลี่ยน image, traffic, secrets หรือ database รอฉันยืนยันก่อนทำ
   ~~~

7. เมื่อตรวจเป้าหมายและอนุมัติแล้ว ส่ง prompt ให้ทำและตรวจข้อมูลเดิม

   ~~~text
   restart เฉพาะ revision ตามแผนที่ฉันเพิ่งอนุมัติ แล้วรอพร้อม
   ตรวจ health โดยไม่เปิด secrets และให้ฉัน login ใหม่เพื่อค้น UUID เดิมด้วยตนเอง
   ไม่ seed หรือสร้างข้อมูลชดเชยถ้าหารายการเดิมไม่พบ
   อธิบายสั้น ๆ ว่า restart ต่างจาก rollback อย่างไร
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
   อ่านเฉพาะ docs/review-log.md และ docs/project-brief.md
   สรุปสิ่งที่ทดสอบจริง สิ่งที่ยังไม่ทดสอบ และสิ่งที่ต้องทำก่อนใช้ในบริษัท
   แยก classroom prototype ออกจาก production readiness
   ไม่แต่งผล test และไม่เปิด secrets
   ~~~

3. ให้ Codex อ่านรายการ resources เพื่อทำแผนค่าใช้จ่าย/cleanup แล้วบันทึกเจ้าของและวันที่ตั้งใจปิด lab

   ~~~text
   แสดง resources เฉพาะ lab resource group ที่ฉันยืนยันแบบอ่านอย่างเดียว
   สรุปรายการที่ยังอาจมีค่าใช้จ่าย เช่น ACR/database โดยไม่เดายอดเงินจริง
   ระบุว่า min replicas 0 ไม่ทำให้ทุกบริการไม่มีค่าใช้จ่าย
   เตรียมรายการให้เจ้าของทบทวน cleanup ยังไม่ลบหรือแก้ resource ใด
   ~~~

4. ถ้าเจ้าของต้องการลบ ให้ตรวจรายการและยืนยันแยกครั้งนั้น. ไม่ลบ PostgreSQL/server/database เดิมหรือ resource group ที่มีงานจริง และไม่ใส่ cleanup อัตโนมัติใน workflow
5. เล่าให้เพื่อนฟังหนึ่งอย่างที่ Codex ช่วยเร็วขึ้น และหนึ่งอย่างที่ต้องตรวจด้วยตนเอง ถ้า core ครบและยังมีเวลา เปิด [change request](/resources/change-request) เป็นโจทย์ต่อยอดภายหลัง

**Checkpoint:** มีหลักฐานที่อ่านตามได้, งานค้าง และเจ้าของค่าใช้จ่าย/cleanup ชัดเจน
