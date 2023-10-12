<template>
  <q-list>
    <q-item class="rounded-borders text-subtitle1">
      <q-item-section>
        <q-item-label class="text-h5 text-accent text-weight-bold"
          >Dashboard</q-item-label
        >
      </q-item-section>
    </q-item>
    <q-expansion-item label="Dashboar" header-class="text-h6" default-opened>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1 text-accent">Dashboard1</q-item-label>
        </q-item-section>
      </q-item>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Dashboard2</q-item-label>
        </q-item-section>
      </q-item>
    </q-expansion-item>
    <q-item class="rounded-borders text-subtitle1">
      <q-item-section>
        <q-item-label class="text-h5 text-accent text-weight-bold"
          >Applications</q-item-label
        >
      </q-item-section>
    </q-item>
    <q-expansion-item label="Pages" header-class="text-h6">
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Login</q-item-label>
        </q-item-section>
      </q-item>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Register</q-item-label>
        </q-item-section>
      </q-item>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Forgot Password</q-item-label>
        </q-item-section>
      </q-item>
    </q-expansion-item>
    <q-expansion-item label="Application" header-class="text-h6">
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Mail Box</q-item-label>
        </q-item-section>
      </q-item>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">Chat</q-item-label>
        </q-item-section>
      </q-item>
      <q-item tag="a" to="#" class="rounded-borders text-subtitle1">
        <q-item-section>
          <q-item-label class="text-body1">FAQ</q-item-label>
        </q-item-section>
      </q-item>
    </q-expansion-item>
    <q-item class="rounded-borders text-subtitle1">
      <q-item-section>
        <q-item-label class="text-h5 text-accent text-weight-bold"
          >Components</q-item-label
        >
      </q-item-section>
    </q-item>
    <q-expansion-item label="UI Components" header-class="text-h6">
    </q-expansion-item>
    <q-expansion-item label="Widgets" header-class="text-h6">
    </q-expansion-item>
    <q-expansion-item label="Forms" header-class="text-h6"> </q-expansion-item>
    <q-expansion-item label="Charts" header-class="text-h6"> </q-expansion-item>
  </q-list>
</template>

<script>
import { defineComponent } from "vue";

const pagesList = [
  {
    group: "Dashboard",
    caption: "This is a caption",
    children: [
      {
        title: "Dashboard1",
        link: "/dashboard1",
      },
      {
        title: "Dashboard2",
        link: "/dashboard2",
      },
    ],
  },
  {
    group: "Pages",
    link: "/pages",
    children: [
      {
        title: "Login",
        link: "/login",
      },
      {
        title: "Register",
        link: "/register",
      },
      {
        title: "Forgot Password",
        link: "/forgot_password",
      },
    ],
  },
  {
    group: "Applications",
    link: "/applications",
    children: [
      {
        title: "Mail Box",
        link: "/mail_box",
      },
      {
        title: "Chat",
        link: "/chat",
      },
      {
        title: "FAQ",
        link: "/faq",
      },
    ],
  },
  {
    group: "Καταχωρήσεις",
    link: "/scheduler",
  },
  {
    title: "Ημερολόγιο",
    icon: "summarize",
    link: "/reports",
  },
];

export default defineComponent({
  name: "DrawerMenu",

  setup() {
    return {
      pages: pagesList,
    };
  },
});
</script>
