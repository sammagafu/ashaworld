<template>
  <router-view></router-view>
</template>

<script>
  import axios from 'axios'
  export default {
    
    name: 'app',
    components: {},
    beforeCreate() {
      this.$store.commit('initializeStore')
      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
      // if (!this.$store.state.team.id) {
      //   this.$router.push('/dashboard/add-team')
      // }
    },
  }
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;700;900&display=swap');
body{
  font-family: 'Poppins', Courier, monospace;
}
</style>