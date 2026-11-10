<script setup lang="ts">
import { withBase } from 'vitepress'
defineProps<{ file: string }>()
</script>
<template><p class="file-download"><a :href="withBase('/files/' + file)" :download="file">ดาวน์โหลด {{ file }} ↓</a></p></template>
