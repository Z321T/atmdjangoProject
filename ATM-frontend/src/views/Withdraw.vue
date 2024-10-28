<!-- 取款 -->
 <template>
<div class="common-layout">
    <el-container>
        <el-main>
            <div class="fuction-maincontent">
                <div class="flex gap-4 mb-4">
                <span>请输入取款金额：</span>
                <el-input
        v-model="withdrawmoney"
        style="width: 240px"
        placeholder="Please input"
        :formatter="(value) => `${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
        :parser="(value) => value.replace(/\$\s?|(,*)/g, '')"
    />
                </div>
             </div>
            <div class="right-buttons locate-buttom">
            <el-button>确认</el-button>
            <el-button>更正</el-button>
            </div>
        </el-main>
    </el-container>
</div>
 </template>

 <script setup lang="ts">
 import {ref} from 'vue'
const withdrawmoney=ref('')
</script>

 <style scoped>

 .flex{
    position: relative;
    margin:auto;
    margin-top:15vh;
    display: flex;
    justify-content: center;

 }
</style>