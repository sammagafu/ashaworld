<template>
  <div class="columns">
     <aside class="column is-2 aside hero is-fullheight is-hidden-mobile">
      <SideBarNavigation />
     </aside>
    
    <div class="column is-10 admin-panel mx-3">
      <nav class="navbar is-transparent is-hidden-tablet" id="top">
        <div class="navbar-brand">
          <a class="navbar-item" href="https://bulma.io">
            <img src="../assets/asha-logo-dark.svg" alt="Bulma: a modern CSS framework based on Flexbox"
              width="112" height="28">
          </a>
          <div class="navbar-burger" data-target="navbarExampleTransparentExample">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
        <div class="container">
          <div class="nav-right nav-menu">
            <a href="#" class="nav-item is-active">
              Dashboard
            </a>
            <a href="#" class="nav-item">
              Activity
            </a>
            <a href="#" class="nav-item">
              Timeline
            </a>
            <a href="#" class="nav-item">
              Folders
            </a>
          </div>
        </div>
      </nav>
      <section>
        <router-view>
       </router-view>
      </section>
    </div>
  </div>
  <FooterNavigation />
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
  import {
    defineComponent,
    ref
  } from 'vue';
  import SideBarNavigation from '@/components/SideBarNavigation.vue';
  import TopBarNavigation from '@/components/TopBarNavigation.vue';
import FooterNavigation from '@/components/FooterNavigation.vue';
  export default defineComponent({
    name: 'BaseAppView',
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
      ShopOutlined,
      SideBarNavigation,
      TopBarNavigation,
        FooterNavigation
    },

  });
</script>
<style>
aside{ 
  padding: 30px 30px;  
  background-color: #141414;
  width: 250px !important;
}
</style>