<template>
    <div class="basis-full py-3 mx-3">
        <div class="flex items-center justify-between">
            <div class="basis-3/4">
                <h2 class="title text-2xl font-semibold">Orders</h2>
            </div>
            <div class="basis-1/2">
                <div class="inline-flex rounded-lg">
                    <!-- focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded -->
                    <button 
                    @click="exportAllPosOrders"
                    id="dropdownDefault" data-dropdown-toggle="dropdown"
                        class="text-white bg-indigo-700 hover:bg-indigo-600 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800"
                        type="button">
                        <span class="mr-2"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                            </svg></span>
                        Export
                        <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7">
                            </path>
                        </svg></button>
                </div>

            </div>
        </div>
    </div>


    <div class="sm:px-6 w-full">
        <div class="inline-flex rounded-md shadow-sm" role="group">
            <button type="button"
                class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-l-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                Pending
            </button>
            <button type="button"
                class="py-2 px-4 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                Paid
            </button>
            <button type="button"
                class="py-2 px-4 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                Cancelled
            </button>
            <button type="button"
                class="py-2 px-4 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                Refunded
            </button>
            <button type="button"
                class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-r-md border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                Shipped
            </button>
            
        </div>

        <div class="flex flex-col">
            <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
                <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
                    <div class="overflow-hidden">
                        <table class="min-w-full">
                            <thead class="bg-gray-100 border-b">
                                <tr>
                                    <th scope="col" class="py-3 px-6">
                                        <div class="flex items-center">
                                            ID
                                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="ml-1 w-3 h-3"
                                                    aria-hidden="true" fill="currentColor" viewBox="0 0 320 512">
                                                    <path
                                                        d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z" />
                                                </svg></a>
                                        </div>
                                    </th>
                                    <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                        customer
                                    </th>
                                    <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                        Total Price
                                    </th>
                                    <th scope="col" class="py-3 px-6">
                                        <div class="flex items-center">
                                            Status
                                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="ml-1 w-3 h-3"
                                                    aria-hidden="true" fill="currentColor" viewBox="0 0 320 512">
                                                    <path
                                                        d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z" />
                                                </svg></a>
                                        </div>
                                    </th>
                                    <th scope="col" class="py-3 px-6">
                                        <div class="flex items-center">
                                            Ordering Date
                                            <a href="#"><svg xmlns="http://www.w3.org/2000/svg" class="ml-1 w-3 h-3"
                                                    aria-hidden="true" fill="currentColor" viewBox="0 0 320 512">
                                                    <path
                                                        d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z" />
                                                </svg></a>
                                        </div>
                                    </th>
                                    <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                        Action
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="bg-gray-100 border-b" v-for="orderItem in order" :key="orderItem.id">
                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                        {{orderItem.id}}
                                    </td>

                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                        <span 
                                            class="cursor-pointer text-green-600 font-medium"
                                            @click="openOrderDetails(orderItem)"
                                            >{{ orderItem.owner.email }}</span>
                                    </td>

                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                        {{ orderItem.totalprice}}
                                    </td>

                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap lowercase">
                                        {{orderItem.orderstatus}}
                                    </td>
                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                        {{orderItem.created_at}}
                                    </td>
                                    <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                        <div
                                         @click="openContext(orderItem.id)"
                                         class="relative inline-block text-left">
                                            <!-- dropdown menu -->
                                            <div 
                                            :id="orderItem.id"
                                            class="origin-top-right hidden absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100 z-10 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
                                                <div class="py-1" role="none">
                                                <!-- <a class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="+1" id="menu-item-0">Edit</a> -->
                                                <a 
                                                @click="deleteOrder(orderItem.id)"
                                                class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="+1" id="menu-item-1">Delete</a>
                                                </div>
                                            </div>
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                                viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                    d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                                            </svg>
                                    </div>
                                    </td>
                                </tr>

                            </tbody>
                        </table>
                        
                    </div>
                    <ashaModal
                        @close="toggleModal"
                        title="Order Details"
                        v-if="detailsModal"
                        >
                            <div class="table-wrapper">
                                <div class="header flex justify-between">
                                    <p class="font-semibold">Products</p>
                                    <button 
                                    @click="exportOrder"
                                    id="dropdownDefault" data-dropdown-toggle="dropdown"
                                        class="text-white bg-indigo-700 hover:bg-indigo-600 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-1.5 text-center inline-flex items-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800"
                                        type="button">
                                        <span class="mr-2"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
                                                viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                            </svg></span>
                                        Export
                                        <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7">
                                            </path>
                                        </svg>
                                    </button>
                                </div>
                                <table class="min-w-full">
                                    <thead class="bg-white border-b">
                                        <tr>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Id
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Product Name
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Price
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Quantity
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Action
                                        </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="prod, i in currentOrder" :key="prod.id" class="bg-gray-100 border-b">
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.id}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.productName}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.price}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.order_quantity}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            <div class="flex justify-between">
                                            <button type="button"
                                                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-1.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                                stroke="currentColor" stroke-width="2">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                                                </svg>
                                                Edit
                                            </button>
                                            <button type="button"
                                                class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-1.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                                stroke="currentColor" stroke-width="2">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                                </svg>
                                                Delete
                                            </button>
                                            </div>
                                        </td>
                                        </tr>

                                    </tbody>
                                    </table>
                            </div>
                    </ashaModal>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import AshaModal from "@/components/AshaModal.vue";

    export default {
        name: 'Orders',
        components:{AshaModal},
        data() {
            return {
                order: [],
                detailsModal:false,
                currentOrder:{},
                currentOrderId:null,
                currentContext:[]
            }
        },
        mounted() {
            this.getOrders();
        },
        methods: {
            getOrders() {
                axios.get('/order')
                    .then(response => {
                        this.order = response.data;
                    }).catch(error => {
                        console.log(error);
                    });
            },
            deleteOrder(id){
                axios.delete(`pos/order/${id}`)
                    .then(response => {
                        this.order = this.order.filter(x=>{
                        if(x.id!=id) return x
                    });
                    }).catch(error => {
                        console.log(error);
                    });
            },
            exportOrder(){
                axios.get(`pos/order/${this.currentOrderId}/export_order/?id=${this.currentOrderId}`)
                    .then(response => {
                        const fileURL = window.URL.createObjectURL(new Blob([response.data]));
                        const fileLink = document.createElement('a');
                        fileLink.href = fileURL;
                        fileLink.setAttribute('download', 'order.csv');
                        document.body.appendChild(fileLink);
                        fileLink.click();
                    }).catch(error => {
                        console.log(error);
                    });
            },
            exportAllPosOrders(){
                axios.get(`pos/order/export_order_list/?id=${localStorage.getItem('userid')}`)
                    .then(response => {
                        const fileURL = window.URL.createObjectURL(new Blob([response.data]));
                        const fileLink = document.createElement('a');
                        fileLink.href = fileURL;
                        fileLink.setAttribute('download', 'all_orders.csv');
                        document.body.appendChild(fileLink);
                        fileLink.click();
                    }).catch(error => {
                        console.log(error);
                    });
            },
            getTotalPrice(str){//takes a stringified array of products
                //parse array
                let prods = JSON.parse(str)
                //aggregate prices for each products in order
                let price=0
                prods.forEach(x=>{
                    price = price +  (x.price * x.order_quantity)
                })
                return price
            },
            openOrderDetails(item){
                this.detailsModal = true;
                const items = item.orderproducts
                console.log(items)
                this.currentOrder  = items
                this.currentOrderId  = item.id
            },
            toggleModal(){
                this.detailsModal = !this.detailsModal;
            },
            openContext(id){
                const el = document.getElementById(id)
                el.classList.toggle('hidden')
                if(this.currentContext.length>0){
                    this.currentContext[0].classList.toggle('hidden');
                    this.currentContext[0] = el;
                }
            }
        }


    }
</script>

<style>

</style>