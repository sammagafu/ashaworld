<template>

  <div class="basis-full py-3 mx-3">
    <div class="flex items-center justify-between">
      <div class="basis-3/4">
        <h2 class="title text-2xl font-semibold">Products</h2>
      </div>
      <div class="basis-1/2">
        <div class="inline-flex rounded-lg">
          <!-- focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded -->
          <button
            @click="exportAllProducts"
            id="dropdownDefault" data-dropdown-toggle="dropdown"
            class="text-white bg-indigo-700 hover:bg-indigo-600 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800"
            type="button">
            <span class="mr-2"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg></span>
            Export
            <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg></button>
          <!-- Dropdown menu -->
          <div id="dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded shadow w-44 dark:bg-gray-700"
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
                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Sign
                  out</a>
              </li>
            </ul>
          </div>

          <button @click="openModal"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm mx-4 px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
              stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
            </svg>
          </button>
        </div>

      </div>
    </div>
  </div>

  <div class="sm:px-6 w-full">
    <div class="flex flex-col">
      <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
          <div class="inline-flex rounded-md shadow-sm" role="group">
            <button type="button"
              @click="filterProductsByStatus('nothing')"
              class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-l-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
              All Products
            </button>
            <button type="button"
              @click="filterProductsByStatus('nothing')"
              class="py-2 px-4 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
              available
            </button>
            <button type="button"
              @click="filterProductsByStatus('available')"
              class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-r-md border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
              Unavailable
            </button>

          </div>
          <div class="overflow-hidden">
            <table class="min-w-full">
              <thead class="bg-white border-b">
                <tr>
                  <th 
                    @click="sortProducts('id')"
                    scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    ID
                  </th>
                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    image
                  </th>
                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    Product Name
                  </th>
                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    SKU
                  </th>
                  <th 
                    @click="sortProducts('price')"
                    scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    Price
                  </th>
                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    Category
                  </th>
                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    Status
                  </th>

                  <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                    Action
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr class="bg-gray-100 border-b" v-for="prod in product" :key="prod.id">
                  <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    {{prod.id}}
                  </td>
                  <td class="px-6 py-4 whitespace-nowraw">
                    <img :src="prod.get_coverImage" alt="img">
                  </td>
                  <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    <span 
                      class=" font-medium">
                      {{prod.productName}}
                    </span>
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
                    <span
                      class="bg-green-100 text-green-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-green-200 dark:text-green-900">Available</span>
                  </td>
                  <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                    <div class="flex justify-between">
                      <button 
                        @click="openModal"
                        type="button"
                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-1.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor" stroke-width="2">
                          <path stroke-linecap="round" stroke-linejoin="round"
                            d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg>
                        Edit
                      </button>
                      <button 
                      @click="deleteProduct(prod.id)"
                      type="button"
                        class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-1.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
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
        </div>
      </div>
    </div>
  </div>
  

  <div class="overflow-y-auto overflow-x-hidden fixed z-50 w-full md:inset-0 h-modal md:h-full"
    :class="{hidden : isOpen}">
    <div class="relative p-4 w-full max-w-4xl h-full md:h-auto mx-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <button type="button"
        @click="closeModal"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
          data-modal-toggle="authentication-modal">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clip-rule="evenodd"></path>
          </svg>
        </button>
        <div class="py-6 px-6 lg:px-8">
          <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add Product</h3>

          <div class="mb-4 border-b border-gray-200 dark:border-gray-700">
            <ul class="flex flex-wrap -mb-px text-sm font-medium text-center" id="myTab"
              data-tabs-toggle="#myTabContent" role="tablist">
              <li class="mr-2" role="presentation" @click="isActive = 'information'">
                <button
                  class="inline-block p-4 rounded-t-lg border-b-2 text-blue-600 hover:text-blue-600 dark:text-blue-500 dark:hover:text-blue-500 border-blue-600 dark:border-blue-500"
                  id="information-tab" data-tabs-target="#information" type="button" role="tab" aria-controls="profile"
                  aria-selected="true">Information</button>
              </li>
              <li class="mr-2" role="presentation" @click="isActive = 'images'">
                <button
                  class="inline-block p-4 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 dark:border-transparent text-gray-500 dark:text-gray-400 border-gray-100 dark:border-gray-700"
                  id="images-tab" data-tabs-target="#images" type="button" role="tab" aria-controls="dashboard"
                  aria-selected="false">Images</button>
              </li>
              <li class="mr-2" role="presentation" @click="isActive = 'pricing'">
                <button
                  class="inline-block p-4 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 dark:border-transparent text-gray-500 dark:text-gray-400 border-gray-100 dark:border-gray-700"
                  id="pricing-tab" data-tabs-target="#pricing" type="button" role="tab" aria-controls="settings"
                  aria-selected="false">Pricing</button>
              </li>
              <li role="presentation" @click="isActive = 'invetory' ">
                <button
                  class="inline-block p-4 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 dark:border-transparent text-gray-500 dark:text-gray-400 border-gray-100 dark:border-gray-700"
                  id="inventory-tab" data-tabs-target="#inventory" type="button" role="tab" aria-controls="contacts"
                  aria-selected="false">Invetory</button>
              </li>
            </ul>
          </div>
          <form class="space-y-6" action="#">
            <div id="myTabContent">
              <div class="p-4" id="information" role="tabpanel" aria-labelledby="information-tab" :class="{ 'hidden': isActive != 'information' }">
                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Product
                    name</label>
                  <input type="text" name="product" id="product"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Product name" required>
                </div>
                
                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Product
                    Description</label>
                  <textarea name=""
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"></textarea>
                </div>
              </div>

              <div
              :class="{ 'hidden': isActive != 'images' }"
               class="p-4 bg-gray-50 rounded-lg dark:bg-gray-800" id="images" role="tabpanel"
                aria-labelledby="images-tab">
              <input type="file" name="image" id="">
              </div>
              <div 
              :class="{ 'hidden': isActive != 'pricing' }"
              class="p-4 bg-gray-50 rounded-lg dark:bg-gray-800" id="pricing" role="tabpanel"
                aria-labelledby="pricing-tab">
                                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Normal
                    Price</label>
                  <input type="text" name="price" id="price"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Product price" required>
                </div>
                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Wholesale
                    Price</label>
                  <input type="text" name="wholesaleprice" id="price"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Wholesale price" required>
                </div>
              </div>
              <div 
              :class="{ 'hidden': isActive != 'invetory' }"
              class="p-4 bg-gray-50 rounded-lg dark:bg-gray-800" id="inventory" role="tabpanel"
                aria-labelledby="inventory-tab">
                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Stock
                    Keeping
                    Unit</label>
                  <input type="text" name="sku" id="price"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="Stock Keeping Unit" required>
                </div>
                <div class="mb-6">
                  <label for="product" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Stock
                    Quantity</label>
                  <input type="text" name="quantity" id="price"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    placeholder="quanity" required>
                </div>
              </div>
            </div>
            <button type="submit"
              class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create
              Product</button>
          </form>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
  import axios from 'axios';
  export default {

    name: "Products",
    data() {
      return {
        openTab: 1,
        product: [],
        isOpen: true,
        isActive : "information"
        
      }
    },
    methods: {
      openModal(){
        this.isOpen = !this.isOpen
      },
      closeModal(){
        this.isOpen = !this.isOpen
      },
      toggleTabs: function (tabNumber) {
        this.openTab = tabNumber
      },
      getProducts() {
        axios.get('product/')
          .then(response => {
            this.product = response.data;
            console.log('response.data :>> ', response.data);
          }).catch(error => {
            console.log(error);
          });
      },
      deleteProduct(id){
        axios.delete(`product/${id}`)
            .then(response => {
                this.product = this.product.filter(x=>{
                if(x.id!=id) return x
            });
            }).catch(error => {
                console.log(error);
            });
      },
      exportAllProducts(){
          axios.get(`product/export_product_list`)
              .then(response => {
                  const fileURL = window.URL.createObjectURL(new Blob([response.data]));
                  const fileLink = document.createElement('a');
                  fileLink.href = fileURL;
                  fileLink.setAttribute('download', 'all-products.csv');
                  document.body.appendChild(fileLink);
                  fileLink.click();
              }).catch(error => {
                  console.log(error);
              });
      },
      sortProducts(by){
          const sortFn = (a,b)=>{
              if(a[by]<b[by]){
                  return -1
              }
              if(a[by]>b[by]){
                  return 1
              }
              return 0
              }
          this.product.sort(sortFn)
      },
      filterProductsByStatus(status){
        if(status!='nothing'){
        this.product = this.product.filter(x=>x.status==status)
        }else{
          this.getProducts()
        }
      }
    },
    mounted() {
      this.getProducts();
    },
  }
</script>