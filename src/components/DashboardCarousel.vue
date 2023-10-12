<template>
  <q-carousel
    v-model="slide"
    swipeable
    animated
    :autoplay="autoplay"
    infinite
    :arrows="true"
    :navigation="true"
    navigation-position="top"
    :padding="true"
    height="300px"
    control-color="primary"
    transition-prev="slide-right"
    transition-next="slide-left"
    @mouseenter="autoplay = false"
    @mouseleave="autoplay = true"
  >
    <template v-for="(item, index) in items" :key="index">
      <q-carousel-slide :name="index" class="column no-wrap flex-center">
        <img :src="item.img" alt="User Profile" class="q-mb-sm" />
        <div class="text-h5 text-weight-bolder">{{ item.name }}</div>
        <div class="text-body1 text-weight-bold color-caption">
          {{ item.caption }}
        </div>
      </q-carousel-slide>
    </template>
  </q-carousel>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "DashboardCarousel",

  props: {
    items: { type: Array, default: new Array() },
  },

  setup() {
    const slide = ref(0);
    const autoplay = ref(true);

    return {
      slide,
      autoplay,
      lorem: "Lorem Ipsum test code is here",
    };
  },
});
</script>
