<script setup>
const avatarUrl = '/gallery/avatar.jpg'
</script>

<template>
  <div class="w-full max-w-5xl mx-auto px-6 relative z-10">
    <div
      class="bg-warm-gray/60 border border-warm-border/40 rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-start gap-8 backdrop-blur-md shadow-2xl"
    >
      <div class="flex-shrink-0">
        <div
          class="w-24 h-24 md:w-32 md:h-32 rounded-full p-[2px] bg-gradient-to-br from-accent/60 to-accent-dim/30 shadow-lg"
        >
          <div class="w-full h-full rounded-full bg-warm-dark overflow-hidden">
            <img :src="avatarUrl" alt="Avatar" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>

      <div class="flex-1 space-y-5">
        <div>
          <h1
            class="text-3xl md:text-4xl font-bold text-text-main flex items-center gap-3 tracking-wide"
          >
            你好，我是 丁伟航
          </h1>
          <p class="text-text-muted font-mono text-sm mt-2 tracking-wider uppercase">
            AIGC Video Creator / Workflow Specialist
          </p>
        </div>

        <p class="text-text-soft leading-relaxed text-base md:text-lg max-w-3xl font-light">
          我是一名专注于AI图像生成到AI视频生成优化和自动化的内容创作者，致力于探索视觉叙事的边界。
        </p>

        <div class="flex flex-wrap gap-2.5 pt-3">
          <span class="skill-pill">ComfyUI工作流</span>
          <span class="skill-pill">Runway</span>
          <span class="skill-pill">可灵 AI</span>
          <span class="skill-pill">即梦 AI</span>
          <span class="skill-pill">Midjourney</span>
          <span class="skill-pill">Photoshop</span>
          <span class="skill-pill">剪映</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skill-pill {
  @apply px-4 py-1.5 rounded-full bg-accent/10 border border-accent/40 text-accent-light text-sm font-medium transition-all hover:bg-accent/20 hover:scale-105 cursor-default;
}
</style>
