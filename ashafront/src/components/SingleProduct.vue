<template>
    <div class="product product-image-gap product-simple">
        <figure class="product-media">
            <router-link :to="product.get_absolute_url"> <img :src="product.get_coverImage" alt="Product" width="295" height="335">
            </router-link>
            <div class="product-action-vertical">
                <a href="#" class="btn-product-icon btn-compare w-icon-compare" title="Compare" @click="addTocompare(product)">
                </a>
            </div>
            <div class="product-action">
                <a href="#" @click="showModal = true" class="btn-product btn-quickview" title="Quick View">Quick
                    View</a>
            </div>
            <!-- <modal v-if="showModal" @close="showModal = false"></modal>
             -->
             <quick-view-product v-if="showModal"></quick-view-product>
        </figure>
        <div class="product-details">
            <a href="#" @click="addToWishlist(product.slug)" class="btn-wishlist w-icon-heart" title="Add to wishlist"></a>
            <div class="product-cat">
                <a href="shop-banner-sidebar.html">{{ product.category.categoryname }}</a>
            </div>
            <h4 class="product-name text-uppercase">
                <router-link :to="product.get_absolute_url">{{ product.productName }}</router-link>
            </h4>
            <div class="ratings-container">
                <div class="ratings-full">
                    <span class="ratings" style="width: 100%;"></span>
                    <span class="tooltiptext tooltip-top">5.00</span>
                </div>
                <a href="product-default.html" class="rating-reviews">(3 reviews)</a>
            </div>
            <div class="product-pa-wrapper">
                <div class="product-price">TZS {{product.price}}</div>
                <div class="product-action" v-show="$store.state.isAuthenticated">
                    <a href="#" class="btn-cart btn-product btn btn-link btn-underline"
                        :class="isAdded ? cartOverlayClass : '' " @click="addProductToCart(product.slug)">Add
                        To Cart</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
import QuickViewProduct from './QuickViewProduct.vue'
    export default {
  components: { QuickViewProduct },
        name: "SingleProduct",
        data() {
            return {
                isAdded: false,
                showModal : false,
                cartOverlayClass: ['cart-offcanvas','cart-overlay']
            }
        },
        props: {
        product: Object
    },
        methods: {
            addTocompare(product) {
            //      if (isNaN(this.quantity) || this.quantity < 1) {
            //     this.quantity = 1
            // }
            // const item = {
            //     product: this.product,
            //     quantity: this.quantity
            // }
            this.$store.commit('addToCompare', product)
            },
            addProductToCart(product){
                const data = {
                    quantity:1,
                     product:product
                }
                axios.post('/cart/add/',data)
            },
            addToWishlist(product){
                const data = {
                     product:product
                }
                axios.post('/cart/wishlist/',data)
            }


        },
    }
</script>