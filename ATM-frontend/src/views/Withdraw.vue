<!-- 取款 -->
 <template>
  <div class="common-layout">
    <el-container>
      <el-header style="font-size: 24px; ">
        请输入取款金额：<br> Please key in amount
      </el-header>
      <el-main>
        <div class="left-buttons">
          <el-button @click="oneHundred">100</el-button>
          <el-button @click="twoHundred">200</el-button>
          <el-button @click="fiveHundred">500</el-button>
          <el-button @click="toSelectService">返回/Return</el-button>

        </div>
        <div>
          <input
            v-model.number="plus"
            type="number"
            placeholder="Enter amount"
          />
        </div>

        <div class="right-buttons">
          <el-button @click="eightHundred">800</el-button>
          <el-button @click="oneThousand">1000</el-button>
          <el-button @click="twoThousand">2000</el-button>
          <el-button @click="withdraw()">确认/Confirm</el-button>
        </div>

      </el-main>
    </el-container>
  </div>
</template>

 <script setup lang="ts">
import { ref, inject, computed } from "vue";
import type { AxiosInstance } from "axios";
import { useRouter } from "vue-router";

const withdrawmoney = ref(0);

const router = useRouter();
/// 从应用实例中注入 axios
const http = inject<AxiosInstance>("axios");
if (!http) {
  console.error("Axios instance is not provided");
}

//向后端传取款金额
const withdraw = () => {
  // 从localStorage中获取之前存储的Authentication值
  const authHeaderValue = localStorage.getItem("Authentication");

  // 构建请求的headers对象，包含Authentication头
  const headers = {
    "Content-Type": "application/json",
    Authentication: authHeaderValue, // 添加Authentication头
  };

  http
    .post(
      "/api/withdraw/",
      {
        withdrawmoney: withdrawmoney.value,
      },
      {
        headers: headers, // 包含自定义headers
      }
    )
    .then((res) => {
      console.log(res.data);
      const message = res.data.message;
      if (message === "Withdraw successful") {
        router.push("/WithdrawSuccess");
      } else {
        router.push("/WithdrawFailure");
      }
    })
    .catch((error) => {
      console.error("Error during login:", error);
    });
};

// 创建一个计算属性
const plus = computed({
  get: () => withdrawmoney.value,
  set: (val) => {
    withdrawmoney.value = Number(val); // Ensure numeric value
  },
});

const oneHundred = () => {
  plus.value += 100;
  console.log(withdrawmoney.value);
};
const twoHundred = () => {
  plus.value += 200;
  console.log(withdrawmoney.value);
};
const fiveHundred = () => {
  plus.value += 500;
  console.log(withdrawmoney.value);
};
const oneThousand = () => {
  plus.value += 1000;
  console.log(withdrawmoney.value);
};
const twoThousand = () => {
  plus.value += 2000;
  console.log(withdrawmoney.value);
};
const eightHundred = () => {
  plus.value += 800;
  console.log(withdrawmoney.value);
};

const toSelectService = () => {
  router.push("/SelectService");
};
</script>
