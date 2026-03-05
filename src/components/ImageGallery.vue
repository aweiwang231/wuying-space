<script setup>
import { ref } from 'vue'
import { NModal } from 'naive-ui'

// 数据和分组逻辑保持，不展示
const artworks = Array.from({ length: 16 }).map((_, i) => {
  const id = i + 1
  return {
    id: id,
    title: `Project Demo ${id}`,
    category: id <= 4 ? 'FLUX' : id <= 8 ? 'MJ' : 'Pony',
    thumbnail: `/gallery/thumbs/${id}.webp`,
    full: `/gallery/full/${id}.webp`,
  }
})

const gallerySections = [
  {
    title: '基于 FLUX2',
    items: artworks.slice(0, 4),
  },
  {
    title: '基于 Midjourney',
    items: artworks.slice(4, 8),
  },
  {
    title: '基于 pony/illustrious 等多种动漫模型',
    items: artworks.slice(8, 16),
  },
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
        <h3 class="text-xl md:text-2xl font-bold mb-6 text-white/90 flex items-center gap-3">
          <span class="w-1.5 h-6 bg-neon-blue rounded-full block"></span>
          {{ section.title }}
        </h3>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div
            v-for="art in section.items"
            :key="art.id"
            class="group relative aspect-square overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
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
              class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
            >
              <span
                class="inline-flex items-center px-6 py-2 rounded-full border border-white/20 bg-black/60 text-white text-lg md:text-xl font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
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
        class="max-w-6xl w-full p-2 outline-none relative flex justify-center items-center bg-black/50 rounded-lg"
        @click="showModal = false"
      >
        <template v-if="selectedArt">
          <img
            :src="selectedArt.thumbnail"
            class="absolute inset-0 w-full h-full object-contain blur-md opacity-50 scale-95"
          />
          <img
            :src="selectedArt.full"
            class="relative z-10 w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
            loading="eager"
          />
        </template>
      </div>
    </n-modal>
  </div>
</template>
