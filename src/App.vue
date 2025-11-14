<script setup>
import { RouterView } from 'vue-router'
// 我们只需要这些基础组件，其他的都去掉了
import {
  NConfigProvider,
  NLayout,
  NLayoutHeader,
  NLayoutContent,
  NMessageProvider,
  NFlex,
  darkTheme,
} from 'naive-ui'
</script>

<template>
  <!-- 这里我们直接写死 :theme="darkTheme"，永远都是暗黑模式 -->
  <n-config-provider :theme="darkTheme">
    <n-message-provider>
      <n-layout style="height: 100vh">
        <!-- 顶部导航栏 -->
        <n-layout-header class="nav-header" bordered>
          <div class="logo">梧影的作品集</div>
          <n-flex align="center" class="nav-links">
            <!-- 最简单的导航链接，稳定可靠 -->
            <a href="#about-me">关于我</a>
            <a href="#gallery">图片作品</a>
            <a href="#workflow">工作流</a>
          </n-flex>
        </n-layout-header>

        <!-- 主要内容区域 -->
        <n-layout-content class="main-content">
          <RouterView />
        </n-layout-content>
      </n-layout>
    </n-message-provider>
  </n-config-provider>
</template>

<style scoped>
.nav-header {
  padding: 0 32px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;

  position: sticky;
  top: 0;
  z-index: 1000;

  /* 毛玻璃效果的背景，写死暗黑主题的颜色 */
  background-color: rgba(22, 22, 26, 0.8);
  backdrop-filter: blur(12px);
  /* 边框颜色也写死 */
  border-bottom: 1px solid #333;
}

.logo {
  font-size: 20px;
  font-weight: 600;
}

.nav-links a {
  /* 链接颜色写死 */
  color: #ccc;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 6px;
  transition: all 0.2s ease-in-out;
}
.nav-links a:hover {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
}

.main-content {
  scroll-behavior: smooth;
  overflow-y: auto;
}
</style>
