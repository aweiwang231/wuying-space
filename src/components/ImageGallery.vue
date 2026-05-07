<script setup>
import { ref } from 'vue'
import { NModal } from 'naive-ui'

const artworks = Array.from({ length: 20 }).map((_, i) => {
  const id = i + 1
  return {
    id,
    title: `Project Demo ${id}`,
    thumbnail: `/gallery/thumbs/${id}.webp`,
    full: `/gallery/full/${id}.webp`,
  }
})

const gallerySections = [
  {
    title: '基于 FLUX2',
    // 获取前4张 (1-4) 和最后4张 (17-20)，组成两行
    items: [...artworks.slice(0, 4), ...artworks.slice(16, 20)],
  },
  { title: '基于 Midjourney', items: artworks.slice(4, 8) },
  { title: '基于 pony/illustrious 等多种动漫模型', items: artworks.slice(8, 16) },
]

const showModal = ref(false)
const selectedArt = ref(null)
const preloadedImages = new Set()

const preloadFullImage = (url) => {
  if (preloadedImages.has(url)) return
  const img = new Image()
  img.src = url
  preloadedImages.add(url)
}

const openLightbox = (art) => {
  selectedArt.value = art
  showModal.value = true
}
</script>

<template>
  <div>
    <div class="space-y-16">
      <div v-for="(section, index) in gallerySections" :key="index">
        <h3 class="text-xl md:text-2xl font-bold mb-6 text-text-main/90 flex items-center gap-3">
          <span class="w-1.5 h-6 bg-accent rounded-full block"></span>
          {{ section.title }}
        </h3>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div
            v-for="art in section.items"
            :key="art.id"
            class="group relative aspect-square overflow-hidden rounded-xl bg-warm-gray border border-warm-border/30 cursor-zoom-in"
            @click="openLightbox(art)"
            @mouseenter="preloadFullImage(art.full)"
          >
            <img
              :src="art.thumbnail"
              alt="Artwork"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
              loading="lazy"
            />
            <div
              class="absolute inset-0 bg-warm-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center"
            >
              <span
                class="inline-flex items-center px-5 py-2 rounded-full border border-accent/30 bg-warm-black/70 text-accent-light text-sm font-bold tracking-wider"
              >
                查看原图
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <n-modal v-model:show="showModal">
      <div
        class="max-w-6xl w-full p-2 outline-none relative flex justify-center items-center bg-warm-black/85 backdrop-blur-sm rounded-lg"
        @click="showModal = false"
      >
        <template v-if="selectedArt">
          <img
            :src="selectedArt.full"
            class="relative z-10 w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
          />
        </template>
      </div>
    </n-modal>
  </div>
</template>
