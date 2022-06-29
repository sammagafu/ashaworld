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

<style>
  @import './assets/css/style.min.css';
  @import './assets/css/asha.min.css';
</style>