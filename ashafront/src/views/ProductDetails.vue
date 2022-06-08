<template>
    <section class="mt-10">
        <div class="page-content">
            <div class="container" v-if="product">
                <ProductDetail 
                v-if="product"
                :productname="product.productName" 
                :category="product.category" 
                :sku="product.sku" 
                :price="product.price" 
                :images="product.images" 
                :brand="product.brand"
                />
            </div>
            <div class="" v-else>Loading Data</div>
        </div>

    </section>
</template>

<script>
    import axios from 'axios';
    import ProductDetail from '@/components/ProductDetail.vue';

    export default {
        name: "ProductDetails",
        data() {
            return {
                product: {},
                url_data: this.$route.params.slug
            };
        },
        mounted() {
            // this.url_data = this.$route.params.slug
           
            this.getProductdetail()
            console.log('kimepop',this.product);
        },
        methods: {
            getProductdetail() {
                console.log('this.url_data :>> ', this.url_data);
                axios.get(`product/${this.$route.params.slug}/`)
                    .then((response) => {
                        this.product = response.data
                        console.log('this.product :>> ', this.product);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
        components: {
            ProductDetail
        }
    }
</script>