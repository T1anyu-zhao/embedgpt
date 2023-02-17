<template>
  <Header></Header>
  <router-view />
  <Footer></Footer>
</template>
<script>

import Header from './components/header.vue'
import Footer from './components/footer.vue'
export default {
  name: 'App',
  components: {
    // Home
    Footer,
    Header,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgb(255, 255, 255);
  height: 100%;
  /* background-image: url("http://pic.616pic.com/bg_w1180/00/17/08/xsgGkAMMmm.jpg"); */
}
</style>
