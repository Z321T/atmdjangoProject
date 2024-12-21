<template>
  <div class="common-layout">
    <el-container>
      <el-header>转账失败 <br> Transfer fails</el-header>

      <el-main>

        <el-button
          type="success"
          @click="toSelectService"
        >确认/Confirm</el-button>

      </el-main>

    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const toSelectService = () => {
  router.push("/SelectService");
};
</script>


<style scoped>
.maincontent {
  font-size: 30px;
  text-align: center; /* 文本居中对齐 */
}
.el-main {
  justify-content: center; /* 水平居中 */
}

.el-button--success {
  position: absolute;
  bottom: 5vh; /* 底部对齐 */
  right: 5vh; /* 右侧对齐 */
}

.return {
  position: absolute;
  bottom: 5vh; /* 底部对齐 */
  left: 5vh; /* 右侧对齐 */
}
</style>