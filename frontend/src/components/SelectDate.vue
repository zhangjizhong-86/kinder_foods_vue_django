<template>
  <div>
    <b-container>
      <b-row>
        <b-col md="4"/>
        <b-col md="4">
          <datepicker placeholder="选择日期" :language="languages[language]" :format="format"  v-on:selected = "sendEvent" wrapper-class="form-group" input-class="form-control"></datepicker>
        </b-col>
        <b-col md="4"/>
      </b-row>
    </b-container>
    <!-- <button v-on:click = "sendEvent">产生事件</button> -->
  </div>
</template>

<script>

import Datepicker from 'vuejs-datepicker';
import * as lang from "vuejs-datepicker/src/locale";

export default {
    // name:"SelectDate",
    components: {
        Datepicker
    },
    data() {
        return {
            format: "yyyy年MM月dd日",
            language: "zh",
            languages: lang,
        }
    },
    methods: {
      do_ajax: function() {
        // 发生日期改变则发起数据请求
      },
      today: function() {
        // 生成今日日期字符串
        let d = new Date();
        let year = d.getFullYear();
        let month = d.getMonth() + 1;
        let day = d.getDate();
        return year + '-' + month + '-' + day
      },
      sendEvent: function(query_date) {
        console.log("sendEvent");
        this.$emit("selected", query_date);
      }
    },
    created: function() {
      console.log("SelectDate created.");
      // this.count = 0
    },
    mounted: function() {
      // 组件加载后根据今日日期向后台请求菜单
      // 并触发isReady事件，将结果传递给APP
      console.log("SelectDate mounted.");
      
      // let o = this
      // setInterval(function () {
      //   o.count++;
      //   o.$root.$emit("isReady", o.count);
      // }, 2000);

      // this.$http.post('http://localhost:8888/ajax/',
      //                 {query_date:'2018-10-22'}, 
      //                 {emulateJSON: true}) // 使用form-data才可以，否则querydict空
      // .then(function(response){
      //   // console.log(response.data);
      //   this.$root.$emit("data-ready", response.data);
      // })
    }
}



</script>

<style>

</style>
