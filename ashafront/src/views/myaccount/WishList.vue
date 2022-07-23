<template>
<main class="main wishlist-page">
            <!-- Start of Page Header -->
            <div class="page-header">
                <div class="container">
                    <h1 class="page-title mb-0">Wishlist</h1>
                </div>
            </div>
            <!-- End of Page Header -->

            <!-- Start of PageContent -->
            <div class="page-content mt-10">
                <div class="container">
                    <h3 class="wishlist-title">My wishlist</h3>
                    <table class="shop-table wishlist-table">
                        <thead>
                            <tr>
                                <th class="product-name"><span>Product</span></th>
                                <th></th>
                                <th class="product-price"><span>Price</span></th>
                                <th class="product-stock-status"><span>Stock Status</span></th>
                                <th class="wishlist-action">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(wish,index) in wishlist" :key="index">
                                <td class="product-thumbnail">
                                    <div class="p-relative">
                                        <router-link :to="wish.product.get_absolute_url">
                                        <figure><img :src="wish.product.get_coverImage" alt="product"/></figure>
                                        </router-link>

                                        <button type="submit" class="btn btn-close"><i class="fas fa-times"></i></button>
                                    </div>
                                </td>
                                <td class="product-name">
                                    <router-link :to="wish.product.get_absolute_url" class="product-name">{{wish.product.productName}}</router-link>
                                </td>
                                <td class="product-price">
                                    <ins class="new-price">{{wish.product.price}}</ins>
                                </td>
                                <td class="product-stock-status">
                                    <span class="wishlist-in-stock">In Stock</span>
                                </td>
                                <td class="wishlist-action">
                                    <div class="d-lg-flex">
                                        <a href="#" class="btn btn-quickview btn-outline btn-default btn-rounded btn-sm mb-2 mb-lg-0">Quick
                                            View</a>
                                        <a href="#" class="btn btn-dark btn-rounded btn-sm ml-lg-2 btn-cart">Add to
                                            cart</a>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- End of PageContent -->
        </main>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'WishList',
        data() {
            return {
                wishlist: []
            }
        },
        mounted(){
            this.getWishlistProduct()
        },
        methods: {
            getWishlistProduct() {
                axios.get('cart/wishlist/')
                    .then(response => {
                        this.wishlist = response.data;
                        console.log('response.data :>> ', response.data);
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }


    }
</script>

<style>

</style>