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
                :images="product.get_coverImage" 
                :brand="product.brand"
                :description="product.descripton"
                :slug="product.slug"
                :productImages="product.images"
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
        },
        methods: {
            getProductdetail() {
                const category_slug = this.$route.params.category_slug
                const product_slug = this.$route.params.product_slug

                console.log('this.url_data :>> ', this.url_data);
                axios.get(`product/${category_slug}/${product_slug}/`)
                    .then((response) => {
                        this.product = response.data
                        document.title = this.product.productName + ' | Asha'
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