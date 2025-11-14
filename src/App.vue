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
/* 导航栏容器：保持原有样式，调整移动端布局 */
.nav-header {
  padding: 0 32px;
  height: auto; /* 关键：去掉固定高度，让内容自适应 */
  min-height: 60px; /* 最小高度保证宽屏时正常 */
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap; /* 允许 logo 和导航项换行（极端窄屏时） */
  gap: 12px; /* 换行后 logo 和导航的间距 */

  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: rgba(22, 22, 26, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid #333;
}

.logo {
  font-size: 20px;
  font-weight: 600;
}

/* 关键：控制 Naive UI 的 NFlex 组件，让导航项可换行 */
.custom-nav-links {
  display: flex !important; /* 强制 flex 布局 */
  flex-wrap: wrap !important; /* 允许导航项换行（核心） */
  gap: 8px !important; /* 导航项之间的间距（缩小更紧凑） */
  justify-content: center !important;
}

/* 导航链接样式 */
.nav-links a {
  color: #ccc;
  text-decoration: none;
  padding: 6px 12px; /* 调整内边距，更紧凑 */
  border-radius: 6px;
  transition: all 0.2s ease-in-out;
  white-space: nowrap; /* 不允许文字换行（保持链接整体性） */
  font-size: 16px;
}

.nav-links a:hover {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
}

.main-content {
  scroll-behavior: smooth;
  overflow-y: auto;
}

/* 移动端专项优化（768px 以下） */
@media (max-width: 768px) {
  .nav-header {
    padding: 10px 16px !important; /* 左右留边，不贴屏 */
  }

  .logo {
    font-size: 18px; /* 缩小 logo 文字 */
  }

  .nav-links a {
    font-size: 14px !important; /* 缩小链接文字 */
    padding: 5px 10px !important; /* 进一步缩小内边距 */
  }

  /* 让导航项在移动端占满宽度，居中排列 */
  .custom-nav-links {
    width: 100% !important; /* 占满整行 */
  }
}

/* 超小屏优化（576px 以下，比如旧手机） */
@media (max-width: 576px) {
  .nav-links a {
    font-size: 13px !important;
  }
}
</style>
