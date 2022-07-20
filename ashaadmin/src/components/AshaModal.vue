<template>
  <div>
    <div class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
      <div class="relative w-auto my-6 mx-auto max-w-6xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
            <h3 class="text-3xl font-semibold">
              {{title || "title goes here"}}
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-red-600  float-right text-3xl leading-none font-normal" v-on:click="$emit('close')">
              <span class=" text-red-600 block focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative p-6 flex-auto">
            <slot>
            <p class="my-4 text-slate-500 text-lg leading-relaxed">
              I always felt like I could do anything. That’s the main
              thing people are controlled by! Thoughts- their perception
              of themselves! They're slowed down by their perception of
              themselves. If you're taught you can’t do anything, you
              won’t do anything. I was taught I could do everything.
            </p>
            </slot>
          </div>
          <!--footer-->
          <div v-if="showFooter" class="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
            <button
            @click="$emit('close')" 
            class="text-red-500 bg-transparent border border-solid border-red-500 hover:bg-red-500 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AshaModal",
  props:{
    title:String,
    showFooter:{
      type:Boolean,
      default:false,
    }
  },
  emits:["close"],
  data:()=>{
    return{
      footer:true,
    }
  }
}
</script>