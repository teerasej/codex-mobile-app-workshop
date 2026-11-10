---
title: "ก่อนวันแรก — เตรียมเครื่อง บัญชี และพื้นที่ฝึก"
prev: false
next: false
---

# ก่อนวันแรก — เตรียมเครื่อง บัญชี และพื้นที่ฝึก

[กลับสารบัญ](/)

เราใช้ Windows เป็นหลักและมีทางเลือก macOS. ผู้เรียนใช้ ChatGPT desktop app โดยเลือก Codex และ local project; browser ใช้กับ GitHub, API docs และ Azure portal. ไม่ต้องติดตั้ง VS Code

## 1. ตรวจ ChatGPT desktop และ GitHub

1. อัปเดต ChatGPT desktop app จากช่องทางองค์กรหรือ [official quickstart](https://learn.chatgpt.com/docs/quickstart) และลงชื่อเข้าใช้
2. ตรวจว่าเลือก **Codex** ได้ และเพิ่ม local folder เป็น project ได้. ChatGPT project ที่แนบไฟล์เฉย ๆ ไม่เท่ากับ local project ที่แก้ไฟล์บนเครื่อง
3. เปิดโฟลเดอร์ทดลองว่าง แล้วขอให้อ่านรายชื่อไฟล์และสร้าง `hello.txt` หนึ่งไฟล์ ตรวจใน File Explorer/Finder. ทดสอบนี้ห้ามใช้โฟลเดอร์บริษัทที่มีข้อมูลจริง
4. ลงชื่อเข้า GitHub และตรวจว่าสร้าง **private repository**, push branch, เปิด/merge PR และใช้ GitHub Actions ได้. ผู้ดูแลอาจจำกัด Actions หรือ app authentication
5. ตรวจสิทธิ์และ usage ของ ChatGPT/Codex กับผู้จัดก่อนเรียน ไม่มีการสมมติว่าทุกแผนใช้ได้ไม่จำกัด. GitHub private repo/Actions มี quota และอาจมีค่าใช้จ่ายเกินสิทธิ์

> หากไม่มี Codex/local project ให้แจ้งผู้จัดก่อนเรียน เพราะ Chat ทั่วไปที่ตอบ code อย่างเดียวไม่ทำขั้นตอนแก้ไฟล์/รัน test ให้ครบตาม guide นี้ ดู [Projects](https://learn.chatgpt.com/docs/projects) และ [Windows desktop](https://learn.chatgpt.com/docs/windows/windows-app)

## 2. ติดตั้งเครื่องมือก่อนอบรม

ติดตั้ง Git, Python 3.12, Flutter stable พร้อม Dart, Chrome, Android Studio/SDK/Platform Tools และ Android emulator หรือ Android device สำหรับทดสอบ, Azure CLI และ container engine ที่องค์กรอนุญาต. Python 3.12 เป็น baseline ของแบบฝึกหัด ไม่ได้หมายถึงรุ่นใหม่สุด

ให้ Codex **ตรวจแบบ read-only** ด้วย prompt นี้:

```text
ตรวจความพร้อมเครื่องสำหรับ workshop นี้โดยไม่ติดตั้งหรือแก้ system settings:
OS, git --version, Python 3.12, flutter --version, flutter doctor -v,
flutter devices, adb devices, docker version, az version
อธิบายเป็นตาราง พร้อม/ยังไม่พร้อม/สิ่งที่ต้องทำ โดยไม่แสดงข้อมูลบัญชีหรือ secrets
Windows ใช้ PowerShell native; macOS ใช้ Terminal. ไม่เปลี่ยนไป WSL เอง
```

- Windows: คำสั่งสร้าง virtual environment ใช้ `py -3.12 -m venv .venv`. macOS: `python3.12 -m venv .venv`
- `flutter doctor -v` ต้องไม่มี blocker ใน Android toolchain และอุปกรณ์ที่เลือก. คำเตือน iOS/Xcode บนเครื่องที่ไม่ทำ iOS ไม่ใช่ blocker
- Android: เปิด emulator และรันแอป Flutter ตัวอย่างให้ได้ก่อนเรียน. ถ้าใช้เครื่องจริง ต้องอนุญาต USB debugging และยืนยันเครื่องบนหน้าจอ; ตรวจ `adb devices` ว่าไม่เป็น unauthorized
- `docker version` ต้องเห็นทั้ง Client และ Server. ตรวจ virtualization กับ IT ถ้าเครื่อง Windows เริ่ม container engine ไม่ได้
- ไม่ให้ผู้เรียนปิด security policy หรือเปลี่ยน PowerShell execution policy ทั้งเครื่องเพื่อแก้ activate. ใช้ `.venv\Scripts\python.exe` โดยตรงได้

> **Docker Desktop:** มีเงื่อนไข paid subscription สำหรับบางองค์กร ต้องให้ผู้จัดตรวจตาม [Docker license](https://docs.docker.com/subscription-billing/desktop-license/). ไม่สมมติว่าใช้ในบริษัทแล้วฟรีทุกกรณี. Toolchain อื่นยังต้องเป็นไปตาม license และ policy ขององค์กร

### iOS Simulator — ทางเลือกเฉพาะ macOS {#ios-simulator-optional}

สำหรับผู้ที่ต้องการทำ Practice เสริมท้าย Day 3 เท่านั้น: เตรียม **Mac, Xcode และ iPhone Simulator runtime** ที่รองรับ Flutter รุ่นที่ใช้ตาม [Flutter iOS setup](https://docs.flutter.dev/platform-integration/ios/setup) ก่อนเรียน และเปิด Simulator ให้ได้หนึ่งเครื่อง

- ให้ Codex ตรวจ `flutter doctor -v` ว่า iOS toolchain พร้อม และ `flutter devices` มองเห็น iPhone Simulator
- เตรียม native dependencies ที่ Flutter และ `url_launcher` รุ่นที่ใช้ต้องการให้เรียบร้อยตามเอกสาร รวมถึง CocoaPods หาก setup นั้นต้องใช้ และทดลองรันแอปตัวอย่างบน Simulator ก่อนเรียน
- ใช้ API ที่รันบน Mac เครื่องเดียวกัน ไม่ต้องใช้ iPhone จริง ตั้งค่า signing หรือสมัคร Apple Developer แบบเสียเงินสำหรับกิจกรรม Simulator นี้
- Windows และผู้ที่ทำเฉพาะ Android ข้ามส่วนนี้ได้ คำเตือน iOS/Xcode ไม่กระทบ checkpoint หลัก

**Checkpoint เสริมก่อน Day 3:** Simulator เปิดและรัน Flutter app ตัวอย่างได้แล้ว. ถ้าไม่พร้อม ให้บันทึก optional pending; ไม่ติดตั้ง Xcode หรือดาวน์โหลด runtime ขนาดใหญ่ระหว่างกิจกรรม และไม่ลดเวลางาน Android หรือสรุปท้ายวันเพื่อรอ

## 3. Azure PostgreSQL ของผู้เรียน — ก่อน Day 2

เส้นทางหลักใช้ **database แยกต่อผู้เรียนที่ผู้สอนเตรียม** บน PostgreSQL server ของชั้นเรียน. Student ZIP ส่วนตัวมี runtime `.env`, setup login และ app passwords ของ learner01/learner02. Entra account ใช้เข้า Azure; app users เป็นคนละบัญชี และไม่ได้ให้สิทธิ์ ChatGPT/Codex หรือ GitHub โดยอัตโนมัติ

1. ตรวจรหัสผู้เรียนและ database ที่ได้รับผ่านช่องทางส่วนตัว. เก็บ Student ZIP ในที่ส่วนตัวนอก Git repository; ห้ามส่ง ZIP/README ส่วนตัวหรือ `.env` เข้า chat
2. ใช้ **runtime login** กับ API; **setup login** เฉพาะ schema/seed. ผู้สอนเตรียม users 2/requests 4 แล้ว; ต้องคง passwords/hash/status เมื่อ rerun. ใช้ app passwords ที่ได้รับ ไม่เลือก password ใหม่ให้ user ที่มีอยู่
3. คัดลอกเฉพาะ `api/.env` ของตนเมื่อยังไม่มีไฟล์นี้ในโปรเจค และคง `.gitignore` ของ starter. ถ้ามี `.env` แล้วให้ตรวจเป้าหมายเองโดยไม่แสดงค่า ห้ามเขียนทับหรือสร้าง JWT_SECRET ใหม่อัตโนมัติ. ตรวจว่า `.env` ถูก ignore
4. ให้ผู้สอนตรวจ runtime TLS connection และข้อมูล seed ก่อน Day 2. หากเชื่อมต่อไม่ได้ ให้ผู้สอนตรวจ network access และ runtime login ผ่านช่องทางส่วนตัว. ผู้เรียนคง TLS และให้ผู้สอนดูแล firewall ของ shared server
5. คู่มือใช้ `sslmode=require` เป็น minimum ของ lab; ถ้าองค์กรกำหนด `verify-full` ให้เตรียม CA ตาม policy ไม่ปิด TLS เพื่อแก้ error

> **ใช้ PostgreSQL ของตนเอง:** ให้เจ้าของอนุมัติ database ใหม่ที่แยกจากงานจริงและเตรียม setup/runtime logins. Setup สร้าง schema/seed ได้; runtime ได้เฉพาะ CONNECT/USAGE กับ SELECT/INSERT/UPDATE ที่จำเป็นและ sequence privileges ไม่ได้ CREATE/DDL. ผู้ดูแลต้องกำหนด schema permissions ตาม Azure ก่อนใช้ setup login. ให้ IT เตรียม network ที่อนุญาต หรือ VPN/VNet สำหรับ private endpoint. ถ้ายังไม่มี `.env` จึงเริ่มจาก `.env.example` โดยใส่ runtime connection และสร้าง JWT_SECRET แบบสุ่มในเครื่อง ไม่ใช้ admin เป็น runtime

**Checkpoint ก่อน Day 2:** database ของตนเข้าถึงผ่าน TLS ได้, `.env` ใช้ runtime login และผู้สอนยืนยันว่ามีข้อมูลตัวอย่างพร้อมใช้. ถ้ายังไม่พร้อม ส่วน memory/test ทำต่อได้ แต่ PostgreSQL checkpoint ต้องระบุว่ายังไม่ผ่าน

## 4. Azure subscription — เตรียมสิทธิ์ก่อน Day 4

Day 4 ผู้เรียนสร้างและ deploy แอปเอง; การเตรียม account/database/identities ไม่ได้หมายความว่ามีแอปพร้อมแล้ว

- ใช้ subscription/region/student resource group และ pipeline/pull identities จาก `deployment.txt` ของ Student ZIP. ผู้เรียนมี Contributor เฉพาะกลุ่มของตน ไม่ต้องมีสิทธิ์สร้าง resource group ใหม่หรือแตะ shared infrastructure
- ตรวจ quota สำหรับ Container Apps และ ACR Basic/Tasks. Registered providers หลัก: Microsoft.App, Microsoft.ContainerRegistry, Microsoft.ManagedIdentity; ให้ผู้ดูแลจัดการที่ subscription scope. แผนนี้ใช้ Consumption-only, app ละ 0.25 vCPU/0.5Gi, min=0/max=1 และ logs destination=none ไม่สร้าง Log Analytics/dedicated profiles/private endpoints
- สร้างเฉพาะ ACR และ Container Apps environment/app ที่ได้รับอนุมัติใน student group เดิม. ใช้ pull identity ที่ได้รับ ไม่สร้าง identity ซ้ำ. ถ้ามี resource อยู่แล้วให้ตรวจเจ้าของก่อนใช้
- **ก่อน deploy private image:** หลังสร้าง ACR ให้ผู้สอนตรวจ **GitHub OIDC subject** ของ repository และ branch `main` จาก GitHub จริง แล้วเตรียมสิทธิ์ OIDC และ AcrPull ของ pull identity. รอผู้สอนยืนยันว่า access พร้อมก่อนเริ่ม image pull. ขั้นนี้ยังไม่ต้องมี app หรือ API URL
- OIDC ใช้ issuer `https://token.actions.githubusercontent.com` และ audience `api://AzureADTokenExchange`. **อย่าเดา subject จากชื่อ repository:** repository ใหม่หลัง 15 กรกฎาคม 2026 ใช้รูปแบบ `repo:OWNER@OWNER_ID/REPOSITORY@REPOSITORY_ID:ref:refs/heads/main`. Repository เก่าอาจใช้รูปแบบเดิมได้เฉพาะเมื่อ GitHub ยืนยัน. ผู้สอนตรวจ `sub_claim_prefix` กับ owner/repository IDs จาก GitHub OIDC settings/API แบบอ่านอย่างเดียว แล้วกรอก **full subject ของ main** และยืนยัน checkbox ว่าได้ตรวจรูปแบบและ IDs แล้ว. ID เหมือนเลขประจำพัสดุที่ช่วยแยกเจ้าของ แม้ชื่อหน้ากล่องจะเปลี่ยน. ดู [GitHub immutable subject claims](https://docs.github.com/en/actions/reference/security/oidc#immutable-subject-claims)
- Pipeline AZURE_CLIENT_ID ต้องตรง identity ที่ได้รับ ไม่ใช่ pull identity. หากเปลี่ยน repository/owner หรือรูปแบบ subject ให้ทบทวน access ใหม่ก่อนรัน Actions; ไม่เปลี่ยน GitHub OIDC settings กลับเป็นรูปแบบเก่าหรือขยาย trust เพื่อข้าม error
- **หลัง deploy API:** ให้ผู้สอนกด **Check Day 4 resources** เพื่อตรวจ app/registry/identity/HTTPS health และบันทึก API URL. ต้อง login/create/read และตรวจ persistence แยกจาก health; การตรวจนี้ไม่สร้างหรือแก้สิทธิ์แทนขั้นเตรียม
- Contributor ไม่ได้รวมสิทธิ์ role assignment. ให้ผู้สอน/ผู้ดูแลเตรียม AcrPull ที่ ACR ของ lab; registry แบบ ABAC ต้องใช้ role ตาม policy ไม่เปลี่ยน mode เพื่อข้ามปัญหา
- ตรวจ Container Apps → PostgreSQL ผ่าน TLS จริง แม้ laptop จะเชื่อมได้แล้ว. Shared public server ใช้ firewall ตามแผนชั้นเรียน; private network ใช้ environment/VNet ที่ IT เตรียม ไม่แก้ shared firewall หรือลด TLS จากบัญชีผู้เรียน
- GitHub Actions runner ต้องเข้าถึง ACR/Azure management และใช้ ACR Tasks ได้. หากองค์กรปิด ACR Tasks ให้ผู้จัดเตรียม runner ที่อนุญาตก่อนเรียน
- กำหนดเจ้าของค่าใช้จ่ายและวัน cleanup. min replicas=0 ไม่ทำให้ค่า ACR/database/logs เป็นศูนย์; ไม่ลบ shared server หรือ resource group อื่นจาก exercise

> **ใช้ subscription ของตนเอง:** เจ้าของอนุมัติ region/budget/resource group ใหม่ ให้ผู้ดูแลเตรียม pipeline/pull identities, OIDC และ roles ข้างต้น. ผู้เรียนสร้าง group/identity ได้เฉพาะเมื่อได้รับสิทธิ์และอนุมัติ ไม่ใช้ account ของเพื่อน. ถ้าใช้ private PostgreSQL ให้ IT เตรียม environment/network ก่อนเรียน

สิ่งที่ใส่ใน private GitHub repository ภายหลัง: Secrets `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`; Variables `ACR_NAME`, `RESOURCE_GROUP`, `CONTAINER_APP_NAME`. ใช้ pipeline client ID เดิม ไม่สร้าง Azure client secret สำหรับ OIDC และไม่ใส่ DATABASE_URL/JWT_SECRET ใน workflow

**Checkpoint ก่อน Day 4:** target/owner/budget/network/permissions พร้อม และมีผู้รับผิดชอบตรวจ exact GitHub subject แล้ว Preview/Prepare deployment access หลัง ACR พร้อม. ถ้าไม่พร้อม ให้เรียนอ่าน log/revision จากผู้สอน แต่ไม่ทำเครื่องหมายว่าตน deploy สำเร็จ

## 5. คำสั่งและข้อความลับ

ใน guide เครื่องหมาย `<...>` หมายถึงค่าที่ผู้เรียนต้องแทน ไม่ใช่คำสั่งพร้อมรันทันที. ให้ Codex แสดงเป้าหมายและคำสั่งที่เติม **เฉพาะค่าที่ไม่เป็นความลับ** ก่อนรัน. อย่าวาง password/token/connection string ใน chat หรือภาพหน้าจอ

Secret ให้กรอกใน Terminal ที่ไม่ echo หรือ Azure portal ด้วยตนเอง. หาก Codex จำเป็นต้องช่วยตรวจ config ให้ตรวจเฉพาะว่าตัวแปรมีอยู่หรือไม่ ไม่อ่านค่า
