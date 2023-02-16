<template>
  <div style="margin-top: 160px; width: 100%;   display: flex; justify-content: center; align-items: center;">
          <el-row style="width: 1000px; height: 400px;">
            <el-col :span="12">
              <span style="font-size: 20px;margin-bottom: 15px">For Mobiles</span>
              <br>
              <img src="../assets/app_phone_en_m.png" style="height: 240px; margin-top: 30px;">
              <br> <br>
              <el-button plain type="primary" @click="downloadAPK" size="small" style="margin-top: 4px"><i
                  class="el-icon-download"> </i> Android
              </el-button>
              <el-button :disabled="true" size="small" style="margin-top: 4px"><i
                  class="el-icon-download"> </i> IOS( Coming Soon )
              </el-button>
              <br> <br>
            </el-col>
            <el-col :span="12">
              <span style="font-size: 20px;margin-bottom: 15px">For Computers</span>
              <br>
              <img src="../assets/app_pc.png" style="height: 240px; margin-top: 30px;">
              <br> <br>
              <el-button :disabled="true" size="small" style="margin-top: 4px"><i
                  class="el-icon-download"> </i> Windows ( Coming Soon )
              </el-button>
              <el-button :disabled="true" size="small" style="margin-top: 4px"><i
                  class="el-icon-download"> </i> MacOs ( Coming Soon )
              </el-button>
            </el-col>
          </el-row>
  </div>
</template>

<script>
  export default {
    name: 'HomePage',
    data () {
      return {
        url: 'https://mypi.mystrikingly.com'
      };
    },
  }
</script>

<style scoped>
.question_page_container {
  /*设置次级页面高度控制动画位置*/
  min-height: 300px;
}

.three_exam_row {
  width: 80%;
  margin-top: 50px;
  margin-bottom: 50px;
}

.sp_view_container {
  overflow-x: auto;
  max-height: 1600px;
  margin-bottom: 20px;
  margin-top: 20px;
  width: 100%;
}

.app_container {
  width: 100%;
  height: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
  position: relative;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
</style>