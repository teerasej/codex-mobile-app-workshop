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

API เปิดแล้ว เราต้องพิสูจน์จากมุมผู้ใช้จริงและรู้ว่าจะดูอะไรเมื่อเกิดปัญหา

## Practice 1 — ใช้ Android กับ HTTPS API

<PracticeIllustration asset="d04-e04-p01" eager />

**Primary target:** ส่งคำขอจาก Android ไปถึง API บน Azure ได้

### Steps

1. หยุด local API/container. นี่ช่วยยืนยันว่า app ไม่ได้เผลอเรียกเครื่องเดิม
2. จาก client ให้เปิด browser preview ด้วย URL ที่ได้จริง:

   ~~~shell
   flutter run -d chrome --web-hostname localhost --web-port 3000 --dart-define=API_BASE_URL=https://<APP_FQDN>
   ~~~
3. Login และสร้างคำขอหนึ่งรายการ. ถ้า browser CORS ล้ม ตรวจ origin localhost:3000 กับค่าใน Container App; อย่าใส่ API URL เป็น allowed frontend origin
4. หยุด browser previewแล้วรัน Android และ build APK ใหม่:

   ~~~shell
   flutter run -d <FLUTTER_DEVICE_ID> --dart-define=API_BASE_URL=https://<APP_FQDN>
   flutter build apk --debug --dart-define=API_BASE_URL=https://<APP_FQDN>
   ~~~

   ให้จบ flutter run ก่อนสั่ง build. Android HTTPS path นี้ไม่ต้องใช้ adb reverse
5. ใส่รหัสผ่านเอง สร้าง **คำขอจาก Android บน Cloud** และตรวจ UUID/status ใน /docs. Logout/login ใหม่ต้องพบรายการเดิม
6. บันทึก APK path และ API host ที่ build ใช้. APK debug นี้สำหรับฝึก ไม่ใช่ signed release หรือ store publication

**Checkpoint:** local API ปิดอยู่ แต่ Android ยังสร้าง/อ่านคำขอได้ผ่าน HTTPS

## Practice 2 — อ่าน Log และ Revision เพื่อตรวจปัญหา

<PracticeIllustration asset="d04-e04-p02" />

**Primary target:** ใช้หลักฐานของ revision ที่กำลังทำงานอธิบายอาการ API ได้

### Steps

1. ให้ Codex แสดง revision list และ latest ready revision เฉพาะ app นี้. จดชื่อ active revision และ image
2. เปิด **Log stream** ของ app หรือใช้คำสั่งอ่าน log โดยจำกัด output:

   ~~~shell
   az containerapp logs show --name <APP_NAME> --resource-group <LAB_RG> --type console --tail 30
   ~~~
3. ใน /docs เรียก GET UUID ที่ไม่มีอยู่ด้วย valid token เพื่อให้ได้ 404. เทียบเวลา/path/status ใน log โดยไม่พิมพ์ token
4. ใน app settings ตรวจ CPU=0.25 vCPU, memory=0.5Gi, min replicas=0/max=1 และ cold start ตามแผนค่าใช้จ่าย. Environment ใช้ Consumption-only ไม่มี Log Analytics; ใช้ Log stream ที่เปิดระหว่างทดสอบ ไม่คาดหวังประวัติ log ที่จัดเก็บระยะยาว. ไม่ใช้ load test หรือเพิ่มขนาดโดยไม่ให้เจ้าของทบทวนแผน
5. หลังจด UUID ที่เพิ่งสร้าง ให้ restart เฉพาะ active revision ของ app ฝึก:

   ~~~shell
   az containerapp revision restart --revision <ACTIVE_REVISION_NAME> --resource-group <LAB_RG>
   ~~~
6. รอ ready, login ใหม่ แล้วค้น UUID เดิม. ให้ Codex อธิบายว่า restart ไม่ใช่ rollback และการเปลี่ยน secret อาจต้อง restart active revision เพื่อใช้ค่าใหม่
7. อภิปราย fallback รุ่นก่อน: ต้องเลือก **image tag ที่รู้ว่าทำงานได้**, deploy เป็น revision ใหม่และทดสอบอีกครั้ง. ไม่สลับ traffic หรือ rollback จริงโดยไม่ระบุเป้าหมายและผลต่อผู้ใช้

**Checkpoint:** ชี้ log ของ 404, revision/image ที่กำลังใช้ และข้อมูลที่ยังอยู่หลัง restart ได้

## Practice 3 — ส่งมอบหลักฐานและวางแผนปิด lab

<PracticeIllustration asset="d04-e04-p03" />

**Primary target:** สรุปความพร้อมของต้นแบบและการจัดการ resources หลังเรียนได้

### Steps

1. เปิด docs/review-log.md เติมหลักฐาน 4 วัน: PR, tests, persistence UUID, Android, image SHA/revision. ช่องที่ยังไม่ผ่านให้คงสถานะจริง
2. ส่ง prompt:

   ~~~text
   อ่านเฉพาะ docs/review-log.md และ docs/project-brief.md
   สรุปสิ่งที่ทดสอบจริง สิ่งที่ยังไม่ทดสอบ และสิ่งที่ต้องทำก่อนใช้ในบริษัท
   แยก classroom prototype ออกจาก production readiness
   ไม่แต่งผล test และไม่เปิด secrets
   ~~~
3. ให้ Codex list resources **เฉพาะ lab resource group** และแสดงค่าใช้จ่ายที่ยังอาจเกิด เช่น ACR/database/logs. บันทึกเจ้าของและวันที่ตั้งใจปิด lab
4. ถ้าเจ้าของต้องการลบ ให้ตรวจรายการก่อนและขอการยืนยันเฉพาะครั้งนั้น. ห้ามลบ PostgreSQL server/database เดิมหรือ resource group ที่ปนงานจริง. ไม่ใส่คำสั่งลบอัตโนมัติใน workflow
5. สรุปกับเพื่อน: หนึ่งอย่างที่ Codex ช่วยเร็วขึ้น และหนึ่งอย่างที่เราต้องตรวจเองเสมอ
6. ถ้า core ครบและยังมีเวลา เปิด [change request](/resources/change-request) เป็นโจทย์ต่อยอดภายหลัง. ไม่เบียดเวลาตรวจ Android/Cloud ที่ยังไม่ผ่าน

**Checkpoint:** มีหลักฐานที่อ่านตามได้ รายการงานค้าง และผู้รับผิดชอบค่าใช้จ่าย/cleanup ชัดเจน
