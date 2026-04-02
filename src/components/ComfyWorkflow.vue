<script setup>
import { ref } from 'vue'
import { NModal } from 'naive-ui'
// 定义工作流类别
const workflows = [
  {
    id: 'workflow_1',
    title: '修复优化工作流',
    description:
      '对最后确定的图片进行优化，修复脸部手部眼睛以及其他细节问题，确保最终生成的图像质量达标',
    workflowImages: [
      { id: 'workflow_1_1', path: '/img/workflow_1_1.png', title: '修复优化工作流 - 节点组1' },
      { id: 'workflow_1_2', path: '/img/workflow_1_2.png', title: '修复优化工作流 - 节点组2' },
    ],
    comparisonImages: [
      { id: 'result_1_before', path: '/img/result_1_before.png', title: '处理前', type: 'before' },
      { id: 'result_1_after', path: '/img/result_1_after.png', title: '处理后', type: 'after' },
    ],
    additionalImages: [],
  },
  {
    id: 'workflow_2',
    title: '扩图工作流',
    description: '延伸需要的场景或者角色细节。',
    workflowImages: [
      { id: 'workflow_2_1', path: '/img/workflow_2_1.png', title: '扩图工作流 - 节点组1' },
      { id: 'workflow_2_2', path: '/img/workflow_2_2.png', title: '扩图工作流 - 节点组2' },
    ],
    comparisonImages: [
      { id: 'result_2_before', path: '/img/result_2_before.png', title: '处理前', type: 'before' },
      { id: 'result_2_after', path: '/img/result_2_after.png', title: '处理后', type: 'after' },
    ],
    additionalImages: [
      // 第二组对比图
      {
        id: 'result_2.2_before',
        path: '/img/result_2.2_before.png',
        title: '处理前',
        type: 'before',
      },
      { id: 'result_2.2_after', path: '/img/result_2.2_after.png', title: '处理后', type: 'after' },
    ],
  },
  {
    id: 'workflow_3',
    title: '换发换头工作流',
    description: '替换需要角色的脸部或者头发。',
    workflowImages: [
      { id: 'workflow_3_1', path: '/img/workflow_3_1.png', title: '换发换头工作流 - 节点组1' },
      { id: 'workflow_3_2', path: '/img/workflow_3_2.png', title: '换发换头工作流 - 节点组2' },
    ],
    comparisonImages: [
      { id: 'result_3_before', path: '/img/result_3_before.png', title: '处理前', type: 'before' },
      { id: 'result_3_after', path: '/img/result_3_after.png', title: '处理后', type: 'after' },
    ],
    additionalImages: [],
  },
  {
    id: 'workflow_4',
    title: '换衣工作流',
    description: '替换需要的角色的服装。',
    workflowImages: [
      { id: 'workflow_4_1', path: '/img/workflow_4_1.png', title: '换衣工作流 - 节点组1' },
      { id: 'workflow_4_2', path: '/img/workflow_4_2.png', title: '换衣工作流 - 节点组2' },
    ],
    comparisonImages: [
      { id: 'result_4_before', path: '/img/result_4_before.png', title: '处理前', type: 'before' },
      { id: 'result_4_after', path: '/img/result_4_after.png', title: '处理后', type: 'after' },
    ],
    additionalImages: [
      // 单张参考图
      { id: 'compare4', path: '/img/compare4.png', title: '参考效果', type: 'reference' },
    ],
  },
  {
    id: 'workflow_5',
    title: '重绘消除工作流',
    description: '重绘需要的图片细节，比如脸部，手部和眼睛等，或者移除图片中需要移除的元素。',
    workflowImages: [
      { id: 'workflow_5_1', path: '/img/workflow_5_1.png', title: '重绘消除工作流 - 节点组1' },
      { id: 'workflow_5_2', path: '/img/workflow_5_2.png', title: '重绘消除工作流 - 节点组2' },
    ],
    comparisonImages: [
      { id: 'result_5_before', path: '/img/result_5_before.png', title: '处理前', type: 'before' },
      { id: 'result_5_after', path: '/img/result_5_after.png', title: '处理后', type: 'after' },
    ],
    additionalImages: [],
  },
]
// 当前选中的工作流
const activeWorkflowIndex = ref(0)
// 选择工作流
const selectWorkflow = (index) => {
  activeWorkflowIndex.value = index
  currentWorkflowImageIndex.value = 0 // 重置工作流图片索引
}
// 工作流图片索引
const currentWorkflowImageIndex = ref(0)
// 切换工作流图片
const nextWorkflowImage = () => {
  const maxIndex = workflows[activeWorkflowIndex.value].workflowImages.length - 1
  currentWorkflowImageIndex.value =
    currentWorkflowImageIndex.value >= maxIndex ? 0 : currentWorkflowImageIndex.value + 1
}
const prevWorkflowImage = () => {
  const maxIndex = workflows[activeWorkflowIndex.value].workflowImages.length - 1
  currentWorkflowImageIndex.value =
    currentWorkflowImageIndex.value <= 0 ? maxIndex : currentWorkflowImageIndex.value - 1
}
// 图片查看模态框逻辑
const showModal = ref(false)
const selectedImage = ref(null)
const openLightbox = (image) => {
  selectedImage.value = image
  showModal.value = true
}
</script>
<template>
  <div id="comfy-workflow" class="py-20 relative overflow-hidden">
    <!-- 标题区域 -->
    <div class="container mx-auto px-6 mb-16 text-center">
      <div class="flex flex-col items-center mb-8">
        <div
          class="inline-block px-4 py-1.5 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-full text-sm text-blue-300 mb-4"
        >
          工作流展示
        </div>
        <h2 class="text-4xl md:text-5xl font-bold mb-4">
          <span class="text-white">专业</span>
          <span class="text-blue-400">ComfyUI工作流</span>
        </h2>
        <p class="text-lg text-text-muted max-w-2xl mx-auto">
          为不同创作需求精心打造的ComfyUI工作流程，让AI绘图创作更简单高效。
        </p>
      </div>

      <!-- 工作流类别导航 -->
      <div class="flex flex-wrap justify-center gap-3 mb-12">
        <button
          v-for="(workflow, index) in workflows"
          :key="workflow.id"
          @click="selectWorkflow(index)"
          :class="[
            'px-5 py-2.5 rounded-full text-sm font-medium transition-all',
            activeWorkflowIndex === index
              ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg shadow-blue-500/25'
              : 'bg-white/10 hover:bg-white/15 text-white/80 hover:text-white',
          ]"
        >
          {{ workflow.title }}
        </button>
      </div>
    </div>

    <!-- 当前工作流展示区域 -->
    <div class="container mx-auto px-6">
      <!-- 工作流介绍 -->
      <div class="mb-8 max-w-3xl mx-auto text-center">
        <h3 class="text-2xl font-bold mb-3">{{ workflows[activeWorkflowIndex].title }}</h3>
        <p class="text-text-muted">{{ workflows[activeWorkflowIndex].description }}</p>
      </div>

      <!-- 工作流图片轮播展示 -->
      <div class="relative mb-16 max-w-5xl mx-auto">
        <!-- 工作流图片容器 -->
        <div
          class="relative aspect-[16/9] overflow-hidden rounded-xl bg-cyber-gray border border-white/10"
        >
          <img
            :src="workflows[activeWorkflowIndex].workflowImages[currentWorkflowImageIndex].path"
            :alt="workflows[activeWorkflowIndex].workflowImages[currentWorkflowImageIndex].title"
            class="w-full h-full object-contain"
          />

          <!-- 图片索引指示器 -->
          <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
            <div
              v-for="(_, index) in workflows[activeWorkflowIndex].workflowImages"
              :key="index"
              :class="[
                'w-2.5 h-2.5 rounded-full transition-colors',
                index === currentWorkflowImageIndex ? 'bg-blue-500' : 'bg-white/30',
              ]"
            ></div>
          </div>
        </div>

        <!-- 左右箭头 -->
        <button
          @click="prevWorkflowImage"
          class="absolute left-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/50 hover:bg-black/70 flex items-center justify-center text-white transition-colors"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-5 h-5"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
          </svg>
        </button>
        <button
          @click="nextWorkflowImage"
          class="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-black/50 hover:bg-black/70 flex items-center justify-center text-white transition-colors"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-5 h-5"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
          </svg>
        </button>

        <!-- 当前图片标题 -->
        <div class="mt-3 text-center">
          <p class="text-sm text-text-muted">
            {{ workflows[activeWorkflowIndex].workflowImages[currentWorkflowImageIndex].title }}
            ({{ currentWorkflowImageIndex + 1 }}/{{
              workflows[activeWorkflowIndex].workflowImages.length
            }})
          </p>
        </div>
      </div>

      <!-- 对比图展示 -->
      <div class="mb-10">
        <h4 class="text-xl font-bold mb-4 text-center">效果对比</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          <div
            v-for="image in workflows[activeWorkflowIndex].comparisonImages"
            :key="image.id"
            :class="[
              'relative aspect-square overflow-hidden rounded-lg cursor-zoom-in group',
              image.type === 'before'
                ? 'border-2 border-red-500 shadow-md shadow-red-500/30'
                : 'border-2 border-green-500 shadow-md shadow-green-500/30',
            ]"
            @click="openLightbox(image)"
          >
            <img
              :src="image.path"
              :alt="image.title"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
            />
            <div
              :class="[
                'absolute top-0 left-0 px-3 py-1 text-white text-xs font-bold',
                image.type === 'before' ? 'bg-red-500' : 'bg-green-500',
              ]"
            >
              {{ image.title }}
            </div>

            <!-- 放大提示 -->
            <div
              class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
            >
              <div class="bg-black/60 rounded-full px-4 py-2 flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-5 h-5 text-white"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6"
                  />
                </svg>
                <span class="text-white text-sm">点击放大</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 额外对比图或参考图区域 -->
        <div v-if="workflows[activeWorkflowIndex].additionalImages.length > 0" class="mb-10">
          <!-- 第二个工作流额外对比图 -->
          <div
            v-if="activeWorkflowIndex === 1"
            class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto mb-8"
          >
            <div
              v-for="image in workflows[activeWorkflowIndex].additionalImages"
              :key="image.id"
              :class="[
                'relative aspect-square overflow-hidden rounded-lg cursor-zoom-in group',
                image.type === 'before'
                  ? 'border-2 border-red-500 shadow-md shadow-red-500/30'
                  : 'border-2 border-green-500 shadow-md shadow-green-500/30',
              ]"
              @click="openLightbox(image)"
            >
              <img
                :src="image.path"
                :alt="image.title"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
              />
              <div
                :class="[
                  'absolute top-0 left-0 px-3 py-1 text-white text-xs font-bold',
                  image.type === 'before' ? 'bg-red-500' : 'bg-green-500',
                ]"
              >
                {{ image.title }}
              </div>

              <!-- 放大提示 -->
              <div
                class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
              >
                <div class="bg-black/60 rounded-full px-4 py-2 flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="w-5 h-5 text-white"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6"
                    />
                  </svg>
                  <span class="text-white text-sm">点击放大</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 第三和第四个工作流单张参考图 -->
          <div
            v-if="activeWorkflowIndex === 2 || activeWorkflowIndex === 3"
            class="flex justify-center"
          >
            <div
              class="relative max-w-2xl overflow-hidden rounded-lg cursor-zoom-in group"
              @click="openLightbox(workflows[activeWorkflowIndex].additionalImages[0])"
            >
              <img
                :src="workflows[activeWorkflowIndex].additionalImages[0].path"
                :alt="workflows[activeWorkflowIndex].additionalImages[0].title"
                class="w-full object-contain transition-transform duration-500 group-hover:scale-105"
              />

              <!-- 放大提示 -->
              <div
                class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
              >
                <div class="bg-black/60 rounded-full px-4 py-2 flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="w-5 h-5 text-white"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6"
                    />
                  </svg>
                  <span class="text-white text-sm">点击放大</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 图片查看模态框 -->
    <n-modal v-model:show="showModal">
      <div
        class="max-w-6xl w-full p-2 outline-none relative flex justify-center items-center bg-black/50 backdrop-blur-sm rounded-lg"
        @click="showModal = false"
      >
        <template v-if="selectedImage">
          <img
            :src="selectedImage.path"
            class="absolute inset-0 w-full h-full object-contain blur-md opacity-30 scale-95"
          />
          <img
            :src="selectedImage.path"
            :alt="selectedImage.title"
            class="relative z-10 w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
            loading="eager"
          />
          <div
            v-if="selectedImage.type === 'before' || selectedImage.type === 'after'"
            class="absolute bottom-4 left-1/2 transform -translate-x-1/2"
            :class="[
              'px-6 py-2 rounded-full',
              selectedImage.type === 'before' ? 'bg-red-500/80' : 'bg-green-500/80',
            ]"
          >
            <p class="text-white font-medium">{{ selectedImage.title }}</p>
          </div>
        </template>
      </div>
    </n-modal>
  </div>
</template>

<style scoped>
/* 处理前/处理后图标样式增强 */
.before-badge {
  position: absolute;
  top: 0;
  left: 0;
  background: linear-gradient(135deg, rgba(220, 38, 38, 0.9), rgba(185, 28, 28, 0.8));
  color: white;
  padding: 6px 12px;
  font-weight: bold;
  border-radius: 0 0 8px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.after-badge {
  position: absolute;
  top: 0;
  left: 0;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.9), rgba(5, 150, 105, 0.8));
  color: white;
  padding: 6px 12px;
  font-weight: bold;
  border-radius: 0 0 8px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
</style>
