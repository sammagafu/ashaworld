<template>
   <div class="">
   <!-- {{ subcategories.length }} -->
         <ul>
        <li class="megamenu" v-for="(subcategory, index) in subcategories" :key="index">
            <!-- <h4 class="menu-title">{{ subcategory }}</h4>
            <hr class="divider"> -->
            <!-- <a :to="{ name:'ProductCategory', parans: { slug: subcategory.slug } }">{{ subcategory.subcategoryname }}</a> -->
            <ul>
                <!-- <li><a :to="{ name:'ProductCategory', parans: { slug: subcategory.slug } }">{{ subcategory.subcategoryname }}</a>
                </li> -->
                <li >
                    <a :to="{ name:'ProductCategory', parans: { slug: subcategory.slug } }">{{ subcategory.subcategoryname }}</a>
                </li>
            </ul>
        </li>
    </ul>
</div>
</template>

<script>

export default {
    name:"SubCategoryTopNav", 

    props:["subcategories"]
}
</script>
