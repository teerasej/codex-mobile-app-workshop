<script setup lang="ts">
import { withBase } from 'vitepress'
const days = [{"number": 1, "name": "Git", "href": "/exercises/day-01-git/", "heading": "วางInstructionและเก็บประวัติ", "body": "Branch, commit, PR, conflict และข้อตกลงร่วมงานกับ Codex", "result": "ได้ repository และแผน API"}, {"number": 2, "name": "Python API", "href": "/exercises/day-02-api/", "heading": "สร้างบริการข้อมูล", "body": "FastAPI, validation, PostgreSQL, login และ tests", "result": "ได้ API ที่ตรวจข้อมูลและสิทธิ์"}, {"number": 3, "name": "Flutter", "href": "/exercises/day-03-flutter/", "heading": "นำแอปมาอยู่ในมือผู้ใช้", "body": "Dart, หน้าจอ, navigation, HTTP/JSON และ Android", "result": "ได้ browser preview และ Android app"}, {"number": 4, "name": "Azure", "href": "/exercises/day-04-azure/", "heading": "เปิดบริการบน Cloud", "body": "Docker, ACR, Container Apps, deployment และ logs", "result": "ได้ HTTPS API และหลักฐาน release"}]
</script>
<template>
  <section class="journey-section" aria-labelledby="journey-title">
    <div class="journey-heading"><span class="eyebrow">ONE PROJECT · FOUR DAYS</span><h2 id="journey-title">ต่อยอดทีละวัน ตรวจได้ทีละขั้น</h2><p>16 Exercises · 40 Practices หลัก + 1 Practice เสริม · 20 ชั่วโมงเรียน</p></div>
    <div class="journey-grid">
      <a v-for="day in days" :key="day.number" :href="withBase(day.href)" class="day-card">
        <div class="day-top"><span class="day-number">DAY {{ day.number }}</span><span class="day-tech">{{ day.name }}</span></div>
        <h3>{{ day.heading }}</h3><p>{{ day.body }}</p><div class="day-result">{{ day.result }} <span aria-hidden="true">↗</span></div>
      </a>
    </div>
  </section>
</template>
