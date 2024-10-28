<template>
    <div class="common-layout">
        <el-container>
           <el-main>
      <div class="function-maincontent">
            <el-descriptions
    class="margin-top"
    
    :column="1"
    :size="size"
    :style="blockMargin"
  >
 
    <el-descriptions-item label="余额">kooriookami</el-descriptions-item>
    <el-descriptions-item label="可用余额">18100000000</el-descriptions-item>
            </el-descriptions>
       </div>

  <div class="right-buttons locate-buttom">
            <el-button @click="toSelectService">继续</el-button>
            <el-button>取卡</el-button>
            </div>

           </el-main>
        </el-container>  
    </div>
</template>

<script setup lang="js">
import{useRouter} from 'vue-router'
const router=useRouter();
const toSelectService = () =>{
    router.push('/SelectService')
}
</script>