<template>
    <div class="product product-image-gap product-simple">
        <figure class="product-media">
            <a href="product-default.html">
                <img :src="image" alt="Product" width="295" height="335">
            </a>
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
                <router-link :to=this.$route.params>{{ title }}</router-link>
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
                    <a href="#" class="btn-cart btn-product btn btn-link btn-underline">Add
                        To Cart</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name:"SingleProduct",
    props:[
        'image','category','price','title','get_absolute_url'
    ]
}
</script>