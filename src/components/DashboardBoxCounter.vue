<template>
  <div class="bg-light rounded-borders">
    <div class="q-pa-xl row items-center justify-center">
      <q-icon :name="icon" size="xl" class="q-mr-md" :color="color" />
      <div>
        <div class="text-h3 text-weight-bolder">{{ counter }}</div>
        <div class="text-body1 text-weight-bold color-caption">
          {{ name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "DashboardBoxCounter",

  props: {
    name: { type: String, default: "Default" },
    counter: { type: String, default: "0" },
    icon: { type: String, default: "" },
    color: { type: String, default: "" },
  },
});
</script>
