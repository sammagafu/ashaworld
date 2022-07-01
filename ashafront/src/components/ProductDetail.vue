<template>

    <div class="row gutter-lg">
        <div class="main-content">
            <div class="product product-single row">
                <div class="col-md-6 mb-6">
                    <div class="product-gallery product-gallery-sticky product-gallery-vertical">
                        <ProductImageSwiper :images="productImages" />
                    </div>
                </div>
                <div class="col-md-6 mb-4 mb-md-6">
                    <div class="product-details" data-sticky-options="{'minWidth': 767}">
                        <h1 class="product-title">{{ productname }}</h1>
                        <div class="product-bm-wrapper">
                            <figure class="brand">
                                <img :src="brand.get_brandImg" width="102" height="48">
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
                            {{description}}
                        </div>

                        <hr class="product-divider">
                        <div class="sticky-content-wrapper">
                            <div class="fix-bottom product-sticky-content sticky-content">
                                <div class="product-form container">
                                    <div class="product-qty-form">
                                        <div class="input-group">
                                            <input class="quantity form-control" type="number" min="1" max="10000000"
                                                v-model="numberOfProducts">
                                            <button class="quantity-plus w-icon-plus"
                                                @click="numberOfProducts ++ "></button>
                                            <button class="quantity-minus w-icon-minus" @click="decrement"></button>
                                        </div>
                                    </div>
                                    <button class="btn btn-primary btn-cart" @click="addProductToCart(slug)">
                                        <i class="w-icon-cart"></i>
                                        <span>Add to Cart</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductImageSwiper from "./ProductImageSwiper.vue";
    import axios from "axios";
    export default {
        name: "ProductDetail",
        // props: ["productname", "category", "sku", "price", "images", "brand"],
        props: {
            productname: {
                type: String,
                required: true,
            },
            category: {
                type: Object,
                default: {},
            },
            productImages: {
                type: Object,
                default: {},
            },
            sku: {
                type: String,
            },
            price: {
                type: String,
            },
            images: {
                type: String,
            },
            brand: {
                type: String,
                default: {},
            },
            description: {
                type: String,
                default: {},
            },
            slug: {
                type: String,
                default: {},
            },
        },
        mounted() {},
        components: {
            ProductImageSwiper
        },
        data() {
            return {
                numberOfProducts: 1,
            }
        },
        methods: {
            decrement() {
                if (this.numberOfProducts === 0) return
                this.numberOfProducts -= 1
            },
            addProductToCart(product){;
                const data = {
                    quantity:this.numberOfProducts,
                     product:product
                }
                axios.post('/cart/add/',data)
                const toPath = this.$route.query.to || '/cart'
                this.$router.push(toPath)
            },
        }

    }
</script>