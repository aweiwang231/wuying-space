<script setup>
import { ref, reactive } from 'vue'
import { NModal } from 'naive-ui'

// -------------------------------------------------------------
// 1. 数据定义 (保持不变)
// -------------------------------------------------------------
const coreLogic = {
  title: 'Flux工作流效果展示区',
  description:
    '基于 Flux.1 Dev 全参数模型构建。专为 24GB+ 显存环境设计，涵盖了从智能局部重绘、画面扩展、风格迁移到 4K/8K 极致放大的全链路商业解决方案。',
  tags: ['Flux.1 Dev', 'Ultimate Upscale', 'High-VRAM', 'Commercial Quality'],
}

const workflowVariants = [
  {
    id: 1,
    imgId: 2,
    title: 'OneReward 局部重绘流 (Smart Inpainting)',
    file: 'Flux-fill-OneReward局部重绘流.json',
    desc: '解决传统重绘边缘生硬问题。利用 OneReward 模型计算遮罩边缘的潜空间特征，实现像素级的无痕融合，特别适合复杂的衣物褶皱或背景纹理修复。',
    features: ['OneReward 引导', '无痕融合', '复杂纹理修复'],
    workflowCount: 2,
  },
  {
    id: 2,
    imgId: 3,
    title: 'OneReward 扩展图像流 (Outpainting)',
    file: 'Flux-fill-OneReward扩展图像流.json',
    desc: '基于语义的画布无限扩展。分析画面透视与光源方向，自动补全缺失的场景元素，支持 2x 甚至 4x 的画布外扩。',
    features: ['智能扩图', '透视保持', '环境补全'],
    workflowCount: 2,
  },
  {
    id: 3,
    imgId: 4,
    title: 'OneReward 万物迁移流 (Style Transfer)',
    file: 'Flux-fill-OneReward万物迁移流.json',
    desc: '风格与主体的精准移植。通过 Attention 注入机制，将参考图的特征“注射”到目标图像的潜空间中。',
    features: ['风格迁移', '主体移植', '权重可控'],
    workflowCount: 2,
  },
  {
    id: 4,
    imgId: 5,
    title: 'OneReward 万物移除流 (Object Removal)',
    file: 'Flux-fill-OneReward万物移除流.json',
    desc: '智能物体移除与背景重构。利用 Flux 强大的联想能力重绘被遮挡的背景，完美还原复杂纹理。',
    features: ['智能移除', '背景重构', '逻辑填补'],
    workflowCount: 2,
  },
  {
    id: 5,
    imgId: 1,
    title: 'Flux Ultimate SD Upscale (4K/8K 放大)',
    file: 'Flux-UltimateUpscale-HighRes.json',
    desc: "突破显存限制的极致放大方案。采用 'Ultimate SD Upscale' 节点进行分块绘制（Tiling），结合 4x-UltraSharp 模型进行物理放大，并在 Denoise 0.4 的区间内重绘细节，消除拼缝并增加 8K 级纹理。",
    features: ['分块绘制', '4x-UltraSharp', '无显存上限'],
    workflowCount: 1,
    isUpscale: true,
    resBefore: '960 × 1288',
    resAfter: '1920 × 2576',
  },
]

// -------------------------------------------------------------
// 2. 状态管理
// -------------------------------------------------------------
const slideState = reactive({})
workflowVariants.forEach((item) => {
  slideState[item.imgId] = 0
})

const nextSlide = (imgId, max) => {
  slideState[imgId] = (slideState[imgId] + 1) % max
}
const prevSlide = (imgId, max) => {
  slideState[imgId] = (slideState[imgId] - 1 + max) % max
}

// -------------------------------------------------------------
// 3. 模态框逻辑
// -------------------------------------------------------------
const showModal = ref(false)
const modalImage = ref('')
const modalLabel = ref('')
const modalType = ref('')

const openImage = (imgSrc, label, type) => {
  modalImage.value = imgSrc
  modalLabel.value = label
  modalType.value = type
  showModal.value = true
}
</script>

<template>
  <section id="workflow" class="min-h-screen py-20 relative bg-cyber-black overflow-hidden">
    <div
      class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[500px] bg-cyan-900/10 blur-[120px] pointer-events-none"
    ></div>

    <div class="container mx-auto px-4 md:px-8 relative z-10">
      <div class="mb-24 text-center max-w-3xl mx-auto">
        <h2 class="text-sm font-bold tracking-[0.3em] text-cyan-500 mb-4 uppercase">
          FLUX.1 DEV PIPELINE
        </h2>
        <h1 class="text-4xl md:text-6xl font-black text-white mb-8 tracking-tight">
          {{ coreLogic.title }}
        </h1>
        <p
          class="text-gray-400 text-lg leading-relaxed bg-gray-900/50 backdrop-blur border border-gray-800 rounded-2xl p-6 md:p-8 shadow-2xl"
        >
          {{ coreLogic.description }}
        </p>
      </div>

      <div class="flex flex-col gap-32">
        <div v-for="(item, index) in workflowVariants" :key="item.id" class="relative group">
          <div
            v-if="index !== workflowVariants.length - 1"
            class="absolute left-[50%] top-[100%] h-32 w-px bg-gradient-to-b from-gray-700 to-transparent hidden md:block"
          ></div>

          <div
            class="bg-gray-900/20 border border-gray-800 rounded-3xl overflow-hidden hover:border-gray-700 transition-colors duration-500"
          >
            <div class="p-6 md:p-10 pb-0">
              <div class="mb-8">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                  <h3 class="text-2xl font-bold text-white flex items-center gap-3">
                    <span class="text-cyan-500 text-lg font-mono">0{{ index + 1 }}.</span>
                    {{ item.title }}
                  </h3>
                  <div class="flex gap-2">
                    <span
                      v-for="feat in item.features"
                      :key="feat"
                      class="text-xs bg-gray-800 text-gray-300 px-2 py-1 rounded"
                    >
                      {{ feat }}
                    </span>
                  </div>
                </div>
                <p class="text-gray-400 leading-relaxed max-w-4xl">
                  {{ item.desc }}
                </p>
              </div>
            </div>

            <div
              class="relative w-full aspect-[21/9] bg-gray-800 border-y border-gray-800 group-hover:border-gray-700 transition-colors overflow-hidden"
            >
              <div
                class="absolute inset-0 flex items-center justify-center text-gray-700 font-mono text-sm z-0"
              >
                [ WORKFLOW IMAGE PLACEHOLDER ]
              </div>

              <img
                :src="`/images/workflow_${item.imgId}_${slideState[item.imgId] + 1}.png`"
                alt="Workflow Logic"
                class="w-full h-full object-contain relative z-10 transition-all duration-300 bg-gray-900/50"
              />

              <div v-if="item.workflowCount > 1">
                <button
                  @click.stop="prevSlide(item.imgId, item.workflowCount)"
                  class="absolute left-4 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-gray-900/80 hover:bg-cyan-500 text-white flex items-center justify-center border border-gray-700 z-20 transition-colors cursor-pointer"
                >
                  ‹
                </button>
                <button
                  @click.stop="nextSlide(item.imgId, item.workflowCount)"
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-gray-900/80 hover:bg-cyan-500 text-white flex items-center justify-center border border-gray-700 z-20 transition-colors cursor-pointer"
                >
                  ›
                </button>
                <div
                  class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-black/80 backdrop-blur px-3 py-1 rounded-full text-xs font-mono text-gray-300 border border-gray-600 z-20 pointer-events-none"
                >
                  Step {{ slideState[item.imgId] + 1 }} / {{ item.workflowCount }}
                </div>
              </div>

              <div
                class="absolute top-4 right-4 bg-cyan-950/90 text-cyan-400 text-xs px-3 py-1 rounded border border-cyan-900 font-mono z-20 pointer-events-none"
              >
                📄 {{ item.file }}
              </div>
            </div>

            <div class="p-6 md:p-10 bg-black/20">
              <h4
                class="text-gray-500 text-xs font-bold uppercase tracking-widest mb-4 flex items-center gap-2"
              >
                <span class="w-2 h-2 bg-cyan-500 rounded-full"></span>
                Output Comparison / 效果对比
              </h4>

              <div class="grid grid-cols-2 gap-4 md:gap-8 w-full">
                <div
                  class="relative group/img rounded-xl overflow-hidden border border-gray-700 bg-gray-900 cursor-zoom-in aspect-square"
                  @click="
                    openImage(
                      `/images/result_${item.imgId}_before.png`,
                      '原图 (Original Input)',
                      'before',
                    )
                  "
                >
                  <div
                    class="absolute inset-0 flex items-center justify-center text-gray-700 font-mono text-xs z-0"
                  >
                    [ NO IMAGE ]
                  </div>
                  <div
                    class="absolute top-3 left-3 bg-rose-600 text-white text-xs font-bold px-3 py-1 rounded shadow-lg z-20 transition-transform group-hover/img:scale-110"
                  >
                    原图
                  </div>
                  <div
                    v-if="item.isUpscale"
                    class="absolute inset-0 flex items-center justify-center pointer-events-none z-20"
                  >
                    <span
                      class="bg-black/60 text-rose-300 backdrop-blur-md px-4 py-2 rounded-lg border border-rose-500/30 text-sm font-mono font-bold tracking-wider shadow-2xl"
                    >
                      {{ item.resBefore }}
                    </span>
                  </div>
                  <img
                    :src="`/images/result_${item.imgId}_before.png`"
                    class="w-full h-full object-cover object-center transition-all duration-500 group-hover/img:scale-105 relative z-10"
                    alt="Before"
                  />
                </div>

                <div
                  class="relative group/img rounded-xl overflow-hidden border border-cyan-800 bg-gray-900 cursor-zoom-in aspect-square shadow-[0_0_30px_rgba(8,145,178,0.1)] hover:shadow-[0_0_50px_rgba(8,145,178,0.3)] transition-shadow"
                  @click="
                    openImage(
                      `/images/result_${item.imgId}_after.png`,
                      '重绘后 (Upscaled)',
                      'after',
                    )
                  "
                >
                  <div
                    class="absolute inset-0 flex items-center justify-center text-cyan-900/50 font-mono text-xs z-0"
                  >
                    [ NO IMAGE ]
                  </div>
                  <div
                    class="absolute top-3 left-3 bg-cyan-600 text-white text-xs font-bold px-3 py-1 rounded shadow-lg z-20 transition-transform group-hover/img:scale-110"
                  >
                    {{ item.isUpscale ? '高清放大' : '重绘后' }}
                  </div>
                  <div
                    v-if="item.isUpscale"
                    class="absolute inset-0 flex items-center justify-center pointer-events-none z-20"
                  >
                    <span
                      class="bg-black/60 text-cyan-300 backdrop-blur-md px-4 py-2 rounded-lg border border-cyan-500/30 text-sm font-mono font-bold tracking-wider shadow-2xl"
                    >
                      {{ item.resAfter }}
                    </span>
                  </div>
                  <img
                    :src="`/images/result_${item.imgId}_after.png`"
                    class="w-full h-full object-cover object-center transition-all duration-700 group-hover/img:scale-105 relative z-10"
                    alt="After"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <n-modal
      v-model:show="showModal"
      preset="card"
      style="width: auto; background: transparent; box-shadow: none"
      :bordered="false"
    >
      <div
        class="relative max-w-[95vw] max-h-[90vh] flex flex-col items-center outline-none cursor-zoom-out"
        @click="showModal = false"
      >
        <div
          class="mb-4 flex items-center gap-3 bg-black/60 backdrop-blur px-4 py-2 rounded-full border border-white/10 pointer-events-none"
        >
          <span
            class="px-3 py-1 rounded-full font-bold text-xs shadow-lg uppercase tracking-wide"
            :class="
              modalType === 'before'
                ? 'bg-rose-600 text-white'
                : modalType === 'after'
                  ? 'bg-cyan-600 text-white'
                  : 'bg-gray-700 text-gray-200'
            "
          >
            {{
              modalType === 'before' ? 'Original' : modalType === 'after' ? 'Result' : 'Workflow'
            }}
          </span>
          <span class="text-gray-200 text-sm font-medium">{{ modalLabel }}</span>
        </div>

        <img
          :src="modalImage"
          class="max-w-full max-h-[80vh] object-contain rounded-lg shadow-2xl border border-gray-800"
          alt="Full View"
        />
      </div>
    </n-modal>
  </section>
</template>

<style scoped></style>
