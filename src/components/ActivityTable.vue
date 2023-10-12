<template>
  <q-table
    style="height: 400px"
    flat
    :rows="activity"
    :columns="columns"
    hide-header
    hide-bottom
    :pagination="pagination"
    :rows-per-page-options="[0]"
  >
    <template #body="props">
      <q-tr :props="props">
        <q-td key="time" :props="props">
          <q-badge rounded color="primary" />
        </q-td>
        <q-td key="message" :props="props" class="text-left">
          <div class="text-h6 text-weight-bold">{{ props.row.time }}</div>
          <div class="text-weight-medium">
            {{ props.row.message }}
          </div>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
import { defineComponent, ref } from "vue";

const columns = [
  { name: "time", label: "Time", field: "time", required: true },
  { name: "message", align: "center", label: "Message", field: "message" },
];

export default defineComponent({
  props: {
    activity: { type: Array, default: new Array() },
  },
  setup() {
    return {
      columns,
      pagination: ref({
        rowsPerPage: 0,
      }),
    };
  },
});
</script>
