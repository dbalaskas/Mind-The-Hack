<template>
  <q-dialog ref="dialog">
    <q-card class="q-dialog-plugin q-pa-lg">
      <!--
        ...content
        ... use q-card-section for it?
      -->
      <div class="text-h5 q-pb-lg row justify-between items-center">
        Αλλαγή κωδικού
        <q-btn
          icon="close"
          class="cursor-pointer"
          @click="dialog.hide()"
          flat
          round
        />
      </div>
      <q-form @submit.prevent="onSubmit">
        <q-input
          v-model="oldPassword"
          label="Παλιός κωδικός"
          :type="isPwdOld ? 'password' : 'text'"
          :rules="[(val) => !!val || 'Ο παλιός κωδικός πρέπει να συμπληρωθεί.']"
          outlined
          stack-label
          class="q-mb-sm"
        >
          <template #append>
            <q-icon
              :name="isPwdOld ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwdOld = !isPwdOld"
            />
          </template>
        </q-input>
        <q-input
          v-model="newPassword"
          label="Νέος κωδικός"
          :type="isPwdNew ? 'password' : 'text'"
          :rules="[(val) => !!val || 'Ο νέος κωδικός πρέπει να συμπληρωθεί.']"
          outlined
          stack-label
          class="q-mb-sm"
        >
          <template #append>
            <q-icon
              :name="isPwdNew ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwdNew = !isPwdNew"
            />
          </template>
        </q-input>
        <q-input
          v-model="newPassword2"
          label="Νέος κωδικός 2"
          :type="isPwdNew2 ? 'password' : 'text'"
          :rules="[
            (val) => !!val || 'Ο δεύτερος νέος κωδικός πρέπει να συμπληρωθεί.',
            (val) =>
              val == newPassword ||
              'Οι δύο νέοι κωδικοί δεν ταιριάζουν μεταξύ τους.',
          ]"
          outlined
          stack-label
          class="q-mb-sm"
        >
          <template #append>
            <q-icon
              :name="isPwdNew2 ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwdNew2 = !isPwdNew2"
            />
          </template>
        </q-input>
        <div v-if="failedChngPwd" class="q-pa-xs text-negative">
          Λάθος κωδικός.
        </div>
        <q-btn
          color="primary"
          label="Αλλαγή κωδικού"
          type="submit"
          class="full-width"
        />
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "ChangePasswordDialog",

  setup() {
    const isPwdOld = ref(true);
    const isPwdNew = ref(true);
    const isPwdNew2 = ref(true);
    const failedChngPwd = ref(false);
    const oldPassword = ref("");
    const newPassword = ref("");
    const newPassword2 = ref("");
    const dialog = ref(null);

    return {
      oldPassword,
      newPassword,
      newPassword2,
      failedChngPwd,
      isPwdOld,
      isPwdNew,
      isPwdNew2,
      dialog,

      onSubmit() {
        console.log("On Submit");
      },
    };
  },
});
</script>
