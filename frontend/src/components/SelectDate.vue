<template>
  <div>
    <b-container>
      <b-row>
        <b-col md="3"/>
        <b-col md="6">
          <datepicker placeholder="选择日期（默认是今天）" :language="languages[language]" :format="format"  v-on:selected = "sendEvent" wrapper-class="form-group" input-class="form-control"></datepicker>
        </b-col>
        <b-col md="3"/>
      </b-row>
    </b-container>
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
      sendEvent: function(query_date) {
        // console.log("sendEvent");
        this.$emit("selected", query_date);
      }
    },
    created: function() {
      // console.log("SelectDate created.");
    },
    mounted: function() {
      // console.log("SelectDate mounted.");
      
    }
}



</script>

<style>

</style>
