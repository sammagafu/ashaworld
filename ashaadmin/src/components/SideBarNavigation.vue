<template>
      <div class="mt-6 mx-4">
        <ul class="menu-list">
        <img src="../assets/asha-logo.svg" alt="" class="pb-6">
        <div class="main">
            <!-- <div class="title">Dashboard</div> -->
            <router-link :to="{name:'home'}" class="item"><span class="icon"><appstore-outlined /></span><span class="name">Dashboard</span></router-link>
            <router-link :to="{name:'productlist'}" class="item"><span class="icon"><shopping-cart-outlined /></span><span class="name">Products</span> </router-link>
            <router-link :to="{name:'orderlist'}" class="item"><span class="icon"><bar-chart-outlined /></span><span class="name">Orders</span> </router-link>
            <router-link :to="{name:'customers'}" class="item"><span class="icon"><user-outlined /></span><span class="name">Customers</span> </router-link>
            <router-link :to="{name:'pos'}" class="item"><span class="icon"><shop-outlined/></span><span class="name">Point Of Sale</span> </router-link>
          
        </div>
          </ul>
      </div>
</template>

<script>
import {
  UserOutlined,
  BarcodeOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  BarChartOutlined,
  CloudOutlined,
  AppstoreOutlined,
  TeamOutlined,
  ShopOutlined,
  ShoppingCartOutlined,
} from '@ant-design/icons-vue';
export default {
    components: {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    BarChartOutlined,
    CloudOutlined,
    AppstoreOutlined,
    TeamOutlined,
    BarcodeOutlined,
    ShoppingCartOutlined,
    // <shopping-cart-outlined />
    ShopOutlined,
},

}
</script>

<style scoped>

.active {
  position: relative;
  color: #141414;
}
li{
    display: inline-block;
}

.active::before {
  content: '';
  position: absolute;
  left: 2px;
  top: 0;
  height: 100%;
  border-left: 4px solid #fff;
  color: #fff;
}
#components-layout-demo-fixed-sider .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}

</style>