<template>
    <div class="basis-full py-3 mx-6">
        <div class="flex justify-between">
            <div class="basis-3/4">
                <h2 class="title text-2xl font-semibold">Point of Sale</h2>
            </div>
            <div class="basis-1/2">
                <div class="inline-flex rounded-lg">
                    <!-- focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded -->
                    <button id="dropdownDefault" data-dropdown-toggle="dropdown"
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
                    <!-- Dropdown menu -->
                    <div id="dropdown"
                        class="z-10 hidden bg-white divide-y divide-gray-100 rounded shadow w-44 dark:bg-gray-700"
                        style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(387.5px, 735.5px, 0px);"
                        data-popper-placement="bottom">
                        <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefault">
                            <li>
                                <a href="#"
                                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Dashboard</a>
                            </li>
                            <li>
                                <a href="#"
                                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Settings</a>
                            </li>
                            <li>
                                <a href="#"
                                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Earnings</a>
                            </li>
                            <li>
                                <a href="#"
                                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Sign
                                    out</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="basis-full py-6 mx-6">
        <div class="grid grid-cols-12">
            <div class="col-span-4 bg-slate-200 py-6 rounded-md px-3 mx-3">
                <h5>Products</h5>
                <div class="flex flex-col pt-3">
                    <div class="w-full px-4">

                        <form class="flex items-center">
                            <div class="flex items-center p-3 bg-gray-800 w-full">
                                <div class="">
                                    <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor"
                                        viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd"
                                            d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                            clip-rule="evenodd"></path>
                                    </svg>
                                </div>
                                <vue3-simple-typeahead
                                    :id="ID"
                                    placeholder="Search by name"
                                    :items="products"
                                    :minInputLength="1"
                                    :defaultItem="products[0]"
                                    :itemProjection="(item)=> item.productName"
                                    @selectItem="selectItemEventHandler"
                                    @focus="blurEventHandler"
                                >
                                </vue3-simple-typeahead>

                            </div>
                        </form>

                    </div>
                </div>
            </div>
            <div class="col-span-8 bg-slate-200 py-6 rounded-md px-3 mx-3">
                <h5>Products</h5>
                <div class="flex flex-col pt-3">
                    <div class="w-full">
                        <div class=""></div>
                        <div class="">
                            <table class="min-w-full">
                                <thead class="bg-white border-b">
                                    <tr>
                                    <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Image
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Product
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Quantity
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Price
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Subtotal
                                        </th>
                                        <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                            Action
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="bg-gray-100 border-b" v-for="prod in selected" :key="prod.id">
                                        <td class="px-6 py-4 whitespace-nowraw">
                                            <img :src="prod.get_coverImage" alt="">
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.productName}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.sku}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.price}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.category.categoryname}}
                                        </td>
                                        <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            {{prod.price}}
                                        </td>
                                        <!-- <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                            available
                                        </td> -->
                                    </tr>

                                </tbody>
                                <!-- <tfoot>
                                    <tr class="bg-gray-100 border-b py-6">
                                        <td>Sum</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                    </tr>
                                    <tr class="bg-gray-100 border-b py-6">
                                        <td>Sum</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                        <td>$180</td>
                                    </tr>
                                </tfoot> -->

                            </table>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    
</template>

<script>
import axios from'axios';
import AddProduct from '@/components/AddProduct.vue';
    export default {
    components: { AddProduct },
    data (){
        return {
            isopen : false,
            ID:"typehead-id", //id name for type-ahead search input
            products:[],
            selected:[],
            selectedItemIds: [],
            selectedItem: null
        }
    },
     methods: {
      getPosProducts() {
        axios.get('product/')
          .then(response => {
            this.products = response.data;
            console.log('response.data :>> ', response.data);
          }).catch(error => {
            console.log(error);
          });
      },
      selectItemEventHandler(value){
          this.selected.push(value);
      },

      blurEventHandler(e){
          console.log("value: ",e.target.value)
          e.target.value=''
      }
    },
    mounted() {
      this.getPosProducts();
    },
    computed : {
        printworking(){
            console.log('this.isopen :>> ', this.isopen);
        }
    }
}
</script>

<style>
#typehead-id{
    background: transparent !important;
    padding-left: .5rem;
    color:white;
    width:inherit;
}   
</style>