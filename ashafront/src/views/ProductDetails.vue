<template>
    <section>
        <h3>Product Details</h3>
        {{ $route.params.id }}
    </section>
</template>

<script>

export default {

    name:"ProductDetails",
    data(){
        product : {}
    },
    mounted(){
        this.getProduct()
    },
    methods:{
        getProduct(){
            const product_slug = this.$root.params.prouct_slug 
        }
    }
}
</script>