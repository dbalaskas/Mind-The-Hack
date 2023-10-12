<template>
  <div class="bg-light rounded-borders q-pa-lg q-mb-lg">
    <div class="text-h5 text-weight-bolder q-mb-sm">{{ title }}</div>
    <q-separator class="q-mb-md" />
    <slot name="body" />
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "DashboardSection",
  props: {
    title: { type: String, default: "" },
  },
});
</script>
