<template>
    <ul class="megamenu">
        <li>
            <h4 class="menu-title"> {{ name }} </h4>
            <hr class="divider">
            <ul>
                <li v-for="(subcategory, index) in subcategories" :key="index">
                    <a>{{ subcategory.subcategoryname }}</a>
                </li>
            </ul>
        </li>
    </ul>
</template>

<script>
    export default {
        name: "SubCategoryTopNav",

        props: ["subcategories", "name"]
    }
</script>