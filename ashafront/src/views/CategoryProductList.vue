<template>
    <div class="page-content">
        <div class="container">
            <div class="shop-content row gutter-lg mt-10">
                <!-- Start of Sidebar, Shop Sidebar -->
                <aside class="sidebar shop-sidebar sticky-sidebar-wrapper sidebar-fixed">
                    <!-- Start of Sidebar Overlay -->
                    <div class="sidebar-overlay"></div>
                    <a class="sidebar-close" href="#"><i class="close-icon"></i></a>

                    <!-- Start of Sidebar Content -->
                    <div class="sidebar-content scrollable">
                        <!-- Start of Sticky Sidebar -->
                        <div class="pin-wrapper" style="height: 1813.61px;">
                            <div class="sticky-sidebar"
                                style="border-bottom: 0px none rgb(102, 102, 102); width: 280px;">
                                <div class="filter-actions">
                                    <label>Filter :</label>
                                    <a href="#" class="btn btn-dark btn-link filter-clean">Clean All</a>
                                </div>
                                <!-- End of Collapsible Widget -->
                                <!-- <div class="widget widget-collapsible">
                                    <h3 class="widget-title mb-2"><label>Filter By Brand</label><span
                                            class="toggle-btn"></span></h3>
                                    <template v-for="(brand,index) in brands" :key="index">
                                        <div class="mt-3 form-check">
                                            <input type="radio" :value="brand.brandName" v-model="checkedNames" />
                                            <label for="brand" class="ml-1">{{brand.brandName}}</label>
                                        </div>
                                    </template>
                                </div> -->

                                <!-- End of Collapsible Widget -->
                            </div>
                        </div>
                        <!-- End of Sidebar Content -->
                    </div>
                    <!-- End of Sidebar Content -->
                </aside>
                <!-- End of Shop Sidebar -->

                <!-- Start of Shop Main Content -->
                <div class="main-content">
                    <nav class="toolbox sticky-toolbox sticky-content fix-top">
                        <div class="toolbox-left">
                            <a href="#" class="btn btn-primary btn-outline btn-rounded left-sidebar-toggle 
                                        btn-icon-left d-block d-lg-none"><i
                                    class="w-icon-category"></i><span>Filters</span></a>
                            <div class="toolbox-item toolbox-sort select-box text-dark">
                                <label>Sort By :</label>
                                <select name="orderby" class="form-control">
                                    <option value="default" selected="selected">Default sorting</option>
                                    <option value="popularity">Sort by popularity</option>
                                    <option value="rating">Sort by average rating</option>
                                    <option value="date">Sort by latest</option>
                                    <option value="price-low">Sort by pric: low to high</option>
                                    <option value="price-high">Sort by price: high to low</option>
                                </select>
                            </div>
                        </div>
                        <div class="toolbox-right">
                            <div class="toolbox-item toolbox-show select-box">
                                <select name="count" class="form-control">
                                    <option value="9">Show 9</option>
                                    <option value="12" selected="selected">Show 12</option>
                                    <option value="24">Show 24</option>
                                    <option value="36">Show 36</option>
                                </select>
                            </div>
                        </div>
                    </nav>

                    <div class="row product-wrapper mb-7 show-code-action">

                        <div class="col-md-4 col-6" v-for="product in product" :key="product.id">
                            <SingleProduct v-bind:product="product" />
                        </div>

                    </div>


                    <div class="toolbox toolbox-pagination justify-content-between">
                        <p class="showing-info mb-2 mb-sm-0">
                            Showing<span>1-12 of {{product.length}}</span>Products
                        </p>
                        <ul class="pagination">
                            <li class="prev disabled">
                                <a href="#" aria-label="Previous" tabindex="-1" aria-disabled="true">
                                    <i class="w-icon-long-arrow-left"></i>Prev
                                </a>
                            </li>
                            <li class="page-item active">
                                <a class="page-link" href="#">1</a>
                            </li>
                            <li class="page-item">
                                <a class="page-link" href="#">2</a>
                            </li>
                            <li class="next">
                                <a href="#" aria-label="Next">
                                    Next<i class="w-icon-long-arrow-right"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- End of Shop Main Content -->
            </div>
        </div>
    </div>
</template>

<script>
    import TheProducts from './TheProducts.vue'
    import SingleProduct from '../components/SingleProduct.vue'
    import axios from 'axios';
    export default {
        data() {
            return {
                category_slug: '',
                product: {},
            }

        },
        components: {
            TheProducts,
            SingleProduct
        },
        computed() {
            // this.category_slug = this.$route.params.cateogory_slug
        },

       watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
        mounted() {
            this.getProducts()
            console.log('this.$route.params.slug :>> ', this.$route.params.slug);
        },
        methods: {
            getProducts() {
                axios.get(`category/${this.$route.params.slug}/product/`)
                    .then(response => {
                        this.product = response.data;
                        
                        console.log('response.data :>> ', response.data);
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },
        },

        name: "CategoryProductList"
    }
</script>