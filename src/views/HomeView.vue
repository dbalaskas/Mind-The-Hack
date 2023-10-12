<template>
  <div class="row q-col-gutter-lg q-mb-lg">
    <div class="col-sm-6 col-xs-12">
      <dashboard-box-counter
        name="Doctors"
        counter="520"
        icon="person"
        color="light-blue-3"
      />
    </div>
    <div class="col-sm-6 col-xs-12">
      <dashboard-box-counter
        name="Nurses"
        counter="6969"
        icon="vaccines"
        color="deep-orange-6"
      />
    </div>
    <div class="col-sm-6 col-xs-12">
      <dashboard-box-counter
        name="Patients"
        counter="7509"
        icon="medication"
        color="orange-6"
      />
    </div>
    <div class="col-sm-6 col-xs-12">
      <dashboard-box-counter
        name="Pharmacusts"
        counter="2110"
        icon="local_pharmacy"
        color="teal-4"
      />
    </div>
  </div>
  <dashboard-section>
    <template #body>
      <div class="row justify-between q-my-lg">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <dashboard-single-counter name="Doctors" counter="520" />
        </div>
        <div class="col-md-3 col-sm-6 col-xs-12">
          <dashboard-single-counter name="Nurses" counter="6969" />
        </div>
        <div class="col-md-3 col-sm-6 col-xs-12">
          <dashboard-single-counter name="Patients" counter="7509" />
        </div>
        <div class="col-md-3 col-sm-6 col-xs-12">
          <dashboard-single-counter name="Pharmacusts" counter="2110" />
        </div>
      </div>
      <candle-chart :series="candleChartSeries" />
      <div class="bg-light rounded-borders q-pa-lg q-mb-lg">
        <div class="text-h5 text-weight-bolder q-mb-sm">
          Total Recover Report
        </div>
        <q-separator class="q-mb-md" />
        <line-chart :series="lineChartSeries" />
        <div class="row justify-between q-my-lg">
          <div class="col-sm-6 col-xs-12">
            <dashboard-single-counter name="Last Month" counter="358" />
          </div>
          <div class="col-sm-6 col-xs-12">
            <dashboard-single-counter name="Current Month" counter="194" />
          </div>
        </div>
      </div>
    </template>
  </dashboard-section>
  <dashboard-section>
    <template #body>
      <line-chart color="#FC9F5B" :series="lineChartSeries" />
      <div class="row justify-between q-my-lg">
        <div class="col-sm-6 col-xs-12">
          <dashboard-single-counter name="Last Month" counter="358" />
        </div>
        <div class="col-sm-6 col-xs-12">
          <dashboard-single-counter name="Current Month" counter="194" />
        </div>
      </div>
    </template>
  </dashboard-section>
  <dashboard-section>
    <template #body>
      <dashboard-carousel :items="carouselItems" />
    </template>
  </dashboard-section>
  <dashboard-section>
    <template #body>
      <activity-table :activity="activity" />
    </template>
  </dashboard-section>
  <dashboard-section>
    <template #body>
      <div class="text-weight-bold">
        <div class="row justify-between"><span>USA</span><span>95%</span></div>
        <q-linear-progress
          rounded
          size="12px"
          :value="0.95"
          color="light-blue-6 q-mb-lg"
        />
        <div class="row justify-between">
          <span>AFRICA</span><span>75%</span>
        </div>
        <q-linear-progress
          rounded
          size="12px"
          :value="0.75"
          color="green-6 q-mb-lg"
        />
        <div class="row justify-between"><span>UK</span><span>55%</span></div>
        <q-linear-progress
          rounded
          size="12px"
          :value="0.55"
          color="amber-7 q-mb-lg"
        />
        <div class="row justify-between">
          <span>CANADA</span><span>25%</span>
        </div>
        <q-linear-progress
          rounded
          size="12px"
          :value="0.25"
          color="red-6 q-mb-md"
        />
      </div>
    </template>
  </dashboard-section>
  <dashboard-section>
    <template #body>
      <div class="text-center text-body2">
        2023 © MindTheHack - Builtby Dionysis Balaskas
      </div>
    </template>
  </dashboard-section>
</template>

<script>
import { defineComponent, ref } from "vue";
import DashboardSection from "../components/DashboardSection.vue";
import DashboardBoxCounter from "../components/DashboardBoxCounter.vue";
import DashboardSingleCounter from "../components/DashboardSingleCounter.vue";
import DashboardCarousel from "../components/DashboardCarousel.vue";
import CandleChart from "../components/CandleChart.vue";
import LineChart from "../components/LineChart.vue";
import ActivityTable from "src/components/ActivityTable.vue";

const lineChartSeries = [
  {
    name: "series-1",
    data: [30, 40, 45, 50, 49, 60, 70, 91],
  },
];

const candleChartSeries = [
  {
    name: "series-1",
    data: [
      [1538856000000, [6593.34, 6600, 6582.63, 6600]],
      [1538856100000, [6595.16, 6604.76, 6590.73, 6593.86]],
      [1538856200000, [7595.16, 6608.76, 6160.73, 6597.86]],
      [1538856300000, [6295.16, 6124.76, 6590.73, 6598.86]],
      [1538856400000, [6533.16, 6623.76, 6593.73, 6556.86]],
      [1538856500000, [6511.16, 6601.76, 6220.73, 6193.86]],
      [1538856600000, [6516.16, 6732.76, 6230.73, 6714.86]],
      [1538856700000, [6531.16, 6853.76, 6340.73, 6744.86]],
      [1538856800000, [6551.16, 6964.76, 6450.73, 6784.86]],
    ],
  },
];

const carouselItems = [
  { img: "user1.png", name: "Dr Sysla J Smith", caption: "Doctor" },
  { img: "user2.png", name: "Dr Giannis Cruise", caption: "Doctor" },
  { img: "user3.png", name: "Dionysis Clooney", caption: "Driver" },
  { img: "user4.png", name: "Christos J Smith", caption: "Chef" },
];

const activity = [
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
  {
    time: "5 mins ago",
    message:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque",
  },
];

export default defineComponent({
  name: "HomeView",

  components: {
    DashboardSection,
    DashboardBoxCounter,
    DashboardSingleCounter,
    DashboardCarousel,
    CandleChart,
    LineChart,
    ActivityTable,
  },

  setup() {
    return {
      tab: ref("services"),
      lineChartSeries,
      candleChartSeries,
      carouselItems,
      activity,
    };
  },
});
</script>
