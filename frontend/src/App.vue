<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="success">
      <b-navbar-nav>
        <b-row>
          <b-col sm="3" md="2" xl="1">
            <b-nav-item><router-link to="/" class="text-white">菜单</router-link></b-nav-item> 
          </b-col>
          <b-col sm="3" md="2" xl="2">
            <b-nav-item><router-link to="/chart" class="text-white">敬请期待</router-link></b-nav-item>
          </b-col>
        </b-row>
      </b-navbar-nav>
        <!-- <b-row>
          <b-col sm="3" md="2" xl="1">
            <router-link to="/" class="text-white">菜单</router-link>
          </b-col>
          <b-col sm="3" md="2" xl="1">
            <router-link to="/chart" class="text-white">敬请期待</router-link>
          </b-col>
        </b-row> -->
      <!-- </b-navbar-nav> -->
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
export default {
  data() {
    return {
      mail: 'zhangjizhong@outlook.com',
      fontSize: '12px'
    }
  },
  components: {

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

nav a.router-link-exact-active {
  font-weight: bold;
}

.copyright {
  height: 1px;
}

.row, .navbar-nav {
  width: 100%
}

</style>


