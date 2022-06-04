<template>
    <section class="admin-base__view">
        <div class="container">
            <h3>Admin Routes</h3>
        </div>

        <main class="admin__main">
            <router-view></router-view>
        </main>
    </section>
</template>

<script>
export default {

    name:"AdminBaseView",
    
}
</script>