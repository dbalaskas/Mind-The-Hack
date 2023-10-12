<template>
  <div class="text-center">
    <div class="text-h4 text-weight-bolder">{{ counter }}</div>
    <div class="text-body1 text-weight-bold color-caption">{{ name }}</div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "DashboardSingleCounter",

  props: {
    name: { type: String, default: "Default" },
    counter: { type: String, default: "0" },
  },
});
</script>
