<template>
  <div class="container">
    <div>
      <div class="shadedbox">
        <form>
          <div class="form-group" style="background: #e6e6e6; height: 260px;">
            <img src="../assets/icon/user.png" style="height:100px; width: 100px; ">
          </div>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" v-model="username">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" v-model="password">
          </div>
          <el-button type="primary" @click="submitLogin" style="margin: 10px">Log in</el-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'LoginPage',
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
    submitLogin() {
      this.$router.push({ name: 'User' });    
    }
  }
}
</script>
<style>
.container {
  padding: 20px;
  height: 660px;
  display: flex; 
  justify-content: center;
  align-items: center;
}

.form-group{
  margin: 10px;
  display: flex; 
  justify-content: center;
  align-items: center;
}

.form-control{
  margin: 10px;
}

.shadedbox {
    background-color: white;
    border-radius: 14px;
    border: 2px solid rgb(199, 198, 198);
    box-shadow: 2px 2px 2px 1px rgba(78, 78, 255, 0.2);
    margin: 25px
  }
</style>