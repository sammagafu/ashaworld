<template>
    <header class="header">
        <div class="header-top">
            <div class="container">
                <div class="header-left">
                    <p class="welcome-msg">Welcome to Asha</p>
                </div>
                <div class="header-right">
                    <div class="dropdown">
                        <a href="#currency">USD</a>
                        <div class="dropdown-box">
                            <a href="#USD">USD</a>
                            <a href="#EUR">TZS</a>
                            <a href="#EUR">GBP</a>
                        </div>
                    </div>
                    <!-- End of DropDown Menu -->

                    <div class="dropdown">
                        <a href="#language"><img src="../assets/images/flags/eng.png" alt="ENG Flag" width="14"
                                height="8" class="dropdown-image" /> EN</a>
                        <div class="dropdown-box">
                            <a href="#ENG">
                                <img src="../assets/images/flags/eng.png" alt="ENG Flag" width="14" height="8"
                                    class="dropdown-image" />
                                EN
                            </a>
                            <a href="#FRA">
                                <img src="../assets/images/flags/fra.png" alt="FRA Flag" width="14" height="8"
                                    class="dropdown-image" />
                                FR
                            </a>

                            <a href="#FRA">
                                <img src="../assets/images/flags/fra.png" alt="FRA Flag" width="14" height="8"
                                    class="dropdown-image" />
                                SW
                            </a>
                        </div>
                    </div>
                    <!-- End of Dropdown Menu -->
                    <span class="divider d-lg-show"></span>
                    <a href="blog.html" class="d-lg-show">Blog</a>
                    <a href="contact-us.html" class="d-lg-show">Contact Us</a>
                    <a href="my-account.html" class="d-lg-show">My Account</a>
                    <a href="assets/ajax/login.html" class="d-lg-show login sign-in"><i class="w-icon-account"></i>Sign
                        In</a>
                    <span class="delimiter d-lg-show">/</span>
                    <a href="assets/ajax/login.html" class="ml-0 d-lg-show login register">Register</a>
                </div>
            </div>
        </div>
        <!-- End of Header Top -->

        <div class="header-middle">
            <div class="container">
                <div class="header-left mr-md-4">
                    <a href="#" class="mobile-menu-toggle  w-icon-hamburger" aria-label="menu-toggle">
                    </a>
                    <router-link to="/"><img src="../assets/images/asha-logo-dark.svg" alt="logo" width="160"
                            height="50" /></router-link>

                    <form method="get" action="#"
                        class="header-search hs-expanded hs-round d-none d-md-flex input-wrapper">
                        <div class="select-box">
                            <select id="category" name="category">
                                <option value="">All Categories</option>
                                <option v-for="(cat, id) in categories" :key="id">
                                    <!-- //todo::pass dyanic value to value -->
                                    {{ cat.categoryname }}
                                </option>
                            </select>
                        </div>
                        <input type="text" class="form-control" name="search" id="search" placeholder="Search in..."
                            required />
                        <button class="btn btn-search" type="submit"><i class="w-icon-search"></i>
                        </button>
                    </form>
                </div>
                <div class="header-right ml-4">
                    <div class="header-call d-xs-show d-lg-flex align-items-center">
                        <a href="tel:#" class="w-icon-call"></a>
                        <div class="call-info d-lg-show">
                            <h4 class="chat font-weight-normal font-size-md text-normal ls-normal text-light mb-0">
                                <a href="mailto:#" class="text-capitalize">Live Chat</a> or :</h4>
                            <a href="tel:+255716282328" class="phone-number font-weight-bolder ls-50">+255 716 282
                                328</a>
                        </div>
                    </div>
                    <a class="wishlist label-down link d-xs-show" href="wishlist.html">
                        <i class="w-icon-heart"></i>
                        <span class="wishlist-label d-lg-show">Wishlist</span>
                    </a>
                    <a class="compare label-down link d-xs-show" href="compare.html">
                        <i class="w-icon-compare"></i>
                        <span class="compare-label d-lg-show">Compare</span>
                    </a>
                    <div class="dropdown cart-dropdown cart-offcanvas mr-0 mr-lg-2">
                        <div class="cart-overlay"></div>
                        <a href="#" class="cart-toggle label-down link">
                            <i class="w-icon-cart">
                                <span class="cart-count">2</span>
                            </i>
                            <span class="cart-label">Cart</span>
                        </a>
                        <div class="dropdown-box">
                            <div class="cart-header">
                                <span>Shopping Cart</span>
                                <a href="#" class="btn-close">Close<i class="w-icon-long-arrow-right"></i></a>
                            </div>

                            <div class="products">
                                <div class="product product-cart">
                                    <div class="product-detail">
                                        <a href="product-default.html" class="product-name">Beige knitted
                                            elas<br>tic
                                            runner shoes</a>
                                        <div class="price-box">
                                            <span class="product-quantity">1</span>
                                            <span class="product-price">$25.68</span>
                                        </div>
                                    </div>
                                    <figure class="product-media">
                                        <a href="product-default.html">
                                            <img src="assets/images/cart/product-1.jpg" alt="product" height="84"
                                                width="94" />
                                        </a>
                                    </figure>
                                    <button class="btn btn-link btn-close" aria-label="button">
                                        <i class="fas fa-times"></i>
                                    </button>
                                </div>

                                <div class="product product-cart">
                                    <div class="product-detail">
                                        <a href="product-default.html" class="product-name">Blue utility
                                            pina<br>fore
                                            denim dress</a>
                                        <div class="price-box">
                                            <span class="product-quantity">1</span>
                                            <span class="product-price">$32.99</span>
                                        </div>
                                    </div>
                                    <figure class="product-media">
                                        <a href="product-default.html">
                                            <img src="assets/images/cart/product-2.jpg" alt="product" width="84"
                                                height="94" />
                                        </a>
                                    </figure>
                                    <button class="btn btn-link btn-close" aria-label="button">
                                        <i class="fas fa-times"></i>
                                    </button>
                                </div>
                            </div>

                            <div class="cart-total">
                                <label>Subtotal:</label>
                                <span class="price">$58.67</span>
                            </div>

                            <div class="cart-action">
                                <a href="cart.html" class="btn btn-dark btn-outline btn-rounded">View Cart</a>
                                <a href="checkout.html" class="btn btn-primary  btn-rounded">Checkout</a>
                            </div>
                        </div>
                        <!-- End of Dropdown Box -->
                    </div>
                </div>
            </div>
        </div>
        <!-- End of Header Middle -->

        <div class="header-bottom sticky-content fix-top sticky-header has-dropdown">
            <div class="container">
                <div class="inner-wrap">
                    <div class="header-left">
                        <div class="dropdown category-dropdown has-border" :class="{show: hoveredMenu}"
                            data-visible="true" @mouseover="hoveredMenu = true" @mouseout="hoveredMenu = false">
                            <a href="#" class="category-toggle text-primary" role="button" data-toggle="dropdown"
                                aria-haspopup="true" aria-expanded="true" data-display="static"
                                title="Browse Categories">
                                <i class="w-icon-category"></i>
                                <span>Browse Categories</span>
                            </a>

                            <div class="dropdown-box" v-show="hoveredMenu">
                                <ul class="menu vertical-menu category-menu">
                                    <template v-if="categories">
                                        <li v-for="(category, index) in categories" :key="index">
                                            <a href="shop-fullwidth-banner.html">
                                                {{ category.categoryname }}
                                            </a>
                                            <SubCategoryTopNav :name="category.categoryname"
                                                :subcategories="category.subcategory" v-if="category.subcategory">
                                            </SubCategoryTopNav>
                                        </li>
                                    </template>
                                </ul>
                            </div>
                        </div>
                        <!--  -->
                        <nav class="main-nav">
                            <ul class="menu active-underline">
                                <li class="active">
                                    <router-link :to="{ name:'home'}">Home</router-link>
                                </li>
                                <li class="has-submenu">
                                    <router-link :to="{ name : 'TheProducts'}">Shop All</router-link>
                                    <!-- <a href="shop-banner-sidebar.html">Shop</a> -->

                                    <!-- Start of Megamenu -->
                                    <ul class="megamenu">
                                        <li v-for="(category, index) in categories" :key="index">
                                            <h4 class="menu-title">{{ category.categoryname }}</h4>
                                            <ul v-for="(subcat, index) in category.subcategory" :key="index">
                                                <li><a href="shop-banner-sidebar.html">{{ subcat.subcategoryname }}</a>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>

                                    <!-- End of Megamenu -->
                                </li>
                                <li><a href="#">Blog</a></li>
                                <li><a href="#">Contact Us</a></li>
                            </ul>
                        </nav>
                    </div>
                    <div class="header-right">
                        <a href="#" class="d-xl-show"><i class="w-icon-map-marker mr-1"></i>Track Order</a>
                        <a href="#"><i class="w-icon-sale"></i>Daily Deals</a>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
    // import { categoryService } from '@/api';
    import axios from 'axios'
    import SubCategoryTopNav from './SubCategoryTopNav.vue'
    export default {
        name: "TopNavigationBar",
        data() {
            return {
                categories: [],
                hoveredMenu: false
            };
        },
        created() {
            // this.fetchCategories().then(data => {
            //     this.categories = data
            // });
        },
        mounted() {
            this.getCategories()
            // .then(data => {
            //                 this.categories = data
            //             });
            console.log('categories', this.categories)
        },
        methods: {
            getCategories() {
                axios.get("/api/v1/category/")
                    .then(response => {
                        this.categories = response.data;
                    }).catch(error => {
                        console.log(error);
                    });
                // categoryService.fetchCategories().then(cat => this.categories = cat).catch(e => console.log(e))
            },
            async fetchCategories() {
                const {
                    data
                } = axios.get("/api/v1/category/")
                return data
            },
            showSub() {
                console.log("its showing")
            }

        }
        //   props: {
        //     msg: String
        //   }
        ,
        components: {
            SubCategoryTopNav
        }
    }
</script>