---
title: "แหล่งอ้างอิงทางเทคนิค"
prev: false
next: false
---

# แหล่งอ้างอิงทางเทคนิค

[กลับสารบัญ](/)

เอกสารเหล่านี้ใช้ตรวจ terminology และวิธีทำงานของเครื่องมือ ไม่ใช่แหล่งที่กำหนด business scenario. บทฝึก Service Desk Lite, data contract, fixtures และ checkpoints ออกแบบสำหรับหลักสูตรนี้. ตรวจแหล่งข้อมูลวันที่ 2026-09-13–14; ก่อนสอนให้ตรวจ UI/versions และ policy ของบัญชีที่ใช้จริงอีกครั้ง

| เรื่อง | เอกสารเจ้าของผลิตภัณฑ์ | ใช้กับ |
| --- | --- | --- |
| ChatGPT desktop / เลือก Codex | [Quickstart](https://learn.chatgpt.com/docs/quickstart) | readiness, Day 1 |
| Local project ต่างจาก uploaded sources | [Projects and chats](https://learn.chatgpt.com/docs/projects) | readiness |
| PowerShell native บน Windows | [Windows desktop app](https://learn.chatgpt.com/docs/windows/windows-app) | readiness |
| Core instructions | [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Day 1 |
| Pull requests | [Creating a PR](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) | Day 1 |
| FastAPI/password hashing/JWT | [OAuth2 and JWT tutorial](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) | Day 2 |
| Browser origin | [CORS](https://fastapi.tiangolo.com/tutorial/cors/) | Day 3 |
| PostgreSQL connection encryption | [Azure PostgreSQL TLS](https://learn.microsoft.com/en-us/azure/postgresql/security/security-tls) | readiness, Day 2 |
| Flutter networking | [Fetch data](https://docs.flutter.dev/cookbook/networking/fetch-data) | Day 3 |
| Android build | [Build and release](https://docs.flutter.dev/deployment/android) | Day 3 |
| iOS Simulator setup (Optional · macOS) | [Set up iOS development](https://docs.flutter.dev/platform-integration/ios/setup) | readiness, Day 3 |
| Simulator .app build | [Flutter iOS build command](https://github.com/flutter/flutter/blob/stable/packages/flutter_tools/lib/src/commands/build_ios.dart) | Day 3 · Exercise 4 · Practice เสริม |
| Native URL launch | [url_launcher](https://pub.dev/packages/url_launcher) | Day 3 |
| Container runtime entitlement | [Docker Desktop license](https://docs.docker.com/subscription-billing/desktop-license/) | readiness |
| Azure CLI app commands | [az containerapp](https://learn.microsoft.com/en-us/cli/azure/containerapp) | Day 4 |
| ACR build | [az acr](https://learn.microsoft.com/en-us/cli/azure/acr) | Day 4 |
| Private image access | [Managed identity image pull](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity-image-pull) | Day 4 |
| Ingress | [Configure ingress](https://learn.microsoft.com/en-us/azure/container-apps/ingress-how-to) | Day 4 |
| GitHub deployment | [Container Apps GitHub Actions](https://learn.microsoft.com/en-us/azure/container-apps/github-actions) | Day 4 |
| OIDC federation | [Azure login with OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect) | readiness, Day 4 |
| Secrets | [Manage secrets](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets) | Day 4 |
| Revisions | [Manage revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions-manage) | Day 4 |
| Logs | [Log streaming](https://learn.microsoft.com/en-us/azure/container-apps/log-streaming) | Day 4 |
| Scaling | [Scale rules](https://learn.microsoft.com/en-us/azure/container-apps/scale-app) | Day 4 |

ไม่มีการคัดลอกขั้นตอน Microsoft 365 Copilot จาก repository ตัวอย่างมาเป็นข้อกำหนดของหลักสูตรนี้. Screenshots ของบัญชีผู้เรียนยังไม่ถูกรวบรวม จึงใช้ขั้นตอนข้อความและ URL/checkpoint ที่ตรวจได้แทนภาพที่สมมติขึ้น


## การตรวจเพื่อจัดทำเว็บไซต์

ตรวจ VitePress รุ่น stable และเอกสาร ChatGPT local project/quickstart อีกครั้งเมื่อ 2026-10-09 การจัดหน้าเว็บไม่ใช่ผลซ้อม Windows/Android/Azure หรือการยืนยันสิทธิ์บัญชีผู้เรียน

ตรวจ Flutter iOS setup, คำสั่ง build สำหรับ Simulator และการรองรับ iOS ของ `url_launcher` เมื่อ 2026-10-24 เพื่อเพิ่ม Practice เสริมใน Day 3 การตรวจเอกสารและเว็บไซต์ยังไม่ใช่ผลทดลอง build iOS จริง
