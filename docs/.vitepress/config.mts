import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(defineConfig({
  title: 'Nextflow · Service Desk Lite',
  description: 'คู่มือ Codex Mobile App Workshop 4 วัน: Git, FastAPI, PostgreSQL, Flutter และ Azure Container Apps',
  lang: 'th-TH',
  base: '/codex-mobile-app-workshop/',
  cleanUrls: true,
  vite: {
    server: { host: '127.0.0.1', port: 4173, strictPort: true },
    // Mermaid loads CommonJS dependencies dynamically; bundle them for dev too.
    optimizeDeps: { include: ['mermaid'] }
  },
  srcExclude: ['public/**'],
  // VitePress treats .py links as pages; the public-file checker verifies this download.
  ignoreDeadLinks: [/^\/files\/check_api\.py$/],
  head: [['meta', { name: 'theme-color', content: '#11786b' }]],
  themeConfig: {
    siteTitle: 'Nextflow · Service Desk Lite',
    nav: [
      { text: 'เส้นทาง 4 วัน', link: '/' },
      { text: 'ก่อนเริ่ม', link: '/resources/readiness' },
      { text: 'ไฟล์ฝึก', link: '/resources/downloads' }
    ],
    sidebar: [
  {
    "text": "เริ่มต้น",
    "items": [
      {
        "text": "ภาพรวมหลักสูตร",
        "link": "/"
      },
      {
        "text": "ก่อนวันแรก",
        "link": "/resources/readiness"
      },
      {
        "text": "วิธีเรียน",
        "link": "/resources/learning-path"
      }
    ]
  },
  {
    "text": "Day 1 · Git",
    "collapsed": false,
    "items": [
      {
        "text": "ภาพรวมและเวลาเรียน",
        "link": "/exercises/day-01-git/"
      },
      {
        "text": "1. เปิดโปรเจคและเก็บภาพแรก",
        "link": "/exercises/day-01-git/exercise-01"
      },
      {
        "text": "2. เปลี่ยนข้อความผ่าน branch และ PR",
        "link": "/exercises/day-01-git/exercise-02"
      },
      {
        "text": "3. รวมงานที่แก้บรรทัดเดียวกัน",
        "link": "/exercises/day-01-git/exercise-03"
      },
      {
        "text": "4. กำหนดวิธีร่วมงานกับ Codex",
        "link": "/exercises/day-01-git/exercise-04"
      },
      {
        "text": "สรุปและส่งต่องาน",
        "link": "/exercises/day-01-git/summary"
      }
    ]
  },
  {
    "text": "Day 2 · Python API",
    "collapsed": false,
    "items": [
      {
        "text": "ภาพรวมและเวลาเรียน",
        "link": "/exercises/day-02-api/"
      },
      {
        "text": "1. Python bridge และ API แรก",
        "link": "/exercises/day-02-api/exercise-01"
      },
      {
        "text": "2. Route, model และ validation",
        "link": "/exercises/day-02-api/exercise-02"
      },
      {
        "text": "3. เก็บข้อมูลลง PostgreSQL",
        "link": "/exercises/day-02-api/exercise-03"
      },
      {
        "text": "4. Login, ownership และ tests",
        "link": "/exercises/day-02-api/exercise-04"
      },
      {
        "text": "สรุปและส่งต่องาน",
        "link": "/exercises/day-02-api/summary"
      }
    ]
  },
  {
    "text": "Day 3 · Flutter",
    "collapsed": false,
    "items": [
      {
        "text": "ภาพรวมและเวลาเรียน",
        "link": "/exercises/day-03-flutter/"
      },
      {
        "text": "1. Dart และหน้าจอแรก",
        "link": "/exercises/day-03-flutter/exercise-01"
      },
      {
        "text": "2. Navigation และ State",
        "link": "/exercises/day-03-flutter/exercise-02"
      },
      {
        "text": "3. เชื่อม API กับงานของผู้ใช้",
        "link": "/exercises/day-03-flutter/exercise-03"
      },
      {
        "text": "4. Native plugin และ mobile build",
        "link": "/exercises/day-03-flutter/exercise-04"
      },
      {
        "text": "สรุปและส่งต่องาน",
        "link": "/exercises/day-03-flutter/summary"
      }
    ]
  },
  {
    "text": "Day 4 · Azure",
    "collapsed": false,
    "items": [
      {
        "text": "ภาพรวมและเวลาเรียน",
        "link": "/exercises/day-04-azure/"
      },
      {
        "text": "1. แพ็กและทดสอบ container",
        "link": "/exercises/day-04-azure/exercise-01"
      },
      {
        "text": "2. เปิด API บน Azure",
        "link": "/exercises/day-04-azure/exercise-02"
      },
      {
        "text": "3. Deploy จาก GitHub",
        "link": "/exercises/day-04-azure/exercise-03"
      },
      {
        "text": "4. เชื่อม Android และดูแลรุ่นที่ใช้งาน",
        "link": "/exercises/day-04-azure/exercise-04"
      },
      {
        "text": "สรุปและส่งต่องาน",
        "link": "/exercises/day-04-azure/summary"
      }
    ]
  },
  {
    "text": "ไฟล์และแหล่งอ้างอิง",
    "items": [
      {
        "text": "ดาวน์โหลดไฟล์ฝึก",
        "link": "/resources/downloads"
      },
      {
        "text": "Project brief",
        "link": "/resources/project-brief"
      },
      {
        "text": "API contract",
        "link": "/resources/api-contract"
      },
      {
        "text": "AGENTS.md template",
        "link": "/resources/agents-template"
      },
      {
        "text": "บันทึกผลการเรียน",
        "link": "/resources/review-log"
      },
      {
        "text": "โจทย์ต่อยอด",
        "link": "/resources/change-request"
      },
      {
        "text": "แหล่งอ้างอิง",
        "link": "/resources/sources"
      }
    ]
  }
],
    outline: { level: [2, 3], label: 'ในหน้านี้' },
    docFooter: { prev: 'ก่อนหน้า', next: 'ถัดไป' },
    sidebarMenuLabel: 'เส้นทางการเรียน',
    returnToTopLabel: 'กลับด้านบน',
    darkModeSwitchLabel: 'โหมดสี',
    lightModeSwitchTitle: 'โหมดสว่าง',
    darkModeSwitchTitle: 'โหมดมืด',
    search: { provider: 'local', options: { locales: { root: { translations: {
      button: { buttonText: 'ค้นหา', buttonAriaLabel: 'ค้นหาแบบฝึกหัด' },
      modal: { noResultsText: 'ไม่พบผลสำหรับ', resetButtonTitle: 'ล้างคำค้น', displayDetails: 'แสดงรายละเอียด',
        footer: { selectText: 'เลือก', navigateText: 'เลื่อน', closeText: 'ปิด' } }
    } } } } },
    footer: { message: 'Nextflow · Codex Mobile App Workshop · ข้อมูลสมมติสำหรับฝึก', copyright: '4 วัน · 16 Exercises · หนึ่งโปรเจคต่อเนื่อง' }
  },
  mermaid: { theme: 'neutral', startOnLoad: false, fontFamily: 'Noto Sans Thai, sans-serif' },
  mermaidPlugin: { class: 'course-diagram' }
}))
