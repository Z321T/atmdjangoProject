<template>
  <div class="common-layout">
    <el-container>
      <el-header></el-header>
      <el-main>
        <div>
        </div>
        <div class="maincontent">
          <el-descriptions :column="1">
            <el-descriptions-item
              label="余额￥">{{ balance }}</el-descriptions-item>
            <el-descriptions-item
              label="可用余额￥">{{ balance }}</el-descriptions-item>
          </el-descriptions>
        </div>
        <div></div>

        <el-button
          @click="toSelectService"
          class="return"
        >返回</el-button>

      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { ref, inject, onMounted } from "vue";
import type { AxiosInstance } from "axios";

const router = useRouter();
const balance = ref("");
/// 从应用实例中注入 axios
const http = inject<AxiosInstance>("axios");
if (!http) {
  console.error("Axios instance is not provided");
}

const getBalance = () => {
  console.log("click success!");
  // 从localStorage中获取之前存储的Authentication值
  const authHeaderValue = localStorage.getItem("Authentication");

  // 构建请求的headers对象，包含Authentication头
  const headers = {
    "Content-Type": "application/json",
    Authentication: authHeaderValue, // 添加Authentication头
  };
  http
    .get("/api/balance/", {
      headers: headers, // 包含自定义headers
    })
    .then((res) => {
      // 假设后端返回的数据结构是 { data: { balance: '实际余额' } }
      console.log(res);
      balance.value = res.data.balance;
    })
    .catch((error) => {
      console.error("Error during balance:", error);
    });
};

const toSelectService = () => {
  router.push("/SelectService");
};
// 使用onMounted钩子在组件挂载时调用getBalance函数
onMounted(() => {
  getBalance();
});
</script>

<style>
</style>

