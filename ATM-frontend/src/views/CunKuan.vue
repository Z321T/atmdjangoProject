<template>
  <div class="common-layout">
    <el-container>
      <el-header>请将现金放入存款槽<br>Please put cash into the deposit slot</el-header>

      <el-main>

        <el-form
          style="max-width: 300px"
          :model="Form"
          status-icon
          label-width="auto"
          class="demo-ruleForm"
        >
          <el-form-item></el-form-item>
          <el-form-item></el-form-item>
          <el-form-item></el-form-item>
          <el-form-item></el-form-item>
          <el-form-item
            label="存款金额"
            prop="amount"
          >
            <el-input
              v-model="Form.amount"
              type="number"
              autocomplete="off"
            />
          </el-form-item>

        </el-form>
        <el-button
          type="success"
          @click="deposit"
        >确认</el-button>
      </el-main>

    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, inject } from "vue";
import { useRouter } from "vue-router";
import type { AxiosInstance } from "axios";

const router = useRouter();
/// 从应用实例中注入 axios
const http = inject<AxiosInstance>("axios");
if (!http) {
  console.error("Axios instance is not provided");
}

//表格数据
const Form = ref({
  amount: "",
});

const deposit = () => {
  // 从localStorage中获取之前存储的Authentication值
  const authHeaderValue = localStorage.getItem("Authentication");

  // 构建请求的headers对象，包含Authentication头
  const headers = {
    "Content-Type": "application/json",
    Authentication: authHeaderValue, // 添加Authentication头
  };

  http
    .post(
      "/api/deposit/",
      {
        amount: Form.value.amount,
      },
      {
        headers: headers, // 包含自定义headers
      }
    )
    .then((res) => {
      console.log(res.data);
      const message = res.data.message;
      if (message === "Deposit successful") {
        console.log("success!!!!");
        router.push("/DepositSuccess");
      }
    })
    .catch((error) => {
      console.error("Error during deposit:", error);
    });
};
</script>


<style scoped>
.el-input {
  margin: auto;
  display: flex;
  justify-content: center; /* 水平居中 */
}
.el-main {
  justify-content: center;
}

.el-button--success {
  position: absolute;
  bottom: 5vh; /* 底部对齐 */
  right: 5vh; /* 右侧对齐 */
}
</style>