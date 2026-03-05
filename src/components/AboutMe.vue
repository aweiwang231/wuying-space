<script setup>
// 头像地址
const avatarUrl = '/gallery/avatar.jpg'
</script>

<template>
  <div class="w-full max-w-6xl mx-auto px-6 relative z-10">
    <div
      class="bg-cyber-gray/50 border border-white/10 rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-start gap-8 backdrop-blur-md shadow-2xl"
    >
      <div class="flex-shrink-0">
        <div
          class="w-24 h-24 md:w-32 md:h-32 rounded-full p-[2px] bg-gradient-to-br from-white/50 to-white/10 shadow-lg"
        >
          <div class="w-full h-full rounded-full bg-black overflow-hidden">
            <img :src="avatarUrl" alt="Avatar" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>

      <div class="flex-1 space-y-5">
        <div>
          <h1
            class="text-3xl md:text-4xl font-bold text-white flex items-center gap-3 tracking-wide"
          >
            你好，我是 梧影 👋
          </h1>
          <p class="text-gray-400 font-mono text-sm mt-2 tracking-wider uppercase">
            AIGC Video Creator / Workflow Specialist
          </p>
        </div>

        <p class="text-gray-300 leading-relaxed text-base md:text-lg max-w-3xl font-light">
          我是一名专注于完成AI图像生成到AI视频生成优化和自动化的内容创作者。
          从静态的ComfyUI工作流到动态的配合n8n视频工作流。以及使用Runway &
          可灵视频演绎，我致力于探索视觉叙事的边界。
        </p>

        <div class="flex flex-wrap gap-3 pt-3">
          <span class="skill-pill-highlight">n8n 视频工作流</span>
          <span class="skill-pill-highlight">ComfyUI工作流</span>
          <span class="skill-pill-highlight">Runway</span>
          <span class="skill-pill-highlight">可灵 AI</span>
          <span class="skill-pill-highlight">即梦 AI</span>
          <span class="skill-pill-highlight">Stable Diffusion</span>
          <span class="skill-pill-highlight">Midjourney</span>
          <span class="skill-pill-highlight">Photoshop</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 核心技能：更亮的背景和边框，突出显示 */
.skill-pill-highlight {
  @apply px-4 py-1.5 rounded-full bg-neon-blue/10 border border-neon-blue/50 text-neon-blue text-sm font-medium transition-all hover:bg-neon-blue/20 hover:scale-105 cursor-default;
}

/* 基础技能：白色半透明，干净利落 */
.skill-pill {
  @apply px-4 py-1.5 rounded-full bg-white/5 border border-white/20 text-gray-300 text-sm font-medium transition-all hover:border-white/50 hover:text-white hover:bg-white/10 cursor-default;
}
</style>
