<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import images from '../practice-images.json'

const props = withDefaults(defineProps<{
  asset: string
  eager?: boolean
}>(), { eager: false })
type Asset = {
  alt: string
  width: number
  height: number
  sources: { url: string; width: number; height: number }[]
}
const image = computed(() => (images as Record<string, Asset>)[props.asset])
const failed = ref(false)
const element = ref<HTMLImageElement>()
onMounted(() => {
  // An eager SSR image can fail before Vue attaches its error listener.
  if (element.value?.complete && element.value.naturalWidth === 0) {
    failed.value = true
  }
})
watch(() => props.asset, () => { failed.value = false })
const srcset = computed(() => image.value?.sources
  .map(source => `${withBase(source.url)} ${source.width}w`).join(', '))
</script>

<template>
  <figure
    v-if="image"
    class="practice-illustration"
    :data-practice="asset"
    :style="{ aspectRatio: `${image.width} / ${image.height}` }"
  >
    <img
      v-if="!failed"
      ref="element"
      :src="withBase(image.sources[0].url)"
      :srcset="srcset"
      sizes="(min-width: 1344px) 686px, (min-width: 1280px) calc(100vw - 658px), (min-width: 1088px) 686px, (min-width: 960px) calc(100vw - 402px), (min-width: 768px) 686px, calc(100vw - 50px)"
      :width="image.width"
      :height="image.height"
      :alt="image.alt"
      :loading="eager ? 'eager' : 'lazy'"
      decoding="async"
      @error="failed = true"
    >
    <figcaption v-else class="practice-illustration-fallback">
      {{ image.alt }}
    </figcaption>
  </figure>
</template>

<style scoped>
.practice-illustration {
  display: grid;
  place-items: center;
  width: 100%;
  margin: 20px 0 28px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: #fffefb;
}
.practice-illustration img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: contain;
}
.practice-illustration-fallback {
  max-width: 90%;
  padding: 24px;
  color: #173b36;
  font-size: 14px;
  text-align: center;
  overflow-wrap: anywhere;
}
</style>
