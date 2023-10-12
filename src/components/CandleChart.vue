<template>
  <div id="candleChart">
    <apex-charts type="candlestick" :options="options" :series="series" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import ApexCharts from "vue3-apexcharts";

export default defineComponent({
  name: "CandleChart",
  components: {
    ApexCharts,
  },

  props: {
    series: { type: Array, default: new Array() },
  },

  setup() {
    return {
      options: {
        candlestick: {
          wick: {
            useFillColor: true,
          },
        },
      }
    };
  },
});
</script>
