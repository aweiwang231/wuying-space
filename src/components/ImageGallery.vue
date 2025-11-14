<script setup>
import { ref } from 'vue'
// 【新增】引入 NFlex 用于布局，NCollapse 和 NCollapseItem 用于折叠面板
import { NGrid, NGi, NCard, NModal, NFlex, NCollapse, NCollapseItem } from 'naive-ui'

const showModal = ref(false)
const selectedArtwork = ref(null)

const artworks = ref([
  {
    id: 1,
    title: '黑暗奇幻古堡',
    imageUrl: '/images/artwork-1.png',
    description: '这张图旨在营造神秘而阴森的奇幻氛围，重点在于城堡细节和氛围感的表达。',
    workflowUrl: '/images/workflow-1.png', // 假设你有名为 workflow-1.png 的文件
    techParams: {
      核心工具: 'Stable Diffusion (ComfyUI)',
      基础模型: 'ponyRealism_V22.safetensors',
      '风格 LoRA': 'dark fantasy style LoRA (权重0.7)', // 示例，你可以修改
      采样器: 'DPM++ 2M Karras | 步数: 32',
      核心关键词:
        'dark fantasy, huge castle, moss, mist, fog, low light, depth of field, highly detailed, high contrast, film grain, Rim Lighting, Long Exposure, DSLR',
      后期处理: '高清放大重绘工作流',
    },
  },
  {
    id: 2,
    title: '初音未来',
    imageUrl: '/images/artwork-2.png',
    description:
      '面部裂纹设计带有数字故障艺术(Glitch Art)的科技感,角色造型保持日系动漫的精致美感，但在光影处理上更加写实化。',
    workflowUrl: '/workflows/ControlNet-Inpaint-Example.json', // 假设你有这个json文件
    techParams: {
      // 【修正】这里是关键！每个键值对都是独立的
      基础模型: 'plantMilkModelSuite_walnut.safetensors',
      '风格 LoRA': 'Hatsune Miku(voc)-Illus-Remake.safetensors',
      核心关键词:
        'masterpiece, best quality, absurdres, 1girl, hatsune miku, aqua hair, twintails, intense gaze, pointing through cracked glass, dramatic lighting, volumetric lighting, photorealistic, sharp focus, anime aesthetic, detailed skin, urban night background, centered composition',
      后期处理: '脸部修复工作流 (使用ControlNet Inpaint)', // 示例，你可以修改
    },
  },
  {
    id: 3,
    title: '哥特风亚洲女孩',
    imageUrl: '/images/artwork-3.png',
    description:
      '这张图旨在展现神秘性感的哥特风格人像，重点在于人物妆容、服装质感与杂乱卧室环境的氛围对比。',
    workflowUrl: 'flux_fill_inpaint_example.json',
    techParams: {
      核心工具: 'Stable Diffusion (ComfyUI)',
      核心关键词:
        'score_9, score_8_up, asian girl, goth, emo, portrait, close-up, latex minidress, tattoos, messy bedroom, rim lighting, film grain, high contrast',
      后期处理: '细节增强与色彩优化工作流',
    },
  },
  {
    id: 5,
    title: '惠惠同人作品',
    imageUrl: '/images/artwork-4.png',
    description:
      '这张图生动展现了《为美好的世界献上祝福！》中惠惠的经典形象，通过动态前倾姿势，完美捕捉了角色活泼自信的性格特质。',
    workflowUrl: '/images/workflow-4.png',
    techParams: {
      核心工具: 'Stable Diffusion WebUI',
      基础模型: 'catCitronAnimeTreasure_ilV9.safetensors',
      '角色 LoRA': 'We4reSoB4ck_IXL (权重1.0)',
      采样器: 'DPM++ 2M Karras | 步数: 31 | CFG: 7',
      核心关键词:
        'megumin, solo, dynamic pose, leaning forward, red eyes, witch hat, cape, smile, looking at viewer, cinematic lighting, rim light, gradient background',
      负面提示词: 'blurry, lowres, worst quality, bad anatomy, multiple views, text, watermark',
      分辨率: '832x1216',
      面部修复: 'ADetailer (mediapipe_face_full)',
      种子值: '3003810731',
    },
  },
])

function openModal(artwork) {
  selectedArtwork.value = artwork
  showModal.value = true
}
</script>

<template>
  <n-grid cols="1 s:2 m:3 l:4" :x-gap="24" :y-gap="24" responsive="screen">
    <n-gi v-for="artwork in artworks" :key="artwork.id">
      <n-card :title="artwork.title" hoverable @click="openModal(artwork)" style="cursor: pointer">
        <template #cover>
          <img :src="artwork.imageUrl" class="artwork-image" />
        </template>
      </n-card>
    </n-gi>
  </n-grid>

  <!-- 【修改】重构整个弹窗的内部结构 -->
  <n-modal v-model:show="showModal" preset="card" style="width: 80vw; max-width: 1200px">
    <div v-if="selectedArtwork">
      <!-- 使用 NFlex 创建左右两栏布局 -->
      <n-flex :wrap="false">
        <!-- 左侧：图片展示 -->
        <div class="modal-image-wrapper">
          <img :src="selectedArtwork.imageUrl" class="modal-image" />
        </div>

        <!-- 右侧：信息详情 -->
        <div class="modal-details-wrapper">
          <h2>{{ selectedArtwork.title }}</h2>
          <p class="modal-description">{{ selectedArtwork.description }}</p>

          <!-- 技术参数折叠面板 -->
          <n-collapse arrow-placement="right" class="tech-panel">
            <n-collapse-item title="展开/折叠 技术参数" name="1">
              <ul>
                <li v-for="(value, key) in selectedArtwork.techParams" :key="key">
                  <strong>{{ key }}:</strong> {{ value }}
                </li>
              </ul>
            </n-collapse-item>
          </n-collapse>
        </div>
      </n-flex>
    </div>
  </n-modal>
</template>

<style scoped>
.artwork-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

/* 弹窗内部样式 */
.modal-image-wrapper {
  flex: 1.5; /* 图片区域占比较大 */
  min-width: 0; /* 防止flex项目溢出 */
}
.modal-image {
  width: 100%;
  max-height: 75vh; /* 限制图片最大高度，避免超出视窗 */
  object-fit: contain;
  border-radius: 4px;
}
.modal-details-wrapper {
  flex: 1;
  padding-left: 24px;
  display: flex;
  flex-direction: column;
}
.modal-details-wrapper h2 {
  margin-top: 0;
}
.modal-description {
  color: #ccc;
  line-height: 1.6;
}

.tech-panel {
  margin-top: 16px;
}
.tech-panel ul {
  list-style: none;
  padding: 0 0 0 8px;
  margin: 0;
}
.tech-panel li {
  margin-bottom: 8px;
}
.tech-panel li strong {
  color: #63e2b7;
  margin-right: 8px;
}

/* 响应式：小屏幕时，上下布局 */
@media (max-width: 768px) {
  .n-flex {
    flex-wrap: wrap !important;
  }
  .modal-details-wrapper {
    padding-left: 0;
    margin-top: 24px;
  }
}
</style>
