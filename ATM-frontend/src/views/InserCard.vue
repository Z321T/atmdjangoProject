<!-- 插卡 -->
<template>
    
    <div class="common-layout">
    <el-container>
      <el-header>请插卡</el-header>
      <el-main>
        <el-button type="primary" @click="toLogin">插卡</el-button>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
const router=useRouter();

const toLogin = () => {
    router.push('/Login')
}
</script>

<style scoped>
.el-button--primary {
  position:absolute;
  bottom: 5vh;    /* 底部对齐 */
  right: 5vh;    /* 右侧对齐 */
}
</style>