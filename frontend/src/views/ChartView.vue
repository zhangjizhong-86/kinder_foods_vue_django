<template>
    <div>
        <b-jumbotron lead="还有..." class="bg-white">
            <flip-countdown deadline="2021-07-01 00:00:00"></flip-countdown>
        </b-jumbotron>
    </div>
</template>

<script>
import FlipCountdown from 'vue2-flip-countdown'
export default {
    components: {
        FlipCountdown
    }
  }

// export default {
//     created: function() {
//         console.log("ChartView created.");
//     },
//     mounted: function() {
//         console.log("ChartView mounted.");
//     },
//     destoryed: function() {
//         console.log("ChartView destroyed.");
//     }
// }


</script>

<style>

</style>
