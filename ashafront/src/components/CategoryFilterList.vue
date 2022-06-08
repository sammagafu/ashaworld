<template>
    <ul v-if="categoryList" class="widget-body filter-items search-ul">
        <li v-for="(cat,index) in categoryList" :key="index"><a href="#">{{ cat.categoryname}}</a></li>
    </ul>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "CategoryFilterList",
        data() {
            return {
                categoryList: []
            }
        },
        mounted() {
            this.getCategoryList()
        },
        methods: {
            getCategoryList() {
                axios.get("category/")
                    .then(response => {
                        this.categoryList = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }

    }
</script>