<template>
</template>

<script>
    import TheProducts from './TheProducts.vue'
    export default {
        data (){
            return{
                slug:"",
                selected:{
                    brands:[],
                    prices:[],
                    manufacture:[]
                }
            }
            
        },
        components: {
            TheProducts,
        },
        mounted() {
            this.slug = this.$route.query.name;
            this.filterbyBrand()
        },
        methods: {
            filterbyBrand(brandName){
                console.log();
            }
        },

        name: "CategoryProductList"
    }
</script>