<script setup>
import { RouterView } from 'vue-router'
import { NConfigProvider, darkTheme, NDrawer, NDrawerContent } from 'naive-ui' //
import { ref, onMounted, onUnmounted } from 'vue'

// --- 状态管理 ---
const activeSection = ref('home')
const showMobileMenu = ref(false) // 新增：控制移动端菜单开关

// --- 滚动监听逻辑 ---
let observer = null

onMounted(() => {
  // 优化点：调整 rootMargin 使得高亮判定更符合用户视觉中心
  const options = {
    root: null,
    // 意思是：视口中间 20% 的区域是"触发区"
    // 只有当板块进入屏幕中间时，才高亮对应的导航
    rootMargin: '-45% 0px -45% 0px',
    threshold: 0,
  }

  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        activeSection.value = entry.target.id
      }
    })
  }, options)

  // 延迟挂载观察者
  setTimeout(() => {
    const sections = ['home', 'gallery', 'comic-workshop', 'workflow', 'video']
    sections.forEach((id) => {
      const el = document.getElementById(id)
      if (el) observer.observe(el)
    })
  }, 100)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})

// --- 辅助函数 ---

// 生成导航样式的 Class
const navClass = (id, isMobile = false) => {
  // 移动端的基础样式稍微大一点，方便点击
  const base = isMobile
    ? 'block text-xl py-4 border-b border-white/5'
    : 'nav-item transition-all duration-300'

  // 激活状态逻辑
  const isActive = activeSection.value === id

  if (isActive) {
    return `${base} text-neon-blue font-bold ${!isMobile ? 'scale-110' : ''}`
  } else {
    return `${base} text-text-muted hover:text-neon-blue`
  }
}

// 移动端点击导航后，关闭菜单
const handleMobileClick = (id) => {
  activeSection.value = id
  showMobileMenu.value = false
}
</script>

<template>
  <n-config-provider :theme="darkTheme">
    <nav
      class="fixed top-0 left-0 w-full h-16 flex items-center justify-between px-6 z-50 border-b border-white/10 bg-cyber-black/90 backdrop-blur-md transition-all"
    >
      <a
        href="#home"
        class="text-xl font-bold tracking-wider group cursor-pointer no-underline flex items-center gap-2"
      >
        <span
          class="text-neon-blue group-hover:shadow-[0_0_10px_#00f3ff] transition-all duration-300"
        >
          WUYING
        </span>
      </a>

      <!-- 桌面导航链接 - 这里需要添加漫剧工坊 -->
      <div class="hidden md:flex space-x-8">
        <a href="#home" :class="navClass('home')">首页</a>
        <a href="#gallery" :class="navClass('gallery')">作品画廊</a>
        <a href="#comic-workshop" :class="navClass('comic-workshop')">漫剧工坊</a>
        <a href="#workflow" :class="navClass('workflow')">工作流</a>
        <a href="#video" :class="navClass('video')">实机演示</a>
      </div>

      <!-- 移动端菜单按钮 -->
      <button
        class="md:hidden text-white hover:text-neon-blue transition-colors focus:outline-none"
        @click="showMobileMenu = true"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-8 w-8"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
      </button>
    </nav>

    <n-drawer v-model:show="showMobileMenu" width="280" placement="right">
      <n-drawer-content title="菜单导航" closable>
        <div class="flex flex-col space-y-2 mt-4">
          <a href="#home" :class="navClass('home', true)" @click="handleMobileClick('home')"
            >首页</a
          >
          <a
            href="#gallery"
            :class="navClass('gallery', true)"
            @click="handleMobileClick('gallery')"
            >作品画廊</a
          >
          <a
            href="#comic-workshop"
            :class="navClass('comic-workshop', true)"
            @click="handleMobileClick('comic-workshop')"
            >漫剧工坊</a
          >
          <a
            href="#workflow"
            :class="navClass('workflow', true)"
            @click="handleMobileClick('workflow')"
            >工作流</a
          >
          <a href="#video" :class="navClass('video', true)" @click="handleMobileClick('video')"
            >实机演示</a
          >
        </div>

        <div class="mt-12 pt-8 border-t border-white/10 text-center">
          <p class="text-gray-500 text-xs mb-4">WUYING STUDIO</p>
          <div class="flex justify-center gap-4">
            <span class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-xs"
              >WX</span
            >
            <span class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-xs"
              >B</span
            >
          </div>
        </div>
      </n-drawer-content>
    </n-drawer>
    <main class="pt-16 min-h-screen">
      <RouterView />
    </main>

    <footer class="py-8 bg-black border-t border-white/10 text-center relative z-10">
      <p class="text-gray-500 text-sm font-mono">Wuying. Designed for AIGC & Engineering.</p>
      <div
        class="mt-4 flex justify-center space-x-6 opacity-50 hover:opacity-100 transition-opacity"
      >
        <a href="#" class="text-white hover:text-neon-blue transition-colors">电话</a>
        <a href="#" class="text-white hover:text-neon-blue transition-colors">邮箱</a>
        <a href="#" class="text-white hover:text-neon-blue transition-colors">联系我</a>
      </div>
    </footer>
  </n-config-provider>
</template>

<style scoped>
.nav-item {
  @apply text-sm font-medium uppercase tracking-wide cursor-pointer relative;
}

/* 增加一个简单的下划线动效 */
.nav-item::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: #00f3ff; /* neon-blue */
  transition: width 0.3s ease;
}

.nav-item:hover::after {
  width: 100%;
}
</style>
