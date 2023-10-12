<template>
  <q-layout view="lHh Lpr lFf">
    <layout-header @toggle-drawer="toggleLeftDrawer" />
    <left-drawer
      :drawer-open="leftDrawerOpen"
      @toggle-drawer="toggleLeftDrawer"
    />
    <page-container />
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import LayoutHeader from "../components/MainLayout/LayoutHeader.vue";
import LeftDrawer from "../components/MainLayout/LeftDrawer.vue";
import PageContainer from "../components/MainLayout/PageContainer.vue";

export default defineComponent({
  name: "MainLayout",

  components: {
    LayoutHeader,
    LeftDrawer,
    PageContainer,
  },

  setup() {
    const leftDrawerOpen = ref(true);

    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
