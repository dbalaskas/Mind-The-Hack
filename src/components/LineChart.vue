<template>
  <div id="lineChart">
    <apex-charts type="line" :options="options" :series="series" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import ApexCharts from "vue3-apexcharts";

export default defineComponent({
  name: "LineChart",
  components: {
    ApexCharts,
  },

  props: {
    color: { type: String, default: "#089BAB" },
    series: { type: Array, default: new Array() },
  },

  setup(props) {
    return {
      options: {
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
        },
        chart: {
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: false,
          },
          dropShadow: {
            enabled: true,
            top: 10,
            left: 0,
            blur: 20,
            color: props.color,
            opacity: 0.65,
          },
        },
        markers: {
          size: 5,
        },
        grid: {
          show: false,
        },
        colors: [props.color],
      },
    };
  },
});
</script>
