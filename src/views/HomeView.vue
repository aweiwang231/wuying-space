<script setup>
import AboutMe from '../components/AboutMe.vue'
import ImageGallery from '../components/ImageGallery.vue'
import ComfyWorkflow from '../components/ComfyWorkflow.vue'
import VideoGallery from '../components/VideoGallery.vue'
</script>

<template>
  <div class="flex flex-col relative">
    <div class="bg-noise"></div>

    <section
      id="home"
      class="min-h-screen flex items-center justify-center relative overflow-hidden pt-20"
    >
      <div
        class="absolute top-[-20%] left-1/2 -translate-x-1/2 w-[80%] h-[600px] bg-gradient-to-b from-indigo-900/20 to-transparent blur-[120px] -z-10 pointer-events-none"
      ></div>

      <AboutMe />
    </section>

    <section id="gallery" class="py-24 relative">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl md:text-5xl font-bold mb-16 text-center tracking-tight">
          精选 <span class="text-gradient-pro">视觉作品</span>
        </h2>
        <ImageGallery />
      </div>
    </section>

    <section id="workflow" class="py-24 relative">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl md:text-5xl font-bold mb-16 text-center tracking-tight">
          商业级 <span class="text-gradient-warm">工作流解决方案</span>
        </h2>
        <ComfyWorkflow />
      </div>
    </section>

    <section id="video" class="py-24 mb-20">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl md:text-5xl font-bold mb-16 text-center tracking-tight">
          实机 <span class="text-gradient-pro">演示 DEMO</span>
        </h2>
        <VideoGallery />
      </div>
    </section>
  </div>
</template>
