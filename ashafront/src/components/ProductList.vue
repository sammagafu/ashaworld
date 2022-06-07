<template>
    <section>
        <div class="row product-wrapper mb-7 show-code-action">

            <div class="col-md-3 col-6" v-for="prod in product" :key="prod.id">
                <SingleProduct :category="prod.category.categoryname" :title="prod.productName" :image="prod.coverImage" :price="prod.price" :slug="prod.slug"/>
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
            axios.get("/api/v1/product/")
                .then(response => { this.product = response.data; })
                .catch(error => { console.log(error); });
        }
    },
    components: { SingleProduct }
}

</script>