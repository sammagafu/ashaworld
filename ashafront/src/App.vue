<template>
  <router-view></router-view>
</template>

<script>


  export default {
    name: 'app',
    components: {
    },

    mounted:function(){
      const user = {
        isAdmin: true
      }

      localStorage.setItem("ashaUser", JSON.stringify(user))

      const usr = JSON.parse(localStorage.getItem("ashaUser"))
              console.log("user", usr)
    }

  }
</script>

<style>
@import './assets/css/style.min.css';
@import './assets/css/asha.min.css';
  
</style>