<script setup>
import { RouterView } from 'vue-router'
import { NConfigProvider, darkTheme, NDrawer, NDrawerContent } from 'naive-ui'
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('home')
const showMobileMenu = ref(false)

const navLinks = [
  { id: 'home', label: '首页' },
  { id: 'gallery', label: '作品画廊' },
  { id: 'workflow', label: '工作流' },
  { id: 'project-case', label: '项目案例' },
]

let observer = null

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id
        }
      })
    },
    { rootMargin: '-40% 0px -50% 0px', threshold: 0 },
  )

  setTimeout(() => {
    navLinks.forEach(({ id }) => {
      const el = document.getElementById(id)
      if (el) observer.observe(el)
    })
  }, 100)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})

const navClass = (id, isMobile = false) => {
  const base = isMobile
    ? 'block text-lg py-4 border-b border-warm-border/30'
    : 'nav-item transition-all duration-300'
  const isActive = activeSection.value === id
  return isActive
    ? `${base} text-accent font-bold ${!isMobile ? 'scale-105' : ''}`
    : `${base} text-text-muted hover:text-accent`
}

const handleMobileClick = (id) => {
  activeSection.value = id
  showMobileMenu.value = false
}
</script>

<template>
  <n-config-provider :theme="darkTheme">
    <nav
      class="fixed top-0 left-0 w-full h-16 flex items-center justify-between px-6 z-50 border-b border-warm-border/30 bg-warm-black/90 backdrop-blur-md"
    >
      <a
        href="#home"
        class="text-xl font-bold tracking-wider cursor-pointer no-underline flex items-center gap-2"
      >
        <span class="text-accent hover:text-accent-light transition-colors duration-300">
          WUYING
        </span>
      </a>

      <div class="hidden md:flex space-x-8">
        <a v-for="link in navLinks" :key="link.id" :href="`#${link.id}`" :class="navClass(link.id)">
          {{ link.label }}
        </a>
      </div>

      <button
        class="md:hidden text-text-main hover:text-accent transition-colors focus:outline-none"
        @click="showMobileMenu = true"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-7 w-7"
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
      <n-drawer-content title="导航" closable>
        <div class="flex flex-col space-y-1 mt-4">
          <a
            v-for="link in navLinks"
            :key="link.id"
            :href="`#${link.id}`"
            :class="navClass(link.id, true)"
            @click="handleMobileClick(link.id)"
          >
            {{ link.label }}
          </a>
        </div>
        <div class="mt-12 pt-8 border-t border-warm-border/30 text-center">
          <p class="text-text-muted text-xs mb-4">WUYING STUDIO</p>
        </div>
      </n-drawer-content>
    </n-drawer>

    <main class="pt-16 min-h-screen">
      <RouterView />
    </main>

    <footer class="py-10 bg-warm-dark border-t border-warm-border/30 text-center relative z-10">
      <p class="text-text-muted text-sm font-mono">Wuying. Designed for AIGC & Engineering.</p>
      <div
        class="mt-4 flex justify-center space-x-6 opacity-60 hover:opacity-100 transition-opacity"
      >
        <a href="#" class="text-text-soft hover:text-accent transition-colors">电话</a>
        <a href="#" class="text-text-soft hover:text-accent transition-colors">邮箱</a>
        <a href="#" class="text-text-soft hover:text-accent transition-colors">联系我</a>
      </div>
    </footer>
  </n-config-provider>
</template>

<style scoped>
.nav-item {
  @apply text-sm font-medium uppercase tracking-wide cursor-pointer relative;
}

.nav-item::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: #d4a04a;
  transition: width 0.3s ease;
}

.nav-item:hover::after {
  width: 100%;
}
</style>
