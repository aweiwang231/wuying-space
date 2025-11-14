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
    title: '沙漠女战士',
    imageUrl: '/images/artwork-3.png',
    description:
      '这张图通过超写实风格展现了一位成熟女性在沙漠中的威严形象，融合军事元素，重点在于面部纹身、服装细节和专业级景深效果。',
    workflowUrl: null,
    techParams: {
      核心工具: 'Stable Diffusion (ComfyUI)',
      基础模型: 'divingIllustriousReal_proVAE.safetensors',
      '风格 LoRA':
        'Add-cfg_scale_boost (权重0.7), Add-amateur_style_v1_pony (权重1.0), MoriiMee_Gothic_Niji_Style (权重0.2)',
      采样器: 'dpmpp_2m | 步数: 31 | CFG: 7.1 | 调度器: simple',
      核心关键词:
        'mature female, stern expression, barcode tattoo, black jacket, desert, 50mm lens, retro artstyle, hyper-realistic, 8k',
      分辨率: '8K 超高清',
      后期处理: '万物修复工作流',
    },
  },
  {
    id: 4,
    title: '惠惠',
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
/* 作品详情弹窗 - 移动端优化 */
@media (max-width: 768px) {
  /* 弹窗内容改为上下堆叠，避免左右挤压 */
  :deep(.n-modal-card__content .n-flex) {
    flex-direction: column !important; /* 强制垂直排列 */
    align-items: center !important; /* 内容居中 */
  }

  /* 弹窗图片自适应手机宽度 */
  .modal-image-wrapper img {
    width: 100% !important; /* 占满弹窗宽度 */
    height: auto !important; /* 高度自动适应，避免拉伸 */
    max-height: 300px; /* 限制图片最大高度，防止占满屏幕 */
  }

  /* 详情文字部分调整 */
  .modal-details-wrapper {
    padding: 0 16px !important; /* 左右留边 */
    width: 100% !important; /* 占满宽度 */
    margin-top: 20px !important; /* 与图片拉开距离 */
  }

  /* 技术参数部分调整 */
  .modal-details-wrapper .n-collapse {
    font-size: 14px; /* 缩小文字 */
  }
}
@media (max-width: 768px) {
  /* 弹窗整体容器：增加内边距，让内容不贴边 */
  :deep(.n-modal-card) {
    padding: 16px !important;
  }

  /* 图片容器：放大图片并调整比例 */
  .modal-image-wrapper {
    width: 100% !important;
    max-width: 300px !important; /* 限制最大宽度，避免过大 */
    margin: 0 auto !important; /* 图片居中 */
  }

  .modal-image-wrapper img {
    width: 100% !important;
    height: auto !important;
    border-radius: 4px; /* 可选：给图片加圆角，更美观 */
  }

  /* 文字详情容器：缩小间距，增加紧凑感 */
  .modal-details-wrapper {
    margin-top: 16px !important;
    padding: 0 !important;
  }

  /* 技术参数折叠面板：缩小文字和间距 */
  :deep(.n-collapse) {
    font-size: 14px !important;
  }

  :deep(.n-collapse-panel__header) {
    padding: 8px 0 !important;
  }

  :deep(.n-collapse-panel__content) {
    padding: 8px 0 !important;
    line-height: 1.5;
  }

  /* 技术参数项：调整行高和间距 */
  :deep(.n-collapse-panel__content p) {
    margin: 4px 0 !important;
  }
}
</style>
