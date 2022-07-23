<template>
    <div class="basis-full py-6 mx-6">
        <div class="flex items-center justify-between">
            <div class="basis-3/4">
                <h2 class="title text-2xl font-semibold">Team</h2>
                <!-- {{company.team}} -->
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

                    <button
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

    <div class="basis-full py-6 mx-6">
        <div class="p-4 max-w-full bg-white rounded-lg border shadow-md sm:p-8 dark:bg-gray-800 mr-4">
            <div class="flex justify-between items-center mb-4">
                <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white">Team Members</h5>
                <form class="flex items-center">
                        <div class="relative max-w-full">
                            <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                                <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor"
                                    viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </div>
                            <input type="text" id="voice-search"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="Search Users, Email" required>
                        </div>
                    </form>
            </div>
            
            <div class="flow-root">
                <ul role="list" class="divide-y divide-gray-400 dark:divide-gray-700">
                    <li class="py-3 sm:py-4" v-for="member in team.teammember" :key="member.id">
                        <div class="flex items-center space-x-4">
                            <div class="flex-1 min-w-0">
                                <p class="text-sm font-medium text-gray-900 truncate dark:text-white">
                                    {{member.member.username}}
                                </p>
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    Admin
                                </p>
                            </div>
                            <div class="flex-1 min-w-0">
                                <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                    {{member.member.email}}
                                </p>
                            </div>
                            
                            <div class="flex-1 min-w-0">
                                <span
                                    class="bg-blue-100 text-blue-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">
                                    Active
                                </span>
                            </div>
                            <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                                </svg>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "TeamDetail",
        data() {
            return {
                team: [],
            }
        },
        methods: {
            getTeam() {
                const compayid = this.$store.state.companyDetails.id
                axios.get(`/company/team/${compayid}`).then(response => {
                    this.team = response.data
                    console.log('this.team :>> ', this.team);
                }).catch(error => {
                    console.log('error :>> ', error);
                })
            }
        },
        mounted() {
            this.getTeam()
        }

    }
</script>

<style>

</style>