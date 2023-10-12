<template>
  <FTable :rows="services" :columns="columns" @add="addRegistry">
    <template #filter>
      <q-checkbox
        v-model="visibleColumns"
        val="groups"
        label="Κατηγοριοποίση"
        size="sm"
      />
      <q-checkbox
        v-model="visibleColumns"
        val="materials"
        label="Υλικά"
        size="sm"
      />
      <q-checkbox
        v-model="visibleColumns"
        val="services"
        label="Υπηρεσίες"
        size="sm"
      />
    </template>
    <template #header="{ props }">
      <q-tr :props="props">
        <q-th v-for="col in props.cols" :key="col.name" :props="props">
          {{ col.label }}
        </q-th>
        <q-th auto-width />
        <!-- <q-th auto-width /> -->
      </q-tr>
    </template>
    <template #body="{ props }">
      <q-tr :props="props">
        <q-td
          v-for="col in props.cols"
          :key="col.name"
          class="cursor-pointer"
          @click="props.expand = !props.expand"
        >
          {{ col.value }}
        </q-td>
        <q-td auto-width class="bg-light">
          <!-- <q-btn size="sm" round dense @click="props.expand = !props.expand" :icon="props.expand ? 'remove' : 'add'" /> -->
          <q-btn
            size="sm"
            flat
            dense
            round
            icon="edit"
            @click="editRegistry(props.row)"
            class="q-mr-xs"
          />
          <q-btn
            size="sm"
            flat
            dense
            round
            icon="delete"
            @click="deleteRegistry(props.row)"
          />
        </q-td>
        <!-- <q-td auto-width>
          <q-btn size="sm" color="accent" round dense @click="props.expand = !props.expand" :icon="props.expand ? 'remove' : 'add'" />
        </q-td> -->
      </q-tr>
      <q-tr v-show="props.expand">
        <q-td colspan="100%">
          <div class="text-left">
            This is expand slot for row above: {{ props.row.fname }}
            {{ props.row.lname }}.
          </div>
        </q-td>
      </q-tr>
    </template>
  </FTable>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useQuasar } from "quasar";
import ChangePasswordDialog from "../components/ChangePasswordDialog.vue";
import FTable from "./FTable.vue";

const columns = [
  {
    name: "name",
    align: "left",
    label: "Όνομα",
    field: "name",
    sortable: true,
  },
  {
    name: "group",
    align: "left",
    label: "Κατηγορία",
    field: "group_id",
    sortable: true,
  },
  {
    name: "price",
    align: "left",
    label: "Τιμή",
    field: "price",
    sortable: true,
  },
  { name: "reserve", align: "left", label: "Απόθεμα", field: "reserve" },
];

export default defineComponent({
  name: "ServicesTable",

  components: {
    FTable,
  },

  setup() {
    const $q = useQuasar();
    const visibleColumns = ref(["groups"]);
    const services = ref([]);
    let g, s;

    return {
      services,
      columns,
      visibleColumns,
      addRegistry() {
        console.log("addRegistry");
        $q.dialog({
          component: ChangePasswordDialog,
        });
      },
    };
  },
});
</script>

<style scoped>
.q-tab-panel {
  padding: 0 !important;
}
</style>
