---
title: "Day 3 · Exercise 4 — Native plugin และ mobile build"
prev: {"text": "Exercise 3", "link": "/exercises/day-03-flutter/exercise-03"}
next: {"text": "สรุปท้ายวัน", "link": "/exercises/day-03-flutter/summary"}
---

# Exercise 4 — Native plugin และ mobile build


> **Day 3 · Flutter · 14:45–16:00**
>
> อ่าน [ภาพรวมและเงื่อนไขของวันนี้](/exercises/day-03-flutter/) ก่อนเริ่ม ใช้โฟลเดอร์ `service-desk-lite` เดิม และทำทีละ Practice


## Scenario

หน้าจอใน browser ผ่านแล้ว เราจะสร้างไอคอนสำหรับหน้าแอปของ Android เพิ่มปุ่มเปิดคู่มือ แล้วลองทั้งสองอย่างบน Android หากใช้ Mac ที่เตรียมพร้อมและผ่านกิจกรรมหลักแล้ว มี Practice เสริมให้เปิดแอปเดิมใน iPhone Simulator

ใช้ `ApiService` และ Dio จาก Exercise 3 ต่อทั้ง web และ mobile โดยให้ Dio เลือก adapter ตามแพลตฟอร์ม เปลี่ยนเฉพาะวิธีรัน ไม่สร้างแอปใหม่

## Practice 1 — สร้างภาพและใช้เป็นไอคอนแอป Android {#android-app-icon}

<PracticeIllustration asset="d03-e04-app-icon" eager />

**Primary target:** ใช้ภาพที่สร้างเองเป็นไอคอนสำหรับเปิด Service Desk Lite บน Android ได้

### Steps

1. ไอคอนเหมือนป้ายหน้าร้าน ควรมองออกแม้เห็นในขนาดเล็ก เปิด ChatGPT บนเว็บแล้วส่ง prompt นี้ในแชต ดูเพิ่มที่ [วิธีสร้างและดาวน์โหลดภาพด้วย ChatGPT Images](https://help.openai.com/en/articles/11084440-images-in-chatgpt)

   ~~~text
   สร้างภาพไอคอนสำหรับแอปแจ้งคำขอบริการชื่อ Service Desk Lite
   ให้เป็นภาพสี่เหลี่ยมจัตุรัส มีสัญลักษณ์รูปใบคำขอบริการแบบเรียบ ๆ อยู่ตรงกลาง ขนาด 2048x2048 pixel
   ใช้พื้นหลังสีทึบและเว้นขอบ เพื่อให้เห็นสัญลักษณ์เมื่อย่อหรือตัดมุม
   ไม่ใส่ข้อความ ตัวเลข โลโก้บริษัท หรือลายน้ำ
   ~~~

2. ใช้ prompt ด้านล่างในการบอกให้ Codex ช่วยสร้างไฟล์ขนาดที่เหมาะสมสำหรับแอพ Android และวางลงใน flutter project ให้หน่อย

   ~~~text
   แปลงไฟล์ภาพนี้ ให้มีขนาดที่เหมาะสมสำหรับนำไปใช้กับ Flutter Android ใน client/ ให้หน่อย
   ~~~

3. เปิดโปรเจกต์เดิมใน Codex แล้วส่ง prompt นี้เพื่อสร้างไอคอนหลายขนาดจากภาพเดียว

   ~~~text
   ขอรายชื่อไฟล์ภาพ ไฟล์ตั้งค่า และ Android launcher resources ที่เปลี่ยน เก็บ web, iOS และการตั้งค่า API ไว้ตามเดิม
   ~~~

4. เปิดไฟล์ไอคอนใน `client/android/app/src/main/res/` ตามที่ Codex รายงาน เทียบกับ PNG ต้นฉบับ แล้วเก็บโปรเจกต์นี้ไว้ใช้ต่อใน Practice 2 และ 3

**Checkpoint:** มี PNG ต้นฉบับและไฟล์ launcher icon ของ Android ที่ตรงกับภาพนั้น เตรียมตรวจไอคอนจากแอปที่ติดตั้งจริงใน Practice 3

อ่านเพิ่มได้ที่ [Flutter Launcher Icons](https://pub.dev/packages/flutter_launcher_icons)

## Practice 2 — เปิดคู่มือด้วย plugin {#practice-1-—-เปิดคู่มือด้วย-plugin}

<PracticeIllustration asset="d03-e04-p01" />

**Primary target:** ใช้ Flutter plugin เรียกความสามารถของแพลตฟอร์มและจัดการกรณีเปิดไม่สำเร็จได้

### Steps

1. Plugin เหมือนยืมความสามารถของเครื่องแทนเขียนเองทั้งหมด ส่ง prompt ให้เพิ่ม package ใน client เดิม

   ~~~text
   อยากให้แอปเปิดคู่มือบนเว็บได้ ช่วยเพิ่ม url_launcher ให้แอปเดิมใน client/ ก่อน
   ~~~

   `url_launcher` 6.3.3 ที่ใช้ตรวจเอกสารรองรับ Android SDK 24+ และ iOS 13.0+ รุ่นที่ติดตั้งจริงให้ดู lockfile และ pub.dev ไม่เดารุ่นจากตัวอย่างนี้

2. ส่ง prompt ให้เพิ่มปุ่มในหน้าที่มีอยู่

   ~~~text
   อยากให้หลังล็อกอินมีปุ่ม “คู่มือ Flutter” พอกดแล้วจะเปิด https://docs.flutter.dev
   ถ้าเปิดไม่ได้ ให้เห็นลิงก์ไว้คัดลอก และบอกหน่อยว่า ใช้ได้บนเว็บ, Android และ iOS ได้เหมือนกันไหม
   ~~~
3. ส่ง prompt ให้เริ่ม run ใหม่หลังเพิ่ม plugin การ Refresh browser อย่างเดียวไม่แทนการลงทะเบียน native plugin

   ~~~text
   ฉันอยากลองกดปุ่มคู่มือจริง ช่วยหยุดแล้วเปิดเฉพาะ Flutter รอบใหม่ให้ plugin พร้อมใช้
   เปิด preview บน Edge ที่ localhost:3000 และใช้ API ที่ยังรันอยู่ที่ http://127.0.0.1:8000
   ถ้าใช้ Mac ให้รัน web-server แล้วส่งลิงก์ให้ฉันเปิดใน Edge เอง
   ~~~

   Sign in แล้วกดปุ่มคู่มือ ต้องเปิดเอกสาร ส่วน Android/iOS ปุ่มนี้ใช้ browser ตามค่าเริ่มต้นของอุปกรณ์

4. ส่ง prompt ตรวจกรณีเปิดไม่สำเร็จ โดยไม่เปลี่ยน URL ไปเว็บสุ่ม

   ~~~text
   ช่วยเขียนและรัน test ว่าถ้าปุ่มเปิดคู่มือไม่ได้ คนใช้ยังเห็นลิงก์ให้คัดลอก
   ขอให้ลองทั้งตอน plugin ตอบ false และตอนเกิด error ใช้การจำลองทั้งสองแบบ แล้วบอกผลให้ดู
   ~~~

**Checkpoint:** ปุ่มทำงานจาก user action; มี fallback เมื่อ platform เปิด URL ไม่ได้. นี่เป็นตัวอย่างใช้ plugin ไม่ใช่บทเรียนเขียน native plugin ใหม่

## Practice 3 — รันและ build Android {#practice-2-—-รันและ-build-android}

<PracticeIllustration asset="d03-e04-p02" />

**Primary target:** ติดตั้ง Android debug app แล้วทำงานกับ API เดิมได้

### Steps

1. เปิด Android emulator ที่เตรียมไว้ก่อนเรียน ถ้าใช้เครื่องจริงแทน ให้เสียบ USB และยืนยัน USB debugging บนเครื่อง ส่ง prompt ให้เลือกอุปกรณ์

   ~~~text
   ใช้เครื่องมือที่มีช่วยดูว่า Android เครื่องไหนพร้อมลองแอปแล้ว ขอชื่อเครื่องกับ device ID ด้วย
   ถ้ามีหลายเครื่องให้ฉันเลือกก่อน ถ้ายังไม่มีเครื่องพร้อม ให้บอกว่าติดอะไรแล้วหยุดไว้
   ~~~

2. ส่ง prompt ตรวจ Android configuration ที่จำเป็นสำหรับการฝึกวันนี้

   ~~~text
   ก่อนลองต่อ API ช่วยดูให้หน่อยว่าแอป Android ขอสิทธิ์ใช้อินเทอร์เน็ตไว้แล้วหรือยัง แล้วชี้ให้ฉันดูว่าตั้งไว้ที่ไหน
   ~~~
3. ส่ง prompt ให้ต่อ Android กลับมาที่ API บน laptop แล้วรันแอป

   ~~~text
   ช่วยเปิดแอปบน Android เครื่องที่ฉันเลือกไว้ โดยใช้ device ID ของเครื่องนั้น
   ต่อพอร์ตกลับมาที่เครื่องนี้ด้วย adb reverse แล้วใช้ API_BASE_URL เป็น http://127.0.0.1:8000 สำหรับ debug
   ถ้าต่อไม่ติด ช่วยหาว่าติดตรงไหนก่อน ใช้ HTTP เฉพาะตอน debug และคงการตรวจ HTTPS ไว้
   ~~~

   `adb reverse` เหมือนต่อท่อจาก port บน Android กลับมายัง laptop จึงใช้ loopback เดิมได้ ต้องต่อใหม่เมื่อการเชื่อมต่อถูก reset

4. กลับไปที่ Android launcher เปิดรายการแอป แล้วหาไอคอนใหม่จาก Practice 1 ชื่อใต้ไอคอนอาจเป็น `service_desk_lite` ตามที่ตั้งไว้ แตะไอคอนแล้วตรวจว่า Service Desk Lite เปิดขึ้น ถ้ายังเห็นไอคอนเดิม ให้ตรวจว่ารัน build ล่าสุดบนเครื่องที่เลือกก่อน หากยังตรวจไม่ได้ ให้บันทึกผลไอคอนเป็น pending

   Sign in จาก Android สร้าง Request ด้วย **Title** นี้ ใส่ Description อย่างน้อย 10 ตัวอักษรและเลือก Category จากแบบฟอร์ม จากนั้นเปิด detail ตรวจ UUID ใน `/docs` ด้วยบัญชีเดียวกัน และกดปุ่มคู่มือ

   ~~~text
   ทดสอบจาก Android
   ~~~
5. ส่ง prompt ตรวจโปรเจกต์แล้วสร้างไฟล์ติดตั้งสำหรับฝึก

   ~~~text
   ขอไฟล์ติดตั้ง Android สำหรับลองในห้องเรียน ช่วยหยุดเฉพาะแอปที่รันอยู่แล้วปล่อย API ไว้
   เช็กโค้ดและรัน test ก่อน ถ้าติดอะไรให้บอกฉันและหยุดไว้
   ถ้าผ่าน ให้ build debug APK ที่ใช้ API_BASE_URL เป็น http://127.0.0.1:8000 แล้วบอกผลกับตำแหน่งไฟล์
   ~~~

6. ตรวจไฟล์ **client/build/app/outputs/flutter-apk/app-debug.apk**. ไฟล์นี้ผูกกับ local lab/adb reverse; Day 4 ต้อง rebuild ด้วย HTTPS API URL
7. ส่ง prompt เตรียมส่งงานตาม workflow Day 1 แล้วตรวจ diff ก่อนยืนยันขั้นส่งงาน

   ~~~text
   ช่วยเตรียมส่งงานบน feature/flutter-client ตามที่ฝึก Day 1
   จดผล test ที่อยู่ APK และผลตรวจไอคอนจาก Android launcher ลง docs/review-log.md
   ให้ฉันตรวจ PNG ต้นฉบับ ไฟล์ตั้งค่า และ Android launcher resources ที่เปลี่ยน เก็บ APK ไว้นอก commit
   ขอดูรายชื่อไฟล์ที่จะ commit กับแผนส่งงานก่อน รอฉันยืนยันแล้วค่อยส่งตามขั้นตอน Day 1 โดยใช้ push
   ~~~

**Checkpoint:** Android เรียก API จริงได้และมี debug APK พร้อมบันทึกผลว่าเห็นและเปิดแอปจากไอคอนใหม่ได้หรือยัง Browser ผ่านอย่างเดียวไม่ถือว่าผ่าน Android checkpoint

**ถ้าติดขัด:** ถ้าไม่มีอุปกรณ์พร้อม ให้จบ browser/tests และบันทึก Android pending. ถ้าพบ unauthorized ให้ยืนยัน USB debugging บนอุปกรณ์. หาก HTTP ใช้ไม่ได้ให้ตรวจ adb reverse/debug manifest ไม่เปิด cleartext ใน release

## Practice 4 — รันและ build iOS Simulator (Optional · macOS) {#ios-simulator}

<PracticeIllustration asset="d03-e04-p03" />

**Primary target:** ใช้ Flutter project เดิมทำงานกับ API บน iPhone Simulator และสร้างไฟล์แอปสำหรับ Simulator ได้

> **Optional:** ทำหลังผ่านกิจกรรมหลักและยังมีเวลา ประมาณ 10–15 นาทีเมื่อเครื่องพร้อม; เวลา build ขึ้นกับเครื่อง ต้องมี Mac, Xcode และ iPhone Simulator ที่เตรียมตาม [readiness](/resources/readiness#ios-simulator-optional) แล้ว ไม่ต้องตั้งค่า signing หรือสมัคร Apple Developer แบบเสียเงินสำหรับ Simulator. ผู้ใช้ Windows หรือผู้ที่ข้าม Practice นี้ยังผ่าน checkpoint หลักได้ตามปกติ

### Steps

1. ใช้ prompt เปิด API จาก [Exercise 3](/exercises/day-03-flutter/exercise-03#ก่อนเชื่อมข้อมูลจริง) บน **Mac เครื่องเดียวกับ Simulator** และตรวจ `/health` กับ `/docs` ว่าทำงาน จากนั้นส่ง prompt นี้ให้ Codex:

   ~~~text
   อยากลองแอปเดิมบน iPhone Simulator ช่วยอ่าน AGENTS.md แล้วดูว่างาน Git, Xcode และ Flutter พร้อมไหม
   ถ้ามีงานค้างให้ถามฉันก่อน ถ้าเครื่องยังไม่พร้อมให้จด optional pending โดยใช้เฉพาะเครื่องมือที่มี

   ถ้าพร้อม ให้ใช้ feature/ios-simulator หรือสร้างจาก main ที่มีงาน Day 3 ครบ
   เติมเฉพาะส่วน iOS ถ้ายังไม่มี เก็บ iOS ที่มีอยู่ รวมถึง Android และ Web ไว้ตามเดิม
   ใช้ ApiService, Dio และ API_BASE_URL เดิม คงการตรวจ HTTPS และใช้ Simulator โดยไม่ตั้ง signing ส่วนตัว
   ขอให้ฉันดู diff ก่อน
   ~~~
2. ส่ง prompt เปิด Simulator ที่เตรียมไว้ แล้วตรวจ ID จริง

   ~~~text
   ช่วยเปิด iPhone Simulator ที่มีอยู่แล้วและบอก device ID ให้หน่อย
   ถ้ามีหลายเครื่องให้ฉันเลือกก่อน ใช้เฉพาะเครื่องที่เตรียมไว้
   ~~~

3. ส่ง prompt รันแอปบน Simulator ที่เลือก

   ~~~text
   ช่วยเปิดแอปบน iPhone Simulator ที่ฉันเลือก ให้ใช้ API_BASE_URL เป็น http://127.0.0.1:8000 ของ Mac เครื่องนี้
   ถ้าแอปรอบก่อนยังรันอยู่ ให้หยุดเฉพาะรอบนั้นก่อนเปิดใหม่
   ~~~

   iOS Simulator ติดต่อ API บน Mac เครื่องเดียวกันผ่าน loopback จึงไม่ใช้ `adb reverse` ของ Android
4. Sign in ด้วยบัญชีทดลองเดิม สร้าง Request โดยกรอก **Title** ดังนี้ พร้อม Description อย่างน้อย 10 ตัวอักษรและ Category จากแบบฟอร์ม

   ~~~text
   ทดสอบจาก iPhone Simulator
   ~~~

   เปิดรายละเอียดแล้วเทียบ UUID กับ API `/docs` ด้วยบัญชีเดียวกัน และกดปุ่มคู่มือเพื่อตรวจว่าเปิดเอกสารได้
5. ส่ง prompt สร้างไฟล์สำหรับ Simulator

   ~~~text
   ขอไฟล์แอป debug สำหรับ iPhone Simulator ที่ใช้ API_BASE_URL เป็น http://127.0.0.1:8000
   ช่วยหยุดแอปรอบที่กำลังทดสอบแล้ว build สำหรับ Simulator ได้เลย ไม่ต้องตั้ง signing
   เสร็จแล้วบอกผลกับที่อยู่ไฟล์ .app
   ~~~

   ปกติอยู่ที่ `client/build/ios/iphonesimulator/Runner.app` ไฟล์นี้ใช้กับ Simulator ไม่ใช่ IPA สำหรับ iPhone จริงหรือ App Store
6. ส่ง prompt เก็บหลักฐานและเตรียมส่งเฉพาะ iOS source/config

   ~~~text
   ช่วยจด UUID ที่เราตรวจ ผลตอนกดปุ่มคู่มือ และที่อยู่ไฟล์ .app ลง docs/review-log.md โดยไม่ใส่ค่าลับ
   ขอดูรายชื่อไฟล์โค้ดและไฟล์ตั้งค่า iOS ที่จะส่งตามขั้นตอน Day 1 เก็บไฟล์ build และ signing ไว้ในเครื่อง
   รอฉันตรวจและยืนยันก่อนเริ่ม commit, push, เปิด PR หรือ merge
   ~~~

**Checkpoint:** **Optional** — แอปทำงานบน iPhone Simulator, UUID ตรงกับ API และมี `.app` สำหรับ Simulator ตามผล build จริง. หลักฐานนี้เพิ่มเติมจาก Android checkpoint ไม่ใช้แทนกัน

**ถ้าติดขัด:** หาก Xcode/runtime/native dependencies ยังไม่พร้อม ให้บันทึก **optional pending** แล้วไป [สรุปท้ายวัน](/exercises/day-03-flutter/summary). หากเรียก API ไม่ได้ ให้ตรวจ API บน Mac และ `API_BASE_URL`; ไม่แก้ด้วยการเปิด ATS ให้ยอมรับทุก connection หรือปิด HTTPS verification

อ่านเพิ่ม: [Flutter: ใช้ packages](https://docs.flutter.dev/packages-and-plugins/using-packages), [url_launcher](https://pub.dev/packages/url_launcher), [Flutter: restart หลังแก้ native code](https://docs.flutter.dev/tools/hot-reload#native-code), [Android build](https://docs.flutter.dev/deployment/android), [Flutter iOS setup](https://docs.flutter.dev/platform-integration/ios/setup), [Flutter iOS build command](https://github.com/flutter/flutter/blob/stable/packages/flutter_tools/lib/src/commands/build_ios.dart)
