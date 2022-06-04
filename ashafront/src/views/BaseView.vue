<template>
    <div class="base__view">
        <!-- TopNav -->
        <TopNavigationBar></TopNavigationBar>

        <main class="main__view">
            <router-view></router-view>
        </main>


        <!-- Footer -->
        <!-- <main-footer></main-footer> -->
        <TheFooter></TheFooter>
    </div>
</template>

<script>
import MainFooter from '@/components/MainFooter.vue';
import TopNavigationBar from '@/components/TopNavigationBar.vue';
import TheFooter from '@/components/TheFooter.vue';

    export default {
  components: { MainFooter, TopNavigationBar, TheFooter },
        name:"BaseView",
    }
</script>