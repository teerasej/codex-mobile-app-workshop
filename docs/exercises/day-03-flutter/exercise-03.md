---
title: "Day 3 · Exercise 3 — เชื่อม API กับงานของผู้ใช้"
prev: {"text": "Exercise 2", "link": "/exercises/day-03-flutter/exercise-02"}
next: {"text": "Exercise 4", "link": "/exercises/day-03-flutter/exercise-04"}
---

# Exercise 3 — เชื่อม API กับงานของผู้ใช้

> **Day 3 · Flutter · 13:00–14:30**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-03-flutter/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice

## Scenario

หน้าจอจากช่วงเช้ายังเป็นข้อมูลตัวอย่าง ตอนนี้เราจะ Sign in แล้วใช้ข้อมูลจาก API Day 2 แทน โดยใช้ model และหน้าจอเดิม

**Dio** เหมือนพนักงานส่งเอกสาร: ส่งคำขอไปยัง API แนบป้ายผู้ส่ง และแจ้งเมื่อส่งไม่สำเร็จ ส่วนหน้าจอมีหน้าที่บอกว่ากำลังรอ ได้ข้อมูลแล้ว หรือควรลองใหม่

> **Package:** Dio รองรับ web/Android/iOS และไม่ต้องซื้อ paid license เพิ่ม ใช้สิทธิ์ Codex ตามภาพรวม Day 3

## ก่อนเชื่อมข้อมูลจริง

1. ส่ง prompt ให้เปิด API แยกจาก Flutter โดยไม่แก้โค้ดหรือข้อมูล

   ~~~text
   เปิด API Day 2 ให้หน่อย โดยไม่แก้โค้ดหรือข้อมูล
   ดู docs/api-contract.md ก่อนว่า API มี login, การป้องกันข้อมูลรายคน, PostgreSQL และ /health ที่อ่าน APP_VERSION (ค่าเริ่มต้น v1) ครบไหม ถ้าขาดอะไรให้บอกแล้วหยุด
   ใช้ Python ใน .venv เดิมและ api/.env เดิม ถ้า .venv ไม่พร้อมให้หยุดถาม อย่าสร้างหรือติดตั้งใหม่เอง
   รัน API ค้างไว้ใน terminal แยก ที่ 127.0.0.1:8000 ถ้าพอร์ตไม่ว่างให้เช็คก่อนว่าเป็น API ของเราไหม อย่าปิดอย่างอื่น
   อย่าพิมพ์ password/token หรือ seed/reset database
   เสร็จแล้วบอก URL ของ /health กับ /docs และวิธีหยุดเฉพาะ API ที่เปิดครั้งนี้
   ~~~

2. เปิด `/health` และ `/docs` ใน Edge ใช้บัญชีทดลองจาก Day 2 ตรวจดังนี้ ไม่ส่ง password/token เข้า chat

   - `/health` ได้ `200` และ version ตรงกับ `APP_VERSION` ที่ใช้
   - เปิด **Authorize** ถ้ามีบัญชีค้างจาก Day 2 ให้กด **Logout** แล้วปิดกล่อง จากนั้นเรียก `GET /requests` โดยยังไม่ลงชื่อเข้าใช้ ต้องได้ `401`
   - เข้าเป็นบัญชีทดลองแรกจาก Day 2 แล้วอ่าน Request ของตนได้ จด UUID หนึ่งรายการ
   - เปลี่ยนเป็นบัญชีทดลองที่สอง แล้วอ่าน UUID นั้นต้องได้ `404`
   - ตรวจหลักฐาน Day 2 ว่า Request เดิมยังอยู่หลัง restart API หากยังไม่มี ให้กลับไปตรวจ persistence ก่อน

   > ถ้าไม่มี auth/ownership ให้กลับ [Day 2 · Exercise 4](/exercises/day-02-api/exercise-04); ถ้าข้อมูลหายหลัง restart ให้กลับ [Day 2 · Exercise 3](/exercises/day-02-api/exercise-03) ไม่แก้ Flutter ให้ข้ามข้อกำหนดเหล่านี้ ช่วงเช้าที่ใช้ fixture ยังเก็บไว้ได้

ถ้าส่วนอื่นผ่าน แต่ `/health` ยังคืน `v1` แบบเขียนค่าคงที่ ให้ส่ง prompt นี้แก้เฉพาะการรายงานรุ่น เพื่อใช้ตามรอย deployment ใน Day 4 แล้วตรวจจุดเริ่มอีกครั้ง

~~~text
แก้ /health ให้อ่านเลข version จาก APP_VERSION (ถ้าไม่ตั้งใช้ v1) แค่นี้พอ
อย่าแสดง config หรือ secrets อื่น และอย่ายุ่งกับ login, database, routes อื่นหรือ .env
เพิ่ม test ว่าตั้งค่าแล้วได้ค่านั้น ไม่ตั้งแล้วได้ v1 โดยไม่ต่อ database จริง
แสดง diff แล้วรัน test ถ้าผ่านให้ restart เฉพาะ API ที่เราเปิดไว้ แล้วบอกให้ฉันเช็ค /health อีกรอบ
~~~

## Practice 1 — Sign in แล้วโหลด Request ของตน

<PracticeIllustration asset="d03-e03-p01" eager />

**Primary target:** ใช้ Dio เปิดรายการของผู้ใช้จาก authenticated API ได้

### Steps

1. ส่ง prompt ให้ติดตั้งตัวช่วยส่งคำขอเฉพาะใน Flutter project

   ~~~text
   เพิ่ม dio ให้แอปใน client/ แล้วสรุปให้ดูว่าได้ version อะไร และ pubspec เปลี่ยนตรงไหน
   ~~~

2. สร้างบริการกลางก่อน เพื่อให้ทุกหน้าคุยกับ API ด้วยวิธีเดียวกัน

   ~~~text
   อ่าน docs/api-contract.md แล้วสร้าง ApiService เป็นตัวกลางเดียวที่ทุกหน้าใช้คุยกับ API
   ใช้ Dio ตัวเดียว ตั้ง timeout 10 วินาที และอ่าน base URL จาก API_BASE_URL ถ้าไม่ได้ตั้งไว้ให้บอกวิธีตั้งแล้วอย่าส่ง request
   ใช้ model เดิม ไม่ต้องสร้างหน้าหรือ model ใหม่ แล้วแสดง diff
   ~~~

3. เพิ่ม Sign in และใช้บริการกลางนี้กับหน้ารายการ/รายละเอียดเดิม

   ~~~text
   เพิ่มหน้า Sign in ผ่าน ApiService ตาม contract แล้วให้หน้ารายการและรายละเอียดเดิมดึงข้อมูลจริงจาก API แทน fixture (fixture เก็บไว้ใช้ใน test)
   เก็บ token ไว้ใน memory เท่านั้น และแนบไปกับทุก request ที่ต้อง login
   รหัสผ่านผิดให้บอกและลองใหม่ได้ ถ้า token หมดอายุหรือ logout ให้ล้างข้อมูลเก่าแล้วกลับหน้า Sign in
   ถ้า API error ให้โชว์ข้อความที่คนอ่านเข้าใจ ห้าม log password/token
   แสดง diff
   ~~~

4. ให้ browser เรียก API ได้จาก origin ที่กำหนด แล้วเริ่ม run ใหม่

   ~~~text
   ให้ browser ที่เปิดจาก http://localhost:3000 เรียก API ได้ โดยตั้ง CORS ให้ตรงกับ docs/api-contract.md ไม่เปิดให้ทุก origin
   แสดง diff ของ API แยกจาก client แล้ว restart เฉพาะ API ที่เราเปิดไว้
   จากนั้นรันแอปใหม่บน Edge ที่ localhost:3000 โดยต่อ API ที่ http://127.0.0.1:8000
   ถ้ารันบน Mac ให้บอก URL ที่ต้องเปิดเอง อย่าปิด process อื่นและอย่าแสดง secrets
   ~~~

5. เปิดแอปใน Edge ลอง password ผิดหนึ่งครั้ง ต้องมีข้อความและลองใหม่ได้ จากนั้นใส่รหัสผ่านจริงด้วยตนเอง โดยใช้ **Username** นี้

   ~~~text
   learner01
   ~~~

   เทียบ UUID/title กับ `GET /requests` ใน `/docs` ของผู้ใช้เดียวกัน จำนวนอาจเกิน 3 เพราะเพิ่มข้อมูลจาก Day 2 แล้ว ไม่เทียบจำนวนกับ fixture ช่วงเช้า

6. **Logout** แล้ว Sign in เป็นผู้ใช้ต่อไปนี้ ต้องเห็นเฉพาะข้อมูลของเขา ไม่มีรายการของผู้ใช้เดิมค้าง

   ~~~text
   learner02
   ~~~

**Checkpoint:** Sign in ผิดแล้วลองใหม่ได้ Dio โหลดข้อมูลจริง และเปลี่ยนผู้ใช้แล้วรายการตรงกับเจ้าของโดยไม่มีข้อมูลเดิมค้าง

## Practice 2 — ส่ง Request และติดตามสถานะจากหน้าจอ

<PracticeIllustration asset="d03-e03-p02" />

**Primary target:** ทำวงจรสร้าง Request ถึงอัปเดตสถานะผ่าน API ได้

### Steps

1. ส่ง prompt เพิ่มแบบฟอร์มและการเปลี่ยนสถานะ โดยใช้บริการเดิม

   ~~~text
   เพิ่มหน้าสร้าง Request (title, description, category) พร้อมเช็คข้อมูลตาม docs/api-contract.md ส่งผ่าน ApiService เดิม
   กดส่งแล้วปิดปุ่มกันกดซ้ำ สำเร็จให้กลับหน้ารายการและโหลดใหม่จาก API
   ในหน้ารายละเอียดเพิ่มการเปลี่ยนสถานะตาม contract
   ถ้าข้อมูลผิดให้โชว์ข้อความใกล้ช่องนั้น ห้ามนับว่าสำเร็จ
   ไม่ต้องแก้ API แล้วแสดง diff
   ~~~

2. Sign in เป็น `learner01` กดปุ่มสร้าง Request แล้วกรอกตัวอย่างนี้

   - **Title**

     ~~~text
     ทดสอบส่งจาก Flutter
     ~~~

   - **Description**

     ~~~text
     ทดลองสร้างใบงานจากหน้าจอ Flutter และตรวจสถานะกับ API
     ~~~

   - **Category** — เลือกค่าต่อไปนี้จากรายการ

     ~~~text
     it
     ~~~

3. กดส่งหนึ่งครั้ง เปิดรายการที่เพิ่งสร้างแล้วจด UUID เปิด `/docs` ด้วยบัญชีเดียวกันเพื่อตรวจ UUID นี้
4. ในแอปเปลี่ยนสถานะตามลำดับ แล้วตรวจสถานะเดียวกันใน `/docs`

   1. เปลี่ยนเป็น

      ~~~text
      in_progress
      ~~~

   2. จากนั้นเปลี่ยนเป็น

      ~~~text
      done
      ~~~

5. Refresh browser แล้ว Sign in ใหม่ เพราะ token เก็บใน memory เปิด UUID เดิม ต้องยังเป็น `done`
6. ลองสร้างอีกครั้งโดยเว้น Title ว่าง ต้องเห็นข้อความใกล้ช่องและไม่มีรายการใหม่

**Checkpoint:** UI กับ API มี UUID/status เดียวกัน หนึ่งการกดไม่เพิ่มรายการซ้ำ และข้อมูลผิดไม่ถูกส่งสำเร็จ

## Practice 3 — บอกผู้ใช้เมื่อกำลังรอหรือเกิดปัญหา

<PracticeIllustration asset="d03-e03-p03" />

**Primary target:** แสดง UI states ที่สะท้อนผลการเรียก API จริงได้

### Steps

1. ส่ง prompt เตรียม states และตรวจกรณีที่ทำให้เกิดด้วยมือได้ยาก

   ~~~text
   ทำให้หน้ารายการบอกผู้ใช้ได้ชัดว่ากำลังโหลด, ว่างเปล่า, เกิดปัญหา (มีปุ่ม Retry) หรือโหลดสำเร็จ
   Retry/Refresh ให้โหลดรายการใหม่เท่านั้น ห้ามส่ง POST ซ้ำ
   เขียน test จำลองทั้ง 4 สถานะ รวมกรณีเน็ตหลุดและ timeout โดยไม่ต้องต่อ API จริง
   รัน test แล้วสรุปผล และห้ามลบข้อมูลใน database เพื่อทำให้รายการว่าง
   ~~~

2. ในแอป Sign in แล้วอยู่หน้า **My requests** ที่โหลดสำเร็จ ส่ง prompt นี้เพื่อหยุด API ของเรา

   ~~~text
   ช่วยหยุด API ที่เราเปิดไว้ในแบบฝึกหัดนี้ แต่ให้แอป Flutter รันต่อ
   อย่าปิดอย่างอื่นและอย่าแก้ไฟล์หรือข้อมูล
   ~~~

3. ในแอปกด **Refresh** ต้องเห็น error กับ **Retry** แทนหน้าขาวหรือหมุนไม่จบ อย่า Refresh ทั้ง browser เพราะจะล้าง token
4. ส่ง prompt ให้เปิด API กลับ แล้วกลับมาที่แอปกด **Retry**

   ~~~text
   เปิด API กลับเหมือนเดิม โดยไม่ seed/reset database และไม่ต้อง restart Flutter
   บอกฉันเมื่อ /health พร้อมใช้งาน
   ~~~

   ต้องเห็นข้อมูลกลับมา หาก token หมดอายุ ให้ Sign in ใหม่แล้วตรวจ UUID เดิม

**Checkpoint:** tests แสดง loading/empty/error/success และในแอปจริงหยุด API → error → เปิด API → Retry แล้วใช้งานต่อได้

**ถ้าติดขัด:** `/docs` ได้แต่ browser error ให้ตรวจ origin/port/CORS; `401` ให้ตรวจ token lifecycle; `422` ให้ตรวจ schema ถ้าเชื่อมไม่ได้ตรวจ API run ก่อนแก้ UI ไม่เปิด allow-all หรือใส่ database password ใน Flutter

อ่านเพิ่ม: [Dio: form, JSON และ errors](https://pub.dev/packages/dio), [Dio receiveTimeout](https://pub.dev/documentation/dio/latest/dio/Options/receiveTimeout.html), [Flutter web setup](https://docs.flutter.dev/platform-integration/web/setup), [Flutter: ทดสอบด้วย dependencies จำลอง](https://docs.flutter.dev/cookbook/testing/unit/mocking)
