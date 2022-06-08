<template>
    <div class="product product-image-gap product-simple">
        <figure class="product-media">
            <router-link :to="`/product/${slug}`"> <img :src="image" alt="Product" width="295" height="335">
            </router-link>
            <div class="product-action-vertical">
                <a href="#" class="btn-product-icon btn-compare w-icon-compare" title="Compare">

                </a>
            </div>
            <div class="product-action">
                <a href="#" class="btn-product btn-quickview" title="Quick View">Quick
                    View</a>
            </div>
        </figure>
        <div class="product-details">
            <a href="#" class="btn-wishlist w-icon-heart" title="Add to wishlist"></a>
            <div class="product-cat">
                <a href="shop-banner-sidebar.html">{{ category}}</a>
            </div>
            <h4 class="product-name">
                <router-link :to="`/product/${slug}`">{{ title }}</router-link>
            </h4>
            <div class="ratings-container">
                <div class="ratings-full">
                    <span class="ratings" style="width: 100%;"></span>
                    <span class="tooltiptext tooltip-top">5.00</span>
                </div>
                <a href="product-default.html" class="rating-reviews">(3 reviews)</a>
            </div>
            <div class="product-pa-wrapper">
                <div class="product-price">TZS {{price}}</div>
                <div class="product-action">
                    <a href="#" class="btn-cart btn-product btn btn-link btn-underline"
                        :class="isAdded ? cartOverlayClass : '' " @click="addTocart">Add
                        To Cart</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "SingleProduct",
        data() {
            return {
                isAdded: false,
                cartOverlayClass: ['cart-offcanvas','cart-overlay']
            }
        },
        props: [
            'image', 'category', 'price', 'title', 'slug',
        ],
        methods: {
            addTocart() {
                this.isAdded = true
            }
        }
    }
</script>