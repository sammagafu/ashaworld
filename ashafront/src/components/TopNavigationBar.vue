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
                    <!-- <a href="my-account.html" class="d-lg-show">My Account</a> -->
                    <router-link :to="{name:'my-account'}" class="d-lg-show">My Account</router-link>
                    <router-link :to="{name:'login'}" class="d-lg-show"><i class="w-icon-account"></i> Sign
                        In</router-link>
                    <span class="delimiter d-lg-show">/</span>
                    <router-link :to="{name:'signup'}"  class="ml-0 d-lg-show login register"> Register </router-link>
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
                                <option v-for="(cat, id) in $store.state.categories" :key="id">
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
                    <a class="" href="wishlist.html">
                        
                    </a>
                    <router-link :to="{name:'wishlist'}" class="wishlist label-down link d-xs-show"><i class="w-icon-heart"></i><span class="wishlist-label d-lg-show">Wishlist</span></router-link>
                    <router-link :to="{name:'compared'}" class="compare label-down link d-xs-show"><i class="w-icon-compare"></i>
                        <span class="compare-label d-lg-show">Compare</span></router-link>
                    <div class="dropdown cart-dropdown cart-offcanvas mr-0 mr-lg-2" :class="{ opened : isOpenedCart }">
                        <div class="cart-overlay"></div>
                        <router-link :to="{name:'cart'}" class="cart-toggle label-down link"><i class="w-icon-cart">
                                <span class="cart-count">{{$store.state.cartItems.length}}</span>
                            </i>
                            <span class="cart-label">Cart</span></router-link>
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
                                <i class="w-icon-grid"></i>
                                <span>Browse Categories</span>
                            </a>

                            <div class="dropdown-box" v-show="hoveredMenu">
                                <ul class="menu vertical-menu category-menu">
                                    <template v-if="categories">
                                        <li v-for="(category, index) in $store.state.categories" :key="index">
                                        <router-link :to="{name: 'CategoryProducts', params:{slug:category.slug}}">{{ category.categoryname }}</router-link>

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
                                <li>
                                    <router-link :to="{ name : 'TheProducts'}">Shop All</router-link>
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
    // import {useStore} from '../store/index'
    export default {
        name: "TopNavigationBar",
        data() {
            return {
                categories: [],
                hoveredMenu: false,
                isOpenedCart : false,
            };
        },
        created() {
            // this.fetchCategories().then(data => {
            //     this.categories = data
            // });
        },
        mounted() {
            // this.$router.go(this.$router.currentRoute)
            this.$store.dispatch('getCategories')
            this.$store.dispatch('getCartItems')
        },
        methods: {
        },
        components: {
            SubCategoryTopNav
        }
    }
</script>