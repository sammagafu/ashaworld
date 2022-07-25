<template>
    <main class="main cart">
        <!-- Start of Breadcrumb -->
        <nav class="breadcrumb-nav">
            <div class="container">
                <ul class="breadcrumb shop-breadcrumb bb-no">
                    <li>
                        <router-link :to="{name:'home'}">Home</router-link>
                    </li>
                    <li class="active"><a href="#">Cart</a></li>
                </ul>
            </div>
        </nav>
        <!-- End of Breadcrumb -->

        <!-- Start of PageContent -->
        <div class="page-content">
            <div class="container">
                <div class="row gutter-lg mb-10">
                    <div class="col-lg-8 pr-lg-4 mb-6">
                        <table class="shop-table cart-table">
                            <thead>
                                <tr>
                                    <th class="product-name"><span>Product</span></th>
                                    <th></th>
                                    <th class="product-price"><span>Price</span></th>
                                    <th class="product-quantity"><span>Quantity</span></th>
                                    <th class="product-subtotal"><span>Subtotal</span></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(cart,index) in $store.state.cartItems" :key="index">
                                    <td class="product-thumbnail">
                                        <div class="p-relative">
                                            <router-link :to="cart.product.get_absolute_url">
                                                <figure>
                                                    <img :src="cart.product.get_coverImage" alt="product" width="300"
                                                        height="338">
                                                </figure>
                                            </router-link>
                                            <button type="submit" class="btn btn-close"><i class="fas fa-times"
                                                    @click="removeItemFromCart(cart.id)"></i></button>
                                        </div>
                                    </td>
                                    <td class="product-name">
                                        <router-link :to="cart.product.get_absolute_url">{{cart.product.productName}}
                                        </router-link>
                                    </td>
                                    <td class="product-price"><span class="amount">{{cart.product.price}}</span></td>
                                    <td class="product-quantity">
                                        <div class="input-group">
                                            <input class="quantity form-control" type="number" min="1" max="100000">
                                            <button class="quantity-plus w-icon-plus"></button>
                                            <button class="quantity-minus w-icon-minus"></button>
                                        </div>
                                    </td>
                                    <td class="product-subtotal">
                                        <span class="amount">{{cart.get_total_price }}</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="cart-action mb-6">
                            <router-link :to="{name:'home'}" class="btn btn-dark btn-rounded btn-icon-left btn-shopping mr-auto"><i class="w-icon-long-arrow-left"></i>Continue Shopping</router-link>
                            <!-- <a href="#" class="btn btn-dark btn-rounded btn-icon-left btn-shopping mr-auto"><i
                                    class="w-icon-long-arrow-left"></i>Continue Shopping</a> -->
                            <button type="submit" class="btn btn-rounded btn-default btn-clear" name="clear_cart"
                                value="Clear Cart">Clear Cart</button>
                            <button type="submit" class="btn btn-rounded btn-update disabled" name="update_cart"
                                value="Update Cart">Update Cart</button>
                        </div>

                        <form class="coupon">
                            <h5 class="title coupon-title font-weight-bold text-uppercase">Coupon Discount</h5>
                            <input type="text" class="form-control mb-4" placeholder="Enter coupon code here..."
                                required="">
                            <button class="btn btn-dark btn-outline btn-rounded">Apply Coupon</button>
                        </form>
                    </div>
                    <div class="col-lg-4 sticky-sidebar-wrapper">
                        <div class="pin-wrapper" style="height: 791.375px;">
                            <div class="sticky-sidebar"
                                style="border-bottom: 0px none rgb(102, 102, 102); width: 393.32px;">
                                <div class="cart-summary mb-4">
                                    <h3 class="cart-title text-uppercase">Cart Totals</h3>
                                    <ul class="shipping-methods mb-2">
                                        <li>
                                            <label class="shipping-title text-dark font-weight-bold">Shipping</label>
                                        </li>
                                        <li>
                                            <div class="custom-radio">
                                                <input type="radio" id="free-shipping" class="custom-control-input"
                                                    name="shipping">
                                                <label for="free-shipping" class="custom-control-label color-dark">Shipping</label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="custom-radio">
                                                <input type="radio" id="local-pickup" class="custom-control-input"
                                                    name="shipping">
                                                <label for="local-pickup" class="custom-control-label color-dark">Local
                                                    Pickup</label>
                                            </div>
                                        </li>
                                        
                                    </ul>

                                    <div class="shipping-calculator">
                                        <form class="shipping-calculator-form" @submit.prevent="checkout">
                                            <div class="form-group">
                                                <input class="form-control form-control-md" type="text" name="town-city"
                                                    placeholder="Full Name">
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control form-control-md" type="text" name="town-city"
                                                    placeholder="Phone Number">
                                            </div>
                                            <div class="form-group">
                                                <textarea name="address" id="" class="form-control" placeholder="Enter your Phyiscal address"></textarea>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control form-control-md" type="text" name="town-city"
                                                    placeholder="Town / City">
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control form-control-md" type="text" name="zipcode"
                                                    placeholder="ZIP">
                                            </div>
                                            <input type="hidden" name="items" v-model="$store.state.cartItems">
                                            <input type="hidden" name="sum" v-model="Sum">
                                        
                                    

                                    <hr class="divider mb-6">
                                    <div class="order-total d-flex justify-content-between align-items-center">
                                        <label>Total</label>
                                        <span class="ls-50">TZS {{Sum}}</span>
                                    </div>
                                         <button type="submit" class="btn btn-block btn-dark btn-icon-right btn-rounded  btn-checkout">Proceed to checkout<i class="w-icon-long-arrow-right"></i></button>
                                    </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- End of PageContent -->
    </main>
</template>

<script>
import axios from 'axios';
import { useRouter } from "vue-router";
import { mapState } from 'vuex';
    export default {
        name: 'CartItems',
        data(){
            return {
                sum : 0,
                router:useRouter(),
            }
        },
        methods: {
            removeItemtoCart(item) {
                axios.delete(`/cart/${localStorage.getItem('userid')}/delete`)
                    .then(response => this.$router.go(this.$router.currentRoute))
                    .catch(error => {
                        element.parentElement.innerHTML = `Error: ${error.message}`;
                        console.error('There was an error tony!', error);
                    });
            },
            checkout(){
                this.sum = this.Sum //calculates totalproce
                const data = {
                    'orderproducts' :  this.cartItems.map(x=>{return x.product.id}),
                    'totalprice' : this.sum.toString(),
                    'owner':localStorage.getItem('userid')
                }
                console.log('orderitems :>> ', data);
                axios.post('order/',data)
                .then(response => {
                    console.log('object >> ', response);
                    //clear cart here
                    this.$store.commit("clearCart")
                    this.removeItemtoCart(1)
                    //go home
                    this.router.push({name:"home"})
                    })
                    .catch(error => {
                        // element.parentElement.innerHTML = `Error: ${error.message}`;
                        console.error('There was an error!', error.stack);
                    });
            },
            clearCart(){
                this.$store.commit("clearCart")
            }
        },
        computed:{
            ...mapState(["cartItems"]),
            Sum(){ return this.$store.state.cartItems.reduce( (Sum, product) => product.get_total_price + Sum  ,0);},
        }
    }
</script>

<style>
</style>