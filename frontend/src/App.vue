<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="success">
      <b-navbar-nav>
        <b-nav-item><router-link to="/" class="text-white">幼儿园菜单</router-link></b-nav-item> 
        <b-nav-item><router-link to="/chart" class="text-white">敬请期待</router-link></b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <keep-alive>
      <router-view/>
    </keep-alive>
    <b-container fluid class="copyright my-3 bg-dark" />
    <b-container v-bind:style="{ fontSize: fontSize }">
      <p class="mb-0" > oh-mykids.com v1.1 © 2018-20xx All rights reserved. </p>
      <a href = "mailto: zhangjizhong@outlook.com">Contact Me</a> | 
      <a href = "https://github.com/zhangjizhong-86">My Github</a>
    </b-container>
  </div>
</template>

<script>
import MenuView from '@/views/MenuView.vue'; 
import ChartView from '@/views/ChartView.vue';
export default {
  data() {
    return {
      mail: 'zhangjizhong@outlook.com',
      fontSize: '12px'
    }
  },
  components: {
    MenuView, // local registration
    ChartView
  },
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.navbar {
  padding: 30px;
  /* background-color: success; */
}

nav a.router-link-exact-active {
  font-weight: bold;
}

.copyright {
  height: 1px;
}

p {
  font-size: '6px';
}
</style>


