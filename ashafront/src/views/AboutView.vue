<template>
  <div class="about">
    <TopNavigationBar/>
    <h1>This is an about page</h1>
  </div>
</template>


<script>
import TopNavigationBar from '@/components/TopNavigationBar.vue'
export default{
  name:'AboutView',
  components:{
  TopNavigationBar,
  }
}
</script>