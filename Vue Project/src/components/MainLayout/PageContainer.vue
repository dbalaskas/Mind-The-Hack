<template>
  <q-page-container>
    <q-page>
      <div class="q-pa-lg bg-secondary">
        <!-- <div class="text-body1 q-pa-md row justify-between items-center">
          <span>
            <q-icon name="calendar_month"/>
            <span class="q-pl-sm">Καταχωρήσεις</span>
          </span>
        </div>
        <q-separator/> -->
        <router-view />
      </div>
    </q-page>
  </q-page-container>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageContainer",
});
</script>
