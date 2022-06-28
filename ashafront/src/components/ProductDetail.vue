<template>

            <div class="row gutter-lg">
                <div class="main-content">
                    <div class="product product-single row">
                        <div class="col-md-6 mb-6">
                            <div class="product-gallery product-gallery-sticky product-gallery-vertical"><ProductImageSwiper :images="images"/></div>
                        </div>
                        <div class="col-md-6 mb-4 mb-md-6">
                            <div class="product-details" data-sticky-options="{'minWidth': 767}">
                                <h1 class="product-title">{{ productname }}</h1>
                                <div class="product-bm-wrapper">
                                    <figure class="brand">
                                        <img :src="brand.brandlogo" width="102"
                                            height="48">
                                    </figure>
                                    <div class="product-meta">
                                        <div class="product-categories">
                                            Category:
                                            <span class="product-category"><a href="#">{{ category.categoryname}}</a></span>
                                        </div>
                                        <div class="product-sku">
                                            SKU: <span>{{sku}}</span>
                                        </div>
                                    </div>
                                </div>

                                <hr class="product-divider">

                                <div class="product-price"><ins class="new-price">TZS {{price}}</ins></div>

                                <div class="ratings-container">
                                    <div class="ratings-full">
                                        <span class="ratings" style="width: 80%;"></span>
                                        <span class="tooltiptext tooltip-top"></span>
                                    </div>
                                    <a href="#product-tab-reviews" class="rating-reviews scroll-to">(3
                                        Reviews)</a>
                                    </div>

                                    <div class="product-short-desc">
                                        <ul class="list-type-check list-style-none">
                                            <li>Ultrices eros in cursus turpis massa cursus mattis.</li>
                                            <li>Volutpat ac tincidunt vitae semper quis lectus.</li>
                                            <li>Aliquam id diam maecenas ultricies mi eget mauris.</li>
                                        </ul>
                                    </div>

                                <hr class="product-divider">                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
</template>

<script>
import ProductImageSwiper from "./ProductImageSwiper.vue";
    export default {
    name: "ProductDetail",
    // props: ["productname", "category", "sku", "price", "images", "brand"],
    props:{
        productname:{
            type: String,
            required:true,
        },
        category:{
            type: Object,
            default:{},
        },
        sku:{
            type: String,
        },price:{
            type: String,
        },images:{
            type: String,
        },brand:{
            type: String,
            default:{},
        },
    },
    mounted() { },
    components: { ProductImageSwiper }
}
    
</script>