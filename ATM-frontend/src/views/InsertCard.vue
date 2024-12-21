<!-- 插卡 -->
<template>
    
    <div class="common-layout">
    <el-container>
      <el-header>欢迎使用矿大银行 <br> 自动柜员机<br>请插入磁卡</el-header>
      <el-main>
        <el-button type="primary" @click="toLogin">确认/Confirm</el-button>
      </el-main>
      <el-footer>Welcome to USE CUMT System <br> Please Insert Card</el-footer>
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