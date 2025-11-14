<script setup>
import { NFlex, NCard, NButton } from 'naive-ui'
import { ref } from 'vue'

const workflowData = ref([
  {
    title: 'FLUX 开发版重绘放大工作流',
    imageUrl: '/images/workflow-1.png',
    jsonUrl: '/workflows/workflow-1.json',
    scenario:
      '该工作流旨在解决高质量图像放大与风格迁移中的核心难题：如何在提升图像分辨率、注入新风格的同时，精确保留原始图片的构图、结构和细节，避免AI过度"自由发挥"导致的形体崩坏或细节丢失。',
    breakdown: [
      '模型与风格加载：加载 FLUX.1 Dev 大模型作为生成基础，配合特定风格LoRA（如Nunchaku FLUX），奠定高质生成的"能力"与"风格"基调。',
      '双重ControlNet结构控制：一路使用Canny边缘检测锁定轮廓线条，另一路使用Depth深度图维持空间层次，为AI提供可靠的"结构脚手架"，确保重绘后主体结构不崩坏。',
      'IPAdapter风格注入：读取风格参考图的视觉特征（色彩、光影、笔触），直接作为隐式条件注入生成过程，实现超越文字描述的精准、协调的风格迁移。',
      '低降噪幅度采样：在KSampler中设置较低的Denoise值（0.6-0.75），使AI主要在ControlNet约束下对原图进行"优化"而非"重绘"，完美平衡细节保留与风格注入。',
    ],
  },
  {
    title: '智能图像缩放与样式处理工作流',
    imageUrl: '/images/workflow-2.png',
    jsonUrl: '/workflows/workflow-2.json',
    scenario:
      '该工作流专注于图像的智能缩放、样式调整与批量处理，通过非破坏性编辑技术实现多尺寸适配和视觉风格统一，极大提升UI设计、社交媒体内容制作的效率。',
    breakdown: [
      '智能缩放核心：使用ImageScaleByAspectFit模块，根据原始宽高比自动计算最佳缩放比例，支持按宽度、高度或原始比例进行自适应调整。',
      '图层样式处理：集成LayerStyle处理器，可对图像进行色彩校正、对比度调整、滤镜应用等非破坏性后期处理。',
      '实时对比分析：通过Image Comparator实现不同参数设置的A/B测试，直观对比处理效果，确保输出质量最优。',
      '批量输出管理：支持自定义文件名前缀、多格式导出配置，满足商业化项目中多尺寸、多平台的内容分发需求。',
    ],
  },
])
</script>

<template>
  <div class="workflow-container">
    <!-- 使用 v-for 循环，可以展示多个工作流 -->
    <div v-for="(item, index) in workflowData" :key="index" class="workflow-item">
      <!-- 需求场景描述 (采纳你的新设计，非常棒！) -->
      <n-card size="small">
        <template #header>
          <span style="font-weight: bold; font-size: 16px">需求场景</span>
        </template>
        <p>{{ item.scenario }}</p>
      </n-card>

      <!-- 主体内容：左边截图，右边拆解 -->
      <n-flex class="workflow-content" :wrap="false">
        <!-- 【解决方案】把 img 标签放回这里 -->
        <div class="workflow-image-wrapper">
          <img :src="item.imageUrl" alt="ComfyUI Workflow" class="workflow-image" />
        </div>

        <div class="workflow-details">
          <h3>工作流核心步骤解析</h3>
          <ol class="breakdown-list">
            <li v-for="(step, stepIndex) in item.breakdown" :key="stepIndex">
              <span class="step-number">{{ stepIndex + 1 }}</span>
              <p>{{ step }}</p>
            </li>
          </ol>

          <a :href="item.jsonUrl" download>
            <n-button type="primary" strong>
              <template #icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="1em"
                  height="1em"
                  viewBox="0 0 24 24"
                >
                  <path fill="currentColor" d="M5 20h14v-2H5m14-9h-4V3H9v8H5l7 7Z"></path>
                </svg>
              </template>
              下载 .json 工作流文件
            </n-button>
          </a>
        </div>
      </n-flex>
    </div>
  </div>
</template>

<style scoped>
.workflow-item {
  margin-bottom: 60px;
}
.workflow-item p {
  margin: 0;
  line-height: 1.7;
}
.workflow-content {
  margin-top: 24px;
}
.workflow-image-wrapper {
  flex: 1.2;
  min-width: 400px;
}
.workflow-image {
  width: 100%;
  border-radius: 8px;
  border: 1px solid #333;
}
.workflow-details {
  flex: 1;
  padding-left: 24px;
}
.workflow-details h3 {
  font-size: 20px;
  margin-top: 0;
  margin-bottom: 16px;
}
.breakdown-list {
  list-style: none;
  padding: 0;
  margin-bottom: 24px;
}
.breakdown-list li {
  display: flex;
  align-items: flex-start;
  margin-bottom: 16px;
}
.step-number {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: #63e2b7;
  color: #111;
  font-weight: bold;
  margin-right: 12px;
  flex-shrink: 0;
}

@media (max-width: 992px) {
  .workflow-content {
    flex-wrap: wrap;
  }
  .workflow-details {
    padding-left: 0;
    margin-top: 24px;
  }
}
/* 工作流模块 - 移动端优化 */
@media (max-width: 768px) {
  /* 工作流的图片+文字改为上下堆叠 */
  .workflow-content {
    flex-direction: column !important; /* 强制垂直排列 */
  }

  /* 工作流图片自适应手机宽度 */
  .workflow-image-wrapper img {
    width: 100% !important; /* 占满宽度 */
    height: auto !important; /* 高度自适应 */
    max-height: 250px; /* 限制图片高度，避免太长 */
  }

  /* 右边解说部分调整 */
  .workflow-details {
    padding: 0 16px !important; /* 左右留边 */
    width: 100% !important; /* 占满宽度 */
    margin-top: 20px !important; /* 与图片拉开距离 */
    margin-bottom: 40px !important; /* 减少底部间距 */
  }

  /* 减少模块之间的上下间距 */
  .workflow-item {
    margin-bottom: 20px !important; /* 缩小模块间距 */
  }
}
</style>
