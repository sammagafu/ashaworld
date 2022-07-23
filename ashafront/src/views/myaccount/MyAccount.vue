<template>
    <div class="page-header">
        <div class="container">
            <h1 class="page-title mb-0">My Account</h1>
        </div>
    </div>
    <div class="container">
        <div class="row mt-10" id="account-dashboard">
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <router-link :to="{name:'myorders'}">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-orders">
                            <i class="w-icon-orders"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">My Orders</p>
                        </div>
                    </div>
                </router-link>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <a href="#account-downloads" class="link-to-tab">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-download">
                            <i class="w-icon-download"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">Downloads</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <a href="#account-addresses" class="link-to-tab">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-address">
                            <i class="w-icon-map-marker"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">Addresses</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <a href="#account-details" class="link-to-tab">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-account">
                            <i class="w-icon-user"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">Account Details</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <a href="wishlist.html" class="link-to-tab">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-wishlist">
                            <i class="w-icon-heart"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">Wishlist</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 mb-4">
                <a href="#">
                    <div class="icon-box text-center">
                        <span class="icon-box-icon icon-logout">
                            <i class="w-icon-logout"></i>
                        </span>
                        <div class="icon-box-content">
                            <p class="text-uppercase mb-0">Logout</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {

    }
</script>

<style>

</style>