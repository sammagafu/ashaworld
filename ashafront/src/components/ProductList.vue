<template>
    <section>
        <div class="row product-wrapper mb-7 show-code-action">

            <div class="col-md-3 col-6" v-for="product in product" :key="product.id">
                <SingleProduct
                v-bind:product="product" 
                />
            </div>
            
        </div>

    </section>
</template>

<script>
import axios from 'axios'
import SingleProduct from './SingleProduct.vue'

export default{
    name: "ProductList",
    data() {
        return {
            product: []
        };
    },
    mounted() {
        this.getProducts();
    },
    methods: {
        getProducts() {
            axios.get("product/")
                .then(response => { this.product = response.data; })
                .catch(error => { console.log(error); });
        }
    },
    components: { SingleProduct }
}

</script>