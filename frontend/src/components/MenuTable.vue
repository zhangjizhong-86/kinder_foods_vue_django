<template>
    <!-- <p> {{ week }} </p> -->
    <!-- the bootstrap way
    <div class="table-responsive">
      <table class="table table-bordered">  
        <tr><th>日期</th><th>早点</th><th>午餐</th><th>午点</th><th>体弱儿营养菜</th></tr>
        <tr v-for = "(row, date) in daily_menu" v-bind:key = "date" v-bind:class = "{'table-active' : date == query_date}">
          <td>{{ date }}</td>
          <td><span v-for = "(dish, id) in row.早点" v-bind:key = "id">{{ dish }}<br/></span></td>
          <td><span v-for = "(dish, id) in row.午餐" v-bind:key = "id">{{ dish }}<br/></span></td>
          <td><span v-for = "(dish, id) in row.午点" v-bind:key = "id">{{ dish }}<br/></span></td>
          <td><span v-for = "(dish, id) in row.体弱儿营养菜" v-bind:key = "id">{{ dish }}<br/></span></td>
        </tr>
      </table> -->
    <!-- </div> -->
      <b-table responsive="md" bordered :items="daily_menu">
        <template slot="日期" slot-scope="data">
          <strong>{{ data.value.date }}<br/>{{ data.value.weekday }}</strong>
        </template>
        <span slot="早点" slot-scope="data" v-html="data.value"></span>
        <span slot="午餐" slot-scope="data" v-html="data.value"></span>
        <span slot="午点" slot-scope="data" v-html="data.value"></span>
        <span slot="体弱儿营养菜" slot-scope="data" v-html="data.value"></span>
      </b-table>
</template>

<script>
  export default {
    // name:"myTable",
    props: ['menu'], 
    data() {
      return {
        // fields: [
        //   {
        //     key: '日期'
        //   }
        // ],
      }
    },
    computed: {
      week: function () {
        for (let week in this.menu) {
          return week;
        }
        return '';
      },
      daily_menu: function () {
        // console.log(this.items[0].日期);
        for (let week in this.menu) {
          return this.menu[week];
        }
        return ''; // only to deal with error: Expected to return a value in "week" computed property, no actual impact.
      }
    },
    methods: {
      // updateData: function(dt) {
      //   this.week_menu = dt
      // }
    },
    created: function() {
      // console.log("MenuTable created.");
    },
    mounted: function() {
      // console.log("MenuTable mounted.");
    }
  }
</script>

<style scoped>
/* deep selector for v-html created content */
div >>> td { 
  vertical-align: middle;
}

div >>> table {
  min-width: 600px;
}

div {
  font-size: 14px;
}
</style>

