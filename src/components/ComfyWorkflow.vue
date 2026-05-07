<script setup>
import { ref, computed } from 'vue'
import { NModal } from 'naive-ui'

const workflows = [
  {
    id: 'workflow_2',
    title: '扩图',
    description: '延伸需要的场景或者角色细节，实现画面画幅的自然扩展',
    workflowImages: [
      { id: 'wf_2_1', path: '/img/workflow_2_1.png', title: '节点组 1' },
      { id: 'wf_2_2', path: '/img/workflow_2_2.png', title: '节点组 2' },
    ],
    comparisonImages: [
      { id: 'r2_b', path: '/img/result_2_before.png', title: '处理前', type: 'before' },
      { id: 'r2_m', path: '/img/result_2_mid.png', title: '修改中', type: 'mid' },
      { id: 'r2_a', path: '/img/result_2_after.png', title: '处理后', type: 'after' },
    ],
  },
  {
    id: 'workflow_3',
    title: '换发换头',
    description: '替换角色的脸部或者头发，保持整体风格一致性',
    workflowImages: [
      { id: 'wf_3_1', path: '/img/workflow_3_1.png', title: '节点组 1' },
      { id: 'wf_3_2', path: '/img/workflow_3_2.png', title: '节点组 2' },
    ],
    comparisonImages: [
      { id: 'r3_b', path: '/img/result_3_before.png', title: '处理前', type: 'before' },
      { id: 'r3_a', path: '/img/result_3_after.png', title: '处理后', type: 'after' },
    ],
  },
  {
    id: 'workflow_4',
    title: '换衣',
    description: '替换角色的服装，支持高度自定义的材质与款式',
    workflowImages: [
      { id: 'wf_4_1', path: '/img/workflow_4_1.png', title: '节点组 1' },
      { id: 'wf_4_2', path: '/img/workflow_4_2.png', title: '节点组 2' },
    ],
    comparisonImages: [
      { id: 'r4_b', path: '/img/result_4_before.png', title: '处理前 1', type: 'before' },
      { id: 'r4_b2', path: '/img/result_4.2_before.png', title: '处理前 2', type: 'before' },
      { id: 'r4_a', path: '/img/result_4_after.png', title: '处理后 1', type: 'after' },
      { id: 'r4_a2', path: '/img/result_4.2_after.png', title: '处理后 2', type: 'after' },
    ],
  },
  {
    id: 'workflow_5',
    title: '重绘消除',
    description: '重绘图片细节或移除图片中不需要的元素',
    workflowImages: [
      { id: 'wf_5_1', path: '/img/workflow_5_1.png', title: '节点组 1' },
      { id: 'wf_5_2', path: '/img/workflow_5_2.png', title: '节点组 2' },
    ],
    comparisonImages: [
      { id: 'r5_b', path: '/img/result_5_before.png', title: '处理前', type: 'before' },
      { id: 'r5_a', path: '/img/result_5_after.png', title: '处理后', type: 'after' },
    ],
  },
  {
    id: 'workflow_6',
    title: '图案提取',
    description: '从复杂背景中精准提取图案、Logo或特定元素，生成透明资产',
    workflowImages: [
      { id: 'wf_6_1', path: '/img/workflow_6_1.png', title: '提取节点 1' },
      { id: 'wf_6_2', path: '/img/workflow_6_2.png', title: '提取节点 2' },
    ],
    comparisonImages: [
      { id: 'r6_b', path: '/img/result_6_before.png', title: '原图 1', type: 'before' },
      { id: 'r6_a', path: '/img/result_6_after.png', title: '提取效果 1', type: 'after' },
      { id: 'r6_b2', path: '/img/result_6.2_before.png', title: '原图 2', type: 'before' },
      { id: 'r6_a2', path: '/img/result_6.2_after.png', title: '提取效果 2', type: 'after' },
    ],
  },
  {
    id: 'workflow_7',
    title: '背景替换',
    description: '保持主体不变，利用 AI 重新生成高质量的场景背景',
    workflowImages: [
      { id: 'wf_7_1', path: '/img/workflow_7_1.png', title: '背景生成节点 1' },
      { id: 'wf_7_2', path: '/img/workflow_7_2.png', title: '背景生成节点 2' },
    ],
    comparisonImages: [
      { id: 'r7_b1', path: '/img/result_7_before1.png', title: '原图 1', type: 'before' },
      { id: 'r7_b2', path: '/img/result_7_before2.png', title: '原图 2', type: 'before' },
      { id: 'r7_a', path: '/img/result_7_after.png', title: '合成效果', type: 'after' },
      { id: 'r7_a2', path: '/img/result_7_after2.png', title: '合成效果', type: 'after' },
    ],
  },
]

const activeIndex = ref(0)
const activeWorkflow = computed(() => workflows[activeIndex.value])

const selectWorkflow = (index) => {
  activeIndex.value = index
}

const showModal = ref(false)
const modalImage = ref(null)

const openLightbox = (image) => {
  modalImage.value = image
  showModal.value = true
}
</script>

<template>
  <div class="container mx-auto px-6">
    <div class="text-center mb-16">
      <h2 class="text-4xl md:text-6xl font-extrabold tracking-tighter mb-6">
        商业级 <span class="text-gradient-warm">工作流解决方案</span>
      </h2>
      <p class="text-text-muted text-lg max-w-3xl mx-auto font-light leading-relaxed">
        为不同创作需求精心打造的 ComfyUI 工作流程，让 AI 绘图创作更简单高效。
      </p>
    </div>

    <div class="flex justify-center mb-6">
      <div
        class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-accent/10 border border-accent/30 text-accent-light text-sm font-medium animate-bounce shadow-[0_0_15px_rgba(212,160,74,0.15)]"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"
          />
        </svg>
        点击下方标签，切换查看不同工作流
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 14l-7 7m0 0l-7-7m7 7V3"
          />
        </svg>
      </div>
    </div>

    <div class="flex flex-wrap justify-center gap-3 mb-14">
      <button
        v-for="(wf, index) in workflows"
        :key="wf.id"
        @click="selectWorkflow(index)"
        :class="[
          'px-5 py-2.5 rounded-full text-sm font-medium transition-all duration-300',
          activeIndex === index
            ? 'bg-accent text-warm-black shadow-lg shadow-accent/20 scale-105'
            : 'bg-warm-gray border border-warm-border/40 text-text-muted hover:text-text-main hover:border-accent/40',
        ]"
      >
        {{ wf.title }}
      </button>
    </div>

    <div class="mb-10 max-w-3xl mx-auto text-center">
      <h3 class="text-2xl font-bold mb-3 text-text-main">{{ activeWorkflow.title }}工作流</h3>
      <p class="text-text-muted">{{ activeWorkflow.description }}</p>
    </div>

    <div class="mb-14">
      <h4 class="text-lg font-semibold mb-5 text-text-soft flex items-center gap-2">
        <span class="w-1 h-5 bg-accent rounded-full block"></span>
        工作流节点
      </h4>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <div
          v-for="img in activeWorkflow.workflowImages"
          :key="img.id"
          class="group relative overflow-hidden rounded-xl bg-warm-gray border border-warm-border/30 cursor-zoom-in"
          @click="openLightbox(img)"
        >
          <div class="aspect-[16/9] overflow-hidden">
            <img
              :src="img.path"
              :alt="img.title"
              class="w-full h-full object-contain bg-warm-dark transition-transform duration-500 group-hover:scale-105"
            />
          </div>
          <div class="px-4 py-3 flex items-center justify-between">
            <span class="text-sm text-text-muted">{{ img.title }}</span>
            <span class="text-xs text-accent opacity-0 group-hover:opacity-100 transition-opacity"
              >点击放大</span
            >
          </div>
        </div>
      </div>
    </div>

    <div class="mb-6">
      <h4 class="text-lg font-semibold mb-5 text-text-soft flex items-center gap-2">
        <span class="w-1 h-5 bg-accent rounded-full block"></span>
        效果对比
      </h4>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div
          v-for="image in activeWorkflow.comparisonImages"
          :key="image.id"
          class="group relative overflow-hidden rounded-xl cursor-zoom-in border border-warm-border/30 hover:border-accent/40 transition-colors"
          @click="openLightbox(image)"
        >
          <div class="aspect-square overflow-hidden">
            <img
              :src="image.path"
              :alt="image.title"
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
            />
          </div>
          <div
            :class="[
              'absolute top-2 left-2 px-2.5 py-1 rounded-md text-xs font-bold',
              image.type === 'before'
                ? 'bg-red-500/80 text-white'
                : image.type === 'after'
                  ? 'bg-emerald-500/80 text-white'
                  : 'bg-accent/80 text-warm-black',
            ]"
          >
            {{ image.title }}
          </div>
        </div>
      </div>
    </div>
  </div>

  <n-modal v-model:show="showModal">
    <div
      class="max-w-6xl w-full p-2 outline-none flex justify-center items-center bg-warm-black/85 backdrop-blur-sm rounded-lg"
      @click="showModal = false"
    >
      <template v-if="modalImage">
        <img
          :src="modalImage.path"
          :alt="modalImage.title"
          class="w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
        />
      </template>
    </div>
  </n-modal>
</template>
