<template>
  <q-header class="bg-light">
    <q-toolbar class="q-py-md">
      <q-btn
        flat
        dense
        round
        icon="menu"
        aria-label="Menu"
        @click="toggleDrawer"
      />

      <q-toolbar-title> </q-toolbar-title>
      <div>
        <q-btn flat dense round icon="notifications" class="q-mr-sm">
          <q-badge floating color="red" rounded />
        </q-btn>
        <q-btn flat dense round icon="chat_bubble" class="q-mr-sm">
          <q-badge floating color="red" rounded />
        </q-btn>
        <q-btn flat dense round size="1.5em">
          <q-avatar>
            <img src="profile.jpg" />
          </q-avatar>
          <q-popup-proxy transition-show="jump-down" transition-hide="jump-up">
            <q-list
              class="text-no-wrap rounded-borders proxy"
              style="min-width: 200px"
            >
              <q-item v-close-popup @click="onAccountInfo">
                <q-item-section>
                  <q-item-label caption>Full-Stack Developer</q-item-label>
                  <q-item-label>Dionysis Balaskas</q-item-label>
                </q-item-section>
              </q-item>
              <q-separator />
              <q-item clickable v-close-popup @click="onMyProfile">
                <q-item-section>
                  <q-item-label>My Profile</q-item-label>
                </q-item-section>
              </q-item>
              <q-item v-close-popup @click="onSettings">
                <q-item-section>
                  <q-item-label disabled>Setting</q-item-label>
                </q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="onLogout">
                <q-item-section to="/login">
                  <q-item-label style="color: red">Log out</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-popup-proxy>
        </q-btn>
      </div>
    </q-toolbar>
  </q-header>
</template>

<script>
import { defineComponent } from "vue";
import { useQuasar } from "quasar";
import { useRouter } from "vue-router";
import ChangePasswordDialog from "../ChangePasswordDialog.vue";

export default defineComponent({
  name: "LayoutHeader",

  emits: ["toggleDrawer"],

  setup(_, context) {
    const $q = useQuasar();
    const $r = useRouter();

    return {
      toggleDrawer() {
        context.emit("toggleDrawer");
      },
      toggleLanguage() {
        console.log("ToggleLanguage");
      },
      toggleDarkMode() {
        $q.dark.toggle();
      },
      onAccountInfo() {
        console.log("AccountInfo");
      },
      onSettings() {
        console.log("Support");
      },
      onMyProfile() {
        console.log("ChangePassword");
      },
      onLogout() {
        auth.logout().then(() => {
          $r.push("/login");
        });
      },
    };
  },
});
</script>
