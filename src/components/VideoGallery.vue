<script setup>
import { ref } from 'vue'

const videos = ref([
  {
    id: 1,
    title: '成品1',
    videoUrl: '/videos/demo1.mp4',
    posterUrl: '/videos/poster1.webp',
    isPlaying: false,
  },
  {
    id: 2,
    title: '成品2',
    videoUrl: '/videos/demo2.mp4',
    posterUrl: '/videos/poster2.webp',
    isPlaying: false,
  },
])

const playVideo = (video) => {
  video.isPlaying = true
}
</script>

<template>
  <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
    <div
      v-for="video in videos"
      :key="video.id"
      class="bg-cyber-gray/30 border border-white/5 p-4 md:p-6 rounded-2xl transition-colors hover:border-white/10 flex flex-col items-center"
    >
      <div
        class="w-full max-w-sm aspect-[9/16] bg-black rounded-lg overflow-hidden relative group shadow-lg"
      >
        <video
          v-if="video.isPlaying"
          :src="video.videoUrl"
          controls
          autoplay
          class="w-full h-full object-contain bg-black outline-none"
        ></video>

        <div v-else class="w-full h-full relative cursor-pointer" @click="playVideo(video)">
          <img
            :src="video.posterUrl"
            class="w-full h-full object-cover opacity-60 group-hover:opacity-80 transition-opacity bg-gray-900"
            alt="Video Poster"
            @error="(e) => (e.target.src = 'https://picsum.photos/400/711?grayscale&blur=2')"
          />

          <div class="absolute inset-0 flex items-center justify-center">
            <div
              class="w-16 h-16 rounded-full bg-neon-blue/20 backdrop-blur border border-neon-blue flex items-center justify-center group-hover:scale-110 transition-transform shadow-[0_0_15px_rgba(0,243,255,0.3)]"
            >
              <span class="text-white text-2xl ml-1">▶</span>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-6 px-1 w-full text-center">
        <h3 class="text-white font-bold text-lg md:text-xl tracking-wide">{{ video.title }}</h3>
      </div>
    </div>
  </div>
</template>
