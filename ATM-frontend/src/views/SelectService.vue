<!-- 选择服务 -->
<template>

  <div class="common-layout">
    <el-container>
      <el-header>请选择服务项目 <br> PLEASE SELECT SERVICE</el-header>
      <el-main class="twolist">
        <div class="left-buttons">
          <el-button @click="toInquiry">查询</el-button>
          <el-button @click="toZhuanZhang">转账</el-button>
          <el-button @click="toCunKuan">存款</el-button>
          <el-button @click="toTakeCard">取卡</el-button>
        </div>
        <div class="right-buttons">
          <el-button @click="toWithdraw">取款</el-button>
          <el-button @click="toModifyPassword">修改个人密码</el-button>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const toWithdraw = () => {
  router.push("/Withdraw");
};

const toInquiry = () => {
  router.push("/Inquiry");
};

const toCunKuan = () => {
  router.push("/CunKuan");
};

const toZhuanZhang = () => {
  router.push("/ZhuanZhang");
};

const toModifyPassword = () => {
  router.push("/ModifyPassword");
};

const toTakeCard = () => {
  router.push("/TakeCard");
};
</script>
<style>
.el-button {
  margin-top: 5vh;
}
</style>
