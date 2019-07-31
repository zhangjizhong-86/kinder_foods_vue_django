<template>
  <!-- <div v-for="(value, name, index) in object">
    {{ index }}. {{ name }}: {{ value }}
  </div> -->
  <div class="table-responsive">
    <!-- <p> {{ week }} </p><br />
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
    <b-table responsive bordered :items="daily_menu">
      <template slot="日期" slot-scope="data">
        {{ data.value.date }}<br/>{{ data.value.weekday }}
      </template>
      <span slot="早点" slot-scope="data" v-html="data.value"></span>
      <span slot="午餐" slot-scope="data" v-html="data.value"></span>
      <span slot="午点" slot-scope="data" v-html="data.value"></span>
      <span slot="体弱儿营养菜" slot-scope="data" v-html="data.value"></span>
    </b-table>

    <!-- <b-table :items="items">
      <span slot="html" slot-scope="data" v-html="data.value"></span>
    </b-table> -->
  </div>
</template>

<script>
  export default {
    // name:"myTable",
    props: ['menu', 'query_date'],
    data() {
      return {
        fields: [
          {
            key: '日期'
          }
        ],
      }
    },
    computed: {
      week: function () {
        for (let week in this.menu) {
          return week;
        }
      },
      daily_menu: function () {
        // console.log(this.items[0].日期);
        for (let week in this.menu) {
          return this.menu[week];
        }
      }
    },
    methods: {
      updateData: function(dt) {
        this.week_menu = dt
      }
    },
    created: function() {
      console.log("MenuTable created.");
      this.$root.$on("data-ready", function(dt) {
        console.log(dt);
        return dt;
        // for (let week in dt) {
        //   for (let day in dt[week]) {
        //     console.log(dt[week][day]['早点']);
        //   }
        // }
      });
      console.log(this.week_menu);
    },
    mounted: function() {
      console.log("MenuTable mounted.");
      // console.log(this.week_menu);
      // this.$root.$on("isReady", function(d) {
      //   console.log(d);
      // })
      // this.items.push({ 日期: '2019-7-3<br>星期三', 早点: '粥<br/>牛奶', 午餐: '饭<br/>汤', 午点: '饼干<br/>果汁', 体弱儿营养菜: '...' })
    }
  }
</script>

<style>

</style>
