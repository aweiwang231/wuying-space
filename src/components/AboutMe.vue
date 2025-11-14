<script setup>
import { NCard, NFlex, NTag, NButton } from 'naive-ui'

const avatarUrl = new URL('/images/avatar.jpg', import.meta.url).href
</script>

<template>
  <n-card class="about-card">
    <n-flex align="center">
      <div class="avatar-container">
        <img :src="avatarUrl" alt="个人头像" class="avatar" />
      </div>

      <div class="info-container">
        <h2>你好，我是 [梧影] 👋</h2>
        <!-- 【优化】重写了这段介绍，更突出你的复合背景和解决问题的能力 -->
        <p class="description">
          我是一名来自软件工程专业的 AIGC 探索者，致力于成为技术与创意之间的桥梁。 我不仅能熟练运用
          Stable Diffusion (ComfyUI/WebUI) 与 Midjourney 进行内容创作，
          更能利用我的编程背景，搭建和优化高效的工作流，解决实际的生产力问题。
        </p>

        <n-flex class="skills">
          <n-tag type="info" round>Vue.js</n-tag>
          <n-tag type="success" round>Stable Diffusion</n-tag>
          <n-tag type="warning" round>ComfyUI</n-tag>
          <n-tag type="error" round>Photoshop</n-tag>
          <n-tag round>Midjourney</n-tag>
        </n-flex>

        <n-flex style="margin-top: 20px">
          <!-- 【修改】将 a 标签的 href 指向你的简历，并增加了 download 属性 -->
          <!-- 假设你放进 public 文件夹的文件名叫“我的简历.pdf” -->
          <a href="/我的简历.pdf" download="悟影-AIGC方向-简历.pdf">
            <n-button type="primary">
              <template #icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="1em"
                  height="1em"
                  viewBox="0 0 24 24"
                >
                  <path fill="currentColor" d="M5 20h14v-2H5m14-9h-4V3H9v8H5l7 7Z"></path>
                </svg>
              </template>
              下载我的简历
            </n-button>
          </a>
        </n-flex>
      </div>
    </n-flex>
  </n-card>
</template>

<style scoped>
/* 样式部分保持不变 */
.about-card {
  margin-bottom: 40px;
}
.avatar-container {
  margin-right: 32px;
}
.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #555;
}
.info-container h2 {
  font-size: 28px;
  font-weight: bold;
  margin: 0 0 12px 0;
}
.description {
  font-size: 16px;
  color: #ccc;
  line-height: 1.6;
  max-width: 600px;
}
.skills {
  margin-top: 16px;
}
</style>
