<template>
<TopNavigationBar />
<div class="flex">
    <div class="w-1/4">
        <SideBar />
    </div>
    <div class="w-3/4">
        <router-view></router-view> 
    </div>
</div>    
</template>

<script>
    import TopNavigationBar from '@/components/TopNavigationBar.vue'
    import SideBar from '@/components/SideBar.vue'
    import Footer from '@/components/Footer.vue'
    export default {
        name: 'BaseApp',
        components: {
            TopNavigationBar,SideBar,Footer
        }
    }
</script>

<style>

</style>