<template>
<TopNavigationBar />
<div class="flex flex-row">
    <div class="md:flex">
        <div class="basis-3/12">
            <SideBar />
        </div>
        <div class="basis-9/12 mt-4 mx-6">
            <router-view></router-view> 
        </div>
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