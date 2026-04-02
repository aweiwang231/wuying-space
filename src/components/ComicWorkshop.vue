<script setup>
import { ref } from 'vue'
import { NModal } from 'naive-ui'

// 定义工作流程图片数据
const workflowImages = [
  // 第一阶段 - 元素塑造 (3张图)
  {
    id: 1,
    title: '角色元素',
    path: '/ComicWorkshop/1.png',
    group: 'elements',
  },
  {
    id: 2,
    title: '道具元素',
    path: '/ComicWorkshop/2.png',
    group: 'elements',
  },
  {
    id: 3,
    title: '背景元素',
    path: '/ComicWorkshop/3.png',
    group: 'elements',
  },
  // 第二阶段 - 导入元素设置剧集
  {
    id: 4,
    title: '导入元素设置剧集',
    path: '/ComicWorkshop/4.png',
    group: 'import',
  },
  // 第三阶段 - 分镜设计
  {
    id: 5,
    title: '分镜设计',
    path: '/ComicWorkshop/5.png',
    group: 'storyboard',
  },
  // 第四阶段 - 融图融视频 (2张图)
  {
    id: 6,
    title: '融图示例',
    path: '/ComicWorkshop/6.png',
    group: 'fusion',
  },
  {
    id: 7,
    title: '融视频示例',
    path: '/ComicWorkshop/7.png',
    group: 'fusion',
  },
  // 第五阶段 - 后期合成
  {
    id: 8,
    title: '后期合成',
    path: '/ComicWorkshop/8.png',
    group: 'composite',
  },
]

// 图片查看模态框逻辑
const showModal = ref(false)
const selectedImage = ref(null)

const openLightbox = (image) => {
  selectedImage.value = image
  showModal.value = true
}
</script>

<template>
  <div id="comic-workshop" class="min-h-screen py-20 relative overflow-hidden">
    <!-- 标题区域 -->
    <div class="container mx-auto px-6 mb-16 text-center">
      <div class="flex flex-col items-center mb-12">
        <div
          class="inline-block px-4 py-1.5 bg-gradient-to-r from-purple-500/20 to-blue-500/20 rounded-full text-sm text-purple-300 mb-4"
        >
          创作流程
        </div>
        <h2 class="text-4xl md:text-5xl font-bold mb-4">
          <span class="text-white">漫剧</span>
          <span class="text-purple-400">创作工坊</span>
        </h2>
        <p class="text-lg text-text-muted max-w-2xl mx-auto">
          从角色设计到后期合成，我的AIGC漫剧创作流程融合了多种工具与技术，打造沉浸式视觉叙事体验。
        </p>
      </div>
    </div>

    <!-- 流程步骤 1: 元素塑造 -->
    <div class="container mx-auto px-6 mb-24">
      <!-- 示例工具区域 - 移动到序号上方并居中 -->
      <div class="mb-10 max-w-xl mx-auto text-center">
        <div class="bg-white/5 p-4 rounded-lg border border-white/10">
          <h4 class="text-sm uppercase tracking-wider text-neon-blue mb-3">示例工具</h4>
          <div class="flex flex-wrap justify-center gap-2">
            <span class="px-3 py-1 bg-white/10 rounded text-sm">漫屋</span>
            <span class="px-3 py-1 bg-white/10 rounded text-sm">Midjourney</span>
            <span class="px-3 py-1 bg-white/10 rounded text-sm">StableDiffusion</span>
          </div>
        </div>
      </div>

      <div class="flex flex-col md:flex-row items-start">
        <div class="md:w-2/5 mb-10 md:mb-0 md:pr-12 sticky top-24">
          <div
            class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 text-white text-2xl font-bold mb-6"
          >
            1
          </div>
          <h3 class="text-3xl font-bold mb-4">元素塑造</h3>
          <p class="text-text-muted mb-6">
            使用AI辅助工具生成高质量的角色形象、场景背景和道具元素，为漫剧创作打下坚实基础。
          </p>
        </div>

        <!-- 三张图片横向展示 -->
        <div class="md:w-3/5">
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div
              v-for="img in workflowImages.filter((img) => img.group === 'elements')"
              :key="img.id"
              class="group relative aspect-square overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
              @click="openLightbox(img)"
            >
              <img
                :src="img.path"
                :alt="img.title"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
              />
              <div
                class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
              >
                <span
                  class="inline-flex items-center px-4 py-1.5 rounded-full border border-white/20 bg-black/60 text-white text-sm font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
                >
                  {{ img.title }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 流程步骤 2: 导入元素，设置剧集 -->
    <div class="container mx-auto px-6 mb-24">
      <div class="flex flex-col md:flex-row items-start">
        <div class="md:w-2/5 mb-10 md:mb-0 md:pr-12 sticky top-24">
          <div
            class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 text-white text-2xl font-bold mb-6"
          >
            2
          </div>
          <h3 class="text-3xl font-bold mb-4">导入元素，设置剧集</h3>
          <p class="text-text-muted mb-6">
            将创作的角色、道具和背景元素导入系统，设定故事主线和剧集结构，为后续分镜设计做准备。
          </p>
        </div>

        <div class="md:w-3/5">
          <div
            v-for="img in workflowImages.filter((img) => img.group === 'import')"
            :key="img.id"
            class="group relative aspect-video overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
            @click="openLightbox(img)"
          >
            <img
              :src="img.path"
              :alt="img.title"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div
              class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
            >
              <span
                class="inline-flex items-center px-6 py-2 rounded-full border border-white/20 bg-black/60 text-white text-lg md:text-xl font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
              >
                查看原图
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 流程步骤 3: 分镜设计 -->
    <div class="container mx-auto px-6 mb-24">
      <div class="flex flex-col md:flex-row items-start">
        <div class="md:w-2/5 mb-10 md:mb-0 md:pr-12 sticky top-24">
          <div
            class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 text-white text-2xl font-bold mb-6"
          >
            3
          </div>
          <h3 class="text-3xl font-bold mb-4">分镜设计</h3>
          <p class="text-text-muted mb-6">
            根据剧情需要设计每一格分镜，构建场景构图，选择角度选择与情感表达，优化视觉叙事效果。
          </p>
        </div>

        <div class="md:w-3/5">
          <div
            v-for="img in workflowImages.filter((img) => img.group === 'storyboard')"
            :key="img.id"
            class="group relative aspect-video overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
            @click="openLightbox(img)"
          >
            <img
              :src="img.path"
              :alt="img.title"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div
              class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
            >
              <span
                class="inline-flex items-center px-6 py-2 rounded-full border border-white/20 bg-black/60 text-white text-lg md:text-xl font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
              >
                查看原图
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 流程步骤 4: 融图融视频 -->
    <div class="container mx-auto px-6 mb-24">
      <div class="flex flex-col md:flex-row items-start">
        <div class="md:w-2/5 mb-10 md:mb-0 md:pr-12 sticky top-24">
          <div
            class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 text-white text-2xl font-bold mb-6"
          >
            4
          </div>
          <h3 class="text-3xl font-bold mb-4">融图融视频</h3>
          <p class="text-text-muted mb-6">
            通过先进的AI技术，将各元素自然融合到场景中，同时为部分场景添加动态效果，增强画面表现力。
          </p>
        </div>

        <div class="md:w-3/5">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div
              v-for="img in workflowImages.filter((img) => img.group === 'fusion')"
              :key="img.id"
              class="group relative aspect-square overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
              @click="openLightbox(img)"
            >
              <img
                :src="img.path"
                :alt="img.title"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
              />
              <div
                class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
              >
                <span
                  class="inline-flex items-center px-4 py-1.5 rounded-full border border-white/20 bg-black/60 text-white text-sm font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
                >
                  {{ img.title }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 流程步骤 5: 后期合成 -->
    <div class="container mx-auto px-6 mb-12">
      <div class="flex flex-col md:flex-row items-start">
        <div class="md:w-2/5 mb-10 md:mb-0 md:pr-12 sticky top-24">
          <div
            class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 text-white text-2xl font-bold mb-6"
          >
            5
          </div>
          <h3 class="text-3xl font-bold mb-4">后期合成</h3>
          <p class="text-text-muted mb-6">
            进行最终的色彩调整、特效添加和过渡效果设计，完成整部漫剧的输出与发布准备。
          </p>
        </div>

        <div class="md:w-3/5">
          <div
            v-for="img in workflowImages.filter((img) => img.group === 'composite')"
            :key="img.id"
            class="group relative aspect-video overflow-hidden rounded-xl bg-cyber-gray border border-white/5 cursor-zoom-in"
            @click="openLightbox(img)"
          >
            <img
              :src="img.path"
              :alt="img.title"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div
              class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 backdrop-blur-sm transition-opacity duration-300 flex items-center justify-center p-4 text-center"
            >
              <span
                class="inline-flex items-center px-6 py-2 rounded-full border border-white/20 bg-black/60 text-white text-lg md:text-xl font-bold tracking-wider drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] transition-transform duration-300 group-hover:scale-105"
              >
                查看原图
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 图片查看模态框 -->
    <n-modal v-model:show="showModal">
      <div
        class="max-w-6xl w-full p-2 outline-none relative flex justify-center items-center bg-black/50 rounded-lg"
        @click="showModal = false"
      >
        <template v-if="selectedImage">
          <img
            :src="selectedImage.path"
            class="absolute inset-0 w-full h-full object-contain blur-md opacity-50 scale-95"
          />
          <img
            :src="selectedImage.path"
            class="relative z-10 w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
            loading="eager"
          />
        </template>
      </div>
    </n-modal>
  </div>
</template>
