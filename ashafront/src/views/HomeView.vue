<template>
  <section>
    <SliderComponent />
    <div class="page-content mb-10 pb-2 mt-10">
      <div class="container">
        <div class="title-link-wrapper pb-1 mb-4">
          <h2 class="title ls-normal mb-0">Recently Added</h2>
          <router-link :to="{name: 'TheProducts'}" class="font-size-normal font-weight-bold ls-25 mb-0">More
            Products<i class="w-icon-long-arrow-right"></i></router-link>
        </div>
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