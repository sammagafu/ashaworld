<template>

  <div class="basis-full py-3 mx-3">
    <div class="flex items-center justify-between">
      <div class="basis-3/4">
        <h2 class="title text-2xl font-semibold">Products</h2>
      </div>
      <div class="basis-1/2">
        <div class="inline-flex rounded-lg">
          <!-- focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded -->
          <button id="dropdownDefault" data-dropdown-toggle="dropdown"
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

          <asha-modal v-if="isOpen" title="Add Product" @close="openModal"></asha-modal>
        </div>

      </div>
    </div>
  </div>



</template>

<script>
  import axios from 'axios';
  import AshaModal from '@/components/AshaModal.vue';


  export default {
    name: "PosProducts",
    data() {
      return {
        openTab: 1,
        product: [],
        isOpen: false,
        isActive: "information"
      };
    },
    methods: {
      openModal() {
        this.isOpen = !this.isOpen;
      },
      closeModal() {
        this.isOpen = !this.isOpen;
      },
      toggleTabs: function (tabNumber) {
        this.openTab = tabNumber;
      },
      getProducts() {
        axios.get("pos/product/")
          .then(response => {
            this.product = response.data;
            // console.log('response.data :>> ', response.data);
          }).catch(error => {
            console.log(error);
          });
      },
    },
    mounted() {
      this.getProducts();
    },
    components: {
      AshaModal
    }
  }
</script>