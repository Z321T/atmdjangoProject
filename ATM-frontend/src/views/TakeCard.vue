<template>
  <div class="common-layout">
    <el-container>
      <el-header>请取走您的卡片<br>Please take your card</el-header>
      <el-main>
        <el-button
          type="primary"
          @click="toInsertCard"
        >确认/Confirm</el-button>
      </el-main>

    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const toInsertCard = () => {
  router.push("/InsertCard");
};
</script>

<style scoped>
.el-button--primary {
  position: absolute;
  bottom: 5vh; /* 底部对齐 */
  right: 5vh; /* 右侧对齐 */
}
</style>

