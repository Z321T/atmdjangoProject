<template>
  <div class="common-layout">
    <el-container>
      <el-header>请输入您的个人密码</el-header>

      <el-main>
        <el-form
          style="max-width: 300px"
          :model="Form"
          status-icon
          label-width="auto"
          class="demo-ruleForm"
        >
          <el-form-item
            label="卡号"
            prop="cardId"
          >
            <el-input
              v-model="Form.cardId"
              type="number"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="密码"
            prop="password"
          >
            <el-input
              v-model="Form.password"
              type="password"
              autocomplete="off"
            />
          </el-form-item>

          <el-form-item>

          </el-form-item>
        </el-form>
        <el-button
          type="success"
          @click=transferPassword()
        >确认/Confirm</el-button>
      </el-main>
      <el-footer>PLEASE KEY IN <br> YOUR PERSONAL IDENTIFICATION
        NUMBER</el-footer>
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
  cardId: "",
  password: "",
});

const transferPassword = () => {
  console.log("click success!");
  http
    .post("/api/login/", {
      cardId: Form.value.cardId,
      password: Form.value.password,
    })
    .then((res) => {
      // 登录成功后存储 token
      const message = res.data.message;
      if (message === "Login successful") {
        // 从响应头中获取Authentication字段的值
        const authHeader = res.headers.get("Authentication");
        if (authHeader) {
          // 将Authentication字段的值存储到localStorage
          localStorage.setItem("Authentication", authHeader);
        }
        router.push("/SelectService"); // 替换为您想要重定向到的路由
      } else {
        router.push("/InvalidPass");
      }
    })
    .catch((error) => {
      console.error("Error during login:", error);
      router.push("/InvalidPass");
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