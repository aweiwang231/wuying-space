<script setup>
import AboutMe from '../components/AboutMe.vue'
import ImageGallery from '../components/ImageGallery.vue'
import ComfyWorkflow from '../components/ComfyWorkflow.vue'
import ProjectCaseStudy from '../components/ProjectCaseStudy.vue'
</script>

<template>
  <div class="flex flex-col relative">
    <div class="bg-noise"></div>

    <section
      id="home"
      class="min-h-screen flex items-center justify-center relative overflow-hidden pt-20"
    >
      <div
        class="absolute top-[-20%] left-1/2 -translate-x-1/2 w-[80%] h-[500px] bg-gradient-to-b from-amber-900/15 to-transparent blur-[120px] -z-10 pointer-events-none"
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
      <ComfyWorkflow />
    </section>

    <section id="project-case" class="py-24 relative bg-warm-dark/30">
      <ProjectCaseStudy />
    </section>
  </div>
</template>
