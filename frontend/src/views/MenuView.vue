<template>
  <div>
    <b-container fluid class="my-3">
      <SelectDate v-on:selected = "get_menu"/>
    </b-container>
    <b-alert v-model="failure" variant="danger" dismissible>
      没有{{query_date}}的数据哦!
    </b-alert>
    <!-- <p v-if = "failure">没有{{query_date}}的数据哦</p> -->
    <MenuTable v-bind:menu = "menu"/>
  </div>
</template>

<script>
// local import
import MenuTable from '@/components/MenuTable.vue'; 
import SelectDate from '@/components/SelectDate.vue';

export default {
  // name: "APP",
  data() {
    return {
      menu: '',
      query_date: '',
      failure: false // 控制错误信息
    }
  },
  // data: {
    
  // },
  components: {
    MenuTable, // local registration
    SelectDate,
  },
  methods: {
    get_menu: function(query_date) {
      // console.log("get_menu");
      let year = query_date.getFullYear();
			let month = query_date.getMonth() + 1;
      let day = query_date.getDate();
      this.query_date = year + '年' + month + '月' + day + '日';
      query_date = year + '-' + month + '-' + day;
      // console.log(query_date);
      this.$http.post('/ajax/',
                      {query_date: query_date}, 
                      {emulateJSON: true}) // 使用form-data才可以，否则querydict空
      .catch(function(error) { // 处理未得到数据的异常
        // console.log("in catch")
        this.failure = true;
        return Promise.reject(error);
      }).then(function(response){ // 成功返回数据
        // console.log("in then");
        this.failure = false;
        this.menu = response.data;
      });
    }
  },
created: function() {
    // console.log("MenuView created.");
},
mounted: function() {
    // console.log("MenuView mounted.");
    this.get_menu(new Date());
},
destoryed: function() {
    // console.log("MenuView destroyed.");
}
}


</script>

<style>

</style>
