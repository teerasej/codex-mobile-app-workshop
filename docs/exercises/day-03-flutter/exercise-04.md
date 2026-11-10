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

## Practice 1 — เปิดคู่มือด้วย plugin

<PracticeIllustration asset="d03-e04-p01" eager />

**Primary target:** ใช้ Flutter plugin เรียกความสามารถของแพลตฟอร์มและจัดการกรณีเปิดไม่สำเร็จได้

### Steps

1. จาก client ให้รัน **flutter pub add url_launcher**
2. ส่ง:

   ~~~text
   เพิ่มปุ่ม “คู่มือ Flutter” บนหน้าที่ login แล้ว
   ใช้ url_launcher launchUrl ไป https://docs.flutter.dev
   เรียกจากการกดปุ่มโดยตรง; ถ้าเปิดไม่ได้แสดง URL ให้ผู้ใช้ copy
   ใช้ plugin API ที่รองรับ web/Android/iOS ไม่ใช้ dart:io ใน code ที่ web import
   อธิบายความต่างระหว่าง plugin กับการเขียน native platform codeเองสั้น ๆ
   ไม่เพิ่ม permission โทรศัพท์/contacts/location และไม่เปิด URL อัตโนมัติ
   ~~~
3. หลังเพิ่ม plugin ให้หยุด `flutter run` เดิม แล้วเริ่มใหม่ด้วยคำสั่ง browser จาก Exercise 3 · Practice 1 พร้อม `--dart-define=API_BASE_URL` เดิม เพื่อให้ Flutter ลงทะเบียน plugin. การทำ hot reload/hot restart หรือ Refresh browser อย่างเดียวอาจยังไม่โหลด plugin ที่เพิ่งเพิ่ม. เปิด preview ใหม่, Sign in แล้วกดปุ่มเพื่อตรวจว่าเปิดหน้าเอกสาร
4. ให้ Codex แสดงการทดสอบ failure ด้วย mock launcher. ไม่เปลี่ยน URL เป็นเว็บสุ่มเพื่อทดสอบ

**Checkpoint:** ปุ่มทำงานจาก user action; มี fallback เมื่อ platform เปิด URL ไม่ได้. นี่เป็นตัวอย่างใช้ plugin ไม่ใช่บทเรียนเขียน native plugin ใหม่

## Practice 2 — รันและ build Android

<PracticeIllustration asset="d03-e04-p02" />

**Primary target:** ติดตั้ง Android debug app แล้วทำงานกับ API เดิมได้

### Steps

1. เปิด Android emulator ที่เตรียมไว้ หรือเสียบเครื่องทดสอบ. ให้ Codex แสดง **flutter devices** และ **adb devices**, เลือกเพียงเครื่องเดียว
2. หยุด browser previewถ้าทรัพยากรเครื่องไม่พอ. ให้ Codex ทำ debug-only setup:

   ~~~text
   ตรวจ Android manifests ของ client:
   main manifest มี android.permission.INTERNET
   debug manifest อนุญาต cleartext traffic เฉพาะเพื่อทดสอบ loopback HTTP วันนี้
   อย่าเพิ่ม cleartext exception ใน release/main และอย่าปิด HTTPS verification
   เก็บ API_BASE_URL เป็น dart-define
   แสดง diff ของ manifests ก่อนให้รัน
   ~~~
3. รันจาก client โดยแทนค่า device IDs ที่ได้จริง; adb ID และ flutter ID ให้ตรวจแยก:

   ~~~shell
   adb -s <ADB_DEVICE_ID> reverse tcp:8000 tcp:8000
   flutter run -d <FLUTTER_DEVICE_ID> --dart-define=API_BASE_URL=http://127.0.0.1:8000
   ~~~

   adb reverse ส่ง port ของ Android กลับมาที่ laptop จึงไม่ต้องใช้ IP Wi-Fi ของคนอื่น. ต้องรันใหม่ถ้าการเชื่อมต่อถูก reset
4. Login จาก Android, สร้าง Request ชื่อ **ทดสอบจาก Android** และตรวจใน /docs. กดปุ่มคู่มือด้วย
5. หยุด flutter run แล้วรัน:

   ~~~shell
   flutter analyze
   flutter test
   flutter build apk --debug --dart-define=API_BASE_URL=http://127.0.0.1:8000
   ~~~
6. ตรวจไฟล์ **client/build/app/outputs/flutter-apk/app-debug.apk**. ไฟล์นี้ผูกกับ local lab/adb reverse; Day 4 ต้อง rebuild ด้วย HTTPS API URL
7. ตรวจ diff โดยเฉพาะ pubspec.lock, Android manifest และ API CORS. Commit/push/PR/merge ทุกส่วนที่จำเป็น; ไม่ commit build outputs, local.properties หรือ secrets

**Checkpoint:** Android เรียก API จริงได้และมี debug APK. Browser ผ่านอย่างเดียวไม่ถือว่าผ่าน Android checkpoint

**ถ้าติดขัด:** ถ้าไม่มีอุปกรณ์พร้อม ให้จบ browser/tests และบันทึก Android pending. ถ้าพบ unauthorized ให้ยืนยัน USB debugging บนอุปกรณ์. หาก HTTP ใช้ไม่ได้ให้ตรวจ adb reverse/debug manifest ไม่เปิด cleartext ใน release

## Practice 3 — รันและ build iOS Simulator (Optional · macOS) {#ios-simulator}

<PracticeIllustration asset="d03-e04-p03" />

**Primary target:** ใช้ Flutter project เดิมทำงานกับ API บน iPhone Simulator และสร้างไฟล์แอปสำหรับ Simulator ได้

> **Optional:** ทำหลังผ่านกิจกรรมหลักและยังมีเวลา ประมาณ 10–15 นาทีเมื่อเครื่องพร้อม; เวลา build ขึ้นกับเครื่อง ต้องมี Mac, Xcode และ iPhone Simulator ที่เตรียมตาม [readiness](/resources/readiness#ios-simulator-optional) แล้ว ไม่ต้องตั้งค่า signing หรือสมัคร Apple Developer แบบเสียเงินสำหรับ Simulator. ผู้ใช้ Windows หรือผู้ที่ข้าม Practice นี้ยังผ่าน checkpoint หลักได้ตามปกติ

### Steps

1. เปิด API เดิมบน **Mac เครื่องเดียวกับ Simulator** และตรวจ `/health` กับ `/docs` ว่าทำงาน จากนั้นส่ง prompt นี้ให้ Codex:

   ~~~text
   เตรียม client เดิมเพื่อรัน iPhone Simulator โดยทำงานบน feature branch ตาม AGENTS.md
   ตรวจ flutter doctor -v, Xcode, iOS runtime และ native dependencies ของ url_launcher
   ห้ามติดตั้ง toolchain หรือดาวน์โหลด runtime ระหว่างกิจกรรม ถ้าไม่พร้อมให้สรุป optional pending
   ถ้าไม่มี client/ios/ ให้รันจาก client เท่านั้น:
   flutter create --platforms=ios --project-name service_desk_lite .
   ถ้ามี ios/ แล้วให้ใช้ของเดิม ไม่ใช้ --overwrite
   รักษา lib, test, Android และ Web เดิม แสดง diff ให้ตรวจ และหยุดถ้าพบการเปลี่ยนที่ไม่เกี่ยวกับ iOS
   ใช้ API_BASE_URL จาก dart-define เดิม ไม่เพิ่ม signing ส่วนตัวหรือปิด HTTPS verification
   ~~~
2. เปิด iPhone Simulator ที่เตรียมไว้ผ่านเครื่องมือของ Xcode รุ่นที่ติดตั้ง แล้วรันจาก `client/` เพื่ออ่าน device ID จริง:

   ~~~shell
   flutter devices
   ~~~
3. แทน `<IOS_SIMULATOR_ID>` ด้วย ID ของ iPhone Simulator ที่เปิดอยู่ แล้วรันจาก `client/`:

   ~~~shell
   flutter run -d <IOS_SIMULATOR_ID> --dart-define=API_BASE_URL=http://127.0.0.1:8000
   ~~~

   iOS Simulator ติดต่อ API บน Mac เครื่องนี้ผ่าน loopback ได้ จึงไม่ใช้ `adb reverse` ของ Android
4. Sign in ด้วยบัญชีทดลองเดิม สร้าง Request โดยกรอก **Title** ดังนี้ พร้อมรายละเอียดอย่างน้อย 10 ตัวอักษร:

   ~~~text
   ทดสอบจาก iPhone Simulator
   ~~~

   เปิดรายละเอียดแล้วเทียบ UUID กับ API `/docs` ด้วยบัญชีเดียวกัน และกดปุ่มคู่มือเพื่อตรวจว่าเปิดเอกสารได้
5. หยุด `flutter run` แล้ว build จาก `client/`:

   ~~~shell
   flutter build ios --simulator --debug --dart-define=API_BASE_URL=http://127.0.0.1:8000
   ~~~

   ตรวจไฟล์ `.app` ตามตำแหน่งที่ Flutter รายงาน ปกติอยู่ที่ `client/build/ios/iphonesimulator/Runner.app`. ไฟล์นี้ใช้กับ Simulator ไม่ใช่ IPA สำหรับ iPhone จริงหรือ App Store
6. บันทึก UUID, ผลทดสอบปุ่มคู่มือ และ `.app` path ใน review log. ตรวจ diff แล้ว commit/push/PR/merge เฉพาะ source/config iOS ที่จำเป็นตาม workflow เดิม ไม่เก็บ build outputs, secrets หรือ signing ส่วนตัว

**Checkpoint:** **Optional** — แอปทำงานบน iPhone Simulator, UUID ตรงกับ API และมี `.app` สำหรับ Simulator ตามผล build จริง. หลักฐานนี้เพิ่มเติมจาก Android checkpoint ไม่ใช้แทนกัน

**ถ้าติดขัด:** หาก Xcode/runtime/native dependencies ยังไม่พร้อม ให้บันทึก **optional pending** แล้วไป [สรุปท้ายวัน](/exercises/day-03-flutter/summary). หากเรียก API ไม่ได้ ให้ตรวจ API บน Mac และ `API_BASE_URL`; ไม่แก้ด้วยการเปิด ATS ให้ยอมรับทุก connection หรือปิด HTTPS verification

อ่านเพิ่ม: [Flutter iOS setup](https://docs.flutter.dev/platform-integration/ios/setup), [Flutter iOS build command](https://github.com/flutter/flutter/blob/stable/packages/flutter_tools/lib/src/commands/build_ios.dart)
