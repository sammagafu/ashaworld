<template>
  <section>
    <SliderComponent />
    <div class="page-content mb-10 pb-2 mt-10">
      <div class="container">
        <ProductList />
      </div>
    </div>
  </section>
</template>

<script>
  import SliderComponent from '@/components/SliderComponent.vue';
  import ProductList from '@/components/ProductList.vue';

  export default {
    name: 'HomeView',
    components: {
      ProductList,
      SliderComponent
    }
  }
</script>