<script setup>
import { ref } from 'vue'
import { NModal } from 'naive-ui'

const caseSteps = ref([
  {
    id: '01',
    phase: 'Phase 01',
    title: '提示词工程与策略优化',
    desc: '从客户模糊的意图出发，通过提示词模板引导 AI 进行深度扩写。通过对比原始指令与优化后的结构化提示词，展示如何精准控制画面的文学性与视觉参数。',
    originalPrompt:
      '一个漂亮的亚洲女生在网红奶茶店喝珍珠奶茶，背景模糊化处理但是也需要细节描述，桌上摆放物品，日常感着装，对着镜头摆pose，非常有出片感。',
    refinedPrompt:
      'A highly photogenic, candid lifestyle portrait photograph capturing a stylish young East Asian woman (mid-20s) in a trendy modern boba milk tea shop. She has fashionable honey-brown bob haircut with soft waves and wispy bangs, looking slightly off-camera with a genuine, relaxed smile and glowing, natural makeup. She is seated at a polished marble cafe table, wearing an oversized cream-colored knit sweater layered over a subtle floral patterned midi-dress, carrying a small tan leather crossbody bag. Her right hand is holding a large cup of brown sugar boba milk tea with visible tapioca pearls, a slice of matcha cake on a ceramic plate, a vintage-style point-and-shoot digital camera, and her smartphone are resting on the table next to her. The bustling background is softly blurred (creamy bokeh) but shows signs of other aesthetic patrons, vibrant neon signs with stylish text (e.g., "DAILY JOY" and "FRESH FRUIT"), potted greenery, patterned floor tiles, and warm ambient indoor lights combined with soft natural daylight filtering from a large window. Soft, warm ambient light floods the interior, creating gentle highlights on her hair and face, creating a cozy and photogenic atmosphere. Highly detailed skin textures, visible fabric weave of the sweater, realistic details of the food and drink. Shot on a Sony A7RIV with a 35mm f/1.8 lens, sharp focus on her face and drink, natural depth of field. Slight film grain texture, natural but rich color grading with pops of warmth and greenery. professional editorial aesthetic.',
    refinedPromptTranslation:
      '这是一张非常上镜、自然的生活照，捕捉到一位时尚的年轻东亚女性（二十多岁）在一家时髦的现代珍珠奶茶店里的身影。她留着时髦的蜜棕色波波头，发丝微微卷曲，刘海轻盈飘逸，眼神略微看向镜头外，脸上带着真诚放松的微笑，妆容自然清新。她坐在光滑的大理石咖啡桌旁，身穿一件宽松的米色针织衫，内搭一条精致的碎花中长连衣裙，肩挎一只小巧的棕褐色皮质斜挎包。她的右手拿着一大杯黑糖珍珠奶茶，珍珠清晰可见；旁边桌子上放着一块抹茶蛋糕、一台复古风格的傻瓜数码相机和她的智能手机。熙熙攘攘的背景经过柔和的虚化处理（奶油般的散景），隐约可见其他顾客的身影，以及醒目的霓虹灯招牌（例如“每日喜悦”和“新鲜水果”）、盆栽绿植和各种图案的装饰品。地板瓷砖，温暖的室内氛围灯光，以及透过大窗户洒进来的柔和自然光。柔和温暖的氛围光充满整个室内，在她头发和脸上投下淡淡的高光，营造出温馨而上镜的氛围。肌肤纹理清晰可见，毛衣的织物纹理也清晰可见，食物和饮料的细节也十分逼真。照片使用索尼A7RIV相机和35mm f/1.8镜头拍摄，面部和饮料的焦点清晰锐利，景深自然。略带胶片颗粒感，色彩自然而丰富，并点缀着温暖的色调和绿色植物。呈现出专业的编辑美感。',
    chatImage: '/img/case/chat_screenshot.png',
    chatImage2: '/img/case/chat_screenshot2.png',
  },
  {
    id: '02',
    phase: 'Phase 02',
    title: '生图工作流与资产构建',
    desc: '在 ComfyUI 中利用 IP-Adapter 锁定角色特征，配合 ControlNet 约束构图。',
    workflowImage: '/img/case/step2_workflow.png',
    resultImage: '/img/case/step2_base_result.png',
  },
  {
    id: '03',
    phase: 'Phase 03',
    title: '局部重绘与商业级精修',
    desc: '针对 AI 原始生成中不满意的地方，进行个性化的修复。',
    beforeImage: '/img/case/step3_before.png',
    afterImage: '/img/case/step3_after.png',
    focusDesc: '重点修复：给蛋糕加上盘子，去除不合适的相机，并对角色脸部进行质感优化。',
  },
  {
    id: '04',
    phase: 'Phase 04',
    title: '4K超清放大与质感交付',
    desc: '使用分块渲染技术将分辨率提升至 4K，确保在各种终端完美展示。',
    finalHeroImage: '/img/case/step4_ultra_high.png',
  },
  {
    id: '05',
    phase: 'Phase 05',
    title: '视频动态化与视听合成',
    desc: '将精修底图导入可灵 AI 生成动态序列，在后期软件中完成调色与音效合成。',
    videoUrl: '/img/case/case_final_video.mp4',
    videoPoster: '/img/case/case_final_poster.png',
  },
])

// ===== 极简浏览逻辑 =====
const showModal = ref(false)
const modalImage = ref('')

const openLightbox = (imgSrc) => {
  modalImage.value = imgSrc
  showModal.value = true
}
</script>

<template>
  <div id="project-case" class="case-study-container py-24 space-y-32">
    <div class="container mx-auto px-6 text-center mb-20">
      <h2 class="text-4xl md:text-6xl font-extrabold tracking-tighter mb-6">
        实战项目：<span class="text-gradient-warm">视觉开发全流程</span>
      </h2>
      <p class="text-text-muted text-lg max-w-3xl mx-auto font-light leading-relaxed">
        本案例展示了如何从一个模糊的概念出发，通过专业的 AIGC 工业化管线，最终交付高标准的视频内容。
      </p>
    </div>

    <section class="container mx-auto px-6">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <div class="text-accent font-mono tracking-widest">{{ caseSteps[0].phase }}</div>
          <h3 class="text-3xl font-bold">{{ caseSteps[0].title }}</h3>
          <p class="text-text-soft leading-relaxed">{{ caseSteps[0].desc }}</p>
          <div class="space-y-4 pt-4">
            <div class="p-4 bg-warm-black/40 border-l-2 border-text-muted rounded-r-lg">
              <p class="text-xs text-text-muted uppercase mb-1">原始提示词</p>
              <p class="text-sm italic">" {{ caseSteps[0].originalPrompt }} "</p>
            </div>
            <div class="p-4 bg-accent/5 border-l-2 border-accent rounded-r-lg">
              <p class="text-xs text-accent uppercase mb-1">优化后提示词</p>
              <p class="text-sm font-mono text-accent-light mb-3">
                " {{ caseSteps[0].refinedPrompt }} "
              </p>
              <div class="pt-3 border-t border-accent/20">
                <p class="text-xs text-accent/60 uppercase mb-1 font-bold">翻译 / Translation</p>
                <p class="text-sm text-text-soft leading-relaxed italic">
                  {{ caseSteps[0].refinedPromptTranslation }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col gap-6">
          <div class="relative group cursor-zoom-in" @click="openLightbox(caseSteps[0].chatImage)">
            <img
              :src="caseSteps[0].chatImage"
              class="rounded-2xl border border-warm-border/30 shadow-2xl opacity-80 group-hover:opacity-100 transition-opacity w-full"
              alt="Chat Screenshot 1"
            />
          </div>
          <div class="relative group cursor-zoom-in" @click="openLightbox(caseSteps[0].chatImage2)">
            <img
              :src="caseSteps[0].chatImage2"
              class="rounded-2xl border border-warm-border/30 shadow-2xl opacity-80 group-hover:opacity-100 transition-opacity w-full"
              alt="Chat Screenshot 2"
            />
          </div>
        </div>
      </div>
    </section>

    <section class="bg-warm-black/20 py-24 border-y border-warm-border/10">
      <div class="container mx-auto px-6">
        <div class="flex flex-col gap-10">
          <div class="max-w-3xl">
            <h3 class="text-3xl font-bold">{{ caseSteps[1].title }}</h3>
            <p class="text-text-soft mt-4">{{ caseSteps[1].desc }}</p>
          </div>
          <div class="space-y-8">
            <div>
              <p class="text-sm font-bold text-accent mb-2">工作流：</p>
              <img
                :src="caseSteps[1].workflowImage"
                @click="openLightbox(caseSteps[1].workflowImage)"
                class="w-full max-w-5xl mx-auto rounded-xl border border-warm-border/30 cursor-zoom-in"
              />
            </div>
            <div>
              <p class="text-sm font-bold text-accent mb-2">初版图：</p>
              <img
                :src="caseSteps[1].resultImage"
                @click="openLightbox(caseSteps[1].resultImage)"
                class="w-full max-w-2xl mx-auto rounded-xl border border-warm-border/30 cursor-zoom-in"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="container mx-auto px-6">
      <div class="grid lg:grid-cols-2 gap-16 items-center">
        <div class="grid grid-cols-2 gap-4">
          <div class="space-y-2">
            <img
              :src="caseSteps[2].beforeImage"
              @click="openLightbox(caseSteps[2].beforeImage)"
              class="rounded-lg border border-red-500/20 cursor-zoom-in"
            />
            <p class="text-center text-sm font-bold text-red-400">修复前</p>
          </div>
          <div class="space-y-2">
            <img
              :src="caseSteps[2].afterImage"
              @click="openLightbox(caseSteps[2].afterImage)"
              class="rounded-lg border border-emerald-500/20 cursor-zoom-in"
            />
            <p class="text-center text-sm font-bold text-emerald-400">精修后</p>
          </div>
        </div>
        <div class="space-y-6">
          <h3 class="text-3xl font-bold">{{ caseSteps[2].title }}</h3>
          <p class="text-text-soft">{{ caseSteps[2].desc }}</p>
          <div
            class="p-4 bg-warm-gray/40 rounded-xl border border-warm-border/30 text-sm text-text-soft"
          >
            {{ caseSteps[2].focusDesc }}
          </div>
        </div>
      </div>
    </section>

    <section class="bg-warm-black/20 py-24 border-y border-warm-border/10">
      <div class="container mx-auto px-6">
        <div class="max-w-4xl mx-auto flex flex-col items-center text-center space-y-10">
          <div>
            <div class="text-accent font-mono tracking-widest">{{ caseSteps[3].phase }}</div>
            <h3 class="text-3xl md:text-4xl font-bold mt-2">{{ caseSteps[3].title }}</h3>
            <p class="text-text-soft mt-4">{{ caseSteps[3].desc }}</p>
          </div>

          <div class="relative group max-w-2xl w-full">
            <img
              :src="caseSteps[3].finalHeroImage"
              class="w-full rounded-2xl border border-warm-border/30 shadow-2xl cursor-zoom-in hover:border-accent/50 transition-all"
              @click="openLightbox(caseSteps[3].finalHeroImage)"
            />
            <div class="mt-4 text-xs text-text-muted italic">点击查看大图</div>
          </div>
        </div>
      </div>
    </section>

    <section class="container mx-auto px-6 pb-20">
      <div class="max-w-4xl mx-auto space-y-10">
        <div class="text-center">
          <div class="text-accent font-mono tracking-widest">{{ caseSteps[4].phase }}</div>
          <h3 class="text-3xl md:text-4xl font-bold mt-2">{{ caseSteps[4].title }}</h3>
          <p class="text-text-soft mt-4">{{ caseSteps[4].desc }}</p>
        </div>
        <div
          class="aspect-[9/16] w-full max-w-sm sm:max-w-md md:max-w-lg mx-auto rounded-3xl overflow-hidden border border-accent/30 shadow-[0_0_50px_rgba(212,160,74,0.15)] bg-warm-dark"
        >
          <video
            :src="caseSteps[4].videoUrl"
            controls
            :poster="caseSteps[4].videoPoster"
            class="w-full h-full object-contain"
          ></video>
        </div>
      </div>
    </section>
  </div>

  <n-modal v-model:show="showModal">
    <div
      class="max-w-6xl w-full p-2 outline-none relative flex justify-center items-center bg-warm-black/85 backdrop-blur-sm rounded-lg cursor-zoom-out"
      @click="showModal = false"
    >
      <img
        :src="modalImage"
        class="relative z-10 w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
        @click.stop
      />
    </div>
  </n-modal>
</template>

<style scoped>
.text-gradient-warm {
  background: linear-gradient(135deg, #d4a04a 0%, #e8b86a 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
