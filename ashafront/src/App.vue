<template>
  <TopNavigationBar />
  <SliderComponent />
  <div class="page-content mb-10 pb-2 mt-10">
    <div class="container">
      <ProductList />
    </div>
  </div>
</template>

<script>
  import TopNavigationBar from './components/TopNavigationBar.vue';
  import SliderComponent from './components/SliderComponent.vue';
  import MainFooter from './components/MainFooter.vue';
  import ProductList from './components/ProductList.vue';

  export default {
    name: 'app',
    components: {
      TopNavigationBar,
      SliderComponent,
      MainFooter,
      ProductList
    }
  }
</script>

<style>
  @import './assets/css/asha.min.css';
  @import './assets/css/style.min.css';
</style>