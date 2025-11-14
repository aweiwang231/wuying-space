<script setup>
import ComfyWorkflow from '../components/ComfyWorkflow.vue'
import AboutMe from '../components/AboutMe.vue'
import ImageGallery from '../components/ImageGallery.vue'
// 1. 引入我们的新武器
import SectionWrapper from '../components/SectionWrapper.vue'
</script>

<template>
  <div class="home-container">
    <!-- “关于我”区块 -->
    <SectionWrapper id="about-me">
      <!-- 我们把 AboutMe 组件放在这里，它不需要标题 -->
      <AboutMe />
    </SectionWrapper>

    <!-- “图片作品”区块 -->
    <SectionWrapper id="gallery">
      <template #title>图片作品展示</template>
      <ImageGallery />
      <p class="gallery-hint">点击图片查看大图及技术参数</p>
    </SectionWrapper>

    <!-- “ComfyUI工作流”区块 -->
    <SectionWrapper id="workflow">
      <template #title>ComfyUI 工作流拆解</template>
      <!-- 使用我们刚创建的组件 -->
      <ComfyWorkflow />
    </SectionWrapper>

    <!-- “Photoshop联合”区块 (暂时放个占位符) -->
  </div>
</template>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}
/* ... 媒体查询部分和之前一样 ... */
</style>
