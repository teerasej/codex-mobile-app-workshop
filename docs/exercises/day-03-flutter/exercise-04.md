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

หน้าจอใน browser ผ่านแล้ว เราจะลองบน Android และเพิ่มความสามารถเปิดคู่มือใน browser ของอุปกรณ์ หากใช้ Mac ที่เตรียมพร้อมและผ่านกิจกรรมหลักแล้ว มี Practice เสริมให้เปิดแอปเดิมใน iPhone Simulator

ใช้ `ApiService` และ Dio จาก Exercise 3 ต่อทั้ง web และ mobile โดยให้ Dio เลือก adapter ตามแพลตฟอร์ม เปลี่ยนเฉพาะวิธีรัน ไม่สร้างแอปใหม่

## Practice 1 — เปิดคู่มือด้วย plugin

<PracticeIllustration asset="d03-e04-p01" eager />

**Primary target:** ใช้ Flutter plugin เรียกความสามารถของแพลตฟอร์มและจัดการกรณีเปิดไม่สำเร็จได้

### Steps

1. Plugin เหมือนยืมความสามารถของเครื่องแทนเขียนเองทั้งหมด ส่ง prompt ให้เพิ่ม package ใน client เดิม

   ~~~text
   เพิ่ม url_launcher ให้แอปใน client/ หน่อย
   ~~~

   `url_launcher` 6.3.3 ที่ใช้ตรวจเอกสารรองรับ Android SDK 24+ และ iOS 13.0+ รุ่นที่ติดตั้งจริงให้ดู lockfile และ pub.dev ไม่เดารุ่นจากตัวอย่างนี้

2. ส่ง prompt ให้เพิ่มปุ่มในหน้าที่มีอยู่

   ~~~text
   เพิ่มปุ่ม “คู่มือ Flutter” ในหน้าหลังล็อกอิน กดแล้วเปิด https://docs.flutter.dev
   ให้เปิดเมื่อผู้ใช้กดเท่านั้น ถ้าเปิดไม่ได้ให้โชว์ลิงก์ให้ copy แทน
   ต้องใช้ได้ทั้ง web, Android และ iOS ไม่ต้องขอ permission เพิ่ม
   ใช้ ApiService เดิมต่อไป แล้วเล่าให้ฟังสั้น ๆ ว่า plugin ต่างจากเขียน native เองยังไง
   ~~~
3. ส่ง prompt ให้เริ่ม run ใหม่หลังเพิ่ม plugin การ Refresh browser อย่างเดียวไม่แทนการลงทะเบียน native plugin

   ~~~text
   รีสตาร์ทแอป Flutter ใหม่เพื่อให้ plugin ทำงาน แล้วเปิดบน Edge
   ใช้ localhost:3000 ต่อ API เดิมที่ http://127.0.0.1:8000
   ปล่อย API ที่รันอยู่ไว้ และอย่าปิดอย่างอื่นที่ไม่เกี่ยว
   ถ้ารันบน Mac ให้บอก URL ที่ต้องเปิดเอง
   ~~~

   Sign in แล้วกดปุ่มคู่มือ ต้องเปิดเอกสาร ส่วน Android/iOS ปุ่มนี้ใช้ browser ตามค่าเริ่มต้นของอุปกรณ์

4. ส่ง prompt ตรวจกรณีเปิดไม่สำเร็จ โดยไม่เปลี่ยน URL ไปเว็บสุ่ม

   ~~~text
   เขียน test ให้ปุ่มคู่มือ จำลองกรณีเปิดลิงก์ไม่สำเร็จทั้งสองแบบ (ได้ false และเกิด error)
   ต้องเห็นลิงก์ให้ copy ทั้งคู่ ไม่ต้องเรียก network จริง
   รัน test แล้วสรุปผลให้ดู
   ~~~

**Checkpoint:** ปุ่มทำงานจาก user action; มี fallback เมื่อ platform เปิด URL ไม่ได้. นี่เป็นตัวอย่างใช้ plugin ไม่ใช่บทเรียนเขียน native plugin ใหม่

## Practice 2 — รันและ build Android

<PracticeIllustration asset="d03-e04-p02" />

**Primary target:** ติดตั้ง Android debug app แล้วทำงานกับ API เดิมได้

### Steps

1. เปิด Android emulator ที่เตรียมไว้ก่อนเรียน ถ้าใช้เครื่องจริงแทน ให้เสียบ USB และยืนยัน USB debugging บนเครื่อง ส่ง prompt ให้เลือกอุปกรณ์

   ~~~text
   ดูหน่อยว่ามี Android เครื่องไหนพร้อมทดสอบบ้าง แล้วบอก device ID ของเครื่องที่จะใช้
   ถ้ามีหลายเครื่องให้ถามฉันก่อน ถ้าไม่เจอหรือเครื่องยังไม่พร้อมให้บอกแล้วหยุด
   อย่าติดตั้งอะไรเพิ่ม
   ~~~

2. ส่ง prompt ตรวจ Android configuration ที่จำเป็นสำหรับการฝึกวันนี้

   ~~~text
   เช็คหน่อยว่าแอป Android ของเรามีสิทธิ์ใช้อินเทอร์เน็ตหรือยัง
   ~~~
3. ส่ง prompt ให้ต่อ Android กลับมาที่ API บน laptop แล้วรันแอป

   ~~~text
   รันแอปบน Android เครื่องที่เลือกไว้ แล้วให้คุยกับ API บน laptop ที่ http://127.0.0.1:8000 ได้
   ใช้ device ID จริงของเครื่องนั้น ห้ามเดาหรือไปเลือกเครื่องอื่นเอง
   ถ้าเรียก API ไม่ได้ ให้หาสาเหตุก่อน แต่ห้ามปิด HTTPS verification
   ~~~

   `adb reverse` เหมือนต่อท่อจาก port บน Android กลับมายัง laptop จึงใช้ loopback เดิมได้ ต้องต่อใหม่เมื่อการเชื่อมต่อถูก reset

4. Sign in จาก Android สร้าง Request ด้วย **Title** นี้ ใส่ Description อย่างน้อย 10 ตัวอักษรและเลือก Category จากแบบฟอร์ม จากนั้นเปิด detail ตรวจ UUID ใน `/docs` ด้วยบัญชีเดียวกัน และกดปุ่มคู่มือ

   ~~~text
   ทดสอบจาก Android
   ~~~
5. ส่ง prompt ตรวจโปรเจกต์แล้วสร้างไฟล์ติดตั้งสำหรับฝึก

   ~~~text
   หยุดแอปที่รันอยู่ (ปล่อย API ไว้) แล้วเช็คโค้ดและรัน test ก่อน
   ถ้าไม่ผ่านให้สรุปปัญหา ยังไม่ต้อง build
   ถ้าผ่านให้สร้าง debug APK ที่ต่อกับ http://127.0.0.1:8000
   บอกผลเช็ค/test และไฟล์ APK อยู่ตรงไหน
   ~~~

6. ตรวจไฟล์ **client/build/app/outputs/flutter-apk/app-debug.apk**. ไฟล์นี้ผูกกับ local lab/adb reverse; Day 4 ต้อง rebuild ด้วย HTTPS API URL
7. ส่ง prompt เตรียมส่งงานตาม workflow Day 1 แล้วตรวจ diff ก่อนยืนยันขั้นส่งงาน

   ~~~text
   เตรียมส่งงาน feature/flutter-client ตาม workflow Day 1
   ดู diff ว่ามีอะไรเปลี่ยนบ้าง และต้องไม่มี secrets, .env หรือไฟล์ build หลุดเข้ามา
   จดผล test กับตำแหน่ง APK ลง docs/review-log.md (ห้ามใส่ secrets)
   แสดงรายการไฟล์ที่จะ commit พร้อมแผนส่งงานให้ฉันตรวจก่อน แล้วค่อยทำจริง
   ห้าม force push
   ~~~

**Checkpoint:** Android เรียก API จริงได้และมี debug APK. Browser ผ่านอย่างเดียวไม่ถือว่าผ่าน Android checkpoint

**ถ้าติดขัด:** ถ้าไม่มีอุปกรณ์พร้อม ให้จบ browser/tests และบันทึก Android pending. ถ้าพบ unauthorized ให้ยืนยัน USB debugging บนอุปกรณ์. หาก HTTP ใช้ไม่ได้ให้ตรวจ adb reverse/debug manifest ไม่เปิด cleartext ใน release

## Practice 3 — รันและ build iOS Simulator (Optional · macOS) {#ios-simulator}

<PracticeIllustration asset="d03-e04-p03" />

**Primary target:** ใช้ Flutter project เดิมทำงานกับ API บน iPhone Simulator และสร้างไฟล์แอปสำหรับ Simulator ได้

> **Optional:** ทำหลังผ่านกิจกรรมหลักและยังมีเวลา ประมาณ 10–15 นาทีเมื่อเครื่องพร้อม; เวลา build ขึ้นกับเครื่อง ต้องมี Mac, Xcode และ iPhone Simulator ที่เตรียมตาม [readiness](/resources/readiness#ios-simulator-optional) แล้ว ไม่ต้องตั้งค่า signing หรือสมัคร Apple Developer แบบเสียเงินสำหรับ Simulator. ผู้ใช้ Windows หรือผู้ที่ข้าม Practice นี้ยังผ่าน checkpoint หลักได้ตามปกติ

### Steps

1. ใช้ prompt เปิด API จาก [Exercise 3](/exercises/day-03-flutter/exercise-03#ก่อนเชื่อมข้อมูลจริง) บน **Mac เครื่องเดียวกับ Simulator** และตรวจ `/health` กับ `/docs` ว่าทำงาน จากนั้นส่ง prompt นี้ให้ Codex:

   ~~~text
   เตรียมแอปเดิมให้รันบน iPhone Simulator ได้ โดยทำบน feature branch ตาม AGENTS.md
   เช็คสถานะ branch ก่อน ถ้าไม่มี feature/ios-simulator ให้สร้างจาก main ที่มีงาน Day 3 ครบ ถ้ามีงานค้างให้หยุดถามก่อน
   เช็คว่า Xcode และ Flutter พร้อมไหม ห้ามติดตั้งหรือดาวน์โหลดอะไรเพิ่ม ถ้าไม่พร้อมให้สรุปว่า optional pending
   ถ้ายังไม่มีโฟลเดอร์ iOS ให้เพิ่มเฉพาะ iOS เข้าโปรเจกต์เดิม ถ้ามีแล้วอย่าเขียนทับ
   โค้ด Android และ Web เดิมต้องไม่ถูกแตะ แสดง diff ให้ดูก่อน
   ใช้ ApiService/Dio และ API_BASE_URL เดิม ไม่ตั้ง signing ส่วนตัว ไม่ปิด HTTPS verification
   ~~~
2. ส่ง prompt เปิด Simulator ที่เตรียมไว้ แล้วตรวจ ID จริง

   ~~~text
   เปิด iPhone Simulator ที่เตรียมไว้ แล้วบอก device ID ของมัน
   ถ้ามีหลายเครื่องให้ถามฉันก่อน และอย่าดาวน์โหลดอะไรเพิ่ม
   ~~~

3. ส่ง prompt รันแอปบน Simulator ที่เลือก

   ~~~text
   รันแอปบน iPhone Simulator ที่เลือกไว้ ให้คุยกับ API บน Mac เครื่องนี้ที่ http://127.0.0.1:8000
   ถ้ามีแอปรอบก่อนค้างอยู่ให้หยุดเฉพาะอันนั้น อย่าปิดอย่างอื่น
   ~~~

   iOS Simulator ติดต่อ API บน Mac เครื่องเดียวกันผ่าน loopback จึงไม่ใช้ `adb reverse` ของ Android
4. Sign in ด้วยบัญชีทดลองเดิม สร้าง Request โดยกรอก **Title** ดังนี้ พร้อม Description อย่างน้อย 10 ตัวอักษรและ Category จากแบบฟอร์ม

   ~~~text
   ทดสอบจาก iPhone Simulator
   ~~~

   เปิดรายละเอียดแล้วเทียบ UUID กับ API `/docs` ด้วยบัญชีเดียวกัน และกดปุ่มคู่มือเพื่อตรวจว่าเปิดเอกสารได้
5. ส่ง prompt สร้างไฟล์สำหรับ Simulator

   ~~~text
   หยุดแอปที่รันอยู่ แล้วสร้างไฟล์แอปสำหรับ iPhone Simulator (debug) ที่ต่อกับ http://127.0.0.1:8000
   ไม่ต้องตั้ง signing บอกผล build และไฟล์ .app อยู่ตรงไหน
   ~~~

   ปกติอยู่ที่ `client/build/ios/iphonesimulator/Runner.app` ไฟล์นี้ใช้กับ Simulator ไม่ใช่ IPA สำหรับ iPhone จริงหรือ App Store
6. ส่ง prompt เก็บหลักฐานและเตรียมส่งเฉพาะ iOS source/config

   ~~~text
   จด UUID, ผลปุ่มคู่มือ และตำแหน่ง .app ลง docs/review-log.md (ห้ามใส่ secrets)
   แสดงรายการไฟล์ iOS ที่ต้อง commit ตาม workflow Day 1 โดยไม่รวมไฟล์ build หรือ signing
   รอฉันตรวจก่อน แล้วค่อย commit/push/PR/merge
   ~~~

**Checkpoint:** **Optional** — แอปทำงานบน iPhone Simulator, UUID ตรงกับ API และมี `.app` สำหรับ Simulator ตามผล build จริง. หลักฐานนี้เพิ่มเติมจาก Android checkpoint ไม่ใช้แทนกัน

**ถ้าติดขัด:** หาก Xcode/runtime/native dependencies ยังไม่พร้อม ให้บันทึก **optional pending** แล้วไป [สรุปท้ายวัน](/exercises/day-03-flutter/summary). หากเรียก API ไม่ได้ ให้ตรวจ API บน Mac และ `API_BASE_URL`; ไม่แก้ด้วยการเปิด ATS ให้ยอมรับทุก connection หรือปิด HTTPS verification

อ่านเพิ่ม: [Flutter: ใช้ packages](https://docs.flutter.dev/packages-and-plugins/using-packages), [url_launcher](https://pub.dev/packages/url_launcher), [Flutter: restart หลังแก้ native code](https://docs.flutter.dev/tools/hot-reload#native-code), [Android build](https://docs.flutter.dev/deployment/android), [Flutter iOS setup](https://docs.flutter.dev/platform-integration/ios/setup), [Flutter iOS build command](https://github.com/flutter/flutter/blob/stable/packages/flutter_tools/lib/src/commands/build_ios.dart)
