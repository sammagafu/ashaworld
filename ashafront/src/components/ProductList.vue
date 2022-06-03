<template>
    <section>
        <h2 class="title title-center mb-5">Newest Products</h2>
        <div class="row product-wrapper mb-7 show-code-action">

            <div class="col-md-4 col-6" v-for="prod in product" :key="prod.id">
                <div class="product text-center">
                    <figure class="product-media">
                        <a href="">
                            <img :src="prod.coverImage" alt="altText"/>
                            <!-- <img src="../assets/images/products/elements/1.jpg" alt="Product" width="295" height="335"> -->
                        </a>
                        <div class="product-label-group">
                            <label class="product-label label-new">New</label>
                        </div>
                        <div class="product-action-vertical">
                            <a href="#" class="btn-product-icon btn-cart w-icon-cart" title="Add to cart"></a>
                            <a href="#" class="btn-product-icon btn-wishlist w-icon-heart" title="Wishlist"></a>
                            <a href="#" class="btn-product-icon btn-compare w-icon-compare" title="Compare"></a>
                            <a href="#" class="btn-product-icon btn-quickview w-icon-search" title="Quick View"></a>
                        </div>
                    </figure>
                    <div class="product-details">
                        <h3 class="product-name">
                            <a href="">{{prod.productName}}</a>
                        </h3>
                        <div class="product-price">{{prod.price}}</div>
                    </div>
                </div>
            </div>
            
        </div>

    </section>
</template>

<script>
import axios from 'axios'

export default{
    name:'ProductList',
    data (){
        return {
            product : []
        }
    },
    mounted (){
        this.getProducts()
    },
    methods :{
        getProducts(){
            axios.get('/api/v1/product/')
            .then(response => {this.product = response.data})
            .catch(error => {console.log(error)})
        }
    }

}

</script>