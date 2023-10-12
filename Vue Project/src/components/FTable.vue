<template>
  <q-table
    :rows="rows"
    :columns="columns"
    row-key="name"
    class="no-shadow fit"
    virtual-scroll
    :pagination="pagination"
    :rows-per-page-options="[0]"
    scroll-target="#scroll-bar"
    hide-bottom
    flat
    bordered
    :filter="filter"
  >
    <template #top="props">
      <div class="full-width row justify-between items-center">
        <div class="row items-center">
          <!-- <q-popup-proxy transition-show="jump-down" transition-hide="jump-up">
              <q-list class="text-no-wrap rounded-borders proxy" style="min-width:200px">
                <q-item v-close-popup @click="onAccountInfo">
                  <q-item-section>
                    <q-toggle v-model="visibleColumns" val="groups" label="Κατηγοριοποίση" />
                  </q-item-section>
                </q-item>
                <q-item v-close-popup @click="onAccountInfo">
                  <q-item-section>
                    <q-toggle v-model="visibleColumns" val="materials" label="Υλικά" />
                  </q-item-section>
                </q-item>
                <q-item v-close-popup @click="onAccountInfo">
                  <q-item-section>
                    <q-toggle v-model="visibleColumns" val="services" label="Υπηρεσίες" />
                  </q-item-section>
                </q-item>
              </q-list>
            </q-popup-proxy> -->
          <!-- </q-btn> -->
          <!-- <q-btn flat dense round icon="add_circle"/> -->
          <q-input
            outlined
            dense
            debounce="300"
            v-model="filter"
            placeholder="Search"
            class="q-mr-sm"
          >
            <template #append>
              <q-icon name="search" />
            </template>
          </q-input>
          <q-btn
            v-if="$slots.filter"
            flat
            dense
            round
            icon="filter_alt"
            :color="filterActive ? 'primary' : ''"
            @click="toggleFilterActive"
            class="q-mr-sm"
          />
          <q-btn flat dense round icon="add_circle" @click="$emit('add')" />
        </div>
        <q-btn
          flat
          round
          dense
          :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
          :color="props.inFullscreen ? 'primary' : ''"
          @click="props.toggleFullscreen"
        />
      </div>
      <div
        v-if="filterActive"
        class="full-width q-pt-md row"
        animate
        transition-show="jump-down"
        transition-hide="jump-up"
      >
        <slot name="filter" />
      </div>
    </template>
    <template #header="props">
      <slot name="header" :props="props" />
    </template>
    <template #body="props">
      <slot name="body" :props="props" />
    </template>
  </q-table>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "FTable",

  props: {
    rows: {
      type: Array,
      required: true,
    },
    columns: {
      type: Array,
      required: true,
    },
  },

  emits: ["add"],

  setup() {
    const filterActive = ref(false);

    return {
      pagination: ref({
        rowsPerPage: 0,
      }),
      filterActive,
      filter: ref(""),
      toggleFilterActive() {
        filterActive.value = !filterActive.value;
      },
    };
  },
});
</script>
