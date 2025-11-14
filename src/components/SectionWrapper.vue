<template>
  <section class="section-wrapper">
    <h2 class="section-title">
      <!-- "slot" 是一个插槽，允许我们在使用这个组件时，自定义标题内容 -->
      <slot name="title"></slot>
    </h2>
    <div class="section-content">
      <!-- 这是默认插槽，用来放区块的主要内容 -->
      <slot></slot>
    </div>
  </section>
</template>

<style scoped>
.section-wrapper {
  padding: 40px 0;
  /* 这是解决导航栏遮挡问题的现代CSS魔法！ */
  /* 它告诉浏览器，当滚动定位到我这里时，请在我的顶部留出80px的空白 */
  scroll-margin-top: 80px;
}

.section-title {
  font-size: 28px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 32px;
  /* 你可以给标题加个好看的渐变色 */
  background: linear-gradient(45deg, #63e2b7, #54aeff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
</style>
