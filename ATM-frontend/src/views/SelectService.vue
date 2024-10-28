<!-- 选择服务 -->
<template>

    <div class="common-layout">
    <el-container>
      <el-header>请选择服务项目</el-header>
      <el-main>
        <div class="left-buttons">
        <el-button @click="toInquiry">查询</el-button>
        <el-button>转账</el-button>
        <el-button>存款</el-button>
        <el-button>取卡</el-button>
    </div>
    <div class="right-buttons">
        <el-button @click="toWithdraw">取款</el-button>
        <el-button>修改个人密码</el-button>
    </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
const router=useRouter();

const toWithdraw = () =>{
    router.push('/Withdraw')
}

const toInquiry = () =>{
    router.push('/Inquiry')
}

</script>
<style>
.left-buttons{
    position:absolute;
    left:0;
    display: flex;
    flex-direction: column; /* 设置flex方向为列 */

}

.el-button{
    margin-top:5vh;
}
</style>
