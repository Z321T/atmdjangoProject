<template>
  <div class="common-layout">
    <el-container>
      <el-header>密码修改</el-header>

      <el-main>
        <el-form
          style="max-width: 300px"
          :model="Form"
          status-icon
          label-width="auto"
          class="demo-ruleForm"
        >

          <el-form-item
            label="修改密码:"
            prop="passwordA"
          >
            <el-input
              v-model="Form.passwordA"
              type="password"
              autocomplete="off"
            />
          </el-form-item>

          <el-form-item
            label="确认密码:"
            prop="passwordB"
          >
            <el-input
              v-model="Form.passwordB"
              type="password"
              autocomplete="off"
            />
          </el-form-item>

        </el-form>
        <el-button
          type="success"
          @click="newPassword"
        >确认</el-button>
        <el-button class="return">返回</el-button>
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
  passwordA: "",
  passwordB: "",
});

//传给后端
const newPassword = () => {
  if (Form.value.passwordA === Form.value.passwordB) {
    // 从localStorage中获取之前存储的Authentication值
    const authHeaderValue = localStorage.getItem("Authentication");

    // 构建请求的headers对象，包含Authentication头
    const headers = {
      "Content-Type": "application/json",
      Authentication: authHeaderValue, // 添加Authentication头
    };

    http
      .post(
        "/api/change_password/",
        {
          newpassword: Form.value.passwordA,
        },
        {
          headers: headers, // 包含自定义headers
        }
      )
      .then((res) => {
        console.log(res.data);
        const message = res.data.message;
        if (message === "Password changed successfully") {
          console.log("success!!!!!!");
          router.push("/PasswordSuccess");
        }
      })
      .catch((error) => {
        console.error("Error during password", error);
      });
  } else {
    console.log("密码不一致！！！！");
    router.push("/PasswordFailure");
  }
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