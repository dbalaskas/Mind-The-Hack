<template>
  <q-drawer v-model="leftDrawerOpen" show-if-above bordered class="q-pa-md">
    <q-scroll-area style="height: calc(100% - 70px); margin-top: 70px">
      <drawer-menu />
    </q-scroll-area>
    <div class="absolute-top q-pa-md row justify-center" style="height: 70px">
      <div>
        <q-img
          src="logo.png"
          width="10rem"
          class="rounded-borders cursor-pointer"
          @click="onHome"
        />
      </div>
    </div>
  </q-drawer>
</template>

<script>
import { defineComponent, ref, computed } from "vue";
import { useRouter } from "vue-router";
import DrawerMenu from "./DrawerMenu.vue";

export default defineComponent({
  name: "LeftDrawer",

  components: {
    DrawerMenu,
  },

  props: {
    drawerOpen: Boolean,
  },

  setup(props) {
    const $r = useRouter();

    const leftDrawerOpen = computed({
      get() {
        return props.drawerOpen;
      },
      set(_) {},
    });

    return {
      leftDrawerOpen,

      onHome() {
        $r.push("/");
      },
    };
  },
});
</script>
