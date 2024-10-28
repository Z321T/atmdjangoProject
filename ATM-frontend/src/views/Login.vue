<template>
    

    <div class="common-layout">
    <el-container>
      <el-header>请输入密码</el-header>
      
        <el-main>
          
          <el-input
      v-model="password"
      style="width: 240px"
      type="password"
      placeholder="Please input password"
      show-password
    />

    <el-button type="success">确认</el-button>
  </el-main>
    </el-container>
    </div>
</template>

<script setup lang="ts">
import{ref}from 'vue'
const password=ref('')
</script>


<style scoped>
.el-input{
margin: auto;
display: flex;
justify-content: center; /* 水平居中 */
}

.el-button--success{
  position:absolute;
  bottom: 5vh;    /* 底部对齐 */
  right: 5vh;    /* 右侧对齐 */
}


</style>