<template>
<TopNavigationBar />
<div class="flex flex-row">
    <div class="basis-1/12">
        <SideBar />
    </div>
    <div class="basis-11/12">
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