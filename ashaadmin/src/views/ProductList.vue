<template>
    <div class="mt-6">
        <div class="columns">
            <div class="column is-four-fifths">
                <h1>Products</h1>
            </div>
            <div class="column">
                <p class="buttons">
                    <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                        <span class="icon is-small">
                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M10.8989 7.75503C11.1994 7.48146 11.6647 7.50325 11.9383 7.8037C12.2118 8.10415 12.1901 8.56948 11.8896 8.84306L7.99852 12.3861L4.10744 8.84306C3.80699 8.56948 3.7852 8.10415 4.05877 7.8037C4.33235 7.50325 4.79768 7.48146 5.09813 7.75503L7.26278 9.72604V0.735742C7.26278 0.329402 7.59218 0 7.99852 0C8.40486 0 8.73426 0.329402 8.73426 0.735742V9.72604L10.8989 7.75503ZM1.45455 12.3633C1.45455 11.9617 1.12893 11.6361 0.727273 11.6361C0.325611 11.6361 0 11.9617 0 12.3633V13.333C0 14.8058 1.19391 15.9997 2.66667 15.9997H13.3333C14.8061 15.9997 16 14.8058 16 13.333V12.3633C16 11.9617 15.6744 11.6361 15.2727 11.6361C14.8711 11.6361 14.5455 11.9617 14.5455 12.3633V13.333C14.5455 14.0025 14.0028 14.5451 13.3333 14.5451H2.66667C1.99723 14.5451 1.45455 14.0025 1.45455 13.333V12.3633Z"
                                    fill="#3F434A" />
                            </svg>
                        </span>
                        <span>Export</span>
                    </button>
                    <button class="button is-primary">
                        <span class="icon is-small">
                            <svg width="20" height="20" viewBox="0 0 20 20" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M11 5C11 4.44772 10.5523 4 10 4C9.44772 4 9 4.44772 9 5V9H5C4.44772 9 4 9.44772 4 10C4 10.5523 4.44772 11 5 11H9V15C9 15.5523 9.44772 16 10 16C10.5523 16 11 15.5523 11 15V11H15C15.5523 11 16 10.5523 16 10C16 9.44772 15.5523 9 15 9H11V5Z"
                                    fill="white" />
                            </svg>

                        </span>
                    </button>
                </p>
            </div>
        </div>
        <div class="tabs is-boxed">
            <ul>
                <li class="is-active">
                    <a>
                        <span>All</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span>availabe</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span>Unavailable</span>
                    </a>
                </li>
                <li>
                    <a>
                        <span>Disabled</span>
                    </a>
                </li>
            </ul>
        </div>
        <div class="panel">
            <div class="table-responsive">
                <table class="table is-fullwidth table is-striped">
                    <thead>
                        <tr>
                            <th>
                                <div class="custom-control custom-checkbox">
                                    <input type="checkbox" class="custom-control-input" id="checkAll">
                                    <label class="custom-control-label" for="checkAll"></label>
                                </div>
                            </th>
                            <th>Product Name</th>
                            <th>SKU</th>
                            <th>Category</th>
                            <th>Price</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="product in product" :key="product.id">
                            <td>
                                <div class="custom-control custom-checkbox">
                                    <input type="checkbox" class="custom-control-input" id="checkAll" name="product">
                                    <label class="custom-control-label" for="check"></label>
                                </div>
                            </td>
                            <td>
                                {{product.productName}}
                            </td>
                            <td>
                                {{product.sku}}
                            </td>
                            <td>
                                {{product.category.categoryname}}
                            </td>

                            <td>
                                {{product.price}}
                            </td>

                            <td>
                                <span class="tag is-success">Availabe</span>
                            </td>
                            <td>
                                <div class="dropdown">
                                    <div class="dropdown-trigger">
                                        <a href="" aria-haspopup="true" aria-controls="dropdown-menu3">
                                            <svg width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
                                            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                                                <rect x="0" y="0" width="24" height="24"></rect>
                                                <circle fill="#000000" cx="5" cy="12" r="2"></circle>
                                                <circle fill="#000000" cx="12" cy="12" r="2"></circle>
                                                <circle fill="#000000" cx="19" cy="12" r="2"></circle>
                                            </g>
                                        </svg></a>
                                    </div>
                                    <div class="dropdown-menu" id="dropdown-menu3" role="menu">
                                        <div class="dropdown-content">
                                        <a class="dropdown-item" href="#">Accept Patient</a>
                                        <a class="dropdown-item" href="#">Reject Order</a>
                                        <a class="dropdown-item" href="#">View Details</a>
                                        </div>
                                    </div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: 'ProductList',
        data() {
            return {
                product: []
            }
        },
        mounted() {
            this.getProducts();
        },
        methods: {
            getProducts() {
                axios.get('product/')
                    .then(response => {
                        this.product = response.data;
                    }).catch(error => {
                        console.log(error);
                    });
            }
        }

    }
</script>