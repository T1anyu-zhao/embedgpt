<template>
  <div class="header">
  <el-menu
      :default-active="activeIndex"
      class="menu"
      mode="horizontal"
      @select="handleSelect"
  >
    <img src="../assets/logo.png" style="object-fit: scale-down; height: 30px;margin: 12px 20px -5px;">
    <el-menu-item index="1" style="margin-right: 20px">
      <img src="../assets/icon/home.png" class="menu-icon" style="height: 25px; width:25px">
          Home
    </el-menu-item>
    <el-sub-menu index="2" >
      <template #title>
        <img src="../assets/icon/product-list.png" class="menu-icon">
        <div class="menu-text">
          Products
        </div>
      </template>
      <el-menu-item index="2-1">
        <a href="https://mypi.mystrikingly.com/">
          MyPi
        </a>
      </el-menu-item>
      <el-menu-item index="2-2">Big brother</el-menu-item>
      <el-menu-item index="2-3">Guard Your Soul</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="3">
        <img src="../assets/icon/about.png" class="menu-icon">
        <div class="menu-text">
          About us
        </div>
    </el-menu-item>
    <el-menu-item index="4">
      <img src="../assets/icon/user.png" class="menu-icon" style="height: 25px; width:25px">
      <div class="menu-text">
          {{loginText}}
        </div>
    </el-menu-item>
    <!-- <el-input style="width: 200px;height: 30px;float: right;margin-top: 13px" placeholder="Search Here..."></el-input> -->
  </el-menu>

  </div>
</template>

<script>
import router from '@/router/index.js'

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Header",
  data() {
    return {
      activeIndex: '1',
      routes: {'1':'/',
      '4':'/Login'},
      dialogFormVisible: false,
      loginText: 'Log in'
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      this.loginText = 'User'
      router.push({path: this.routes[key]})
    }
  }
}
</script>

<style scoped>
.header {
  top: 0px;
  height: 60px;
  display: flex;
  width: 100%;
  align-content: center;
  background: #ffffff;
  border-bottom: solid 1px #e6e6e6;
}
.menu {
  width: 1200px;
  margin: auto;
  background: #ffffff;
}
.menu-icon{
  object-fit: scale-down;
  height: 20px;
  margin-right: 5px;
  opacity: 0.7;
  /* background: rgb(175, 175, 175); */
}

.menu-text{
  color: rgb(0, 0, 0);
}
</style>