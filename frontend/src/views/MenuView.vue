<template>
  <div>
    <SelectDate v-on:selected = "get_menu"/> 
    <MenuTable v-bind:menu = "menu" v-bind:query_date = "query_date"/>
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
      query_date: ''
    }
  },
  // data: {
    
  // },
  components: {
    MenuTable, // local registration
    SelectDate,
  },
  methods: {
    today: function() {
      // 生成今日日期字符串，格式：'yyyy-m-d'(eg: '2019-2-21')
			let d = new Date();
			let year = d.getFullYear();
			let month = d.getMonth() + 1;
			let day = d.getDate();
			return year + '-' + month + '-' + day
    },
    getWeek: function() {
      // 返回日期是星期几
    },
    get_menu: function(query_date) {
      console.log("get_menu");
      let year = query_date.getFullYear();
			let month = query_date.getMonth() + 1;
      let day = query_date.getDate();
      query_date = year + '-' + month + '-' + day;
      this.query_date = query_date;
      console.log(query_date);
      this.$http.post('http://localhost:8888/ajax/',
                      {query_date: query_date}, 
                      {emulateJSON: true}) // 使用form-data才可以，否则querydict空
      .then(function(response){
        console.log(response.data);
        this.menu = response.data;
      });
    }
  },
created: function() {
    console.log("MenuView created.");
},
mounted: function() {
    console.log("MenuView mounted.");
    // let today = this.today();
    this.get_menu(new Date(2018,9,22));
},
destoryed: function() {
    console.log("MenuView destroyed.");
}
}


</script>

<style>

</style>
