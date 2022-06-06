<template>
    <section class="mt-10">
        <div class="page-content">
            <div class="container">
                <h3>{{ product.productName }} Details</h3>
                <ProductDetail :productname="product.productName" :category="product.category" :sku="product.sku" :price="product.price" :images="product.images" :brand="product.brand"/>
            </div>
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
                product: [],
                url_data: null
            };
        },
        mounted() {
            this.url_data = this.$route.params.slug;
            this.getProductdetail();
        },
        methods: {
            getProductdetail() {
                axios.get(`api/v1/product/${this.url_data}`)
                    .then((response) => {
                        this.product = response.data;
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